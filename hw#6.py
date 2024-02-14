# drop sequential duplicated symdols

word = 'abbccddak'
word_new = ''
prev_x = ''
for x in word:
    if x != prev_x:
        prev_x = x
        word_new = word-new + # word_new += x
        
        print(word)
        print(word_new)