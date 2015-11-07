with open('yazkora.txt', 'r') as f:
    language = f.read()

language = language.split('.')
answer = open('answer.txt', 'w')
for sentence in language:
    sentence = sentence.replace('\n', ' ')
    words = sentence.split(' ')
    for word in words:
        if word[-2:] == 'yo':
            tmp = word + ' '
            answer.write(tmp)
    answer.write('\n')
answer.close()



