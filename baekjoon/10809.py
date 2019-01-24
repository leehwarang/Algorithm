import string

s = input()
alphabet = string.ascii_lowercase
result = ''
for char in alphabet:
    result += str(s.find(char)) + ' '
print(result[:-1])
