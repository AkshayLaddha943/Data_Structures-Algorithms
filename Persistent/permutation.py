def perm(lst):
    if len(lst) == 0:
        return []
    
    if len(lst) == 1:
        return lst
    
    for i in range(len(lst)):
        
        rem = lst[:i] + lst[i+1:]
        
        for p in perm(rem):
            print(lst[i] + p)

data = ["3", "3", "4"]
for p in perm(data):
    print(p)