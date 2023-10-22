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

CREATE TABLE bots (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    bid_amount INTEGER
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

INSERT INTO items (name, starting_price)
    VALUES ('uPhone 12', 200
);

INSERT INTO items (name, starting_price)
    VALUES ('2 hours of high-quality programmer labor', 50
);

INSERT INTO items (name, starting_price)
    VALUES ('Playstendo switchable', 45
);

INSERT INTO items (name, starting_price)
    VALUES ('2022 Ferrari', 80000
);

INSERT INTO items (name, starting_price)
    VALUES ('Precious ring', 100
);

INSERT INTO items (name, starting_price)
    VALUES ('X company', 50000000
);

INSERT INTO items (name, starting_price)
    VALUES ('5kg Sweet strawberries', 10
);

INSERT INTO items (name, starting_price)
    VALUES ('Election tampering', 50000
);

INSERT INTO auction_history (item_id, winner_id, price, time)
    VALUES (2, NULL, 5, NOW()
);

INSERT INTO auction_history (item_id, winner_id, price, time)
    VALUES (1, NULL, 300, NOW()
);

INSERT INTO users (username, role, password)
    VALUES ('MoneyMcBags', 0, NULL
);

INSERT INTO bots (user_id, bid_amount)
    VALUES (1, 200
);

INSERT INTO users (username, role, password)
    VALUES ('imTwelve', 0, NULL
);

INSERT INTO bots (user_id, bid_amount)
    VALUES (2, 69
);

INSERT INTO users (username, role, password)
    VALUES ('theLegend27', 0, NULL
);

INSERT INTO bots (user_id, bid_amount)
    VALUES (3, 27
);

INSERT INTO users (username, role, password)
    VALUES ('bigCoach', 0, NULL
);

INSERT INTO bots (user_id, bid_amount)
    VALUES (4, 10
);

INSERT INTO users (username, role, password)
    VALUES ('Emppu', 0, NULL
);

INSERT INTO bots (user_id, bid_amount)
    VALUES (5, 15
);

INSERT INTO users (username, role, password)
    VALUES ('James', 0, NULL
);

INSERT INTO bots (user_id, bid_amount)
    VALUES (6, 20
);
