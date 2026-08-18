CREATE TABLE wallet (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES user_(id),
    balance NUMERIC DEFAULT 0
);
