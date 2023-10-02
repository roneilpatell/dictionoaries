


count_words = {}
found_word =[]
chars = [',','.','!','?',',',':',';',''/'','"']



outfile = open('somewhat.txt','r')
readwords = outfile.read()
sep = readwords.split()


for word in clean_words:
    if word in count_words:
        if word in count_words:
            count_words[word] += 1
        else:
            count_words[word] = 1



print(count_words)

outfile.close()






