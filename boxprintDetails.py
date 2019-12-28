def boxprint (symbol, word, height):

    word_to_print = ' ' + word + ' '
    width = len(word) * 2
    print(symbol * width)

    for i in range(height):
        print(symbol + word_to_print.center(width-2, '*') + symbol)

    print(symbol * width)


boxprint('*', 'Christmas sellout only today', 1)