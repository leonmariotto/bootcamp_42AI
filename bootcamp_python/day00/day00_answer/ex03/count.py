def text_analyzer(s=''):
    '''This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.'''
    u, ls, p, sp = 0, 0, 0, 0
    if s == '':
        print('What is the text to analyse ?')
        s = input()
        if s == '':
            print("Test empty")
            return
    for i in s:
        if i.islower():
            ls += 1
        elif i.isupper():
            u += 1
        elif i == ' ':
            sp += 1
        elif i.isdigit() is False:
            p += 1
    print('The text contains', len(s), 'characters')
    print(' - ', u, 'upper letters')
    print(' - ', ls, 'lower letters')
    print(' - ', p, 'punctuation marks')
    print(' - ', sp, 'spaces')
