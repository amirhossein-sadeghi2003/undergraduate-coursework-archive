import tkinter as tk
from tkinter import messagebox, ttk
import pyodbc
from datetime import datetime

def get_connection():
    try:
        server = 'DESKTOP-GSHKE0Q\\MSSQLSERVER01'
        database = 'AirlineDB'
        conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes')
        return conn
    except pyodbc.Error as e:
        messagebox.showerror("Connection Error", f"Failed to connect to the database: {str(e)}")
        raise

def search_flights():
    def execute_search():
        dep = departure_entry.get()
        arr = arrival_entry.get()
        date = date_entry.get()

        if not all([dep, arr, date]):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Invalid date format! Use YYYY-MM-DD (e.g., 2025-05-01)")
            return

        try:
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("EXEC searchFlights ?, ?, ?", dep, arr, date)
                    results = cursor.fetchall()
                    if not results:
                        messagebox.showinfo("No Results", "No flights found for the given criteria.")
                        return
                    show_results(search_window, results, ["Flight ID", "Departure Time", "Price", "From", "To", "Airline"])
        except pyodbc.Error as e:
            sqlstate = e.args[1] if len(e.args) > 1 else str(e)
            messagebox.showerror("Database Error", f"SQL Error: {sqlstate}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {str(e)}")

    search_window = tk.Toplevel(root)
    search_window.title("Search Flights")
   

    search_window.configure(bg = "#D6EAF8")
    screen_width = search_window.winfo_screenwidth()
    screen_height = search_window.winfo_screenheight()
    x = (screen_width // 2) - (400 // 2) 
    y = (screen_height // 2) - (300 // 2) - 200
    search_window.geometry(f"{400}x{300}+{x}+{y}")


    tk.Label(search_window, text="Departure City:").grid(row=0, column=0, padx=10, pady=5)
    departure_entry = tk.Entry(search_window)
    departure_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(search_window, text="Arrival City:").grid(row=1, column=0, padx=10, pady=5)
    arrival_entry = tk.Entry(search_window)
    arrival_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(search_window, text="Travel Date (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=5)
    date_entry = tk.Entry(search_window)
    date_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(search_window, text="Search Flights", bg = "#A9DFBF",command=execute_search).grid(row=3, column=0, columnspan=2, pady=10)

def add_new_ticket():
    def submit_ticket():
        try:
            flight_id = int(flight_id_entry.get())
            customer_id = int(customer_id_entry.get())
            ticket_id = int(ticket_id_entry.get())
            departure_datetime = departure_datetime_entry.get()
            departure_loc = departure_loc_entry.get()
            arrival_loc = arrival_loc_entry.get()
            price = float(price_entry.get())

            if not all([flight_id_entry.get(), customer_id_entry.get(), ticket_id_entry.get(),
                        departure_datetime_entry.get(), departure_loc_entry.get(),
                        arrival_loc_entry.get(), price_entry.get()]):
                messagebox.showerror("Error", "All fields are required!")
                return

            try:
                datetime.strptime(departure_datetime, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                messagebox.showerror("Error", "Invalid date format! Use YYYY-MM-DD HH:MM:SS")
                return

            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("EXEC addNewTicket ?, ?, ?, ?, ?, ?, ?", 
                                   flight_id, customer_id, ticket_id, departure_datetime,
                                   departure_loc, arrival_loc, price)
                    conn.commit()
                    messagebox.showinfo("Success", "Ticket added successfully!")
                    ticket_window.destroy()
        except pyodbc.Error as e:
            sqlstate = e.args[1] if len(e.args) > 1 else str(e)
            messagebox.showerror("Database Error", f"Failed to add ticket: {sqlstate}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for IDs and price!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ticket_window = tk.Toplevel(root)
    ticket_window.title("Add New Ticket")


    ticket_window.configure(bg = "#D6EAF8")
    screen_width = ticket_window.winfo_screenwidth()
    screen_height = ticket_window.winfo_screenheight()
    x = (screen_width // 2) - (400 // 2) 
    y = (screen_height // 2) - (300 // 2) - 200
    ticket_window.geometry(f"{400}x{300}+{x}+{y}")



    tk.Label(ticket_window, text="Flight ID:").grid(row=0, column=0)
    flight_id_entry = tk.Entry(ticket_window)
    flight_id_entry.grid(row=0, column=1)

    tk.Label(ticket_window, text="Customer ID:").grid(row=1, column=0)
    customer_id_entry = tk.Entry(ticket_window)
    customer_id_entry.grid(row=1, column=1)

    tk.Label(ticket_window, text="Ticket ID:").grid(row=2, column=0)
    ticket_id_entry = tk.Entry(ticket_window)
    ticket_id_entry.grid(row=2, column=1)

    tk.Label(ticket_window, text="Departure DateTime (YYYY-MM-DD HH:MM:SS):").grid(row=3, column=0)
    departure_datetime_entry = tk.Entry(ticket_window)
    departure_datetime_entry.grid(row=3, column=1)

    tk.Label(ticket_window, text="Departure Location:").grid(row=4, column=0)
    departure_loc_entry = tk.Entry(ticket_window)
    departure_loc_entry.grid(row=4, column=1)

    tk.Label(ticket_window, text="Arrival Location:").grid(row=5, column=0)
    arrival_loc_entry = tk.Entry(ticket_window)
    arrival_loc_entry.grid(row=5, column=1)

    tk.Label(ticket_window, text="Price:").grid(row=6, column=0)
    price_entry = tk.Entry(ticket_window)
    price_entry.grid(row=6, column=1)

    tk.Button(ticket_window, text="Submit", bg = "#A9DFBF",command=submit_ticket).grid(row=7, column=0, columnspan=2)

def cancel_reservation():
    def submit_cancel():
        try:
            reservation_id = int(reservation_id_entry.get())

            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("EXEC cancelReservation ?", reservation_id)
                    conn.commit()
                    messagebox.showinfo("Success", "Reservation cancelled successfully!")
                    cancel_window.destroy()
        except pyodbc.Error as e:
            sqlstate = e.args[1] if len(e.args) > 1 else str(e)
            messagebox.showerror("Database Error", f"Failed to cancel reservation: {sqlstate}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid reservation ID!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    cancel_window = tk.Toplevel(root)
    cancel_window.title("Cancel Reservation")

    cancel_window.configure(bg = "#D6EAF8")
    screen_width = cancel_window.winfo_screenwidth()
    screen_height = cancel_window.winfo_screenheight()
    x = (screen_width // 2) - (200 // 2) 
    y = (screen_height // 2) - (100 // 2) - 200
    cancel_window.geometry(f"{200}x{100}+{x}+{y}")


    tk.Label(cancel_window, text="Reservation ID:").grid(row=0, column=0)
    reservation_id_entry = tk.Entry(cancel_window)
    reservation_id_entry.grid(row=0, column=1)

    tk.Button(cancel_window, text="Cancel Reservation", bg = "#A9DFBF",command=submit_cancel).grid(row=1, column=0, columnspan=2)

def get_sold_tickets_count():
    def show_count():
        try:
            flight_id = int(flight_id_entry.get())
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT dbo.getSoldTicketsCount(?)", flight_id)
                    count = cursor.fetchone()[0]
                    messagebox.showinfo("Sold Tickets Count", f"Number of tickets sold for flight {flight_id}: {count}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid flight ID!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    count_window = tk.Toplevel(root)
    count_window.title("Sold Tickets Count")


    count_window.configure(bg = "#D6EAF8")
    screen_width = count_window.winfo_screenwidth()
    screen_height = count_window.winfo_screenheight()
    x = (screen_width // 2) - (200 // 2) 
    y = (screen_height // 2) - (100 // 2) - 200
    count_window.geometry(f"{200}x{100}+{x}+{y}")


    tk.Label(count_window, text="Flight ID:").grid(row=0, column=0)
    flight_id_entry = tk.Entry(count_window)
    flight_id_entry.grid(row=0, column=1)

    tk.Button(count_window, text="Show Count", bg = "#A9DFBF",command=show_count).grid(row=1, column=0, columnspan=2)

def get_reservation_status():
    def show_status():
        try:
            customer_id = int(customer_id_entry.get())
            ticket_id = int(ticket_id_entry.get())
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT dbo.getReservationStatus(?, ?)", customer_id, ticket_id)
                    status = cursor.fetchone()[0]
                    messagebox.showinfo("Reservation Status", f"Reservation status for customer {customer_id} and ticket {ticket_id}: {status}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid IDs!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    status_window = tk.Toplevel(root)
    status_window.title("Reservation Status")

    status_window.configure(bg = "#D6EAF8")
    screen_width = status_window.winfo_screenwidth()
    screen_height = status_window.winfo_screenheight()
    x = (screen_width // 2) - (200 // 2) 
    y = (screen_height // 2) - (100 // 2) - 200
    status_window.geometry(f"{200}x{100}+{x}+{y}")


    tk.Label(status_window, text="Customer ID:").grid(row=0, column=0)
    customer_id_entry = tk.Entry(status_window)
    customer_id_entry.grid(row=0, column=1)

    tk.Label(status_window, text="Ticket ID:").grid(row=1, column=0)
    ticket_id_entry = tk.Entry(status_window)
    ticket_id_entry.grid(row=1, column=1)

    tk.Button(status_window, text="Show Status", bg = "#A9DFBF",command=show_status).grid(row=2, column=0, columnspan=2)

def get_total_paid_by_customer():
    def show_total():
        try:
            customer_id = int(customer_id_entry.get())
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT dbo.getTotalPaidByCustomer(?)", customer_id)
                    total = cursor.fetchone()[0]
                    messagebox.showinfo("Total Paid", f"Total amount paid by customer {customer_id}: {total}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid customer ID!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    total_window = tk.Toplevel(root)
    total_window.title("Total Paid by Customer")

    total_window.configure(bg = "#D6EAF8")
    screen_width = total_window.winfo_screenwidth()
    screen_height = total_window.winfo_screenheight()
    x = (screen_width // 2) - (200 // 2) 
    y = (screen_height // 2) - (100 // 2) - 200
    total_window.geometry(f"{200}x{100}+{x}+{y}")


    tk.Label(total_window, text="Customer ID:").grid(row=0, column=0)
    customer_id_entry = tk.Entry(total_window)
    customer_id_entry.grid(row=0, column=1)

    tk.Button(total_window, text="Show Total", bg = "#A9DFBF",command=show_total).grid(row=1, column=0, columnspan=2)

def show_flight_tickets():
    flight_tickets_window = tk.Toplevel(root)
    flight_tickets_window.title("Flight Tickets")
    flight_tickets_window.configure(bg = "#D6EAF8")
    screen_width = flight_tickets_window.winfo_screenwidth()
    screen_height = flight_tickets_window.winfo_screenheight()
    x = (screen_width // 2) - (1200 // 2) 
    y = (screen_height // 2) - (300 // 2) - 200
    flight_tickets_window.geometry(f"{1200}x{300}+{x}+{y}")
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM flightTickets")
                results = cursor.fetchall()
                show_results(flight_tickets_window, results, ["Flight ID", "Departure Time", "Total Capacity", "Flight Price", "Ticket ID", "Departure DateTime", "Departure Location", "Arrival Location", "Ticket Price", "Customer ID"])
    except Exception as e:
        messagebox.showerror("Error", str(e))
    tk.Button(flight_tickets_window, text="Show Flight Tickets", bg = "#A9DFBF",command=show_flight_tickets).pack(pady=10)

def show_ticket_details():
    ticket_details_window = tk.Toplevel(root)
    ticket_details_window.title("Ticket Details")
    ticket_details_window.configure(bg = "#D6EAF8")
    screen_width = ticket_details_window.winfo_screenwidth()
    screen_height = ticket_details_window.winfo_screenheight()
    x = (screen_width // 2) - (800 // 2) 
    y = (screen_height // 2) - (500 // 2) - 200
    ticket_details_window.geometry(f"{800}x{500}+{x}+{y}")


    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM ticketDetails")
                results = cursor.fetchall()
                show_results(ticket_details_window, results, ["Ticket ID", "Departure DateTime", "Departure Location", "Arrival Location", "Ticket Price", "Customer Name", "Flight ID", "Airline"])
    except Exception as e:
        messagebox.showerror("Error", str(e))
    tk.Button(ticket_details_window, text="Show Ticket Details", bg = "#A9DFBF",command=show_ticket_details).pack(pady=10)

def show_active_reservations():
    active_reservations_window = tk.Toplevel(root)
    active_reservations_window.title("Active Reservations")
    active_reservations_window.configure(bg = "#D6EAF8")
    screen_width = active_reservations_window.winfo_screenwidth()
    screen_height = active_reservations_window.winfo_screenheight()
    x = (screen_width // 2) - (800 // 2) 
    y = (screen_height // 2) - (500 // 2) - 200
    active_reservations_window.geometry(f"{800}x{500}+{x}+{y}")

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM activeReservations")
                results = cursor.fetchall()
                show_results(active_reservations_window, results, ["Reservation ID", "Customer Name", "Departure Location", "Arrival Location", "Travel Date", "Status", "Paid Amount"])
    except Exception as e:
        messagebox.showerror("Error", str(e))
    tk.Button(active_reservations_window, text="Show Active Reservations",bg = "#A9DFBF" , command=show_active_reservations).pack(pady=10)

def show_results(window, results, columns):
    result_frame = tk.Frame(window)
    result_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    window.grid_rowconfigure(4, weight=1)
    window.grid_columnconfigure(0, weight=1)

    tree = ttk.Treeview(result_frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for row in results:
        formatted_row = []
        for value in row:
            if isinstance(value, datetime):
                formatted_row.append(value.strftime('%Y-%m-%d %H:%M:%S'))
            else:
                formatted_row.append(str(value))
        tree.insert("", tk.END, values=formatted_row)
    tree.pack(expand=True, fill=tk.BOTH)
root = tk.Tk()
root.title("Airline Reservation System")
width = 500
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (width // 2) 
y = (screen_height // 2) - (height // 2) - 200
root.configure(bg = "#D6EAF8")
root.geometry(f"{width}x{height}+{x}+{y}")
tk.Button(root, text="Search Flights", command=search_flights,bg = "#A9DFBF",width=20).pack(pady=5)
tk.Button(root, text="Add New Ticket", command=add_new_ticket, bg = "#A9DFBF", width=20).pack(pady=5)
tk.Button(root, text="Cancel Reservation", command=cancel_reservation, bg = "#A9DFBF", width=20).pack(pady=5)
tk.Button(root, text="Sold Tickets Count", command=get_sold_tickets_count, bg = "#A9DFBF", width=20).pack(pady=5)
tk.Button(root, text="Reservation Status", command=get_reservation_status,bg = "#A9DFBF" , width=20).pack(pady=5)
tk.Button(root, text="Total Paid by Customer", command=get_total_paid_by_customer, bg = "#A9DFBF", width=20).pack(pady=5)
tk.Button(root, text="Show Flight Tickets", command=show_flight_tickets,bg = "#A9DFBF", width=20).pack(pady=5)
tk.Button(root, text="Show Ticket Details", command=show_ticket_details,bg = "#A9DFBF", width=20).pack(pady=5)
tk.Button(root, text="Show Active Reservations", command=show_active_reservations, bg = "#A9DFBF" , width=20).pack(pady=5)
root.mainloop()

