import pandas as pd
matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')
print(matches.head())
print(deliveries.head())
top_batsmen = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)
print(top_batsmen)
# Count how many matches each team won
wins = matches['winner'].value_counts()

# Also count total matches per team (since some teams appear in both team1 and team2)
total_matches = matches['team1'].value_counts() + matches['team2'].value_counts()

# Calculate win rate by team
win_rate = (wins / total_matches) * 100

print(win_rate.sort_values(ascending=False))
toss_wins = (matches['toss_winner'] == matches['winner'])
toss_win_percentage = toss_wins.mean() * 100

print(f"Percentage of toss winners who also win the match: {toss_win_percentage:.2f}%")
toss_win_percentage_df = pd.DataFrame({'Toss Win %': [toss_win_percentage]})
toss_win_percentage_df.to_csv('toss_win_percentage.csv', index=False)

win_rate.to_csv('team_win_rate.csv')
