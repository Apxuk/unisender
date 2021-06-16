import pandas as pd
from datetime import datetime


events_df = pd.read_csv('data_engineer_task.csv', sep=';', parse_dates=['timestamp'], low_memory=True)

events_df.sort_values(['uid', 'timestamp'], inplace=True)
events_df['delta'] = events_df.groupby('uid')['timestamp'].diff()

events_df['session'] = events_df['uid'].astype(str) + '_' + (events_df['delta'] > pd.Timedelta(minutes=30)).cumsum().astype(str)

events_df.to_csv('events_with_sessions.csv', sep=';', index=False)

