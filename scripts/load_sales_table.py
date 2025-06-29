import pandas as pd
from utils.db_utils import get_engine

engine = get_engine()

game_df = pd.read_sql_query("SELECT * FROM games.game", engine)

game = pd.read_csv('../data/processed/game_final.csv')
sales = pd.read_csv('../data/processed/sales.csv')

# merge game ids to sales
game = game.merge(game_df, on=['title', 'platform_id'])

# add game_id to sales data
sales['game_id'] = game['game_id']

# columns to keep
sales_cols = ['game_id', 'na_sales', 'jp_sales', 'pal_sales', 'other_sales', 'total_sales']
sales = sales[sales_cols]

sales.to_csv('../data/processed/sales_final.csv', index=False)

# load to postgres
sales.to_sql('sales', engine, schema='games', if_exists='append', index=False)