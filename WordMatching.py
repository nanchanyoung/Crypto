#파일 열기
in_file = open('vocabulary.txt', 'r' , encoding='UTF-8')

word = ''
english_word = ''
korean_word = ''

#단어 입력
for word in in_file:
    wordbook = word.strip().split(': ')

    english_word = wordbook[0]
    korean_word = wordbook[1]

    guess = input('%s: ' % korean_word)

    if guess == english_word:
        print('맞았습니다! \n')
    else:
        print('아쉽습니다. 정답은 %s입니다. \n' % english_word)

#파일 닫기
in_file.close()