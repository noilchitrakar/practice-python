heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#   so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#   Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list
# down all functions available in list)

#1 
print(len(heros))

#2
heros.append('black panther')
print(heros)

#3
heros.remove('black panther')
heros.append('hulk')

print(heros)

#4

heros[1:3]=['Doctor strange']
print(heros)

heros.sort()

print(heros)
