import string

for i in string.ascii_lowercase:
    for j in string.ascii_lowercase:
        if i == j:
            print(i)
        else:
            print(i + j)
