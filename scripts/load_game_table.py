import pandas as pd
from utils.db_utils import get_engine

engine = get_engine()

genre_df = pd.read_sql("SELECT * FROM games.genre", engine)
publisher_df = pd.read_sql("SELECT * FROM games.publisher", engine)
platform_df = pd.read_sql("SELECT * FROM games.platform", engine)

game = pd.read_csv('../data/processed/game.csv')

# merge genre, publisher, and platform to include their ids
game = game.merge(genre_df, on='genre')
game = game.merge(publisher_df, on='publisher')
game = game.merge(platform_df, on='platform')

# keep these columns
game_cols = ['title', 'genre_id', 'platform_id', 'publisher_id', 'metacritic_score', 'release_date']
game = game[game_cols]

game.to_csv('../data/processed/game_final.csv', index=False)

# load to postgres
game.to_sql('game', engine, schema='games', if_exists='append', index=False)