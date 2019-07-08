#변수 선언
english_word = ''
korean_meaning = ''

#파일 저장
out_file = open('vocabulary.txt', 'w', encoding='UTF-8')

while english_word != 'q':
    english_word = input('영어 단어를 입력하세요:')
    if english_word == 'q':
        break;
    korean_meaning = input('한국어 뜻을 입력하세요:')

    out_file.write("%s: %s\n" % (english_word, korean_meaning))

#파일 닫기
out_file.close()