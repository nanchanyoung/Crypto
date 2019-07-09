from random import randint

#파일 열기
in_file = open('vocabulary.txt', 'r' , encoding='UTF-8')

#배열에 단어 저장
voca = {}

for word in in_file:
    wordbook = word.strip().split(': ')

    english_word = wordbook[0]
    korean_word = wordbook[1]

    voca[korean_word] = english_word

#list 변환
keys = list(voca.keys())

#단어 맞추기
while True:
    #랜덤 구현
    index = randint(0, len(keys) - 1)
    korean_word = keys[index]
    english_word = voca[korean_word]

    guess = input('%s: ' % korean_word)

    if guess == 'q':
        break

    if guess == voca[korean_word]:
        print('맞았습니다! \n')
    else:
        print('틀렸습니다. 정답은 %s입니다. \n' % english_word)

#파일 닫기
in_file.close()