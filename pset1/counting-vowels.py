s = 'azcbobobegghakl'

vowels = 'aeiou'
count = 0

for char in s:
    for v in vowels:
        if (char == v):
            count += 1
            continue
           
print 'Number of vowels: ' + str(count)