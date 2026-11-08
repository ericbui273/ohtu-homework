from rich import print as rprint
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

def get_season_data():
    rprint(
        """Season [bold magenta]
        [2018-19/2019-20/2020-21/2021-22/2022-23/2024-25/2025-26]
        [/bold magenta][bold cyan](2024-25)[bold cyan]:"""
        )
    season = input()
    if season == "":
        season = "2024-25"
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    return season, stats


def get_nationality_data(stats):
    nationality_list = stats.nationality_list()
    rprint(
        f"""Nationality [bold magenta][{"/".join(nationality_list)}] [/bold magenta]
        [bold cyan]()[/bold cyan]: (Press ENTER to stop)"""
        )

    nationality = input()

    return nationality

def add_table_columns(table):
    table.add_column("Released")
    table.add_column("teams")
    table.add_column("goals", justify="right")
    table.add_column("assists", justify="right")
    table.add_column("points", justify="right")

def add_table_rows(table, players):
    for player in players:
        table.add_row(
            f"[blue]{player.name}[/blue]",
            f"[magenta]{player.team}[/magenta]",
            f"[green]{player.goals}[/green]",
            f"[green]{player.assists}[/green]",
            f"[green]{player.goals+player.assists}[/green]"
        )

def print_table(season, nationality, players):
    table = Table(
        title=f"[italic]Season {season} players from {nationality}[italic]",
        title_justify="center"
        )
    add_table_columns(table)
    add_table_rows(table, players)
    rprint(table)

def main():
    season, stats = get_season_data()
    while True:
        nationality = get_nationality_data(stats)

        if nationality == "":
            break

        players = stats.top_scorers_by_nationality(nationality)
        print_table(season, nationality, players)


if __name__ == "__main__":
    main()
