import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    finns = sorted([player for player in players if player.nation == "FIN"], reverse=True, key=Player.sortByPoints)
    print("Players from FIN:")
    print()

    for player in finns:
        print(player)


if __name__ == "__main__":
    main()
