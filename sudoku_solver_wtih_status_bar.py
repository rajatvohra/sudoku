from tkinter import *
import tkinter.ttk  as ttk
from tkinter import simpledialog
from tkinter import messagebox
from digit_recognizer import arr as ar
from solvability_test import isValidConfig 

rows,cols =(9,9)
arr = [[0 for i in range(cols)] for j in range(rows)] 
brr = [[0 for i in range(cols)] for j in range(rows)] 
crr = [[0 for i in range(cols)] for j in range(rows)] 

arr=ar

count=0


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
def solve_with_steps():    
    z=[0,0]
    if(zero_location(arr,z) == False):
        return True
    x=z[0]
    y=z[1]
    e="white"
    if(arr[x][y] == 0):
        for num in range(1,10):
            if(safe_to_place(arr,x,y,num)):
                arr[x][y]=num          
                wo=IntVar()
                wo.set(num)
                w=wo.get()
                l=Button(my_frame,text=str(w),font=("Helvetica", 16),relief="solid",background="green")
                l.config(width=2)
                l.grid(row=x,column=y)
                
                root.after(40,root.update()) 
                       
                if(solve_with_steps()):
                    return True
                arr[x][y]=0   
                wo=IntVar()
                wo.set(0)
                w=" "     
                l=Button(my_frame,text=str(w),font=("Helvetica", 16), relief="solid",background="red")
                l.config(width=2)
                l.grid(row=x,column=y)
                root.after(40,root.update())                            
                          
    return False
def solve_final():    
    solve()
    update()
def update():
    for r in range(9):
        for t in range(9):
            wo=IntVar()
            wo.set(arr[r][t])
            w=wo.get()
            
            if(w==0):
                w="  "
                l=Button(my_frame,text=str(w),font=("Helvetica", 16), relief="solid",command=lambda row=r,column =t :check_if(row,column))
                l.config(width=2)
                l.grid(row=r,column=t)
            else:

                l=Button(my_frame,text=str(w),font=("Helvetica", 16),relief="solid",command=lambda row=r,column =t :wrong_input(row,column))
                l.config(width=2)
                l.grid(row=r,column=t)            
def under_work():
    status.set("OOPS,this button is under construction right now")
    status_bar.config(borderwidth=3,background="black",foreground="white")
def copy():
    for x in range(9):
        for y in range(9):
            brr[x][y]=arr[x][y]            
def copy_c():
    for x in range(9):
        for y in range(9):
            crr[x][y]=arr[x][y]
def reset():
    for x in range(9):
        for y in range(9):
            arr[x][y]=brr[x][y]
    update()
def copy_to_b():
    for x in range(9):
        for y in range(9):
            brr[x][y]=arr[x][y]   
def validity_check():
    if(isValidConfig(arr,9)==True):
        status.set("this is a Valid configuration")
        status_bar.config(borderwidth=3,background="green",foreground="black")
    else:
        status.set("this is a Invalid configuration")
        status_bar.config(borderwidth=3,background="red",foreground="black")
def check_if(r, c):
    q = simpledialog.askinteger("input","please input an integer between 1 and 9 both inclusive")
    if(crr[r][c]==q):
        global count 
        arr[r][c]=q
        update()
        count=count+1
        var12="correct,keep up the good work,current streak ="+str(count)
        status.set(var12)
        status_bar.config(borderwidth=3,background="green",foreground="black")
    elif(q is None):
        status.set("you forgot to give input ")
        status_bar.config(borderwidth=3,background="pink",foreground="black")
    elif(q>9):
        messagebox.showerror("Error", "your input was greater than 9")
    elif(q<1):
        messagebox.showerror("Error", "your input was less than 1")
    else:
        count=0
        status.set("Incorrect,come on have 1 more try")
        status_bar.config(borderwidth=3,background="red",foreground="white")        
def wrong_input(r, c):
    q = simpledialog.askinteger("input","please input an integer between 1 and 9 both inclusive")
    global count 
    arr[r][c]=q
    update()


root=Tk()
root.geometry('430x430')
my_frame=Frame(root,borderwidth=2,width=500,height=500)




root.title("solve sudoku")

####### Menu  ###########
menu =Menu(root)
root.config(menu=menu)

submenu=Menu(menu)
menu.add_cascade(label="solve",menu =submenu)
submenu.add_command(label="with steps",command=solve_with_steps)
submenu.add_command(label="without steps",command=solve_final)

menu.add_command(label="high score",command =under_work)


menu.add_command(label="reset screen",command =reset)

menu.add_command(label="set as og",command =copy_to_b)



menu.add_command(label="check validity",command =validity_check)

save=Menu(menu)
menu.add_cascade(label="save/logout",menu =save)
save.add_command(label="save",command=under_work)
save.add_command(label="logout",command=under_work)
save.add_command(label="logout and exit",command=under_work)

####### Status Bar###########
status=StringVar()
status.set("hi, I am your status bar")

status_bar= ttk.Label(root, textvariable  =status,relief=SUNKEN)
status_bar.config(pad=10,borderwidth=3,background="blue",foreground="white")
status_bar.pack(side=BOTTOM,fill=X)


####### Main ###########

copy()
solve()
copy_c()
reset()
update()

my_frame.pack()
root.mainloop()