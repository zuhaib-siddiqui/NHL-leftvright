import pandas as pd
import matplotlib.pyplot as plt

#data
df = pd.read_csv("NHL left hand vs right hand.csv")
pd.set_option('display.max.rows', None)
pd.set_option('display.max.columns', None)

#Left Hand
initial_year = 0
for year in df:
    output = (df.Year[initial_year])
    print(output)
    hand = df.loc[(df.Year == output) & (df["Shoots"] == "Left")].count()[0]
    print(hand,"were left handed")
    left_stats = df.loc[(df.Year == output) & (df["Shoots"] == "Left")]
    left_points = sum(left_stats["P"])
    print(left_stats)
    print("")
    print("The total amount of points scored by left handed players were", left_points)
    print("")
    initial_year += 10
    if initial_year == 120:
        break
total_left = df.loc[df['Shoots'] == "Left"].count()[0]
print(total_left, "players in the top 10 were left handed through 2009-2021")
print("")

#Right Hand
initial_year = 0
for year in df:
    output = (df.Year[initial_year])
    print(output)
    hand = df.loc[(df.Year == output) & (df["Shoots"] == "Right")].count()[0]
    right_stats = df.loc[(df.Year == output) & (df["Shoots"] == "Right")]
    right_points = sum(right_stats["P"])
    print(hand,"were right handed")
    print(right_stats)
    print("The total amount of points scored by right handed players were", right_points)
    print("")
    initial_year += 10
    if initial_year == 120:
        break

total_right = df.loc[df['Shoots'] == "Right"].count()[0]
print(total_right, "players in the top 10 were right handed through 2009-2021")
print("")

#Conclusion
if total_right > total_left:
    print("There were", total_right - total_left,  " more right handed players in the top 10")
elif total_right < total_left:
    print("There were", total_left-total_right, "more left handed players in the top 10")
elif total_right == total_left:
    print("The top 10 was divided equally between left and right handed players")

