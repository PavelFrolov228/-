s = input()
if len(s) >= 3:
    if s[-3:] == 'ing':
        print(s[0:-3] + 'ly')
    else:
        print(s + 'ing')
else:
    print(s)
