import matplotlib.pyplot as plt
import pandas as pd

import json
import os

from DrawField import create_full_pitch
from ParseMyVAJson import parse_myva_file

MYVA_FILENAME = 'FIN-WAL-2nd-half.MyVAproject.json'
DF_FILENAME = 'NOR-FIN-esim.csv'

def visualize_myva_scoring():
    dir = os.path.dirname(os.path.abspath(__file__))
    events = f"{dir}/{MYVA_FILENAME}"

    json_df = parse_myva_file(events)
    # Get shots for team Finland
    pd.set_option('display.max_columns', None)
    # First off: get all the penetration attempts:
    df_pens = json_df.loc[json_df['Name'].str.contains('FIN Penetration \+ finishing')]

    # Then pick just the ones with shots:
    results = ['Goal','Shot over','Saved','Blocked']
    df_shots = df_pens.loc[df_pens['Result'].isin(results)]

    fig, ax = plot_events(df_shots,'x','y')
    ax.set_title("WNT FIN - WAL scoring attempts for Finland")
    plt.show()

def plot_events(df,xevent,yevent):
    (fig, ax) = create_full_pitch(105, 68, 'meters', 'white')

    for i, event in df.iterrows():
        #print (event)
        x = int(event[xevent])
        y = int(event[yevent])
        outcome = 'red' if event.Result == 'Goal' else 'blue'
        alpha = 1 if event.Result == 'Goal' else 0.5
        plot_size = 1.5 if event.Result == 'Goal' else 0.8

        event_plot = plt.Circle((x, y), plot_size, color=outcome, alpha=alpha, zorder=5, ec='white')
        ax.add_patch(event_plot)

    return fig, ax

def visualize_dartfish_scoring():
    dartfish_df = pd.read_csv(DF_FILENAME)
    fin_shots = dartfish_df.loc[dartfish_df['Name'].str.contains('Shot FIN')]
    opp_shots = dartfish_df.loc[dartfish_df['Name'].str.contains('Shot OPP')]

    shots_fin = fin_shots['Koordinaatti 1'].str.split(';', expand=True)

    fin_shots[['Y','X']] = fin_shots['Koordinaatti 1'].str.split(';', expand=True)
    opp_shots[['Y','X']] = opp_shots['Koordinaatti 1'].str.split(';', expand=True)

    fig, ax = plot_events(fin_shots,'X','Y')
    ax.set_title("MNT Fin - Nor scoring attempts FIN")
    plt.show()
    fig, ax = plot_events(opp_shots, 'X','Y')
    ax.set_title("MNT Fin - Nor scoring attempts NOR")
    plt.show()

if __name__ == '__main__':
    visualize_myva_scoring()
    visualize_dartfish_scoring()