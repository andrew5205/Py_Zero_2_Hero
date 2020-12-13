
# regex - allowed us to search for general patterns in txt 

# re library

# r""

# example
# phone number 
# (555)555-5555


r"(\d\d\d)-\d\d\d-\d\d\d\d\d"
r"(\d{3)-\d{3}-\d{4}"



text = " The agents phone number is 555-555-5555. Call soon!"

import re 

pattern = "phone"
print(re.search(pattern, text))             # <re.Match object; span=(12, 17), match='phone'>

not_in = "nothing here"
print(re.search(not_in, text))              # None


is_match = re.search(pattern, text)
print(is_match.span())                      # (12, 17)
print(is_match.start())                     # 12
print(is_match.end())                       # 17



text2 = "phone one, phone two, phone three"

# findall return a list
match_collections = re.findall(pattern, text2)
print(match_collections)                    # ['phone', 'phone', 'phone']s
print(len(match_collections))               # 3

# re.finditer()
# re.findall()
for m in re.finditer('phone', text2):
    print(m)
            # <re.Match object; span=(0, 5), match='phone'>
            # <re.Match object; span=(11, 16), match='phone'>
            # <re.Match object; span=(22, 27), match='phone'>
    print(m.group())
            # phone
            # phone
            # phone







