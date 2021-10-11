n = int(input())
for oportunidades in range(n):
    word = input()
    long_word = ''
    if len(word)>10:
        long_word = word[0]+str(len(word[1:-1]))+word[-1]
        print(long_word)
    else:
        print(word)
