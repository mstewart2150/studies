import nfl_data_py as nfl
import pandas as pd

pd.set_option('display.max_columns', None)

# Load play-by-play data for 2023
pbp = nfl.import_pbp_data([2024])
df_roster = (nfl.import_weekly_rosters([2024])[['team', 'player_name']].drop_duplicates()
                                                                       .reset_index()
                                                                       .drop(columns='index'))
df_roster['name_adjusted'] = str.split(df_roster['player_name'])


df_pass_plays = pbp[pbp['play_type'] == 'pass']

unique_qbs = (df_pass_plays[['passer_player_name']].drop_duplicates()
                                                   .reset_index()
                                                   .drop(columns='index'))

unique_receivers = (df_pass_plays[['receiver_player_name']].drop_duplicates()
                                                           .reset_index()
                                                           .drop(columns='index'))

