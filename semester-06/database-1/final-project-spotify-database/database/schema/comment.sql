CREATE TABLE Comment (
    CommentID SERIAL PRIMARY KEY,
    Content TEXT NOT NULL,
    UserID INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    RelatedEntityID INT NOT NULL,
    EntityType VARCHAR(50) NOT NULL,
    FOREIGN KEY (UserID) REFERENCES user_(id),
    FORIEGN KEY (RelatedEntityID) REFRENCES song(songid)
);