from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    console = Console()
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    stats = PlayerStats(PlayerReader(url))
    console.print("[italic]NHL stats by nationality[/italic]")

    while True:
        nation = console.input("Select nationality: ")
        players = stats.top_scorers_by_nationality(nation)
        if players == []:
            return
        playertable = Table(title=f"[italic]Top scorers of {nation}[/italic]")
        playertable.add_column("Name")
        playertable.add_column("Team")
        playertable.add_column("Goals")
        playertable.add_column("Assists")
        playertable.add_column("Points")

        for player in players:
            name, team, goals, assists, points = player.get_table_data()
            playertable.add_row(f"[cyan]{name}[/cyan]",
                                f"[red]{team}[/red]",
                                goals.__str__(),
                                assists.__str__(),
                                f"[cyan]{points.__str__()}[/cyan]"
                                )

        console.print(playertable)


if __name__ == "__main__":
    main()
