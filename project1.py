# Kaplan, Raphael
# Computer Programming, period 4
# Assignment: Project 1
# 2 October 2026

Team_Average = 0.253 # I Started with this value because it is the overall average of the team. I will compare this to the cumulative average of the 5 players.
MLB_Average  = 0.245

players = []
total_ab = 0
total_hits = 0

for player in range(1, 6): # Loop through 5 times to get the input for each player
    name = input(f"Player {player} Name: ")
    ab = int(input(f"Player {player} At-bats: "))
    hits = int(input(f"Player {player} Hits: "))
    ave = hits / ab
    players.append((name, ab, hits, ave))

    total_ab = total_ab + ab # I added this line to add the total number of at-bats for all players
    total_hits = total_hits + hits

cumulative_ave = total_hits / total_ab

print("\nNAME\tAB\tHITS\tAVE") # Beginning of printing the output of the players' data
print("----\t--\t----\t---")
for player in players:
    print(f"{player[0]}\t{player[1]}\t{player[2]}\t{player[3]}")
print(f"TOTAL\t{total_ab}\t{total_hits}\t{cumulative_ave}")

# Comparing with Team Average
if Team_Average > cumulative_ave:
    team_comp = "higher"
else:
    team_comp = "lower"

# Comparing with MLB Average
if MLB_Average > cumulative_ave:
    mlb_comp = "higher"
else:
    mlb_comp = "lower"

print(f"Teams overall average is {team_comp} than the 5 players average.")
print(f"MLBs overall average is {mlb_comp} than the 5 players average.")