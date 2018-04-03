import random
import Word


class Board:

    def __init__(self, master_word_list):
        self.board = []
        game_words = random.sample(master_word_list, 25)
        for w in game_words:
            self.board.append(Word.Word(w))
        self.set_teams()

    def __str__(self):
        return str([str(word) for word in self.word_set])

    def set_teams(self):
        for word in self.board[:9]:
            word.team = 'red'
        for word in self.board[9:17]:
            word.team = 'blue'
        self.board[17].team = 'assassin'

    def get_team_words(self):
        red_words = []
        blue_words = []
        neutral_words = []
        assassin = ''

        for word in self.board:

            if word.team == 'red':
                red_words.append(word.word)
            elif word.team == 'blue':
                blue_words.append(word.word)
            elif word.team == 'neutral':
                neutral_words.append(word.word)
            elif word.team == 'assassin':
                assassin = word.word

        return red_words, blue_words, neutral_words, assassin

    def print(self):
        print('Board: ' + str([str(word) for word in self.board]))




