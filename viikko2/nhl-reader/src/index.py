from rich import print
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    print("""Season [bold magenta][2018-19/2019-20/2020-21/2021-22/2022-23/2024-25/2025-26][/bold magenta]"
         [bold cyan](2024-25)[bold cyan]:""")
    season = input()
    if season == "":
        season = "2024-25" 
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationality_list = stats.nationality_list()    
    while True:
        print(f"""Nationality [bold magenta][{"/".join(nationality_list)}][/bold magenta] 
            [bold cyan]()[/bold cyan]: (Press ENTER to stop)""")
        nationality = input()
        if nationality == "":
            break
        players = stats.top_scorers_by_nationality(nationality)
        table = Table(title=f"[italic]Season {season} players from {nationality}[italic]", title_justify="center")
        table.add_column("Released")
        table.add_column("teams")
        table.add_column("goals", justify="right")
        table.add_column("assists", justify="right")
        table.add_column("points", justify="right")
        for player in players:
            table.add_row(
                f"[blue]{player.name}[/blue]",
                f"[magenta]{player.team}[/magenta]",
                f"[green]{player.goals}[/green]",
                f"[green]{player.assists}[/green]",
                f"[green]{player.goals+player.assists}[/green]")
        print(table)


if __name__ == "__main__":
    main()
