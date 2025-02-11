from itertools import combinations
from hashlib import sha256
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

numbers = '123456789'

def cap_digit_append(word):
    all_words = []
    all_words.append(word.capitalize())
    if len(word) == 6 and word[0].isalpha():
        word = word.capitalize()
        allCombinations = []
        for combination in combinations(numbers, 1):
            allCombinations.append("".join(combination))
        for comb in allCombinations:
            all_words.append(word+comb)
    return all_words

# A eight-character password from the rockyou wordlist with at least one of the
# following special characters in the beginning: *, ~, !, #
# add these permutations until it reaches 8

special = '*~!#'
def special_start_combo(word):
    all_words =[]
    if len(word) < 8:
        allCombinations = []
        r = 8 - len(word)
        for combination in combinations(special, r):
            allCombinations.append("".join(combination))
        
        for comb in allCombinations:
            all_words.append(comb+word)
    return all_words

# A five-character password from the rockyou wordlist with the letter 'a' in it which gets
# replaced with the special character @ and the character ‘l’ is substituted by the number
# ‘1’.

def replace_size_five(word):
    if len(word) == 5:
        word = word.replace('a', '@')
        word = word.replace('l', '1')
    return word

# Any password that is made with only digits and up to 6 digits length.
# permutate with passwords from 1 - 6 length of any number combinations 
def number_combos(nums):
    allCombinations = []
    for r in range(1, 7):
        for combination in combinations(nums, r):
            allCombinations.append("".join(combination))
    return allCombinations

# Any single password from the rockyou wordlist.
def process_words(words):
    for i in range(0, len(words)):
        words.append(replace_size_five(words[i]))
        words += cap_digit_append(words[i])
        words += special_start_combo(words[i])
    words += number_combos(numbers)
    return words

password_hash_map = {}
def create_hash_set(words, hash_map):
    for i in range(0, len(words)):
        encode_string = words[i].encode('utf-8')
        key = sha256(encode_string).hexdigest()
        hash_map[key] = words[i]

def check_passwords(pass_hash, map):
    for i in range(0, len(pass_hash)):
        if(i in map):
            return print("Password found ", map[i])
        else: 
            print("No password found")

word_list = process_words(word_list)
create_hash_set(word_list, password_hash_map)
print( "new word list ", word_list)
print("hash map ", password_hash_map)
check_passwords(hash_list, password_hash_map)