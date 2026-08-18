CREATE TABLE user_ (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(20),
    password VARCHAR(15),
    birth_year VARCHAR(7),
    email VARCHAR(30),
    location VARCHAR(10),
    subscription_type BOOLEAN DEFAULT FALSE
);

