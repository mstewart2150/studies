import nfl_data_py as nfl

# Load play-by-play data for 2023
pbp = nfl.import_pbp_data([2023])

# Show first few rows
print(pbp.head())
