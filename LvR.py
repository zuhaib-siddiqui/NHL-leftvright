import pandas as pd
import matplotlib.pyplot as plt

#Data
df = pd.read_csv("NHL left hand vs right hand.csv")
pd.set_option('display.max.rows', None)
pd.set_option('display.max.columns', None)

#Iterating through hand stats per year
initial_year = 0
for year in df:
    output = (df.Year[initial_year])
    print(output)
    left_hand = df.loc[(df.Year == output) & (df["Shoots"] == "Left")].count()[0]
    print(left_hand, "were left handed in", output)
    left_stats = df.loc[(df.Year == output) & (df["Shoots"] == "Left")]
    left_points = sum(left_stats["P"])
    print(left_stats)
    print("")
    print("The total amount of points scored by left handed players in", output, "were", left_points)
    print("")
    right_hand = df.loc[(df.Year == output) & (df["Shoots"] == "Right")].count()[0]
    right_stats = df.loc[(df.Year == output) & (df["Shoots"] == "Right")]
    right_points = sum(right_stats["P"])
    print(right_hand, "were right handed in", output)
    print(right_stats)
    print("The total amount of points scored by right handed players in", output, "were", right_points)
    if left_points > right_points:
        print("Left handed players scored", left_points - right_points, "more points in", output)
    elif left_points < right_points:
        print("Right handed players scored", right_points - left_points, "more points in", output)
    elif left_points == right_points:
        print("Right handed and left handed players both scored", right_points, "in", output)
    print(""
          "")
    initial_year += 10
    if initial_year == 120:
        break

#Counting total number of left/right handed players
total_left = df.loc[df['Shoots'] == "Left"].count()[0]
print(total_left, "players in the top 10 were left handed through 2009-2021")

total_right = df.loc[df['Shoots'] == "Right"].count()[0]
print(total_right, "players in the top 10 were right handed through 2009-2021")
print(""
      "")

#Calculating sum of left/right handed player points
total_left_players = df.loc[df["Shoots"] == "Left"]
total_left_points =sum(total_left_players["P"])
print("Left handed players scored", total_left_points, "points through 10 seasons")

total_right_players = df.loc[df["Shoots"] == "Right"]
total_right_points =sum(total_right_players["P"])
print("Right handed players scored", total_right_points, "points through 10 seasons")
print(""
      "")

#Conclusion
if total_right > total_left:
    print("There were", total_right - total_left,  " more right handed players in the top 10")
elif total_right < total_left:
    print("There were", total_left-total_right, "more left handed players in the top 10")
elif total_right == total_left:
    print("The top 10 was divided equally between left and right handed players")

if total_right_points > total_left_points:
    print("Right handed players scored", total_right_points - total_left_points, "more points than left handed players from 2009-2021")
elif total_right_points < total_left_points:
    print("Left handed players scored", total_left_points-total_right_points, "more points than right handed players from 2009-2021")
elif total_right_points == total_left_points:
    print("Both right handed and left handed players scored an equal amount of", total_right_points)