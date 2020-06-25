from digit_recognizer import arr as ar


###########Initializing arrays########
rows,cols =(9,9)
arr = [[0 for i in range(cols)] for j in range(rows)] 
brr = [[0 for i in range(cols)] for j in range(rows)] 
crr = [[0 for i in range(cols)] for j in range(rows)] 
#######Copying the array from digit recognizer########
arr=ar

########  Backtracking Algorithm ########
def safe_to_place(arr,row,col,i):
    for x in range(9):
        if(arr[x][col] == i or arr[row][x] == i ):
            return False
    
    u = row
    v =col
    u =int(u/3)
    u  =u*3
    v =int(v/3)
    v =v*3
    for x in range(u,u+3):
        for y in range(v,v+3):
            if(arr[x][y] == i ):
                return False
    return True  

#this function extracts all locations where array is zero.
def zero_location(arr,z):
    for x in range(9):
        for y in range(9):
            if(arr[x][y] == 0):
                z[0]=x
                z[1]=y
                return True 
    return False 
def solve():    
    z=[0,0]
    if(zero_location(arr,z) == False):
        return True
    x=z[0]
    y=z[1]
   
    if(arr[x][y] == 0):
        for num in range(1,10):
            if(safe_to_place(arr,x,y,num)):
                arr[x][y]=num
                
                if(solve()):
                    return True
                arr[x][y]=0
                

    return False