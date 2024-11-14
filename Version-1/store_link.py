import string

base_url = "https://www.drugs.com/alpha/"

with open("drug_urls.txt", "w") as f:
    for i in string.ascii_lowercase:
        for j in string.ascii_lowercase:
            if i == j:
                f.write(base_url + i + ".html\n")
            else:
                f.write(base_url + i + j + ".html\n")