CREATE TABLE Concert (
    ConcertID SERIAL PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Date DATE NOT NULL,
    Location VARCHAR(255) NOT NULL,
    ArtistID INT,
    Price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (ArtistID) REFERENCES Singer(user_id)
);
