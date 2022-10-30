f = open('user-tweets.txt', 'r')
char = "'@"
result = ''
for i in f.readlines():
    result = " ".join(
        filter(
            lambda word: not word.startswith(char), i.split()
        )

    )
    print(result)
    print(i.split())
print(result)
