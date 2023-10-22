CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR (50) UNIQUE,
    role INTEGER,
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

CREATE TABLE feedback (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    title VARCHAR (50),
    content VARCHAR (1000),
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO items (name, starting_price)
    VALUES ('Ghost Game', 300
);

INSERT INTO items (name, starting_price)
    VALUES ('Mona Lisa, authentic', 5
);

INSERT INTO items (name, starting_price)
    VALUES ('Kawasaki motorcycle', 400
);

INSERT INTO auction_history (item_id, winner_id, price, time)
    VALUES (2, NULL, 5, NOW()
);

INSERT INTO auction_history (item_id, winner_id, price, time)
    VALUES (1, NULL, 300, NOW()
);
