import pandas as pd
import matplotlib as plt
import numpy as np
from scipy.stats import chisquare

PLOT = True
plt.rcParams["font.family"] = "Finlandica"

# Read the excel file into a pandas dataframe
goals_dataframe = pd.read_excel("goals.xlsx")

# Show how many columns and rows the data consists of
print(goals_dataframe.shape)
# Print out few of the first rows of the data just to see how it looks like
print(goals_dataframe.head())

# Describe the data contents
print(goals_dataframe.describe())

# Divide the data to goals for and goals against
# goals_fin = goals_dataframe.groupby("Goal for").get_group("Finland")
goals_fin = goals_dataframe.loc[goals_dataframe["Goal for"] == "Finland"]
#print(goals_fin.shape)
#print(goals_fin.head())

goals_opponents = goals_dataframe.loc[goals_dataframe["Goal for"] != "Finland"]
#print(goals_opponents.shape)
#print(goals_opponents.head())

# Plot the histogram more specifically
goals_fin.hist(column='Time', bins=6)
if (PLOT == True):
    plt.pyplot.show()

goals_opponents.hist(column='Time', bins=6)

# Print the 6-bin histograms for both categories
goals_fin_ax = goals_fin.hist(bins=6, rwidth=0.7)
ax = goals_fin_ax[0]
if (PLOT == True):
    for x in ax:
        # Despine
        x.spines['right'].set_visible(False)
        x.spines['top'].set_visible(False)
        x.spines['left'].set_visible(False)

        x.grid(False)
        # Switch off ticks
        x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off",
                      labelleft="on")


        # Draw horizontal axis lines
        vals = x.get_yticks()
        for tick in vals:
            x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

        # Remove title
        x.set_title("FIN Goals scored by 15 minute periods")

        # Set x-axis label
        x.set_xlabel("Periods)", labelpad=20, weight='bold', size=12)

        # Set y-axis label
        x.set_ylabel("Goals scored", labelpad=20, weight='bold', size=12)
        x.set_xticks([12,27,42,54,68,82],["0-15","15-30","30-45","45-60","60-75","75-90+"])

    plt.pyplot.show()

goals_opp_ax = goals_opponents.hist(bins=6)
if (PLOT == True):
    plt.pyplot.show()

# Get the counts for the scoring bins
gf = goals_fin["Time"]
counts_fin_goals = gf.value_counts(bins=[0,15,30,45,60,75,gf.max()])

go = goals_opponents["Time"]
counts_opp_goals = go.value_counts(bins=[0,15,30,45,60,75,go.max()])

print (counts_fin_goals)
print(chisquare(counts_fin_goals))
print(chisquare(counts_opp_goals))