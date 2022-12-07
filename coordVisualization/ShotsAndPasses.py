#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created: 28.09.2021

@author: Mauri Heinonen
Version: 1.0

Example of plotting all shots

Changes:

"""

# Build-in modules
import json
import os

# Other modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Self made modules
from DrawField import create_full_pitch
from DrawField import create_goal_mouth

# Set some variables
FIELD_LENGTH = 105
FIELD_WIDTH = 68
STATS_FIELD_LENGTH = 120
STATS_FIELD_WIDTH = 80
MATCH_ID = 69301


def parse_json_file(filename=''):
    df = pd.DataFrame()

    if os.path.isfile(filename):
        with open(filename) as data_file:
            data = json.load(data_file)

    df = pd.json_normalize(data, sep="_").assign(match_id=MATCH_ID)
    return df


def plot_event(df, teams, field, length, width):
    if field == 'full':
        (fig, ax) = create_full_pitch(length, width, 'meters', 'white')
    elif field == 'half':
        (fig, ax) = create_goal_mouth(length, width, 'bottom', 'white')

    for i, event in df.iterrows():
        team = event.team_name

        x = event.location[0] * (FIELD_LENGTH / STATS_FIELD_LENGTH) if team == teams[0] else FIELD_LENGTH - event.location[0] * (FIELD_LENGTH / STATS_FIELD_LENGTH)
        y = FIELD_WIDTH - event.location[1] * (FIELD_WIDTH / STATS_FIELD_WIDTH) if team == teams[0] else event.location[1] * (FIELD_WIDTH / STATS_FIELD_WIDTH)
        outcome = 'red' if event.shot_outcome_name == 'Goal' else 'blue'
        alpha = 1 if event.shot_outcome_name == 'Goal' else 0.2
        player_name = event.player_name if event.shot_outcome_name == 'Goal' else ""
        plot_size = np.sqrt(event.shot_statsbomb_xg) * 2

        event_plot = plt.Circle((x, y),plot_size, color=outcome, alpha=alpha, zorder=5, ec='white')
        plt.text((x+1), y + 1, player_name, c='white')
        ax.add_patch(event_plot)

    return fig, ax


def main():
    directory = os.path.dirname(os.path.abspath(__file__))
    events = f"{directory}/open-data-master/data/events/{MATCH_ID}.json"
    lineups = f"{directory}/open-data-master/data/lineups/{MATCH_ID}.json"

    events_data = parse_json_file(events)
    players_data = parse_json_file(lineups)

    # solve home and away team
    teams = list(players_data.team_name.unique())

    # take all shots
    all_shots = events_data.loc[(events_data.type_name == 'Shot')]

    (fig, ax) = plot_event(all_shots, teams, 'full', FIELD_LENGTH, FIELD_WIDTH)

    # Set caption and more information to image
    plt.text(FIELD_LENGTH / 2, FIELD_WIDTH + 6, f"Shots from the match between {teams[0]} and {teams[1]}", ha='center', size='x-large', weight='bold')
    plt.text(FIELD_LENGTH / 4, -2, f"{teams[1]} shots".upper(), va='top', ha='center', size='medium')
    plt.text(FIELD_LENGTH / 4 * 3, -2, f"{teams[0]} shots".upper(), va='top', ha='center', size='medium')

    fig.set_size_inches(10, (10 * int(FIELD_WIDTH) / int(FIELD_LENGTH)))

    plt.tight_layout()
    plt.show()


if __name__ == "__main__" :
    main()