CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE user_tests (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    points INTEGER CHECK (points >= 1 AND points <= 10) NOT NULL ,
    description VARCHAR(100) NOT NULL ,
    date timestamp not null default (now() at time zone 'utc')
);