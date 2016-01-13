s = 'azcbobobegghakl'

word = 'bob'
found = 0
word_len = len('bob')
s_len = len(s)

# iterate over chars in s, adding to found if bob is found there
for idx in range( s_len ):
    result = s.find('bob', idx, idx + word_len)
    if (result > -1):
        found += 1
    
print 'Number of times bob occurs is: ' + str(found)