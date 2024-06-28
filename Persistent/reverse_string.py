#Time Complexity: O(N)

def reverse_str(str):
    new_s = ""
    for i in str:
        print(i)
        new_s = i+new_s
    
    return new_s

#Time Complexity: O(N)
def reverse_str_stack(str):
    stack = []
    for i in str:
        stack.append(i)
    
    str = ""
    for _ in range(len(stack)):
        str += stack.pop()
    
    return str

if __name__=="__main__":
    print(reverse_str("Persistent"))