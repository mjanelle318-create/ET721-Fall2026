"""
Janelle Moncrieffe
lab 3: intro to pyhton basics
Sep 9, 2026
"""

print("------example 1: string------")
name = "michael jackson"
print(name[::2])
print(name[3:10:2])

print("------example 2: string methods------")
name1 = name.upper()
name2 = name.lower()
name3 = name.replace('Michael', 'Janet')
indexname = name.find('Jack')
print(f'Name in uppercase{name1}')
print(f'Name in lowercase {name2}')
print(f'Index for Jack = {indexname}')
print(f'split name = {name.split('j')}')

print('------example 3: regular expression')
# import the module for the regular expression, re
import re

s1 = 'Michael Jackson is the best'
# define the pattern to search for
pattern = r'smith'
# use the search() u=function to search for the pattern in the string
result = re.search(pattern, s1)
# print result
print(f'The pattern result is {result}')
if result: 
    print('match found')
else:
    print('match not found')

pattern = r"\d\d\d\d\d" # matches any five consecutive digits
zipcode = 'my zip code is = 12345'
match = re.search(pattern, zipcode)
if match:
    print(f'zip code found = {match.group()}')
else:
    print('zip code not found')

print('-----example 4: tuples-----')

# create tuple
tuple1 = ('disco', 10, 1.2)
print(type(tuple1))
print(f"second element =tuple1[1]")
print(f"last element =tuple1[-1]")
print(f'There are {len(tuple1)} elements in the tuple')
rating = (10, 3, 4, 9,7)
print(f'sorted tuple= {sorted(rating)}')

#nested tuple
nestedtuple = (1,2, ('pop', 'rock'), (3,4), ('disco', (8,9)))
print(f'original tuple {nestedtuple}')
print(f'original tuple = {nestedtuple[2]}')
print(f'nested subtuple = {nestedtuple[3][1]}')
print(f'nested sub-subtuple = {nestedtuple[4][1][0]}')

print('-----example 5: dictionary-----')
# create a dictionary
release_year_dictionary = {
    "thriller" : 1982,
    "back in black" : 1980,
    "the dark side of the moon" : 1973,
    "the bodyguard" : 1992,
    "rumours" : 1977
}
# get the values of the key
print(f'the year of the bodyguard = {release_year_dictionary["the bodyguard"]}')
print(f'all keys = {release_year_dictionary.keys()}')

release_year_dictionary["graduation"] = 2007
print(f'all keys = {release_year_dictionary.keys()}')

print('\n -----example 6: sets-----')

#has no orde, and automatically remove duplicate items
set1 = {'pop', "rock", 'soul', 'hard rock', 'rock', 'r&b', 'disco', 'rock'}
print(set1)
check1 = "ac/dc" in set1
print(f'is ac/dc in genres? {check1}')
set1.add("ac/dc")
check1 = "ac/dc" in set1
print(f'is ac/dc in genres? {check1}')


album1 = {"thriller", "rumours", 'back in black'}
album2 = {'rumours', "the dark side of the moon", "back in black"}
# intersions & returns the element that are in both sets
print(album1 & album2)
# union, | returns bthe element of both sets
print(album1 | album2)
# difference ^ returns the element that are in a set but not in the toehr set
print (album1 ^ album2)