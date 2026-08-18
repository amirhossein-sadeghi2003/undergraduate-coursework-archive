CREATE TABLE singer (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE,
    stage_name VARCHAR(100),
    genre VARCHAR(50)
);
