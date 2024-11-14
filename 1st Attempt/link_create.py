import string

base_url = "https://www.drugs.com/alpha/"

for i in string.ascii_lowercase:
    for j in string.ascii_lowercase:
        if i == j:
            print(base_url + i + ".html")
        else:
            print(base_url + i + j + ".html")