
import matplotlib.pyplot as plt
import pandas as pd


def plot_home_scoring(df: pd.DataFrame) -> None:
    """Plot teams with the highest average home scores."""
    data = df.sort_values("ave_score")

    plt.figure(figsize=(10, 6))
    plt.barh(data["nickname"], data["ave_score"])
    plt.xlabel("Average home points per game")
    plt.ylabel("NBA team")
    plt.title("Highest Average NBA Home Scores Since 2020")
    plt.tight_layout()
    plt.show()


def plot_shoe_height(df: pd.DataFrame) -> None:
    """Plot players with the largest shoe-height differences."""
    data = df.sort_values("shoe_height")

    plt.figure(figsize=(10, 6))
    plt.barh(data["player_name"], data["shoe_height"])
    plt.xlabel("Height difference (inches)")
    plt.ylabel("Player")
    plt.title("Largest Recorded Height Differences With Shoes")
    plt.tight_layout()
    plt.show()


def plot_vertical_leap(df: pd.DataFrame) -> None:
    """Plot active players by vertical leap/body-fat ratio."""
    data = df.sort_values("leap_per_body_fat")

    plt.figure(figsize=(10, 6))
    plt.barh(data["player_name"], data["leap_per_body_fat"])
    plt.xlabel("Vertical leap / body-fat percentage")
    plt.ylabel("Player")
    plt.title("Active NBA Players: Vertical Leap Relative to Body Fat")
    plt.tight_layout()
    plt.show()


def plot_games_by_year(df: pd.DataFrame) -> None:
    """Plot NBA game counts by calendar year."""
    data = df.sort_values("calendar_year")

    plt.figure(figsize=(10, 6))
    plt.plot(
        data["calendar_year"],
        data["num_games"],
        marker="o",
    )
    plt.xlabel("Calendar year")
    plt.ylabel("Number of recorded games")
    plt.title("NBA Game Counts by Calendar Year")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
