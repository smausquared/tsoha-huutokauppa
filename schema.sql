CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR (50) UNIQUE,
    password TEXT
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name TEXT,
    starting_price INTEGER
);

CREATE TABLE auction_history (
    id SERIAL PRIMARY KEY,
    item_id INTEGER REFERENCES items,
    winner_id INTEGER REFERENCES users,
    price INTEGER,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO items (name, starting_price)
    VALUES ('Ghost Game', 300
);

INSERT INTO items (name, starting_price)
    VALUES ('Cereal box toy', 50
);
