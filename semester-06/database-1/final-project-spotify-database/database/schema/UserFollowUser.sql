CREATE TABLE UserFollowUser (
    FollowerID INT REFERENCES user_(id),
    FollowingID INT REFERENCES user_(id),
    PRIMARY KEY (FollowerID, FollowingID)
);
