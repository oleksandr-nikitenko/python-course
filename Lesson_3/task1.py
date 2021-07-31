sample_string = ['helloworld', 'my', 'x']

for s in sample_string:
    if len(s) < 2:
        s = "Empty String"
    else:
        s = s[0:2] + s[-2:]
    print(s)

