import pandas as pd

# input
num_concerts = int(input('Enter the number of concerts: '))
concerts_data = []
for i in range(num_concerts):
    artist = input(f'Enter artist name for concert {i+1}: ')
    venue = input(f'Enter venue name for concert {i+1}: ')
    date = input(f'Enter date for concert {i+1} (YYYY-MM-DD): ')
    concerts_data.append({'artist': artist, 'venue': venue, 'date': date})


concerts = pd.DataFrame(concerts_data) # dataframe


concerts['date'] = pd.to_datetime(concerts['date'])

# Extract year and month from date
concerts['year_month'] = concerts['date'].dt.to_period('M')

# Cross product of artist and venue
artist_venue_pairs = pd.MultiIndex.from_product([concerts['artist'].unique(), concerts['venue'].unique()], names=['artist', 'venue'])

# Count concerts per (artist, venue) and per year-month
concerts_count = concerts.groupby(['year_month', 'artist', 'venue']).size().unstack(fill_value=0)

# Reindex the DataFrame to include all artist-venue pairs
concerts_count = concerts_count.reindex(columns=artist_venue_pairs, fill_value=0)

print(concerts_count)


