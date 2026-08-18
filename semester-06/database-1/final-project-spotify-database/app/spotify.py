import psycopg2
import tkinter as tk
from tkinter import messagebox, ttk
import decimal
import time
import os
PRIMARY_COLOR = "#1DB954"  # Spotify Green
BACKGROUND_COLOR = "#191414"  # Spotify Black
FONT_COLOR = "#FFFFFF"  # White
FONT = ("Helvetica", 12)



try:
    connection = psycopg2.connect(
        user=os.getenv("SPOTIFY_DB_USER", "postgres"),
        password=os.getenv("SPOTIFY_DB_PASSWORD"),
        host=os.getenv("SPOTIFY_DB_HOST", "127.0.0.1"),
        port=os.getenv("SPOTIFY_DB_PORT", "5432"),
        database=os.getenv("SPOTIFY_DB_NAME", "spotify"),
    )
    cursor = connection.cursor()
except Exception as error:
    print(f"Error while connecting to database: {error}")

# Function to center the window on the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

# Function to update the clock
def update_clock(label):
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_clock, label)

# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()
    cursor.execute("SELECT * FROM user_ WHERE user_name=%s AND password=%s", (username, password))
    user_record = cursor.fetchone()
    if user_record:
        user_id = user_record[0]
        user_name = user_record[1]
        cursor.execute("SELECT * FROM singer WHERE user_id=%s", (user_id,))
        singer_record = cursor.fetchone()
        if singer_record:
            messagebox.showinfo("Login", "Login successful as Singer")
            root.destroy()  
            open_singer_dashboard(user_id, user_name)
        else:
            messagebox.showinfo("Login", "Login successful as User")
            root.destroy()  
            open_user_dashboard(user_id, user_name)
    else:
        messagebox.showerror("Login", "Invalid username or password")



def open_singer_dashboard(user_id, user_name):
    def open_add_song_window():
        singer_root.withdraw() #Hide singer_root
        open_add_song(user_id, open_singer_dashboard, user_name)

    def open_album_window():
        singer_root.withdraw()
        open_album_list(user_id, open_singer_dashboard, user_name)

    def open_add_concert_window():
        singer_root.withdraw()
        open_add_concert(user_id, open_singer_dashboard, user_name)
    
    def open_all_songs_window():
        singer_root.withdraw()
        open_all_songs(user_id, user_name)

    singer_root = tk.Tk()
    singer_root.title("Singer Dashboard")
    singer_root.configure(bg=BACKGROUND_COLOR)
    center_window(singer_root, 600, 400)

    top_frame = tk.Frame(singer_root)
    top_frame.pack(side=tk.TOP, fill=tk.X)
    
    welcome_label = tk.Label(top_frame, text=f"Welcome, {user_name}!", anchor='nw', font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    welcome_label.pack(side=tk.LEFT, padx=10, pady=10)

    clock_label = tk.Label(top_frame, font=('Helvetica', 12))
    clock_label.pack(side=tk.RIGHT, padx=10, pady=10)
    update_clock(clock_label)

    button_frame = tk.Frame(singer_root)
    button_frame.pack(side=tk.LEFT, fill=tk.Y)

    button_add_song = tk.Button(button_frame, text="Add Song", command=open_add_song_window, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_add_song.pack(anchor='nw', padx=10, pady=5)

    button_album = tk.Button(button_frame, text="Album", command=open_album_window, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_album.pack(anchor='nw', padx=10, pady=5)

    button_add_concert = tk.Button(button_frame, text="Add Concert", command=open_add_concert_window, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_add_concert.pack(anchor='nw', padx=10, pady=5)

    #button_all_songs = tk.Button(button_frame, text="Show All Songs", command=open_all_songs_window,  bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    #button_all_songs.pack(anchor='nw', padx=10, pady=5)

    # Table for displaying albums
    table_frame = tk.Frame(singer_root)
    table_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    columns = ('Album Name',)
    tree = ttk.Treeview(table_frame, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
    
    tree.pack(fill=tk.BOTH, expand=True)

    # Fetch albums
    cursor.execute("""
        SELECT title 
        FROM album
        WHERE artistid = (SELECT id FROM singer WHERE user_id = %s)
        ORDER BY title
    """, (user_id,))
    albums = cursor.fetchall()

    for album_title in albums:
        tree.insert('', tk.END, values=(album_title[0],))

    singer_root.mainloop()



# Function to open add song window
def open_add_song(user_id, return_function, user_name):
    add_song_root = tk.Tk()
    add_song_root.title("Add Song")
    add_song_root.configure(bg=BACKGROUND_COLOR)
    center_window(add_song_root, 400, 400)

    label_song_name = tk.Label(add_song_root, text="Song Name", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_song_name.pack(pady=5)
    entry_song_name = tk.Entry(add_song_root)
    entry_song_name.pack(pady=5)

    label_lyrics = tk.Label(add_song_root, text="Lyrics", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_lyrics.pack(pady=5)
    entry_lyrics = tk.Entry(add_song_root)
    entry_lyrics.pack(pady=5)

    label_genre = tk.Label(add_song_root, text="Genre", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_genre.pack(pady=5)
    entry_genre = tk.Entry(add_song_root)
    entry_genre.pack(pady=5)

    label_album_name = tk.Label(add_song_root, text="Album Name (optional)", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_album_name.pack(pady=5)
    entry_album_name = tk.Entry(add_song_root)
    entry_album_name.pack(pady=5)

    def add_song():
        song_name = entry_song_name.get()
        lyrics = entry_lyrics.get()
        genre = entry_genre.get()
        album_name = entry_album_name.get()

        album_id = None
        if album_name:
            cursor.execute("SELECT AlbumID FROM album WHERE Title=%s", (album_name,))
            album_record = cursor.fetchone()
            if album_record:
                album_id = album_record[0]
            else:
                messagebox.showerror("Add Song", "Album does not exist")
                return

        try:
            cursor.execute(
                "INSERT INTO song (Title, Lyrics, Genre, ArtistID, AlbumID) VALUES (%s, %s, %s, %s, %s)",
                (song_name, lyrics, genre, user_id, album_id))
            connection.commit()
            messagebox.showinfo("Add Song", "Song added successfully")
            add_song_root.destroy()
            return_function(user_id, user_name) #return to last window
        except Exception as error:
            messagebox.showerror("Add Song", f"Error adding song: {error}")

    button_submit = tk.Button(add_song_root, text="Submit", command=add_song, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_submit.pack(pady=10)

    button_back = tk.Button(add_song_root, text="Back", command=lambda: go_back(add_song_root, return_function, user_id, user_name), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    add_song_root.mainloop()

# Function to open add album window
# Function to open add album window
def open_add_album(user_id, return_function, user_name, existing_root=None, refresh_function=None):
    add_album_root = tk.Tk()
    add_album_root.title("Add Album")
    add_album_root.configure(bg=BACKGROUND_COLOR)
    center_window(add_album_root, 400, 200)

    label_album_name = tk.Label(add_album_root, text="Album Name", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_album_name.pack(pady=5)
    entry_album_name = tk.Entry(add_album_root)
    entry_album_name.pack(pady=5)

    def add_album():
        album_name = entry_album_name.get()

        try:
            cursor.execute("SELECT * FROM singer WHERE user_id=%s", (user_id,))
            singer_record = cursor.fetchone()
            if singer_record is None:
                messagebox.showerror("Add Album", "User is not registered as a singer.")
                return

            artist_id = singer_record[0]

            cursor.execute(
                "INSERT INTO album (Title, ArtistID) VALUES (%s, %s)",
                (album_name, artist_id))
            connection.commit()
            messagebox.showinfo("Add Album", "Album added successfully")
            add_album_root.destroy()
            if refresh_function:
                refresh_function()  # Refresh the album list
            if existing_root:
                existing_root.deiconify()  #show hidden window
        except Exception as error:
            messagebox.showerror("Add Album", f"Error adding album: {error}")
            print(f"Error adding album: {error}")

    button_submit = tk.Button(add_album_root, text="Submit", command=add_album, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_submit.pack(pady=10)

    button_back = tk.Button(add_album_root, text="Back", command=lambda: go_back(add_album_root, return_function, user_id, user_name, existing_root, refresh_function), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    add_album_root.mainloop()



# Function to open user dashboard
def open_user_dashboard(user_id, user_name, existing_root=None):
    if existing_root:
        existing_root.deiconify()
        return

    def open_wallet_window():
        user_root.withdraw()
        open_wallet(user_id, open_user_dashboard, user_name, user_root)

    def open_subscription_window():
        user_root.withdraw()
        show_subscription_options(user_id, user_name, user_root)

    def open_song_selection_window():
        if has_subscription:
            user_root.withdraw()
            open_select_song(user_id, open_user_dashboard, user_name, user_root)
        else:
            messagebox.showerror("Subscription Required", "You need to buy a subscription to access this feature.")

    def open_album_selection_window():
        if has_subscription:
            user_root.withdraw()
            open_album_selection(user_id, open_user_dashboard, user_name, user_root)
        else:
            messagebox.showerror("Subscription Required", "You need to buy a subscription to access this feature.")

    def open_friend_request_window():
        if has_subscription:
            user_root.withdraw()
            open_friend_requests(user_id, user_name, open_user_dashboard, user_root)
        else:
            messagebox.showerror("Subscription Required", "You need to buy a subscription to access this feature.")

    def open_playlist_window():
         if has_subscription:
            user_root.withdraw()
            open_playlist(user_id, open_user_dashboard, user_name, user_root)
         else:
            messagebox.showerror("Subscription Required", "You need to buy a subscription to access this feature.")
    
    def open_ticket_purchase_window():
        if has_subscription:
            user_root.withdraw()
            open_buy_ticket(user_id, open_user_dashboard, user_name)
        else:
            messagebox.showerror("Subscription Required", "You need to buy a subscription to access this feature.")

    def open_follow_artist_window():
        if has_subscription:
            user_root.withdraw()
            open_follow_artist(user_id, user_name)
        else:
            messagebox.showerror("Subscription Required", "You need to buy a subscription to access this feature.")

    def open_purchased_tickets_window():
        if has_subscription:
            user_root.withdraw()
            open_purchased_tickets(user_id, user_name)
        else:
            messagebox.showerror("Subscription Required", "You need to buy a subscription to access this feature.")

    def open_like_album_window():
        if has_subscription:
            user_root.withdraw()
            like_album(user_id, open_user_dashboard, user_name, user_root)
        else:
            messagebox.showerror("Subscription Required", "You need to buy a subscription to access this feature.")
    
    def open_like_playlist_window():
        if has_subscription:
            user_root.withdraw()
            like_playlist(user_id, open_user_dashboard, user_name, user_root)
        else:
            messagebox.showerror("Subscription Required", "You need to buy a subscription to access this feature.")

    user_root = tk.Tk()
    user_root.title("User Dashboard")
    user_root.configure(bg=BACKGROUND_COLOR)
    center_window(user_root, 1000, 700)
    
    top_frame = tk.Frame(user_root, bg=BACKGROUND_COLOR)
    top_frame.pack(side=tk.TOP, fill=tk.X)

    welcome_label = tk.Label(top_frame, text=f"Welcome, {user_name}!", anchor='nw', font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    welcome_label.pack(side=tk.LEFT, padx=10, pady=10)

    clock_label = tk.Label(top_frame, font=('Helvetica', 12), bg=BACKGROUND_COLOR, fg=FONT_COLOR)
    clock_label.pack(side=tk.RIGHT, padx=10, pady=10)
    update_clock(clock_label)

    button_frame = tk.Frame(user_root, bg=BACKGROUND_COLOR)
    button_frame.pack(side=tk.LEFT, fill=tk.Y)

    cursor.execute("SELECT subscription_type FROM user_ WHERE id=%s", (user_id,))
    user_record = cursor.fetchone()
    has_subscription = user_record[0]

    button_wallet = tk.Button(button_frame, text="Manage Wallet", command=open_wallet_window, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_wallet.pack(anchor='nw', padx=10, pady=5)

    button_subscription = tk.Button(button_frame, text="Buy Subscription", command=open_subscription_window, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_subscription.pack(anchor='nw', padx=10, pady=5)

    button_song = tk.Button(button_frame, text="Select Song", command=open_song_selection_window, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_song.pack(anchor='nw', padx=10, pady=5)

    button_album = tk.Button(button_frame, text="Select Album", command=open_album_selection_window, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_album.pack(anchor='nw', padx=10, pady=5)
    if not has_subscription:
        button_album.config(bg="red")

    button_friend_request = tk.Button(button_frame, text="Add Friend", command=open_friend_request_window, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_friend_request.pack(anchor='nw', padx=10, pady=5)
    if not has_subscription:
        button_friend_request.config(bg="red")

    button_playlist = tk.Button(button_frame, text="Playlists", command=open_playlist_window, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_playlist.pack(anchor='nw', padx=10, pady=5)
    if not has_subscription:
        button_playlist.config(bg="red")

    button_buy_ticket = tk.Button(button_frame, text="Buy Ticket", command=open_ticket_purchase_window, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_buy_ticket.pack(anchor='nw', padx=10, pady=5)
    if not has_subscription:
        button_buy_ticket.config(bg="red")

    button_follow_artist = tk.Button(button_frame, text="Follow Artist", command=open_follow_artist_window, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_follow_artist.pack(anchor='nw', padx=10, pady=5)
    if not has_subscription:
        button_follow_artist.config(bg="red")

    button_purchased_tickets = tk.Button(button_frame, text="Purchased Tickets", command=open_purchased_tickets_window, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_purchased_tickets.pack(anchor='nw', padx=10, pady=5)
    if not has_subscription:
        button_purchased_tickets.config(bg="red")

    button_like_album = tk.Button(button_frame, text="Like Album", command=open_like_album_window, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_like_album.pack(anchor='nw', padx=10, pady=5)
    if not has_subscription:
        button_like_album.config(bg="red")

    button_like_playlist = tk.Button(button_frame, text="Like Playlist", command=open_like_playlist_window, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_like_playlist.pack(anchor='nw', padx=10, pady=5)
    if not has_subscription:
        button_like_playlist.config(bg="red")

    table_frame = tk.Frame(user_root, bg=BACKGROUND_COLOR, width=400)
    table_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

    columns = ('SongID', 'Song Name', 'Singer Name', 'Genre')
    tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=10)

    for col in columns:
        tree.heading(col, text=col)
    
    tree.pack(fill=tk.BOTH, expand=True)

    cursor.execute("SELECT SongID FROM UserLikeSong WHERE UserID=%s", (user_id,))
    liked_songs = cursor.fetchall()

    song_ids = [song[0] for song in liked_songs]
    #song of playlist that likes by user
    cursor.execute("""               
        SELECT song.SongID
        FROM song
        JOIN PlaylistContainsSong ON song.SongID = PlaylistContainsSong.song_id
        JOIN Playlist ON PlaylistContainsSong.playlist_id = Playlist.PlaylistID
        JOIN UserLikePlaylist ON Playlist.PlaylistID = UserLikePlaylist.playlistid
        WHERE UserLikePlaylist.userid = %s
    """, (user_id,))
    playlist_songs = cursor.fetchall()

    song_ids += [song[0] for song in playlist_songs]

    cursor.execute("""
        SELECT song.SongID
        FROM song
        JOIN album ON song.AlbumID = album.albumid
        JOIN UserLikeAlbum ON album.albumid = UserLikeAlbum.AlbumID
        WHERE UserLikeAlbum.UserID = %s
    """, (user_id,))
    album_songs = cursor.fetchall()

    song_ids += [song[0] for song in album_songs]

    if song_ids:
        cursor.execute("SELECT SongID, Title, ArtistID, Genre FROM song WHERE SongID IN %s", (tuple(song_ids),))
    else:
        cursor.execute("SELECT SongID, Title, ArtistID, Genre FROM song ORDER BY RANDOM() LIMIT 10")

    songs = cursor.fetchall()

    for song in songs:
        cursor.execute("SELECT stage_name FROM singer WHERE user_id=%s", (song[2],))
        singer_name = cursor.fetchone()[0]
        tree.insert('', tk.END, values=(song[0], song[1], singer_name, song[3]), tags=(song[1],))

    def on_song_select(event):
         for item in tree.selection():
            lyrics = tree.item(item, 'tags')[0]
            song_id = tree.item(item, 'values')[0]
            show_song_options(song_id, lyrics, user_id, user_name, user_root)

    tree.bind('<<TreeviewSelect>>', on_song_select)

    user_root.mainloop()




# Function to show lyrics window
def show_lyrics_window(lyrics, current_window, return_window, user_id, user_name):
    current_window.withdraw()
    lyrics_root = tk.Tk()
    lyrics_root.title("Song Lyrics")
    lyrics_root.configure(bg=BACKGROUND_COLOR)
    center_window(lyrics_root, 400, 300)

    label_lyrics = tk.Label(lyrics_root, text=lyrics, wraplength=380, font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_lyrics.pack(padx=10, pady=10)

    button_close = tk.Button(lyrics_root, text="Close", command=lambda: go_back(lyrics_root, return_window, user_id, user_name), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_close.pack(pady=10)

    lyrics_root.mainloop()



# Function to show comments window
def show_comments_window(song_id, user_id, user_name, current_window, return_window):
    current_window.withdraw()
    comments_root = tk.Tk()
    comments_root.title("Comments")
    comments_root.configure(bg=BACKGROUND_COLOR)
    center_window(comments_root, 400, 400)

    label_comments = tk.Label(comments_root, text="Comments", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_comments.pack(pady=10)

    comments_frame = tk.Frame(comments_root)
    comments_frame.pack(fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(comments_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox_comments = tk.Listbox(comments_frame, yscrollcommand=scrollbar.set)
    listbox_comments.pack(fill=tk.BOTH, expand=True)

    scrollbar.config(command=listbox_comments.yview)

    cursor.execute("""
        SELECT Comment.Content, user_.user_name
        FROM Comment
        JOIN user_ ON Comment.UserID = user_.id
        WHERE Comment.RelatedEntityID = %s AND Comment.EntityType = %s
        ORDER BY Comment.CreatedAt DESC
    """, (song_id, 'Song'))
    comments = cursor.fetchall()

    for comment in comments:
        listbox_comments.insert(tk.END, f"{comment[1]}: {comment[0]}")

    label_new_comment = tk.Label(comments_root, text="Add a comment:", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_new_comment.pack(pady=5)
    entry_new_comment = tk.Entry(comments_root)
    entry_new_comment.pack(pady=5)

    def add_comment():
        new_comment = entry_new_comment.get()
        if new_comment:
            cursor.execute("""
                INSERT INTO Comment (Content, UserID, RelatedEntityID, EntityType)
                VALUES (%s, %s, %s, %s)
            """, (new_comment, user_id, song_id, 'Song'))
            connection.commit()
            messagebox.showinfo("Comments", "Comment added successfully")
            comments_root.destroy()
            show_comments_window(song_id, user_id, user_name, current_window, return_window)
        else:
            messagebox.showerror("Comments", "Comment cannot be empty")

    button_add_comment = tk.Button(comments_root, text="Add Comment", command=add_comment, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_add_comment.pack(pady=10)

    button_back = tk.Button(comments_root, text="Back", command=lambda: go_back(comments_root, return_window, user_id, user_name), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    comments_root.mainloop()

# Function to open wallet management window
def open_wallet(user_id, return_function, user_name, existing_root):
    wallet_root = tk.Tk()
    wallet_root.title("Wallet Management")
    wallet_root.configure(bg=BACKGROUND_COLOR)
    center_window(wallet_root, 400, 300)

    cursor.execute("SELECT balance FROM wallet WHERE user_id=%s", (user_id,))
    wallet_record = cursor.fetchone()
    if wallet_record:
        balance = wallet_record[0]
    else:
        cursor.execute("INSERT INTO wallet (user_id, balance) VALUES (%s, %s)", (user_id, decimal.Decimal(0)))
        connection.commit()
        balance = decimal.Decimal(0)

    label_balance = tk.Label(wallet_root, text=f"Current Balance: {balance}", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_balance.pack(pady=10)

    label_amount = tk.Label(wallet_root, text="Add Amount", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_amount.pack(pady=5)
    entry_amount = tk.Entry(wallet_root)
    entry_amount.pack(pady=5)

    def add_balance():
        amount = decimal.Decimal(entry_amount.get())
        new_balance = balance + amount
        cursor.execute("UPDATE wallet SET balance=%s WHERE user_id=%s", (new_balance, user_id))
        connection.commit()
        label_balance.config(text=f"Current Balance: {new_balance}")
        messagebox.showinfo("Wallet", "Balance updated successfully")
        wallet_root.destroy()  
        return_function(user_id, user_name)  # Reopen the user dashboard

    button_add = tk.Button(wallet_root, text="Add to Wallet", command=add_balance, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_add.pack(pady=10)

    button_back = tk.Button(wallet_root, text="Back", command=lambda: go_back(wallet_root, return_function, user_id, user_name), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    wallet_root.mainloop()

# Function to go back to the previous window
def go_back(current_root, return_function, user_id, user_name, existing_root=None, refresh_function=None):
    current_root.destroy()
    if existing_root:
        if refresh_function:
            refresh_function()  # Refresh the content
        existing_root.deiconify()
    else:
        return_function(user_id, user_name)






# Function to show subscription options
def show_subscription_options(user_id, user_name, existing_root):
    subscription_root = tk.Tk()
    subscription_root.title("Buy Subscription")
    subscription_root.configure(bg=BACKGROUND_COLOR)
    center_window(subscription_root, 400, 300)

    label = tk.Label(subscription_root, text="Select Subscription Plan", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label.pack(pady=10)

    button_monthly = tk.Button(subscription_root, text="Monthly - $10", command=lambda: buy_subscription(user_id, 10, "Monthly", subscription_root, user_name, existing_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_monthly.pack(pady=5)

    button_quarterly = tk.Button(subscription_root, text="Quarterly - $25", command=lambda: buy_subscription(user_id, 25, "Quarterly", subscription_root, user_name, existing_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_quarterly.pack(pady=5)

    button_yearly = tk.Button(subscription_root, text="Yearly - $80", command=lambda: buy_subscription(user_id, 80, "Yearly", subscription_root, user_name, existing_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_yearly.pack(pady=5)

    button_back = tk.Button(subscription_root, text="Back", command=lambda: go_back(subscription_root, open_user_dashboard, user_id, user_name), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    subscription_root.mainloop()

# Function to buy a subscription
def buy_subscription(user_id, cost, plan, root, user_name, existing_root):
    cursor.execute("SELECT balance FROM wallet WHERE user_id=%s", (user_id,))
    wallet_record = cursor.fetchone()
    if wallet_record:
        balance = wallet_record[0]

        if balance >= decimal.Decimal(cost):
            new_balance = balance - decimal.Decimal(cost)
            cursor.execute("UPDATE wallet SET balance=%s WHERE user_id=%s", (new_balance, user_id))
            cursor.execute("UPDATE user_ SET subscription_type=True WHERE id=%s", (user_id,))
            connection.commit()
            messagebox.showinfo("Subscription", f"{plan} subscription purchased successfully")
            root.destroy()
            open_user_dashboard(user_id, user_name, existing_root)
        else:
            messagebox.showerror("Subscription", "Insufficient balance")
    else:
        messagebox.showerror("Subscription", "Wallet not found")

# Function to open song selection window
def open_select_song(user_id, return_function, user_name, existing_root):
    song_root = tk.Tk()
    song_root.title("Select Song")
    song_root.configure(bg=BACKGROUND_COLOR)
    center_window(song_root, 400, 200)

    label_song_name = tk.Label(song_root, text="Song Name", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_song_name.pack(pady=5)
    entry_song_name = tk.Entry(song_root)
    entry_song_name.pack(pady=5)

    def submit_song_name():
        song_name = entry_song_name.get()
        cursor.execute("SELECT SongID, Title, Lyrics, Genre, ArtistID FROM song WHERE Title=%s", (song_name,))
        song = cursor.fetchone()
        if song:
            song_id, title, lyrics, genre, artist_id = song
            cursor.execute("SELECT stage_name FROM singer WHERE user_id=%s", (artist_id,))
            singer_name = cursor.fetchone()[0]
            song_root.destroy()
            show_song_details(song_id, title, singer_name, genre, lyrics, user_id, user_name, return_function, existing_root)
        else:
            messagebox.showerror("Error", "Song not found")

    button_submit = tk.Button(song_root, text="Submit", command=submit_song_name, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_submit.pack(pady=10)

    button_back = tk.Button(song_root, text="Back", command=lambda: go_back(song_root, return_function, user_id, user_name, existing_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    song_root.mainloop()

# Function to show song details
def show_song_details(song_id, title, singer_name, genre, lyrics, user_id, user_name, return_function, existing_root):
    details_root = tk.Tk()
    details_root.title("Song Details")
    details_root.configure(bg=BACKGROUND_COLOR)
    center_window(details_root, 400, 400)

    label_title = tk.Label(details_root, text=f"Title: {title}", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_title.pack(pady=5)

    label_singer = tk.Label(details_root, text=f"Singer: {singer_name}", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_singer.pack(pady=5)

    label_genre = tk.Label(details_root, text=f"Genre: {genre}", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_genre.pack(pady=5)

    button_lyrics = tk.Button(details_root, text="Show Lyrics", command=lambda: show_lyrics_window(lyrics, details_root, details_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_lyrics.pack(pady=10)

    button_comments = tk.Button(details_root, text="Comments", command=lambda: show_comments_window(song_id, user_id, user_name, details_root, details_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_comments.pack(pady=10)

    def like_song():
        try:
            cursor.execute("SELECT * FROM UserLikeSong WHERE UserID=%s AND SongID=%s", (user_id, song_id))
            like_record = cursor.fetchone()
            if like_record:
                messagebox.showinfo("Like Song", "You have already liked this song.")
            else:
                cursor.execute("INSERT INTO UserLikeSong (UserID, SongID) VALUES (%s, %s)", (user_id, song_id))
                connection.commit()
                messagebox.showinfo("Like Song", "Song liked successfully")
                button_like.config(bg="yellow", state=tk.DISABLED)
        except Exception as error:
            messagebox.showerror("Like Song", f"Error liking song: {error}")

    button_like = tk.Button(details_root, text="Like", command=like_song, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_like.pack(pady=10)

    # Check if the user has already liked this song
    #cursor.execute("SELECT * FROM UserLikeSong WHERE UserID=%s AND SongID=%s", (user_id, song_id))
    #if cursor.fetchone():
        #button_like.config(bg="LightGreen", state=tk.DISABLED)

    button_back = tk.Button(details_root, text="Back", command=lambda: go_back(details_root, return_function, user_id, user_name, existing_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    details_root.mainloop()


# Function to open album selection window
def open_album_selection(user_id, return_function, user_name, existing_root):
    album_root = tk.Tk()
    album_root.title("Select Album")
    album_root.configure(bg=BACKGROUND_COLOR)
    center_window(album_root, 400, 300)

    label_album_name = tk.Label(album_root, text="Album Name", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_album_name.pack(pady=5)
    entry_album_name = tk.Entry(album_root)
    entry_album_name.pack(pady=5)

    def submit_album_name():
        album_name = entry_album_name.get()
        cursor.execute("SELECT AlbumID FROM album WHERE Title=%s", (album_name,))
        album = cursor.fetchone()
        if album:
            album_id = album[0]
            album_root.destroy()
            show_album_songs(album_id, user_id, user_name, return_function, existing_root)
        else:
            messagebox.showerror("Error", "Album not found")

    button_submit = tk.Button(album_root, text="Submit", command=submit_album_name, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_submit.pack(pady=10)

    button_back = tk.Button(album_root, text="Back", command=lambda: go_back(album_root, return_function, user_id, user_name, existing_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    album_root.mainloop()




# Function to open friend requests window
def open_friend_requests(user_id, user_name, return_function, existing_root):
    friend_root = tk.Tk()
    friend_root.configure(bg=BACKGROUND_COLOR)
    friend_root.title("Friend Requests")
    center_window(friend_root, 600, 500)

    def send_friend_request():
        receiver_name = entry_friend_name.get()
        cursor.execute("SELECT id FROM user_ WHERE user_name=%s", (receiver_name,))
        receiver_record = cursor.fetchone()
        if receiver_record:
            receiver_id = receiver_record[0]
            cursor.execute("SELECT * FROM FriendRequest WHERE (SenderID=%s AND ReceiverID=%s) OR (SenderID=%s AND ReceiverID=%s) AND Status='Accepted'",
                           (user_id, receiver_id, receiver_id, user_id))
            existing_request = cursor.fetchone()
            if existing_request:
                messagebox.showerror("Friend Request", "You are already friends with this user")
            else:
                cursor.execute("INSERT INTO FriendRequest (SenderID, ReceiverID, Status) VALUES (%s, %s, %s)",
                               (user_id, receiver_id, 'Pending'))
                connection.commit()
                messagebox.showinfo("Friend Request", f"Friend request sent to {receiver_name}")
                refresh_friend_requests()
        else:
            messagebox.showerror("Friend Request", "User not found")

    label_pending_requests = tk.Label(friend_root, text="Pending Friend Requests:", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_pending_requests.pack(pady=5)

    listbox_pending_requests = tk.Listbox(friend_root)
    listbox_pending_requests.pack(fill=tk.BOTH, expand=True, pady=5)

    label_friends = tk.Label(friend_root, text="Friends:", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_friends.pack(pady=5)

    friends_frame = tk.Frame(friend_root)
    friends_frame.pack(fill=tk.BOTH, expand=True, pady=5)

    listbox_friends = tk.Listbox(friends_frame, height=6, font=('Helvetica', 14))
    listbox_friends.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar_friends = tk.Scrollbar(friends_frame)
    scrollbar_friends.pack(side=tk.RIGHT, fill=tk.Y)

    listbox_friends.config(yscrollcommand=scrollbar_friends.set)
    scrollbar_friends.config(command=listbox_friends.yview)

    def refresh_friend_requests():
        listbox_pending_requests.delete(0, tk.END)
        listbox_friends.delete(0, tk.END)
        for widget in friends_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()
        cursor.execute("""
            SELECT FriendRequest.RequestID, sender.user_name, receiver.user_name, FriendRequest.Status
            FROM FriendRequest
            JOIN user_ AS sender ON FriendRequest.SenderID = sender.id
            JOIN user_ AS receiver ON FriendRequest.ReceiverID = receiver.id
            WHERE FriendRequest.ReceiverID = %s AND FriendRequest.Status='Pending'
        """, (user_id,))
        pending_requests = cursor.fetchall()

        status_symbols = {
            'Pending': '?',
            'Accepted': '✓',
            'Rejected': '✗'
        }

        for request in pending_requests:
            listbox_pending_requests.insert(tk.END, f"From: {request[1]} To: {request[2]} (RequestID: {request[0]}) - {status_symbols[request[3]]}")

        cursor.execute("""
            SELECT sender.user_name, receiver.user_name
            FROM FriendRequest
            JOIN user_ AS sender ON FriendRequest.SenderID = sender.id
            JOIN user_ AS receiver ON FriendRequest.ReceiverID = receiver.id
            WHERE (FriendRequest.SenderID = %s OR FriendRequest.ReceiverID = %s) AND FriendRequest.Status = 'Accepted'
        """, (user_id, user_id))
        friends = cursor.fetchall()

        for friend in friends:
            friend_name = friend[0] if friend[1] == user_name else friend[1]
            listbox_friends.insert(tk.END, friend_name)
            cursor.execute("SELECT id FROM user_ WHERE user_name=%s", (friend_name,))
            friend_id = cursor.fetchone()[0]
            button_send_message = tk.Button(friends_frame, text=f"Send Message to {friend_name}", command=lambda friend_id=friend_id, friend_name=friend_name: send_message(user_id, friend_id, friend_name, open_view_messages, friend_root))
            button_send_message.pack(anchor='nw', pady=5)

    refresh_friend_requests()

    def accept_request():
        selected_request = listbox_pending_requests.get(listbox_pending_requests.curselection())
        request_id = int(selected_request.split('RequestID: ')[1].split(')')[0])
        cursor.execute("UPDATE FriendRequest SET Status=%s WHERE RequestID=%s", ('Accepted', request_id))
        connection.commit()
        messagebox.showinfo("Friend Request", "Friend request accepted")
        refresh_friend_requests()

    def reject_request():
        selected_request = listbox_pending_requests.get(listbox_pending_requests.curselection())
        request_id = int(selected_request.split('RequestID: ')[1].split(')')[0])
        cursor.execute("UPDATE FriendRequest SET Status=%s WHERE RequestID=%s", ('Rejected', request_id))
        connection.commit()
        messagebox.showinfo("Friend Request", "Friend request rejected")
        refresh_friend_requests()

    button_accept = tk.Button(friend_root, text="Accept", command=accept_request, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_accept.pack(pady=5)

    button_reject = tk.Button(friend_root, text="Reject", command=reject_request, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_reject.pack(pady=5)

    label_friend_name = tk.Label(friend_root, text="Send Friend Request to:", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_friend_name.pack(pady=5)
    entry_friend_name = tk.Entry(friend_root)
    entry_friend_name.pack(pady=5)

    button_send_request = tk.Button(friend_root, text="Send Request", command=send_friend_request)
    button_send_request.pack(pady=5)

    button_back = tk.Button(friend_root, text="Back", command=lambda: go_back(friend_root, return_function, user_id, user_name, existing_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    friend_root.mainloop()

# Function to open messages window
def open_view_messages(user_id, user_name, return_function, existing_root):
    messages_root = tk.Tk()
    messages_root.configure(bg=BACKGROUND_COLOR)
    messages_root.title("Messages")
    center_window(messages_root, 600, 500)

    def send_message_window(friend_id, friend_name):
        messages_root.withdraw()
        send_message(user_id, friend_id, friend_name, open_view_messages, messages_root)

    label_messages = tk.Label(messages_root, text="Messages", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_messages.pack(pady=5)

    messages_frame = tk.Frame(messages_root)
    messages_frame.pack(fill=tk.BOTH, expand=True, pady=5)

    listbox_messages = tk.Listbox(messages_frame)
    listbox_messages.pack(fill=tk.BOTH, expand=True)

    def refresh_messages():
        listbox_messages.delete(0, tk.END)
        cursor.execute("""
            SELECT Message.Content, user_.user_name
            FROM Message
            JOIN user_ ON Message.SenderID = user_.id
            WHERE Message.ReceiverID = %s
            ORDER BY Message.CreatedAt DESC
        """, (user_id,))
        messages = cursor.fetchall()

        for message in messages:
            listbox_messages.insert(tk.END, f"From {message[1]}: {message[0]}")

    refresh_messages()

    button_back = tk.Button(messages_root, text="Back", command=lambda: go_back(messages_root, return_function, user_id, user_name, existing_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    messages_root.mainloop()

# Function to send a message
def send_message(sender_id, receiver_id, receiver_name, return_function, existing_root):
    send_root = tk.Tk()
    send_root.configure(bg=BACKGROUND_COLOR)
    send_root.title("Send Message")
    center_window(send_root, 600, 500)

    label_message = tk.Label(send_root, text=f"Send message to {receiver_name}:", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_message.pack(pady=5)
    entry_message = tk.Entry(send_root)
    entry_message.pack(pady=5)

    messages_frame = tk.Frame(send_root)
    messages_frame.pack(fill=tk.BOTH, expand=True, pady=5)

    listbox_messages = tk.Listbox(messages_frame)
    listbox_messages.pack(fill=tk.BOTH, expand=True)

    def refresh_messages():
        listbox_messages.delete(0, tk.END)
        cursor.execute("""
            SELECT Message.Content, user_.user_name
            FROM Message
            JOIN user_ ON (Message.SenderID = user_.id AND Message.ReceiverID = %s) OR (Message.ReceiverID = user_.id AND Message.SenderID = %s)
            WHERE (Message.SenderID = %s AND Message.ReceiverID = %s) OR (Message.ReceiverID = %s AND Message.SenderID = %s)
            ORDER BY Message.CreatedAt DESC
        """, (sender_id, sender_id, sender_id, receiver_id, sender_id, receiver_id))
        messages = cursor.fetchall()

        for message in messages:
            listbox_messages.insert(tk.END, f"{message[1]}: {message[0]}")

    refresh_messages()

    def send():
        message_content = entry_message.get()
        if message_content:
            try:
                cursor.execute("""
                    INSERT INTO Message (SenderID, ReceiverID, Content)
                    VALUES (%s, %s, %s)
                """, (sender_id, receiver_id, message_content))
                connection.commit()
                messagebox.showinfo("Send Message", "Message sent successfully")
                entry_message.delete(0, tk.END)
                refresh_messages()
            except Exception as error:
                messagebox.showerror("Send Message", f"Error sending message: {error}")
        else:
            messagebox.showerror("Send Message", "Message cannot be empty")

    button_send = tk.Button(send_root, text="Send", command=send, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_send.pack(pady=10)

    button_back = tk.Button(send_root, text="Back", command=lambda: go_back(send_root, return_function, sender_id, receiver_name, existing_root),bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    send_root.mainloop()

# Function to open sign up type selection window
def open_signup():
    root.destroy()  # Close the login window
    signup_type_window()  # Open the sign up type selection window

# Function to create the sign up type selection window
def signup_type_window():
    type_root = tk.Tk()
    type_root.title("Sign Up Type")
    type_root.configure(bg=BACKGROUND_COLOR)
    center_window(type_root, 400, 300)

    label = tk.Label(type_root, text="Do you want to sign up as a singer or a user?", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label.pack(pady=20)

    button_user = tk.Button(type_root, text="User", command=lambda: open_signup_form(type_root, is_singer=False), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_user.pack(pady=10)

    button_singer = tk.Button(type_root, text="Singer", command=lambda: open_signup_form(type_root, is_singer=True), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_singer.pack(pady=10)

    type_root.mainloop()

# Function to open the appropriate sign up form based on user selection
def open_signup_form(parent_window, is_singer):
    parent_window.destroy()  # Close the type selection window
    signup_window(is_singer)  # Open the sign up window based on selection

# Function to create the sign up window
def signup_window(is_singer):
    signup_root = tk.Tk()
    signup_root.title("Sign Up Page")
    signup_root.configure(bg=BACKGROUND_COLOR)
    center_window(signup_root, 400, 450 if is_singer else 400)

    # Create and place label and entry for new username
    label_username = tk.Label(signup_root, text="New Username", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_username.pack(pady=5)
    entry_new_username = tk.Entry(signup_root)
    entry_new_username.pack(pady=5)

    # Create and place label and entry for new password
    label_password = tk.Label(signup_root, text="New Password", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_password.pack(pady=5)
    entry_new_password = tk.Entry(signup_root, show="*")
    entry_new_password.pack(pady=5)

    # Create and place label and entry for birth year
    label_birthyear = tk.Label(signup_root, text="Birth Year", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_birthyear.pack(pady=5)
    entry_birthyear = tk.Entry(signup_root)
    entry_birthyear.pack(pady=5)

    # Create and place label and entry for email
    label_email = tk.Label(signup_root, text="Email", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_email.pack(pady=5)
    entry_email = tk.Entry(signup_root)
    entry_email.pack(pady=5)

    # Create and place label and entry for location
    label_location = tk.Label(signup_root, text="Location", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_location.pack(pady=5)
    entry_location = tk.Entry(signup_root)
    entry_location.pack(pady=5)

    if is_singer:
        # Create and place label and entry for stage name
        label_stage_name = tk.Label(signup_root, text="Stage Name", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
        label_stage_name.pack(pady=5)
        entry_stage_name = tk.Entry(signup_root)
        entry_stage_name.pack(pady=5)

        # Create and place label and entry for genre
        label_genre = tk.Label(signup_root, text="Genre", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
        label_genre.pack(pady=5)
        entry_genre = tk.Entry(signup_root)
        entry_genre.pack(pady=5)

    # Function to handle sign up
    def signup():
        new_username = entry_new_username.get()
        new_password = entry_new_password.get()
        birthyear = entry_birthyear.get()
        email = entry_email.get()
        location = entry_location.get()
        
        # Check if the username already exists
        cursor.execute("SELECT * FROM user_ WHERE user_name=%s", (new_username,))
        if cursor.fetchone():
            messagebox.showerror("Sign Up", "Username already exists. Please choose a different username.")
            return
        
        try:
            cursor.execute(
                "INSERT INTO user_ (user_name, password, birth_year, email, location) VALUES (%s, %s, %s, %s, %s) RETURNING id",
                (new_username, new_password, birthyear, email, location))
            user_id = cursor.fetchone()[0]
            connection.commit()
            
            if is_singer:
                stage_name = entry_stage_name.get()
                genre = entry_genre.get()
                cursor.execute(
                    "INSERT INTO singer (user_id, stage_name, genre) VALUES (%s, %s, %s)",
                    (user_id, stage_name, genre))
                connection.commit()
            
            messagebox.showinfo("Sign Up", f"Account created for {new_username}")
            signup_root.destroy()
            show_login_window()
        except Exception as error:
            messagebox.showerror("Sign Up", f"Error creating account: {error}")

    # Create and place sign up button
    button_signup = tk.Button(signup_root, text="Sign Up", command=signup, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_signup.pack(pady=5)

    signup_root.mainloop()

# Function to create the login window
def show_login_window():
    global root
    root = tk.Tk()
    root.title("Login Page")
    center_window(root, 400, 300)
    root.configure(bg=BACKGROUND_COLOR)

    # Create and place label and entry for username
    label_username = tk.Label(root, text="Username", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_username.pack(pady=5)
    global entry_username
    entry_username = tk.Entry(root)
    entry_username.pack(pady=5)

    # Create and place label and entry for password
    label_password = tk.Label(root, text="Password", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_password.pack(pady=5)
    global entry_password
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)

    # Create and place login button
    button_login = tk.Button(root, text="Sign In", command=login, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_login.pack(pady=5)

    # Create and place sign up button
    button_signup = tk.Button(root, text="Sign Up", command=open_signup, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_signup.pack(pady=5)

    # Run the main loop
    root.mainloop()

# Function to open playlist window
def open_playlist(user_id, return_function, user_name, existing_root):
    playlist_root = tk.Tk()
    playlist_root.title("Playlists")
    playlist_root.configure(bg=BACKGROUND_COLOR)
    center_window(playlist_root, 600, 400)

    label_playlists = tk.Label(playlist_root, text="Your Playlists", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_playlists.pack(pady=10)

    listbox_playlists = tk.Listbox(playlist_root)
    listbox_playlists.pack(fill=tk.BOTH, expand=True, pady=10)

    search_user_id = user_id  # Initialize with the current user_id

    def refresh_playlists(user_id_to_search=None):
        listbox_playlists.delete(0, tk.END)
        if user_id_to_search:
            cursor.execute("SELECT PlaylistID, Title FROM Playlist WHERE UserID=%s", (user_id_to_search,))
        else:
            cursor.execute("SELECT PlaylistID, Title FROM Playlist WHERE UserID=%s", (user_id,))
        playlists = cursor.fetchall()
        for playlist in playlists:
            listbox_playlists.insert(tk.END, f"{playlist[1]} ({playlist[0]})")

    refresh_playlists()

    def show_playlist_songs(event):
        selected_index = listbox_playlists.curselection()
        if selected_index:
            selected_playlist = listbox_playlists.get(selected_index)
            playlist_id = int(selected_playlist.split('(')[-1].split(')')[0])
            cursor.execute("SELECT song.Title FROM PlaylistContainsSong JOIN song ON PlaylistContainsSong.song_id = song.songid WHERE PlaylistContainsSong.playlist_id = %s", (playlist_id,))
            songs = cursor.fetchall()
            
            songs_root = tk.Toplevel()
            songs_root.title("Songs in Playlist")
            songs_root.configure(bg=BACKGROUND_COLOR)
            center_window(songs_root, 400, 300)
            label_songs = tk.Label(songs_root, text="Songs in Playlist", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
            label_songs.pack(pady=10)
            listbox_songs = tk.Listbox(songs_root)
            listbox_songs.pack(fill=tk.BOTH, expand=True, pady=10)
            
            def refresh_songs():
                listbox_songs.delete(0, tk.END)
                cursor.execute("SELECT song.Title FROM PlaylistContainsSong JOIN song ON PlaylistContainsSong.song_id = song.songid WHERE PlaylistContainsSong.playlist_id = %s", (playlist_id,))
                updated_songs = cursor.fetchall()
                if updated_songs:
                    for song in updated_songs:
                        listbox_songs.insert(tk.END, song[0])
                else:
                    listbox_songs.insert(tk.END, "No songs found in this playlist")

            if songs:
                for song in songs:
                    listbox_songs.insert(tk.END, song[0])
            else:
                listbox_songs.insert(tk.END, "No songs found in this playlist")

            def add_song_to_playlist():
                add_song_root = tk.Toplevel()
                add_song_root.title("Add Song to Playlist")
                center_window(add_song_root, 300, 200)

                label_song_name = tk.Label(add_song_root, text="Enter Song Name", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
                label_song_name.pack(pady=5)
                entry_song_name = tk.Entry(add_song_root)
                entry_song_name.pack(pady=5)

                def add_song():
                    song_name = entry_song_name.get()
                    cursor.execute("SELECT songid FROM song WHERE Title=%s", (song_name,))
                    song_record = cursor.fetchone()
                    if song_record:
                        song_id = song_record[0]
                        try:
                            cursor.execute("INSERT INTO PlaylistContainsSong (playlist_id, song_id) VALUES (%s, %s)", (playlist_id, song_id))
                            connection.commit()
                            messagebox.showinfo("Add Song", "Song added successfully")
                            add_song_root.destroy()
                            refresh_songs()
                        except Exception as error:
                            messagebox.showerror("Add Song", f"Error adding song: {error}")
                    else:
                        messagebox.showerror("Add Song", "Song not found")

                button_add = tk.Button(add_song_root, text="Add", command=add_song, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
                button_add.pack(pady=10)
                
                button_back = tk.Button(add_song_root, text="Back", command=add_song_root.destroy, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
                button_back.pack(pady=10)

                add_song_root.mainloop()

            def remove_song_from_playlist():
                remove_song_root = tk.Toplevel()
                remove_song_root.title("Remove Song from Playlist")
                remove_song_root.configure(bg=BACKGROUND_COLOR)
                center_window(remove_song_root, 300, 200)

                label_song_name = tk.Label(remove_song_root, text="Enter Song Name", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
                label_song_name.pack(pady=5)
                entry_song_name = tk.Entry(remove_song_root)
                entry_song_name.pack(pady=5)

                def remove_song():
                    song_name = entry_song_name.get()
                    cursor.execute("SELECT songid FROM song WHERE Title=%s", (song_name,))
                    song_record = cursor.fetchone()
                    if song_record:
                        song_id = song_record[0]
                        try:
                            cursor.execute("DELETE FROM PlaylistContainsSong WHERE playlist_id=%s AND song_id=%s", (playlist_id, song_id))
                            connection.commit()
                            messagebox.showinfo("Remove Song", "Song removed successfully")
                            remove_song_root.destroy()
                            refresh_songs()
                        except Exception as error:
                            messagebox.showerror("Remove Song", f"Error removing song: {error}")
                    else:
                        messagebox.showerror("Remove Song", "Song not found")

                button_remove = tk.Button(remove_song_root, text="Remove", command=remove_song, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
                button_remove.pack(pady=10)

                button_back = tk.Button(remove_song_root, text="Back", command=remove_song_root.destroy, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
                button_back.pack(pady=10)

                remove_song_root.mainloop()

            button_add_song = tk.Button(songs_root, text="Add Song to Playlist", command=add_song_to_playlist, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
            button_add_song.pack(pady=5)
            button_remove_song = tk.Button(songs_root, text="Remove Song from Playlist", command=remove_song_from_playlist, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
            button_remove_song.pack(pady=5)
            button_close = tk.Button(songs_root, text="Close", command=songs_root.destroy, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
            button_close.pack(pady=10)

            songs_root.mainloop()

    listbox_playlists.bind('<<ListboxSelect>>', show_playlist_songs)

    def search_user_playlists():
        nonlocal search_user_id  # Use the nonlocal keyword to modify the search_user_id variable in the outer function
        search_username = entry_search.get()
        cursor.execute("SELECT id FROM user_ WHERE user_name=%s", (search_username,))
        user_record = cursor.fetchone()
        if user_record:
            search_user_id = user_record[0]
            refresh_playlists(user_id_to_search=search_user_id)
        else:
            messagebox.showerror("Error", "User not found")

    label_search = tk.Label(playlist_root, text="Search User's Playlists", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_search.pack(pady=5)
    entry_search = tk.Entry(playlist_root)
    entry_search.pack(pady=5)
    button_search = tk.Button(playlist_root, text="Search", command=search_user_playlists, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_search.pack(pady=10)

    button_create_playlist = tk.Button(playlist_root, text="Create New Playlist", command=lambda: open_create_playlist(user_id, user_name, return_function, playlist_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_create_playlist.pack(pady=10)

    button_back = tk.Button(playlist_root, text="Back", command=lambda: go_back(playlist_root, return_function, user_id, user_name, existing_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    playlist_root.mainloop()





# Function to open create playlist window



# Function to open create playlist window
def open_create_playlist(user_id, user_name, return_function, existing_root):
    create_playlist_root = tk.Tk()
    create_playlist_root.title("Create Playlist")
    create_playlist_root.configure(bg=BACKGROUND_COLOR)
    center_window(create_playlist_root, 400, 200)

    label_playlist_name = tk.Label(create_playlist_root, text="Playlist Name", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_playlist_name.pack(pady=5)
    entry_playlist_name = tk.Entry(create_playlist_root)
    entry_playlist_name.pack(pady=5)

    label_playlist_type = tk.Label(create_playlist_root, text="Playlist Type", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_playlist_type.pack(pady=5)
    combo_playlist_type = ttk.Combobox(create_playlist_root, values=["private", "public"])
    combo_playlist_type.current(1)  # Default to public
    combo_playlist_type.pack(pady=5)

    def submit_new_playlist():
        playlist_name = entry_playlist_name.get()
        playlist_type = combo_playlist_type.get()
        try:
            cursor.execute("INSERT INTO Playlist (Title, UserID, Type) VALUES (%s, %s, %s)", (playlist_name, user_id, playlist_type))
            connection.commit()
            messagebox.showinfo("Create Playlist", "Playlist created successfully")
            create_playlist_root.destroy()
            return_function(user_id, user_name, existing_root)
        except Exception as error:
            messagebox.showerror("Create Playlist", f"Error creating playlist: {error}")

    button_submit = tk.Button(create_playlist_root, text="Submit", command=submit_new_playlist, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_submit.pack(pady=10)

    button_back = tk.Button(create_playlist_root, text="Back", command=lambda: go_back(create_playlist_root, open_playlist, user_id, user_name, existing_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    create_playlist_root.mainloop()





def open_playlist_songs(playlist_id, user_id, user_name, return_function, existing_root):
    songs_root = tk.Toplevel()  # Use Toplevel to create a new window without closing the current one
    songs_root.title("Playlist Songs")
    songs_root.configure(bg=BACKGROUND_COLOR)
    center_window(songs_root, 600, 400)

    label_songs = tk.Label(songs_root, text="Songs in Playlist", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_songs.pack(pady=10)

    listbox_songs = tk.Listbox(songs_root)
    listbox_songs.pack(fill=tk.BOTH, expand=True, pady=10)

    def refresh_songs():
        listbox_songs.delete(0, tk.END)
        cursor.execute("""
            SELECT song.Title, song.Lyrics
            FROM PlaylistContainsSong
            JOIN song ON PlaylistContainsSong.song_id = song.songid
            WHERE PlaylistContainsSong.playlist_id = %s
        """, (playlist_id,))
        songs = cursor.fetchall()
        for song in songs:
            listbox_songs.insert(tk.END, song[0])

    def on_song_select(event):
        selected_index = listbox_songs.curselection()
        if selected_index:
            selected_song = songs[selected_index[0]]
            show_lyrics_window(selected_song[1], songs_root, return_function, user_id, user_name)

    listbox_songs.bind('<<ListboxSelect>>', on_song_select)
    refresh_songs()

    def like_playlist():
        try:
            cursor.execute("SELECT * FROM UserLikePlaylist WHERE UserID=%s AND PlaylistID=%s", (user_id, playlist_id))
            like_record = cursor.fetchone()
            if like_record:
                messagebox.showinfo("Like Playlist", "You have already liked this playlist.")
            else:
                cursor.execute("INSERT INTO UserLikePlaylist (UserID, PlaylistID, LikeDate) VALUES (%s, %s, CURRENT_DATE)", (user_id, playlist_id))
                connection.commit()
                messagebox.showinfo("Like Playlist", "Playlist liked successfully")
                button_like.config(bg="green", state=tk.DISABLED)
        except Exception as error:
            messagebox.showerror("Like Playlist", f"Error liking playlist: {error}")

    bottom_frame = tk.Frame(songs_root)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

    

    # Check if the user has already liked this playlist
    cursor.execute("SELECT * FROM UserLikePlaylist WHERE UserID=%s AND PlaylistID=%s", (user_id, playlist_id))
    if cursor.fetchone():
        button_like.config(bg="LightGreen", state=tk.DISABLED)

    button_close = tk.Button(bottom_frame, text="Close", command=lambda: go_back(songs_root, return_function, user_id, user_name, existing_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_close.pack(side=tk.RIGHT, padx=10, pady=10)
    button_like = tk.Button(bottom_frame, text="Like Playlist", command=like_playlist, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_like.pack(side=tk.LEFT, padx=0, pady=0)
    songs_root.mainloop()






def open_add_concert(user_id, return_function, user_name):
    add_concert_root = tk.Tk()
    add_concert_root.title("Add Concert")
    add_concert_root.configure(bg=BACKGROUND_COLOR)
    center_window(add_concert_root, 400, 400)

    label_concert_name = tk.Label(add_concert_root, text="Concert Name", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_concert_name.pack(pady=5)
    entry_concert_name = tk.Entry(add_concert_root)
    entry_concert_name.pack(pady=5)

    label_date = tk.Label(add_concert_root, text="Date (YYYY-MM-DD)",font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_date.pack(pady=5)
    entry_date = tk.Entry(add_concert_root)
    entry_date.pack(pady=5)

    label_location = tk.Label(add_concert_root, text="Location", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_location.pack(pady=5)
    entry_location = tk.Entry(add_concert_root)
    entry_location.pack(pady=5)

    label_price = tk.Label(add_concert_root, text="Price", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_price.pack(pady=5)
    entry_price = tk.Entry(add_concert_root)
    entry_price.pack(pady=5)

    def add_concert():
        concert_name = entry_concert_name.get()
        date = entry_date.get()
        location = entry_location.get()
        price = entry_price.get()

        try:
            cursor.execute(
                "INSERT INTO Concert (Title, Date, Location, ArtistID, Price) VALUES (%s, %s, %s, %s, %s)",
                (concert_name, date, location, user_id, decimal.Decimal(price)))
            connection.commit()
            messagebox.showinfo("Add Concert", "Concert added successfully")
            add_concert_root.destroy()
            return_function(user_id, user_name)
        except Exception as error:
            messagebox.showerror("Add Concert", f"Error adding concert: {error}")

    button_submit = tk.Button(add_concert_root, text="Submit", command=add_concert, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_submit.pack(pady=10)

    button_back = tk.Button(add_concert_root, text="Back", command=lambda: go_back(add_concert_root, return_function, user_id, user_name),bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    add_concert_root.mainloop()

def open_buy_ticket(user_id, return_function, user_name):
    buy_ticket_root = tk.Tk()
    buy_ticket_root.title("Buy Ticket")
    buy_ticket_root.configure(bg=BACKGROUND_COLOR)
    center_window(buy_ticket_root, 400, 300)

    label_singer_name = tk.Label(buy_ticket_root, text="Singer Name", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_singer_name.pack(pady=5)
    entry_singer_name = tk.Entry(buy_ticket_root)
    entry_singer_name.pack(pady=5)

    def show_concerts():
        singer_name = entry_singer_name.get()
        cursor.execute("""
            SELECT Concert.ConcertID, Concert.Title, Concert.Date, Concert.Location, Concert.Price
            FROM Concert
            JOIN singer ON Concert.ArtistID = singer.user_id
            WHERE singer.stage_name = %s
        """, (singer_name,))
        concerts = cursor.fetchall()

        if concerts:
            listbox_concerts = tk.Listbox(buy_ticket_root)
            listbox_concerts.pack(fill=tk.BOTH, expand=True, pady=5)
            for concert in concerts:
                listbox_concerts.insert(tk.END, f"{concert[1]} - {concert[2]} - {concert[3]} - {concert[4]}")

            def on_concert_select(event):
                selected_index = listbox_concerts.curselection()
                if selected_index:
                    selected_concert = concerts[selected_index[0]]
                    open_ticket_quantity_window(user_id, selected_concert[0], selected_concert[4], return_function, user_name, buy_ticket_root)

            listbox_concerts.bind('<<ListboxSelect>>', on_concert_select)

        else:
            messagebox.showerror("Error", "No concerts found for this singer")

    button_show = tk.Button(buy_ticket_root, text="Show Concerts", command=show_concerts, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_show.pack(pady=10)

    button_back = tk.Button(buy_ticket_root, text="Back", command=lambda: go_back(buy_ticket_root, return_function, user_id, user_name), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    buy_ticket_root.mainloop()

def open_ticket_quantity_window(user_id, concert_id, concert_price, return_function, user_name, existing_root):
    quantity_root = tk.Tk()
    quantity_root.title("Ticket Quantity")
    quantity_root.configure(bg=BACKGROUND_COLOR)
    center_window(quantity_root, 400, 200)

    label_quantity = tk.Label(quantity_root, text="Enter the number of tickets:", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_quantity.pack(pady=5)
    entry_quantity = tk.Entry(quantity_root)
    entry_quantity.pack(pady=5)

    def submit_quantity():
        quantity = int(entry_quantity.get())
        total_price = concert_price * quantity

        cursor.execute("SELECT balance FROM wallet WHERE user_id=%s", (user_id,))
        wallet_record = cursor.fetchone()
        if wallet_record:
            balance = wallet_record[0]
            if balance >= total_price:
                new_balance = balance - total_price
                cursor.execute("UPDATE wallet SET balance=%s WHERE user_id=%s", (new_balance, user_id))
                for _ in range(quantity):
                    cursor.execute("INSERT INTO Ticket (ConcertID, UserID, PurchaseDate, Status) VALUES (%s, %s, %s, %s)",
                                   (concert_id, user_id, time.strftime("%Y-%m-%d"), "Valid"))
                connection.commit()
                messagebox.showinfo("Buy Ticket", "Tickets purchased successfully")
                quantity_root.destroy()
                existing_root.destroy()
                return_function(user_id, user_name)
            else:
                messagebox.showerror("Error", "Insufficient funds")
        else:
            messagebox.showerror("Error", "Wallet not found")

    button_submit = tk.Button(quantity_root, text="Submit", command=submit_quantity, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_submit.pack(pady=10)

    button_back = tk.Button(quantity_root, text="Back", command=quantity_root.destroy, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    quantity_root.mainloop()



def open_album_list(user_id, return_function, user_name):
    album_list_root = tk.Tk()
    album_list_root.title("Your Albums")
    album_list_root.configure(bg=BACKGROUND_COLOR)
    center_window(album_list_root, 400, 400)

    label_albums = tk.Label(album_list_root, text="Your Albums", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_albums.pack(pady=10)

    listbox_albums = tk.Listbox(album_list_root)
    listbox_albums.pack(fill=tk.BOTH, expand=True, pady=10)

    def refresh_albums():
        listbox_albums.delete(0, tk.END)
        cursor.execute("SELECT title FROM album WHERE artistid IN (SELECT id FROM singer WHERE user_id = %s)", (user_id,))
        albums = cursor.fetchall()
        for album in albums:
            listbox_albums.insert(tk.END, album[0])

    def show_albums():
        refresh_albums()

    button_show_albums = tk.Button(album_list_root, text="Show Albums", command=show_albums, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_show_albums.pack(pady=10)

    button_add_new_album = tk.Button(album_list_root, text="Add New Album", command=lambda: open_add_album(user_id, open_album_list, user_name, album_list_root, refresh_albums), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_add_new_album.pack(pady=10)

    button_back = tk.Button(album_list_root, text="Back", command=lambda: go_back(album_list_root, return_function, user_id, user_name), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    album_list_root.mainloop()




def open_playlist_songs(playlist_id, user_id, user_name, return_function, existing_root):
    songs_root = tk.Toplevel()  # Use Toplevel to create a new window without closing the current one
    songs_root.title("Playlist Songs")
    songs_root.configure(bg=BACKGROUND_COLOR)
    center_window(songs_root, 600, 400)

    label_songs = tk.Label(songs_root, text="Songs in Playlist", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_songs.pack(pady=10)

    listbox_songs = tk.Listbox(songs_root)
    listbox_songs.pack(fill=tk.BOTH, expand=True, pady=10)

    def refresh_songs():
        listbox_songs.delete(0, tk.END)
        cursor.execute("""
            SELECT song.Title
            FROM PlaylistContainsSong
            JOIN song ON PlaylistContainsSong.song_id = song.songid
            WHERE PlaylistContainsSong.playlist_id = %s
        """, (playlist_id,))
        songs = cursor.fetchall()
        for song in songs:
            listbox_songs.insert(tk.END, song[0])

    refresh_songs()

    button_back = tk.Button(songs_root, text="Back", command=songs_root.destroy, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    songs_root.mainloop()



def show_albums_window(user_id):
    show_albums_root = tk.Tk()
    show_albums_root.title("Show Albums")
    show_albums_root.configure(bg=BACKGROUND_COLOR)
    center_window(show_albums_root, 400, 400)

    label_albums = tk.Label(show_albums_root, text="Albums", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_albums.pack(pady=10)

    listbox_albums = tk.Listbox(show_albums_root)
    listbox_albums.pack(fill=tk.BOTH, expand=True, pady=10)

    cursor.execute("SELECT Title FROM album WHERE ArtistID=%s", (user_id,))
    albums = cursor.fetchall()
    print(f"Albums fetched: {albums}")  # افزودن لاگ برای نمایش آلبوم‌های دریافت شده
    for album in albums:
        listbox_albums.insert(tk.END, album[0])

    button_close = tk.Button(show_albums_root, text="Close", command=show_albums_root.destroy, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_close.pack(pady=10)

    show_albums_root.mainloop()



def open_following_followers(user_id, return_function, user_name, existing_root):
    follow_root = tk.Tk()
    follow_root.title("Following and Followers")
    follow_root.configure(bg=BACKGROUND_COLOR)
    center_window(follow_root, 600, 400)

    label_following = tk.Label(follow_root, text="Following", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_following.grid(row=0, column=0, padx=10, pady=10)

    label_followers = tk.Label(follow_root, text="Followers", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_followers.grid(row=0, column=1, padx=10, pady=10)

    listbox_following = tk.Listbox(follow_root)
    listbox_following.grid(row=1, column=0, padx=10, pady=10, sticky='ns')

    listbox_followers = tk.Listbox(follow_root)
    listbox_followers.grid(row=1, column=1, padx=10, pady=10, sticky='ns')


    label_search = tk.Label(follow_root, text="Search User to Follow", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_search.grid(row=2, column=0, padx=10, pady=10)

    entry_search_user = tk.Entry(follow_root)
    entry_search_user.grid(row=2, column=1, padx=10, pady=10)

    def follow_user():
        search_username = entry_search_user.get()
        cursor.execute("SELECT id FROM user_ WHERE user_name=%s", (search_username,))
        user_record = cursor.fetchone()
        if user_record:
            search_user_id = user_record[0]
            try:
                cursor.execute("INSERT INTO UserFollowUser (FollowerID, FollowingID) VALUES (%s, %s)", (user_id, search_user_id))
                connection.commit()
                messagebox.showinfo("Follow User", f"Now following {search_username}")
                refresh_follow_data()
            except Exception as error:
                messagebox.showerror("Follow User", f"Error following user: {error}")
        else:
            messagebox.showerror("Error", "User not found")

    button_follow = tk.Button(follow_root, text="Follow", command=follow_user, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_follow.grid(row=3, column=0, columnspan=2, pady=10)

    def refresh_follow_data():
        listbox_following.delete(0, tk.END)
        listbox_followers.delete(0, tk.END)

        cursor.execute("""
            SELECT user_.user_name
            FROM UserFollowUser
            JOIN user_ ON UserFollowUser.FollowingID = user_.id
            WHERE UserFollowUser.FollowerID = %s
        """, (user_id,))
        following_users = cursor.fetchall()
        for user in following_users:
            listbox_following.insert(tk.END, user[0])

        cursor.execute("""
            SELECT user_.user_name
            FROM UserFollowUser
            JOIN user_ ON UserFollowUser.FollowerID = user_.id
            WHERE UserFollowUser.FollowingID = %s
        """, (user_id,))
        followers = cursor.fetchall()
        for user in followers:
            listbox_followers.insert(tk.END, user[0])

    refresh_follow_data()

    button_back = tk.Button(follow_root, text="Back", command=lambda: go_back(follow_root, return_function, user_id, user_name, existing_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.grid(row=4, column=0, columnspan=2, pady=10)

    follow_root.mainloop()



def open_follow_artist(user_id, user_name, existing_root=None):
    follow_artist_root = tk.Tk()
    follow_artist_root.title("Follow Artist")
    follow_artist_root.configure(bg=BACKGROUND_COLOR)
    center_window(follow_artist_root, 600, 400)

    label_following_artists = tk.Label(follow_artist_root, text="Following Artists", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_following_artists.grid(row=0, column=0, padx=10, pady=10)

    listbox_following_artists = tk.Listbox(follow_artist_root)
    listbox_following_artists.grid(row=1, column=0, padx=10, pady=10, sticky='ns')

    label_search_artist = tk.Label(follow_artist_root, text="Search Artist to Follow", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_search_artist.grid(row=2, column=0, padx=10, pady=10)

    entry_search_artist = tk.Entry(follow_artist_root)
    entry_search_artist.grid(row=2, column=1, padx=10, pady=10)

    def follow_artist():
        search_artist_name = entry_search_artist.get()
        cursor.execute("SELECT id FROM singer WHERE stage_name=%s", (search_artist_name,))
        artist_record = cursor.fetchone()
        if artist_record:
            artist_id = artist_record[0]
            try:
                cursor.execute("INSERT INTO UserFollowSinger (UserID, SingerID) VALUES (%s, %s)", (user_id, artist_id))
                connection.commit()
                messagebox.showinfo("Follow Artist", f"Now following {search_artist_name}")
                refresh_following_artists()
            except Exception as error:
                messagebox.showerror("Follow Artist", f"Error following artist: {error}")
        else:
            messagebox.showerror("Error", "Artist not found")

    button_follow_artist = tk.Button(follow_artist_root, text="Follow", command=follow_artist, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_follow_artist.grid(row=3, column=0, columnspan=2, pady=10)

    def refresh_following_artists():
        listbox_following_artists.delete(0, tk.END)

        cursor.execute("""
            SELECT singer.stage_name
            FROM UserFollowSinger
            JOIN singer ON UserFollowSinger.SingerID = singer.id
            WHERE UserFollowSinger.UserID = %s
        """, (user_id,))
        following_artists = cursor.fetchall()
        for artist in following_artists:
            listbox_following_artists.insert(tk.END, artist[0])

    refresh_following_artists()

    button_back = tk.Button(follow_artist_root, text="Back", command=lambda: go_back(follow_artist_root, open_user_dashboard, user_id, user_name), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.grid(row=4, column=0, columnspan=2, pady=10)

    follow_artist_root.mainloop()



def open_purchased_tickets(user_id, user_name):
    tickets_root = tk.Tk()
    tickets_root.title("Purchased Tickets")
    tickets_root.configure(bg=BACKGROUND_COLOR)
    center_window(tickets_root, 600, 400)

    label_tickets = tk.Label(tickets_root, text="Purchased Tickets", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_tickets.pack(pady=10)

    listbox_tickets = tk.Listbox(tickets_root)
    listbox_tickets.pack(fill=tk.BOTH, expand=True, pady=10)

    cursor.execute("""
        SELECT Concert.Title, Concert.Date, Concert.Location, Ticket.PurchaseDate, Ticket.Status
        FROM Ticket
        JOIN Concert ON Ticket.ConcertID = Concert.ConcertID
        WHERE Ticket.UserID = %s
    """, (user_id,))
    tickets = cursor.fetchall()

    for ticket in tickets:
        listbox_tickets.insert(tk.END, f"Concert: {ticket[0]}, Date: {ticket[1]}, Location: {ticket[2]}, Purchase Date: {ticket[3]}, Status: {ticket[4]}")

    button_back = tk.Button(tickets_root, text="Back", command=lambda: go_back(tickets_root, open_user_dashboard, user_id, user_name), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    tickets_root.mainloop()


def show_album_songs(album_id, user_id, user_name, return_function, existing_root):
    songs_root = tk.Tk()
    songs_root.title("Album Songs")
    songs_root.configure(bg=BACKGROUND_COLOR)
    center_window(songs_root, 600, 400)

    label_songs = tk.Label(songs_root, text="Songs in Album", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_songs.pack(pady=10)

    listbox_songs = tk.Listbox(songs_root)
    listbox_songs.pack(fill=tk.BOTH, expand=True, pady=10)

    cursor.execute("SELECT Title, Lyrics FROM song WHERE AlbumID=%s", (album_id,))
    songs = cursor.fetchall()

    for song in songs:
        listbox_songs.insert(tk.END, song[0])

    def on_song_select(event):
        selected_index = listbox_songs.curselection()
        if selected_index:
            selected_song = songs[selected_index[0]]
            show_lyrics_window(selected_song[1], songs_root, return_function, user_id, user_name)

    listbox_songs.bind('<<ListboxSelect>>', on_song_select)

    button_close = tk.Button(songs_root, text="Close", command=lambda: go_back(songs_root, return_function, user_id, user_name, existing_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_close.pack(pady=10)

    songs_root.mainloop()



def open_album_songs(album_id, user_id, user_name, return_function, existing_root):
    songs_root = tk.Toplevel()
    songs_root.title("Album Songs")
    songs_root.configure(bg=BACKGROUND_COLOR)
    center_window(songs_root, 600, 400)

    label_songs = tk.Label(songs_root, text="Songs in Album", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_songs.pack(pady=10)

    listbox_songs = tk.Listbox(songs_root)
    listbox_songs.pack(fill=tk.BOTH, expand=True, pady=10)

    def refresh_songs():
        listbox_songs.delete(0, tk.END)
        cursor.execute("""
            SELECT song.Title, song.Lyrics
            FROM song
            WHERE song.AlbumID = %s
        """, (album_id,))
        songs = cursor.fetchall()
        for song in songs:
            listbox_songs.insert(tk.END, song[0])

    def on_song_select(event):
        selected_index = listbox_songs.curselection()
        if selected_index:
            selected_song = songs[selected_index[0]]
            show_lyrics_window(selected_song[1], songs_root, return_function, user_id, user_name)

    listbox_songs.bind('<<ListboxSelect>>', on_song_select)
    refresh_songs()

    def like_album():
        try:
            cursor.execute("SELECT * FROM UserLikeAlbum WHERE UserID=%s AND AlbumID=%s", (user_id, album_id))
            like_record = cursor.fetchone()      
            if like_record:
                messagebox.showinfo("Like Album", "You have already liked this album.")
            else:
                cursor.execute("INSERT INTO UserLikeAlbum (UserID, AlbumID) VALUES (%s, %s)", (user_id, album_id))
                connection.commit()
                messagebox.showinfo("Like Album", "Album liked successfully")
                button_like.config(bg="green", state=tk.DISABLED)
        except Exception as error:
            messagebox.showerror("Like Album", f"Error liking album: {error}")

    bottom_frame = tk.Frame(songs_root)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

    button_like = tk.Button(bottom_frame, text="Like Album", command=like_album, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_like.pack(side=tk.LEFT, padx=10, pady=10)

    # Check if the user has already liked this album
    cursor.execute("SELECT * FROM UserLikeAlbum WHERE UserID=%s AND AlbumID=%s", (user_id, album_id))
    if cursor.fetchone():
        button_like.config(bg="LightGreen", state=tk.DISABLED)

    button_close = tk.Button(bottom_frame, text="Close", command=lambda: go_back(songs_root, return_function, user_id, user_name, existing_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_close.pack(side=tk.RIGHT, padx=10, pady=10)

    songs_root.mainloop()




def open_all_songs(user_id, user_name):
    all_songs_root = tk.Tk()
    all_songs_root.title("All Songs")
    all_songs_root.configure(bg=BACKGROUND_COLOR)
    center_window(all_songs_root, 600, 400)

    table_frame = tk.Frame(all_songs_root)
    table_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

    columns = ('Song Name', 'Album Name')
    tree = ttk.Treeview(table_frame, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
    
    tree.pack(fill=tk.BOTH, expand=True)

    cursor.execute("""
        SELECT song.title AS song_title, album.title AS album_title
        FROM song
        LEFT JOIN album ON song.albumid = album.albumid
        WHERE song.artistid = (SELECT id FROM singer WHERE user_id = %s)
    """, (user_id,))
    songs = cursor.fetchall()

    for song_title, album_title in songs:
        album_name = album_title if album_title else "None"
        tree.insert('', tk.END, values=(song_title, album_name))

    button_back = tk.Button(all_songs_root, text="Back", command=lambda: go_back(all_songs_root, open_singer_dashboard, user_id, user_name), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    all_songs_root.mainloop()


def like_album(user_id, return_function, user_name, existing_root=None):
    like_album_root = tk.Tk()
    like_album_root.title("Like Album")
    like_album_root.configure(bg=BACKGROUND_COLOR)
    center_window(like_album_root, 400, 200)

    label_album_name = tk.Label(like_album_root, text="Album Name", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_album_name.pack(pady=5)
    entry_album_name = tk.Entry(like_album_root)
    entry_album_name.pack(pady=5)

    def submit_like_album():
        album_name = entry_album_name.get()
        cursor.execute("SELECT albumid FROM album WHERE title=%s", (album_name,))
        album_record = cursor.fetchone()
        if album_record:
            album_id = album_record[0]
            cursor.execute("SELECT * FROM UserLikeAlbum WHERE UserID=%s AND AlbumID=%s", (user_id, album_id))
            like_record = cursor.fetchone()
            if like_record:
                messagebox.showinfo("Like Album", "You have already liked this album.")
            else:
                cursor.execute("INSERT INTO UserLikeAlbum (UserID, AlbumID, LikeDate) VALUES (%s, %s, CURRENT_DATE)", (user_id, album_id))
                connection.commit()
                messagebox.showinfo("Like Album", "Album liked successfully")
                like_album_root.destroy()
                return_function(user_id, user_name, existing_root)
        else:
            messagebox.showerror("Error", "Album not found")


    button_submit = tk.Button(like_album_root, text="Submit", command=submit_like_album, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_submit.pack(pady=10)

    button_back = tk.Button(like_album_root, text="Back", command=lambda: go_back(like_album_root, return_function, user_id, user_name, existing_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    like_album_root.mainloop()

def like_playlist(user_id, return_function, user_name, existing_root=None):
    like_playlist_root = tk.Tk()
    like_playlist_root.title("Like Playlist")
    like_playlist_root.configure(bg=BACKGROUND_COLOR)
    center_window(like_playlist_root, 400, 200)

    label_playlist_name = tk.Label(like_playlist_root, text="Playlist Name", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_playlist_name.pack(pady=5)
    entry_playlist_name = tk.Entry(like_playlist_root)
    entry_playlist_name.pack(pady=5)

    def submit_like_playlist():
        playlist_name = entry_playlist_name.get()
        cursor.execute("SELECT playlistid FROM playlist WHERE title=%s", (playlist_name,))
        playlist_record = cursor.fetchone()
        if playlist_record:
            playlist_id = playlist_record[0]
            cursor.execute("SELECT * FROM userlikeplaylist WHERE userid=%s AND playlistid=%s", (user_id, playlist_id))
            like_record = cursor.fetchone()
            if like_record:
                messagebox.showinfo("Like Playlist", "You have already liked this playlist.")
            else:
                cursor.execute("INSERT INTO userlikeplaylist (userid, playlistid, likedate) VALUES (%s, %s, CURRENT_DATE)", (user_id, playlist_id))
                connection.commit()
                messagebox.showinfo("Like Playlist", "Playlist liked successfully")
                like_playlist_root.destroy()
                return_function(user_id, user_name, existing_root)
        else:
            messagebox.showerror("Error", "Playlist not found")

    button_submit = tk.Button(like_playlist_root, text="Submit", command=submit_like_playlist, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_submit.pack(pady=10)

    button_back = tk.Button(like_playlist_root, text="Back", command=lambda: go_back(like_playlist_root, return_function, user_id, user_name, existing_root), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    like_playlist_root.mainloop()


def show_song_options(song_id, lyrics, user_id, user_name, current_window):
   
    options_root = tk.Toplevel()
    options_root.title("Song Options")
    options_root.configure(bg=BACKGROUND_COLOR)
    center_window(options_root, 400, 300)

    
    label_song_id = tk.Label(options_root, text=f"Song ID: {song_id}", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_song_id.pack(pady=5)
    label_lyrics = tk.Label(options_root, text=f"Lyrics: {lyrics}", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
    label_lyrics.pack(pady=5)
    button_play = tk.Button(options_root, text="Play", command=lambda: play_song(song_id), bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_play.pack(pady=10)

   
    button_back = tk.Button(options_root, text="Back", command=options_root.destroy, bg=PRIMARY_COLOR, fg=FONT_COLOR, font=FONT)
    button_back.pack(pady=10)

    options_root.mainloop()

def play_song(song_id):
    
    messagebox.showinfo("Play Song", f"Playing song with ID: {song_id}")

def add_to_playlist(song_id, user_id):
    
    messagebox.showinfo("Add to Playlist", f"Adding song with ID: {song_id} to user's playlist")
# Run the login window initially
show_login_window()

# Close the database connection when done
cursor.close()
connection.close()
