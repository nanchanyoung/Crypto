from random import randint

# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    selected_lotto = []

    while len(selected_lotto) < 6:
        lotto_ball = randint(1, 46)

        if selected_lotto.count(lotto_ball) != 1:
            selected_lotto.append(lotto_ball)

    selected_lotto.sort()
    return selected_lotto

# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    selected_lotto_bonus = []

    for ball in generate_numbers():
        selected_lotto_bonus.append(ball)

    while len(selected_lotto_bonus) < 7:

        lotto_ball = randint(1, 46)
        if selected_lotto_bonus.count(lotto_ball) != 1:
            selected_lotto_bonus.append(lotto_ball)

    return selected_lotto_bonus
'''
print(draw_winning_numbers())

list1 = [4, 19, 23, 28, 31, 39]
list2 = [4, 19, 23, 28, 31, 39]

print(count_matching_numbers(list1, list2))
'''

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    list_number = 0
    matching_numbers = 0

    while list_number < len(list1):
        if list1[list_number] in list2:
            matching_numbers = matching_numbers + 1
        list_number = list_number + 1

    return matching_numbers
'''
numbers = [1, 2, 4, 20, 33, 39]
winning_numbers = [1, 2, 4, 20, 33, 39, 10]
'''

# 로또 등수 확인하기
def check(numbers, winning_numbers):
    match_count = 0
    match_bonus_count = 0
    winning_amount = 0

    match_count = count_matching_numbers(numbers, winning_numbers[0:6])
    match_bonus_count = count_matching_numbers(winning_numbers[6:7], numbers)

    if match_count == 6:
        winning_amount = 1000000000
    elif match_count == 5 and match_bonus_count == 1:
        winning_amount = 50000000
    elif match_count == 5:
        winning_amount = 1000000
    elif match_count == 4:
        winning_amount = 50000
    elif match_count == 3:
        winning_amount = 5000

    return winning_amount
