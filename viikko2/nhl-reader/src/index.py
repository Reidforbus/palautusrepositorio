from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    stats = PlayerStats(PlayerReader(url))
    players = stats.top_scorers_by_nationality("FIN")
    print("Players from FIN:")
    print()

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
