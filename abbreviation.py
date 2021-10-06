def abbreviation():
    word = input('enter a word: ')
    long_word = ''
    if len(word)>10:
        long_word = word[0]+str(len(word[1:-1]))+word[-1]
        print(long_word)
    else:
        print(word)
if __name__ == '__main__':
    abbreviation()
