from random import randint

#파일 열기
in_file = open('vocabulary.txt', 'r' , encoding='UTF-8')

word = ''
english_word = ''
korean_word = ''

voca = {}

#단어 입력
for word in in_file:
    wordbook = word.strip().split(': ')

    english_word = wordbook[0]
    korean_word = wordbook[1]

    voca[korean_word] = english_word

    '''
    guess = input('%s: ' % korean_word)

    if guess == voca[korean_word]:
        print('맞았습니다! \n')
    else:
        print('아쉽습니다. 정답은 %s입니다. \n' % voca[english_word])
    '''

keys = list(voca.keys())
print(keys)
'''
while True:
    index = randint(0, len(keys) - 1)
    korean_word = keys[index]
    print(korean_word)
    english_word = voca[korean_word]
'''


#파일 닫기
in_file.close()