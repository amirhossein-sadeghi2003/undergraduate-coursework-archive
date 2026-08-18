CREATE TABLE UserFollowSinger (
    UserID INT,
    SingerID INT,
    FOREIGN KEY (UserID) REFERENCES user_(id),
    FOREIGN KEY (SingerID) REFERENCES singer(id)
);
