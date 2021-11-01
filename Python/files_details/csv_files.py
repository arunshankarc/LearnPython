"""
Learning about csv
"""

from csv import reader
from csv import DictReader
from csv import writer


# set reader(fd) to reader(fd, delimiter='') in order to set different delimiters
with open("fighters.csv", encoding='UTF-8') as fd:
    csv_reader = reader(fd)
    fighters = []
    fighters = [[s.upper() for s in row] for row in csv_reader]
    for row in csv_reader:
        fighters.append(row)
        print(row) # Returns a list of each value in row

with open("fighters.csv", encoding='UTF-8') as fd:
    dict_reader = DictReader(fd)
    for row in dict_reader:
        print(f"{row['Name']} is from {row['Country']}") # Returns a list of each value in row


# set reader(fd) to reader(fd, delimiter='') in order to set different delimiters
with open("fighters.csv", encoding='UTF-8') as fd:
    csv_reader = reader(fd, delimiter='|')
    for row in csv_reader:
        print(row) # Returns a list of each value in row


with open("screaming_fighters.csv", "w",encoding='UTF-8') as fd:
    csv_writer = writer(fd)
    for row in fighters:
        csv_writer.writerow(row)
