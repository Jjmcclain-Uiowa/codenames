class Word:

    def __init__(self, word):
        self.word = word
        self.team = 'neutral'
        self.guessed = False

    def __str__(self):
        #return '(' + self.word + ', ' + self.team + ')'
        return self.word

    def guess(self):
        self.guessed = True
        print(self.word + ' is ' + self.team)

