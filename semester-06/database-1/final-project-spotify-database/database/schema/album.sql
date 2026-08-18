CREATE TABLE album (
    AlbumID SERIAL PRIMARY KEY,
    Title VARCHAR(100),
    ReleaseYear INTEGER,
    ArtistID INTEGER REFERENCES singer(id),
    Status VARCHAR(20)
);
