class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score1 = self.m_score1
        score2 = self.m_score2

        if score1 == score2:
            if score1 > 2:
                return "Deuce"
            return f"{self.score_str(score1)}-All"

        elif score1 >= 4 or score2 >= 4:
            diff = abs(score1 - score2)
            if score1 > score2:
                ahead = self.player1_name
            else:
                ahead = self.player2_name
            if diff >= 2:
                return f"Win for {ahead}"
            else:
                return f"Advantage {ahead}"

        else:
            return f"{self.score_str(score1)}-{self.score_str(score2)}"

    def score_str(self, n):
        if n < 0 or n > 4:
            raise ValueError
        scores = [
                "Love",
                "Fifteen",
                "Thirty",
                "Forty"
                ]
        return scores[n]
