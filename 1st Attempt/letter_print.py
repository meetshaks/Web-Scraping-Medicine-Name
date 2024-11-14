import string

for i in string.b:
    for j in string.b:
        if i == j:
            print(i)
        else:
            print(i + j)