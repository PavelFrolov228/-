s = input()
if s.find('@') != -1:
    print(s[s.index('@')+1:])
else:
    print(s)