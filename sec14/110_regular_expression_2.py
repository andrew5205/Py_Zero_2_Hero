
# \d a Digit                
# \w Alphanumeric           
# \s Space                  

# \D non Dogot              
# \W non Alphanumeric       *-+=)
# \S non Space              

import re
text = " My phone number is 555-555-5555"


phone_num = re.search("555-555-5555", text)
print(phone_num)                    # <re.Match object; span=(20, 32), match='555-555-5555'>
phone_wrong = re.search("777-777-7777", text)
print(phone_wrong)                  # None


phone = re.search(r"\d\d\d-\d\d\d-\d\d\d\d", text)
print(phone)                        # <re.Match object; span=(20, 32), match='555-555-5555'>
print(phone.group())                # 555-555-5555




# Quantifiers table 

# +         \w + \w
# {3}       \d{3}       -> 123
# {2,4}     \d{2,4}     -> occur 2 to 4 times 
# {3,}      \d{3,}      -> three or more 
# *         ABC*        -> occurs more than 0 times 
# ?         plurals?    -> one or more 


phone_reg = re.search(r"\d{3}-\d{3}-\d{4}", text)
print(phone_reg)                    # <re.Match object; span=(20, 32), match='555-555-5555'>


#compile() function
# re.compile(r"()") - grouping inside ()
phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
result = re.search(phone_pattern, text)
print(result)                       # <re.Match object; span=(20, 32), match='555-555-5555'>
print(result.group)                 # <built-in method group of re.Match object at 0x7fe79fc15670>
print(result.group())               # 555-555-5555
print(result.group(1))              # 555
print(result.group(2))              # 555
print(result.group(3))              # 5555
# print(result.group(4))            # IndexError: no such group







