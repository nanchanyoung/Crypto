def is_palindrome(word):
    #print(len(word))
    true_count = 0

    for i in range(int(len(word) / 2)):
        #print('앞' + word[i])
        #print('뒤' + word[len(word) - i - 1])

        if word[i] !=  word[len(word) - i - 1]:
            true_count = true_count + 1
            return_str = False
        else:
            return_str = True
    return  return_str

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
