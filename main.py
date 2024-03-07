f = open("text.txt","r")
read = f.readlines()
for i in read:
    words = i.split()
    i_list = []
    for word in words:
        i_list.extend(word.split(","))
    if (i_list == []):
        continue
    print(i_list)
f.close()