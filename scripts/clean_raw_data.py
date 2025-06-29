import pandas as pd
from utils.cleaning_utils import extract_lookup_table, extract_columns_into_table, drop_columns

# fetch data
game = pd.read_csv('../data/raw/sales.csv')

# drop unused columns
game = game.drop(columns=['developer', 'last_update'])

# drop rows that have no sales data
sales = ['total_sales', 'na_sales', 'jp_sales', 'pal_sales', 'other_sales']
game = game.dropna(subset=sales, how='all')

# drop rows without metacritic score and release date
game = game.dropna(subset=['critic_score', 'release_date'])

# drop duplicate rows based on title and console
game = game.drop_duplicates(subset=['title', 'console'], keep='first')

# rename console -> platform
game.rename(columns={'console': 'platform'}, inplace=True)

# rename critic_score -> metacritic_score
game.rename(columns={'critic_score': 'metacritic_score'}, inplace=True)

# convert release date to datetime objects
game['release_date'] = pd.to_datetime(game['release_date'], format='%m/%d/%y')

# convert metacritic score to integers from 0~100
game['metacritic_score'] = (pd.to_numeric(game['metacritic_score'], downcast='integer', errors='coerce') * 10).astype('Int64')

# extract lookup tables (genre, publisher, platform, )
genre = extract_lookup_table(game, 'genre')
publisher = extract_lookup_table(game, 'publisher')
platform = extract_lookup_table(game, 'platform')

sales_col = ['title', 'platform', 'total_sales', 'na_sales', 'jp_sales', 'pal_sales', 'other_sales']

# extract sales columns (total, na, jp, pal, and other)
sales = extract_columns_into_table(game, sales_col)

# save all tables as csv
game.to_csv('../data/processed/game.csv', index=False)
genre.to_csv('../data/processed/genre.csv', index=False)
publisher.to_csv('../data/processed/publisher.csv', index=False)
platform.to_csv('../data/processed/platform.csv', index=False)
sales.to_csv('../data/processed/sales.csv', index=False)