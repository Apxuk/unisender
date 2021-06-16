import pandas as pd

events_df = pd.read_csv('events_with_sessions.csv', sep=';', parse_dates=['timestamp'])


events_df = events_df[events_df['eventCategory'].isin(['1st_step', '2nd_step', '3rd_step', '4th_step', '5th_step'])]
events_df['date'] = events_df['timestamp'].values.astype(dtype='datetime64[D]')
sessions_analysis_df = events_df.groupby(['date', 'eventCategory'])['session'].nunique().reset_index()
sessions_analysis_df.sort_values(['date', 'eventCategory'], inplace=True)

sessions_analysis_df.to_csv('sessions_analysis.csv', sep=';', index=False)
