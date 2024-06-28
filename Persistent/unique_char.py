def unique_char(str):
    count = {}
    for i in str:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    for key,val in count.items():
        if (val==1):
            print(key,end="")

unique_char('Geeks for Geeks')