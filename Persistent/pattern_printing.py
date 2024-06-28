def pattern(d):
    for i in range(0,d):
        for j in range(i+1, 0):
            print("* ",end="")
        
        print("\r")

#pyramid print
def pattern_pyramid(rows):
    for i in range(1,rows+1):
        print(" "*(rows-i) + "*" * (i))
        # print("*"*(i) + " "*(rows-i))

# #half-left pyramid print
# def pattern_left_pyramid(rows):
#     for i in range(1,rows+1):
#         print(" "*(rows-i) + "*" * (i))

def pyramid(rows):
    k = rows-1
    for i in range(0, rows):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("")
    
    k = rows-1
    for i in range(rows, -1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k = k+1
        for j in range(0,i+1):
            print("* ",end="")
        print("")
        
            
        

if __name__ == "__main__":
    pyramid(5)