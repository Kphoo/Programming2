word_count={}
texts=input("Text: ").split()

for text in texts:
    try:
        word_count[text]+=1
    except KeyError:
        word_count[text]=1

for key,value in sorted(word_count.items()):
    print(key,":",value)



