import Board

if __name__ == '__main__':

    # load word list from text file
    text_file = open('words.txt', 'r')
    master_word_list = []
    for line in text_file:
        master_word_list.append(line.strip('\n').lower())

    game_board = Board.Board(master_word_list)
    red_words, blue_words, neutral_words, assassin = game_board.get_team_words()

    game_board.print()
    #print('Red words: ' + str(red_words))
    #print('Blue: ' + str(blue_words))
    #print('Neutral words: ' + str(neutral_words))
    #print('Assassin word: ' + str(assassin))

    guess = input('Choose a word: ')

    for w in game_board.board:
        if w.word == guess:
            w.guess()

