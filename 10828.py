import sys

n = int(sys.stdin.readline())
stack = []

def switch_case(command):
    match command[0]:
        case "push":
            stack.append(command[1])
            
        case "pop":
            if len(stack) == 0:
                print(-1) 
            else:
                print(stack.pop()) 
            
        case "size":
            print(len(stack)) 
        
        case "empty":
            print(1 if len(stack) == 0 else 0) 
        
        case "top":
            if len(stack) == 0:
                print(-1) 
            else:
                print(stack[-1])
    

for i in range(n):
    command = sys.stdin.readline().split()
    switch_case(command)
    