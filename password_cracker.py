import random
from itertools import combinations
hash_list = []

# processing hash values
with open('hash.txt','r') as hash_file: 
    for line in hash_file:
        if len(line.split(':')[1]) > 20:
            hash_list.append(line.split(':')[1].strip(' '))

word_list = []

with open('test_words.txt', 'r') as word_file:
    for line in word_file:
        word_list.append(line.strip(' \n'))

print("words ", word_list)

# A seven-character password from the rockyou wordlist which gets the first letter
# capitalized and a 1-digit number appended.
# first character 

numbers = [0,1,2,3,4,5,6,7,8,9]
def cap_digit_append(words):
    for i in range(0, len(words)):
        if len(words[i]) == 6 and words[i][0].isalpha():
            words[i] = words[i].capitalize()
            words[i] += str(random.choice(numbers))
    return words

# A eight-character password from the rockyou wordlist with at least one of the
# following special characters in the beginning: *, ~, !, #
# add these permutations until it reaches 8

special = '*~!#'
def special_start_combo(words):
    for i in range(0, len(words)):
        if len(words[i]) < 8:
            allCombinations = []
            r = 8 - len(words[i])
            for combination in combinations(special, r):
                allCombinations.append("".join(combination))
            
            for comb in allCombinations:
                words.append(comb+words[i])
    return words

# A five-character password from the rockyou wordlist with the letter 'a' in it which gets
# replaced with the special character @ and the character ‘l’ is substituted by the number
# ‘1’.

def replace_size_five(words):
    for i in range(0, len(words)):
        if len(words[i]) == 5:
            words[i] = words[i].replace('a', '@')
            words[i] = words[i].replace('l', '1')
    return words

# Any password that is made with only digits and up to 6 digits length.
# permutate with passwords from 1 - 6 length of any number combinations 
# Any single password from the rockyou wordlist.

word_list = cap_digit_append(word_list)
word_list = special_start_combo(word_list)
print( "new word list ", word_list)