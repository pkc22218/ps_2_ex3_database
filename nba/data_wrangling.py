
import sqlite3

import pandas as pd


def get_top_home_scoring_teams(
    con: sqlite3.Connection,
    start_date: str = "2020-01-01",
    top_n: int = 5,
) -> pd.DataFrame:
    """Find teams with the highest average home scores."""

    query = """
        SELECT
            l.team_id_home,
            t.nickname,
            COUNT(*) AS num_games,
            AVG(l.pts_home) AS ave_score
        FROM line_score AS l
        JOIN team_details AS t
            ON l.team_id_home = t.team_id
        WHERE l.game_date_est >= ?
        GROUP BY l.team_id_home, t.nickname
        ORDER BY ave_score DESC
        LIMIT ?
    """

    return pd.read_sql_query(
        query,
        con,
        params=(start_date, top_n),
    )

def get_shoe_height_differences(
    con: sqlite3.Connection,
    top_n: int = 10,
) -> pd.DataFrame:
    """Return players with the largest recorded shoe-height differences."""

    query = """
        SELECT
            player_name,
            height_w_shoes,
            height_wo_shoes,
            height_w_shoes - height_wo_shoes AS shoe_height
        FROM draft_combine_stats
        WHERE height_w_shoes IS NOT NULL
          AND height_wo_shoes IS NOT NULL
        ORDER BY shoe_height DESC
        LIMIT ?
    """

    return pd.read_sql_query(query, con, params=(top_n,))

def get_vertical_leap_ratio(
    con: sqlite3.Connection,
    top_n: int = 10,
) -> pd.DataFrame:
    """Rank active players by vertical leap divided by body-fat percentage."""

    query = """
        SELECT
            d.player_name,
            d.max_vertical_leap,
            d.body_fat_pct,
            1.0 * d.max_vertical_leap / d.body_fat_pct
                AS leap_per_body_fat
        FROM draft_combine_stats AS d
        JOIN player AS p
            ON p.id = d.player_id
        WHERE p.is_active = 1
          AND d.max_vertical_leap IS NOT NULL
          AND d.body_fat_pct > 0
        ORDER BY leap_per_body_fat DESC
        LIMIT ?
    """

    return pd.read_sql_query(query, con, params=(top_n,))


def get_games_by_year(
    con: sqlite3.Connection,
) -> pd.DataFrame:
    """Count recorded NBA games for every calendar year."""

    query = """
        SELECT
            SUBSTR(game_date, 1, 4) AS calendar_year,
            COUNT(*) AS num_games
        FROM game
        WHERE game_date IS NOT NULL
        GROUP BY SUBSTR(game_date, 1, 4)
        ORDER BY calendar_year ASC
    """

    return pd.read_sql_query(query, con)
