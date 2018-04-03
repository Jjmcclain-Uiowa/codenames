class Player:

    def __init__(self, team, is_cluegiver='n', can_guess='y'):
        self.team = team
        self.cluegiver = is_cluegiver
        self.can_guess = can_guess

    def __str__(self):
        return self.team + ' team player'
