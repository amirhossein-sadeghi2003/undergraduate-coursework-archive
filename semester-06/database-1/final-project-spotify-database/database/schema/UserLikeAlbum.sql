CREATE TABLE IF NOT EXISTS UserLikeAlbum (
    UserID INT REFERENCES user_(id),
    AlbumID INT REFERENCES album(albumid),
    LikeDate DATE,
    PRIMARY KEY (UserID, AlbumID)
);
