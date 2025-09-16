from collections import Counter
file = open('text.txt', 'r')
f = file.read()
f = f.split()
print(Counter(f))
print('\nThe word most used is:', Counter(f).most_common(1))