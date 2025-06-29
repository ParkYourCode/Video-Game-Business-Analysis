ALTER TABLE games.genre ADD CONSTRAINT unique_genre UNIQUE (genre);
ALTER TABLE games.publisher ADD CONSTRAINT unique_publisher UNIQUE (publisher);
ALTER TABLE games.platform ADD CONSTRAINT unique_platform UNIQUE (platform);
ALTER TABLE games.game ADD CONSTRAINT unique_game UNIQUE (title, platform_id);
ALTER TABLE games.sales ADD CONSTRAINT unique_sales UNIQUE (game_id);