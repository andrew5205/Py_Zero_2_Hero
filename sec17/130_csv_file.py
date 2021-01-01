
# CSV - comma sepersted variables

# Name,   Hours,  Rates
# David,  20,     15


# Pandas
# Openpyxl
# Google sheets python API


# Steps:
# 1. import csv
# 2. Open file 
# 3. csv.reader
# 4. reformat into a python object list of list


import csv

# Open file 
data = open('example.csv', encoding = 'utf-8')

# csv.reader
csv_data = csv.reader(data)

# reformat into a python object list of list
data_lines = list(csv_data)


# print(data_lines[0])            # ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'city']
# print(data_lines[1])            # ['1', 'Joseph', 'Zaniolini', 'jzaniolini0@simplemachines.org', 'Male', '163.168.68.132', 'Pedro Leopoldo']

# print(len(data_lines))          # 1001



for line in data_lines[:5]:
    print(line)
                                    # ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'city']
                                    # ['1', 'Joseph', 'Zaniolini', 'jzaniolini0@simplemachines.org', 'Male', '163.168.68.132', 'Pedro Leopoldo']
                                    # ['2', 'Freida', 'Drillingcourt', 'fdrillingcourt1@umich.edu', 'Female', '97.212.102.79', 'Buri']
                                    # ['3', 'Nanni', 'Herity', 'nherity2@statcounter.com', 'Female', '145.151.178.98', 'Claver']
                                    # ['4', 'Orazio', 'Frayling', 'ofrayling3@economist.com', 'Male', '25.199.143.143', 'Kungur']




# getting only email
all_emails = []

for line in data_lines[1:5]:
    all_emails.append(line[3])
    
print(all_emails)               # 'jzaniolini0@simplemachines.org', 'fdrillingcourt1@umich.edu', 'nherity2@statcounter.com', 'ofrayling3@economist.com']


# getting full name 
# list of list
all_names = []

for line in data_lines[1:5]:
    all_names.append(line[1] + " " + line[2])

print(all_names)                # ['Joseph Zaniolini', 'Freida Drillingcourt', 'Nanni Herity', 'Orazio Frayling']




# make new csv file 
file_to_output = open('new_csv_file.csv', mode = 'w', newline = '')
# csv.writer()
csv_write = csv.writer(file_to_output, delimiter = ',')

csv_write.writerow(['a','b','c'])
csv_write.writerows([['1','2','3'], ['4','5','6']])

file_to_output.close()


# # append mode 
# f = open('new_csv_file.csv', mode = 'a', newline='')



