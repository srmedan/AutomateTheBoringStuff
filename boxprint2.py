import traceback


def boxPrint(symbol, width, height):

    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of lenth 1.')

    if (width < 2) or (height < 2):
        raise Exception('Width and Height must be higher than 1!')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + ' ' * (width - 2) + symbol)

    print(symbol * width)

    try:
        raise Exception('This is the error message')
    except:
        errorFile = open('error_log.txt', 'a')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info was written error_log.txt')
boxPrint('$', 2, 5)