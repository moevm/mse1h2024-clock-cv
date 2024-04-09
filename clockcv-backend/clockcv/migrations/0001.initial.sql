CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE user_tests (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP DEFAULT (datetime('now','localtime')),
    points INTEGER CHECK (points >= 1 AND points <= 10) NOT NULL ,
    description VARCHAR(100) NOT NULL ,
    user_id INTEGER REFERENCES users(id)
);