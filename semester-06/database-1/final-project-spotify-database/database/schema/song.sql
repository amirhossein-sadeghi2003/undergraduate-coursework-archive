CREATE TABLE song (
    SongID SERIAL PRIMARY KEY,
    Title VARCHAR(100),
    Genre VARCHAR(50),
    ArtistID INTEGER REFERENCES singer(user_id),
    AlbumID INTEGER REFERENCES album(AlbumID),
    Lyrics TEXT,
    Status VARCHAR(20)
);
