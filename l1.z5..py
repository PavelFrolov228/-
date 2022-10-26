s = input()
while s.find(':') != -1:
    s = s.replace(':', '.')
while s.find('.') != -1 or s.find(',') != -1 or s.find('-') != -1 or s.find('!') != -1 or s.find('?') != -1:
    s = s.replace('.', ':)')
    s = s.replace(',', ':)')
    s = s.replace('-', ':)')
    s = s.replace('!', ':)')
    s = s.replace('?', ':)')
print(s)

