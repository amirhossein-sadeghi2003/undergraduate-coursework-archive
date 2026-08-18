CREATE TABLE PlaylistContainsSong (
    playlist_id INT,
    song_id INT,
    PRIMARY KEY (playlist_id, song_id),
    FOREIGN KEY (playlist_id) REFERENCES Playlist(PlaylistID),
    FOREIGN KEY (song_id) REFERENCES Song(SongID)
);
