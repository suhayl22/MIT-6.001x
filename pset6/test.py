from ps6_encryption import * 

ALPHA_SIZE = 26

def buildCoder (shift):
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    
    count = 0
    dict = {}
    # build first half of dict with lowercase letters
    for i in range(ALPHA_SIZE):
        dict[ lowers[i] ] = lowers[(i + shift) % ALPHA_SIZE]
        dict[ uppers[i] ] = uppers[(i + shift) % ALPHA_SIZE]
    
    return dict
    
def applyCoder (text, coder):
    new_text = ''
    dict = coder
    for char in text:
        if char in dict:
            new_text += dict[char]
        else:
            new_text += char
    
    return new_text     
    
def applyShift (text, shift):
    return applyCoder(text, buildCoder(shift))
    
def findBestShift (wordList, text):
    shift = 0
    best_shift = shift
    
    max_recognized_words = 0
    
    tokens = text.split(' ')
    
    for shift in range(ALPHA_SIZE):
        decrypted_words = []
        
        for word in tokens:
            decrypted = applyShift(word, shift)
            decrypted_words.append(decrypted)
        
        recognized_words = 0
        for word in decrypted:
            if word in wordList:
                recognized_words += 1
        
        if recognized_words > max_recognized_words:
            max_recognized_words = recognized_words
            best_shift = shift
        
    return best_shift