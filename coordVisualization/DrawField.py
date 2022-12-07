#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:32:00 2020

@author: davsu428

Draw a football pitch with matplotlib.
Mauri Heinonen added a chance to change the field line and background color and at the same time fixed some bugs.
Added areas variables like 16-area size.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib.patches import Wedge

PENALTY_AREA = 16.5
GK_BOX = 5.5
GOAL = 7.32
CIRCLE_RADIUS = 9.15
PENALTY_SPOT = 11
SPOT = 0.5

def create_full_pitch(length=105, width=68, unity='meters', lc='white', pitch='#80B860'):
    """
    Creates full football pitch

    Parameters
    ----------
    length : int
        Length of the pitch (GOAL to GOAL). Default values is 105 meters.
    width : int
        Width of the pitch (sideline to sideline). Default values is 68 meters.
    unity : string
        Do you like to use meters or yards. Default values is meters.
    lc : string
        Color of pitch lines. Default line color is white.
    pitch : string
        Color of pitch background. Default background color is green.

    Returns
    -------
    fig : matplotlib figure
        Figure it self
    ax : matplotlib subplot
        Subplot it self
    """

    # Check user given unity, is it meters or yards
    if unity == "meters":
        # Set boundaries
        if length >= 120.5 or width >= 75.5:
            return str("Field dimensions are too big for meters as unity, didn't you mean yards as unity?"
                       "Otherwise the maximum length is 120 meters and the maximum width is 75 meters."
                       "Please try again"), str("ERROR")
    elif unity == 'yards':
        if length <= 95:
            return str("Didn't you mean meters as unity?"), str("ERROR")
        elif length >= 131 or width >= 101:
            return str("Field dimensions are too big. Maximum length is 130, maximum width is 100"), str("ERROR")
    else:
        return str("Your set unity what is not supported. Use meters or yards."), str("ERROR")

    # Everything was OK > Create figure
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Pitch Outline & Centre Line
    plt.plot([0, 0], [0, width], color=lc, zorder=2)
    plt.plot([0, length], [width, width], color=lc, zorder=2)
    plt.plot([length, length], [width, 0], color=lc, zorder=2)
    plt.plot([length, 0], [0, 0], color=lc, zorder=2)
    plt.plot([length / 2, length / 2], [0, width], color=lc, zorder=2)

    # Left Penalty Area
    plt.plot([PENALTY_AREA, PENALTY_AREA], [(width / 2 + PENALTY_AREA), (width / 2 - PENALTY_AREA)], color=lc, zorder=2)
    plt.plot([0, PENALTY_AREA], [(width / 2 + PENALTY_AREA), (width / 2 + PENALTY_AREA)], color=lc, zorder=2)
    plt.plot([PENALTY_AREA, 0], [(width / 2 - PENALTY_AREA), (width / 2 - PENALTY_AREA)], color=lc, zorder=2)

    # Right Penalty Area
    plt.plot([(length - PENALTY_AREA), length], [(width / 2 + PENALTY_AREA), (width / 2 + PENALTY_AREA)], color=lc, zorder=2)
    plt.plot([(length - PENALTY_AREA), (length - PENALTY_AREA)], [(width / 2 + PENALTY_AREA), (width / 2 - PENALTY_AREA)], color=lc, zorder=2)
    plt.plot([(length - PENALTY_AREA), length], [(width / 2 - PENALTY_AREA), (width / 2 - PENALTY_AREA)], color=lc, zorder=2)

    # Left gk area
    plt.plot([0, GK_BOX], [(width / 2 + GOAL / 2 + GK_BOX), (width / 2 + GOAL / 2 + GK_BOX)], color=lc, zorder=2)
    plt.plot([GK_BOX, GK_BOX], [(width / 2 + GOAL / 2 + GK_BOX), (width / 2 - GOAL / 2 - GK_BOX)], color=lc, zorder=2)
    plt.plot([GK_BOX, 0.5], [(width / 2 - GOAL / 2 - GK_BOX), (width / 2 - GOAL / 2 - GK_BOX)], color=lc, zorder=2)

    # Right gk area
    plt.plot([length, length - GK_BOX], [(width / 2 + GOAL / 2 + GK_BOX), (width / 2 + GOAL / 2 + GK_BOX)], color=lc, zorder=2)
    plt.plot([length - GK_BOX, length - GK_BOX], [(width / 2 + GOAL / 2 + GK_BOX), width / 2 - GOAL / 2 - GK_BOX], color=lc, zorder=2)
    plt.plot([length - GK_BOX, length], [width / 2 - GOAL / 2 - GK_BOX, width / 2 - GOAL / 2 - GK_BOX], color=lc, zorder=2)

    # Draw GOAL
    plt.plot([0, -1.3], [width / 2 + (GOAL / 2), width / 2 + (GOAL / 2)], alpha=1, color=lc, zorder=2)
    plt.plot([0, -1.3], [width / 2 - (GOAL / 2), width / 2 - (GOAL / 2)], alpha=1, color=lc, zorder=2)
    plt.plot([-1.3, -1.3], [width / 2 - (GOAL / 2), width / 2 + (GOAL / 2)], alpha=1, color=lc, zorder=2)

    plt.plot([length, length + 1.3], [width / 2 + (GOAL / 2), width / 2 + (GOAL / 2)], alpha=1, color=lc, zorder=2)
    plt.plot([length, length + 1.3], [width / 2 - (GOAL / 2), width / 2 - (GOAL / 2)], alpha=1, color=lc, zorder=2)
    plt.plot([length + 1.3, length + 1.3], [width / 2 - (GOAL / 2), width / 2 + (GOAL / 2)], alpha=1, color=lc, zorder=2)

    # Draw Circles
    ax.add_patch(plt.Circle((length / 2, width / 2), CIRCLE_RADIUS, color=lc, fill=False, zorder=2))# Center circles
    ax.add_patch(plt.Circle((length / 2, width / 2), SPOT, color=lc, zorder=2)) # Center SPOT
    ax.add_patch(plt.Circle((PENALTY_SPOT, width / 2), SPOT, color=lc, zorder=2)) # Left penalty SPOT
    ax.add_patch(plt.Circle((length - PENALTY_SPOT, width / 2), SPOT, color=lc, zorder=2)) # Right penalty SPOT

    # Draw Arcs
    ax.add_patch(Arc((PENALTY_SPOT, width / 2), height=18.3, width=18.3, angle=0, theta1=308, theta2=52, color=lc, zorder=2)) # Left arc
    ax.add_patch(Arc((length - PENALTY_SPOT, width / 2), height=18.3, width=18.3, angle=0, theta1=128, theta2=232, color=lc, zorder=2)) # Right arc

    # Pitch rectangle
    ax.add_artist(plt.Rectangle((-1, -1), length + 2, width + 2, ls='-', color=pitch, zorder=1, alpha=1))

    ax.set_aspect('equal')
    plt.axis('off')
    
    return fig, ax


def create_goal_mouth(height=52.5, width=68, direction='bottom', lc='white', pitch='#80B860'):
    """
    Creates half of football pitch

    Parameters
    ----------
    height : int
        Height of the pitch (Center line to goal line). Default values is 52.5 meters.
    width : int
        Width of the pitch (sideline to sideline). Default values is 68 meters.
    direction : string
        Do you like to set goal top or bottom of image. Default is bottom.
    lc : string
        Color of pitch lines. Default line color is white.
    pitch : string
        Color of pitch background. Default background color is green.

    Returns
    -------
    fig : matplotlib figure
        Figure it self
    ax : matplotlib subplot
        Subplot it self
    """
    # Check user given direction, is it bottom or top
    if direction != "top" and direction != "bottom":
        return str("You should set goal top or bottom of image."), str("ERROR")
    else:
        penalty = PENALTY_AREA if direction == "bottom" else height - PENALTY_AREA
        penalty_spot_position = PENALTY_SPOT if direction == "bottom" else height - PENALTY_SPOT
        gk_box_position = GK_BOX if direction == "bottom" else height - GK_BOX
        goal_line = 0 if direction == "bottom" else height
        angle = 0 if direction == "bottom" else 180
        angle2 = 180 if direction == "bottom" else 0
        negative_goal = -1.5 if direction == "bottom" else height + 1.5
        r = SPOT * (-1.) if direction == "bottom" else SPOT

        half_spot = width / 2
        penalty_width = GOAL / 2 + PENALTY_AREA
        gk_width = GOAL / 2 + GK_BOX

        # Create figure
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        # Pitch Outline & Centre Line
        plt.plot([0, width], [0, 0], color=lc, zorder=2)
        plt.plot([width, width], [height, 0], color=lc, zorder=2)
        plt.plot([0, 0], [height, 0], color=lc, zorder=2)
        plt.plot([0, width], [height, height], color=lc, zorder=2)

        # Penalty Area
        plt.plot([(half_spot - penalty_width), half_spot + penalty_width], [penalty, penalty], color=lc, zorder=2)
        plt.plot([half_spot - penalty_width, half_spot - penalty_width], [penalty, goal_line], color=lc, zorder=2)
        plt.plot([half_spot + penalty_width, half_spot + penalty_width], [goal_line, penalty], color=lc, zorder=2)

        # GK area
        plt.plot([half_spot + gk_width, half_spot + gk_width], [gk_box_position, goal_line], color=lc, zorder=2)
        plt.plot([half_spot - gk_width, half_spot + gk_width], [gk_box_position, gk_box_position], color=lc, zorder=2)
        plt.plot([half_spot - gk_width, half_spot - gk_width], [goal_line, gk_box_position], color=lc, zorder=2)

        # GOAL
        plt.plot([half_spot - GOAL / 2, half_spot - GOAL / 2], [negative_goal, goal_line], color=lc, zorder=2)
        plt.plot([half_spot + GOAL / 2, half_spot - GOAL / 2], [negative_goal, negative_goal], color=lc, zorder=2)
        plt.plot([half_spot + GOAL / 2, half_spot + GOAL / 2], [goal_line, negative_goal], color=lc, zorder=2)

        # Draw Penalty Spot
        ax.add_patch(plt.Circle((half_spot, penalty_spot_position), SPOT, color=lc, zorder=2))

        # 16 area Arc
        ax.add_patch(Arc((half_spot, penalty_spot_position), height=18.3, width=18.3, angle=angle, theta1=38, theta2=142, color=lc, zorder=2))

        # Center spot and Arc
        ax.add_patch(Arc((half_spot, height - goal_line), height=18.3, width=18.3, angle=angle2, theta1=0, theta2=180, color=lc, zorder=2))
        ax.add_artist(Wedge((half_spot, height - goal_line), SPOT, angle2, angle2 + 180, ec=lc, fc=lc, zorder=2, visible=True, alpha=1, color=lc))

        # Pitch rectangle
        ax.add_artist(plt.Rectangle((-2, -2), width + 4, height + 4, ls='-', color=pitch, zorder=1, alpha=1))

        ax.set_aspect('equal')
        plt.axis('off')

        return fig, ax
