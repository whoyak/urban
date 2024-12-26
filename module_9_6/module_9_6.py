def all_variants(text:str):
    n = len(text)
    for i in range(1, n + 1):
        for j in range(n - i + 1):
            yield text[j:j+i]


a = all_variants("abc")
for i in a:
    print(i)


