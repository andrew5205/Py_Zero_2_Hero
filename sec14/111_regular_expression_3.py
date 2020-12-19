
import re 

result = re.search(r'cat | dog', "This is the string to be searched, dog is in here")
print(result)           # <re.Match object; span=(34, 38), match=' dog'>

result_all = re.findall(r'at', "the cat in the hat sat there")
print(result_all)       # ['at', 'at', 'at']

# wildcard - period
Wildcard_findall = re.findall(r'.at', "the cat in the hat sat there")
print(Wildcard_findall)       # ['cat', 'hat', 'sat']

# each wildcard count as an char space
wildcard_chars_count = re.findall(r'...at', "the cat in weird hat went splat")
print(wildcard_chars_count)       # ['e cat', 'd hat', 'splat']



# start with ^
# find the text strat with digit 
start = re.findall(r'^\d',"1 is a number")
print(start)                                        # ['1']
start = re.findall(r'^\d',"the 2 is a number")
print(start)                                        # []


# end with $
end = re.findall(r'\d$',"the number is 2")
print(end)                                          # ['2']
end = re.findall(r'\d$',"the number is two")
print(end)                                          # []



# exclude ^
# [] just mean to group together 
phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]'
exclude_result = re.findall(pattern, phrase)
print(exclude_result)
# 't', 'h', 'e', 'r', 'e', ' ', 'a', 'r', 'e', ' ', ' ', 'n', 'u', 'm', 'b', 'e', 'r', 's', ' ', ' ', 'i', 'n', 's', 'i', 'd', 'e', ' ', ' ', 't', 'h', 'i', 's', ' ', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e']

pattern_rm = r'[^\d]+'
easy_remove = re.findall(pattern_rm, phrase)
print(easy_remove)                                  # ['there are ', ' numbers ', ' inside ', ' this sentence']


test_phrase = " this is a string ! But it has punctuation. How to remove it fast?"
pattern_rm_punc = r'[^!?.]+'
result_punc_rm = re.findall(pattern_rm_punc, test_phrase)
print(result_punc_rm)                               # [' this is a string ', ' But it has punctuation', ' How to remove it fast']

clean_pattern = re.findall(r'[^!.? ]+', test_phrase)
clean = " ".join(clean_pattern)
print(clean)                                        # this is a string But it has punctuation How to remove it fast




# include use \
# [] just mean to group together 
phrase2 = " only find the hypen-words in this sentence. But you don't know where is-it"
pattern_dash = r'[\w]+-[\w]+'
include = re.findall(pattern_dash, phrase2)
print(include)                                      # ['hypen-words', 'is-it']
include_cat = " ".join(include)
print(include_cat)                                  # hypen-words is-it


text1 = "hello, would like some catfish?"
text2 = "hello, would you like some catnap"
text3 = "hello, have you seen this caterpillar"

result_in_search = re.search(r'cat(fish|nap|claw)', text1)
print(result_in_search)                             # <re.Match object; span=(23, 30), match='catfish'>

result_in_search = re.search(r'cat(fish| nap|claw)', text2)
print(result_in_search)                             # None # watch out for the space here 




