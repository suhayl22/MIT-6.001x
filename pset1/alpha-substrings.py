s = 'azcbobobegghakl'

# tracks length of biggest substring
max_len = 0

# tracks the indices at which substrings begin
idx = 0
max_idx = 0

# length of input string
s_len = len(s)

while idx < s_len:
    if (s_len - idx <= max_len):
        break
        
    cur_len = 1
    
    start_idx = idx
    while (idx + 1 < s_len and s[idx] <= s[idx + 1]):
        cur_len += 1
        idx += 1
    # print s[start_idx:idx+1]
        
    if (cur_len > max_len):
        max_len = cur_len
        # print 'max_len: ' + str( max_len)
        max_idx = start_idx
        # print 'max_idx: ' + str(max_idx)
        
    idx += 1

winner = s[max_idx:max_idx+max_len]
print 'Longest substring in alphabetical order is: ' + str(winner)