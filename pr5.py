А = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
В = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']


result = {}


for i in range(len(А)):
    letter = В[i]
    number = А[i]


    if letter in result:
        result[letter] += number

    else:
        result[letter] = number

print(result)