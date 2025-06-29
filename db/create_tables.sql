-- Genre table
CREATE TABLE IF NOT EXISTS games.genre (
    genre_id SERIAL PRIMARY KEY,
    genre VARCHAR(255) NOT NULL
);

-- Platform table
CREATE TABLE IF NOT EXISTS games.platform (
    platform_id SERIAL PRIMARY KEY,
    platform VARCHAR(255) NOT NULL
);

-- Publisher table (missing in your script)
CREATE TABLE IF NOT EXISTS games.publisher (
    publisher_id SERIAL PRIMARY KEY,
    publisher VARCHAR(255) NOT NULL
);

-- Game table
CREATE TABLE IF NOT EXISTS games.game (
    game_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    genre_id INT NOT NULL,
    platform_id INT NOT NULL,
    publisher_id INT NOT NULL,
    metacritic_score INT NOT NULL,
    release_date DATE NOT NULL,
    CONSTRAINT fk_genre FOREIGN KEY (genre_id) REFERENCES games.genre(genre_id),
    CONSTRAINT fk_platform FOREIGN KEY (platform_id) REFERENCES games.platform(platform_id),
    CONSTRAINT fk_publisher FOREIGN KEY (publisher_id) REFERENCES games.publisher(publisher_id)
);

-- Sales table
CREATE TABLE IF NOT EXISTS games.sales (
    sales_id SERIAL PRIMARY KEY,
    game_id INT UNIQUE NOT NULL,
    na_sales FLOAT,
    jp_sales FLOAT,
    pal_sales FLOAT,
    other_sales FLOAT,
    total_sales FLOAT,
    CONSTRAINT fk_sales_game FOREIGN KEY (game_id) REFERENCES games.game(game_id)
);