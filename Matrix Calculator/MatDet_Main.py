from tkinter import *
from matrix_functions import *
from tkinter import messagebox
root=Tk()
root.configure(bg="black")
root.geometry("1100x700")
root.title("Matrix")
main_frame=Frame(root,height=700,width=500,bg='black')
result_frame=Frame(root,bg='black')
middle_frame=Frame(root,bg='black')
left_frame=Frame(root,bg='black')
right_frame=Frame(root,bg='black')
matrix_frame=Frame(root,bg='black')

def input_row_column():
    global row,col
    Label(middle_frame,text="Enter number of rows",bg='black',fg='white',borderwidth=3,relief='groove',font=('ariel',10),width=21).grid(row=4,column=12)
    Label(middle_frame,text="Enter number of rows",bg='black',fg='white',borderwidth=3,relief='groove',font=('ariel',10),width=21).grid(row=5,column=12)
    row=IntVar()
    Entry(middle_frame,width=4,textvariable=row,borderwidth=3,bg='gray64',fg='black',relief='solid').grid(row=4,col=12)
    col=IntVar()
    Entry(middle_frame,width=4,textvariable=col,borderwidth=3,bg='gray64',fg='black',relief='solid').grid(row=5,col=12)
    Button(middle_frame,text='submit',bg='black',fg='white',width=5,command=input_grid).grid(row=6,column=10,columnspan=3)
    middle_frame.grid(row=5,rowspan=4,column=2,columnspan=4,padx=200,pady=50)
    
def input_grid():
    global right_frame
    middle_frame.grid_forget()
    right_frame.destroy()
    right_frame=Frame(root,bg='black')
    r=row.get()
    c=col.get()
    global dic
    temp=[]
    dic=[]
    for i in range (r):
        for j in range (c):
            temp.append(IntVar())
        dic.append(temp)
        temp=[]
    Label(right_frame,text="Input Matrix",fg='black',font=('ariel',15)).grid(row=0,col=1,columnspan=3,padx=10,pady=10)
    for i in range(1,r+1):
        for j in range(1,c+1):
            ent=Entry(right_frame,width=4,textvariable=dic[i-1][j-1])
            ent.grid(row=i,column=j)
    Button(right_frame,text='submit',bg='black',fg='white',font=('ariel',15),width=5,command=input_cmd).grid(row=4,column=1,columnspan=3,pady=10)
    right_frame.grid(row=5,rowspan=100,column=50,columnsoan=4,padx=200,pady=50)

def input_cmd():
    global mainmatrix
    mainmatrix=[]
    temp=[]
    for i in dic:
        for j in i:
            mainmatrix.append(temp)
            temp=[]
    return mainmatrix

def frame_destory():
    global middle_frame
    global right_frame
    global result_frame
    
    middle_frame.destroy()
    middle_frame=Frame(root,bg='black')
    
    
    right_frame.destroy()
    right_frame=Frame(root,bg='black')
    
    
    result_frame.destroy()
    result_frame=Frame(root,bg='black')
    
def addition_input_row_column():
    frame_destory()
    global row1,col1
    Label(middle_frame,text="Enter Number of Rows of First Matrix",bg="black",fg="white",borderwidth=3,relief="groove",font=('ariel',10),width=35).grid(row=4,column=11,pady=10,padx=0)
    Label(middle_frame,text="Enter Number of Column of First Matrix",bg="black",fg="white",borderwidth=3,relief="groove",font=('ariel',10),width=35).grid(row=5,column=11,pady=10,padx=0)
    row1=IntVar()
    Entry(middle_frame,width=4,textvariable=row1,borderwidth=3,bg="gray64",fg="black",relief="solid").grid(row=4,column=14,pady=10,padx=0)
    col1=IntVar()
    Entry(middle_frame,width=4,textvariable=col1,borderwidth=3,bg="gray64",fg="black",relief="solid").grid(row=5,column=14,pady=10,padx=0)
    
    global row2,col2
    Label(middle_frame,text="Enter Number of Rows of Second Matrix",bg="black",fg="white",borderwidth=3,relief="groove",font=('ariel',10),width=35).grid(row=8,column=11,pady=10,padx=0)
    Label(middle_frame,text="Enter Number of Column of Second Matrix",bg="black",fg="white",borderwidth=3,relief="groove",font=('ariel',10),width=35).grid(row=9,column=11,pady=10,padx=0)
    row2=IntVar()
    Entry(middle_frame,width=4,textvariable=row2,borderwidth=3,bg="gray64",fg="black",relief="solid").grid(row=8,column=14,pady=10,padx=0)
    col2=IntVar()
    Entry(middle_frame,width=4,textvariable=col2,borderwidth=3,bg="gray64",fg="black",relief="solid").grid(row=9,column=14,pady=10,padx=0)
    
    Label(middle_frame,text="""
          """,bg="black").grid(row=10,column=14,padx=80,pady=2,sticky=EW)
    submit_btn=Button(middle_frame,text="submit",bg="black",fg="white",width=5,command=addition_input_grid)
    submit_btn.grid(row=11,column=14,columnspan=3)
    middle_frame.grid(rows=5,rowspan=10,column=2,columnspan=4,padx=200,pady=50)
    
def addition_input_grid():
        r1=row1.get()
        c1=col1.get()
        r2=row2.get()
        c2=col2.get()
        
        if r1==r2 and c1==c2 and r1!=0 and r2!=0 and c1!=0 and c2!=0:
            global right_frame
            middle_frame.grid_forget()
            right_frame.destroy()
            right_frame=Frame(root,bg="black")
            
            global dic1
            temp=[]
            dic1=[]
            for i in range (r1):
                for j in range (c1):
                    temp.append(IntVar())
                dic1.append(temp)
                temp=[]
            Label(right_frame,text="            Input Matrix 1",bg="black",fg="white",font=("ariel",15)).grid(row=0,column=1,columnspan=c1+c2,padx=10,pady=10)
            for i in range(1,r1+1):
                for j in range(1,c1+1):
                    ent=Entry(right_frame,width=4,textvariable=dic1[i-1][j-1])
                    ent.grid(row=i,column=j+2,padx=5,pady=5)
                    
            global dic2
            temp=[]
            dic2=[]
            for i in range (r2):
                for j in range (c2):
                    temp.append(IntVar())
                dic2.append(temp)
                temp=[]
            Label(right_frame,text="            Input Matrix 2",bg="black",fg="white",font=("ariel",15)).grid(row=r1+1,column=1,columnspan=c1+c2,padx=10,pady=10)
            for i in range(1,r2+1):
                for j in range(1,c2+1):
                    ent=Entry(right_frame,width=4,textvariable=dic2[i-1][j-1])
                    ent.grid(row=i+r1+2,column=j+2,padx=5,pady=5)
            
            Button(right_frame,text="submit",font=('ariel',15),bg='black',fg='white',width=5,command=addition_input_cmd).grid(row=r1+r2+4,column=2,columnspan=c1+c2,padx=10,pady=10)
            right_frame.grid(row=5,rowspan=100,column=50,columnspan=40)
            
        elif r1==0 or r2==0 or c1==0 or c2==0:
            messagebox.showerror("Input Error","Rows and Columns Can't be zero")
        else:
            messagebox.showerror("Input Error","Number of rows and Columns should be equal")
            
def addition_input_cmd():
    
    global add1
    add1=[]
    temp=[]
    for i in dic1:
        for j in i:
            temp.append(j.get())
        add1.append(temp)
        temp=[]
        
    global add2
    add2=[]
    temp=[]
    for i in dic2:
        for j in i:
            temp.append(j.get())
        add2.append(temp)
        temp=[]
    
    addition_result=addition_of_matrix(add1,add2)
    Label(result_frame,text="Result",fg="white",bg="black",font=('ariel',15)).grid(row=0,column=0,columnspan=len(addition_result[0]))
    for i in range(len(addition_result)):
        for j in range(len(addition_result[0])):
            Label(result_frame,text=addition_result[i][j],padx=6,pady=5,width=5,font=('ariel',15)).grid(row=i+1,column=j,padx=5,pady=5)
    result_frame.grid(row=7,column=300,padx=100)
    
def subtraction_input_row_column():
    frame_destory()
    global row1,col1
    Label(middle_frame,text="Enter Number of Rows of First Matrix",bg="black",fg="white",borderwidth=3,relief="groove",font=('ariel',10),width=35).grid(row=4,column=11,pady=10,padx=0)
    Label(middle_frame,text="Enter Number of Column of First Matrix",bg="black",fg="white",borderwidth=3,relief="groove",font=('ariel',10),width=35).grid(row=5,column=11,pady=10,padx=0)
    row1=IntVar()
    Entry(middle_frame,width=4,textvariable=row1,borderwidth=3,bg="gray64",fg="black",relief="solid").grid(row=4,column=14,padx=0)
    col1=IntVar()
    Entry(middle_frame,width=4,textvariable=col1,borderwidth=3,bg="gray64",fg="black",relief="solid").grid(row=5,column=14,padx=0)
    
    global row2,col2
    Label(middle_frame,text="Enter Number of Rows of Second Matrix",bg="black",fg="white",borderwidth=3,relief="groove",font=('ariel',10),width=35).grid(row=8,column=11,pady=10,padx=0)
    Label(middle_frame,text="Enter Number of Column of Second Matrix",bg="black",fg="white",borderwidth=3,relief="groove",font=('ariel',10),width=35).grid(row=9,column=11,pady=10,padx=0)
    row2=IntVar()
    Entry(middle_frame,width=4,textvariable=row2,borderwidth=3,bg="gray64",fg="black",relief="solid").grid(row=8,column=14,pady=10,padx=0)
    col2=IntVar()
    Entry(middle_frame,width=4,textvariable=col2,borderwidth=3,bg="gray64",fg="black",relief="solid").grid(row=9,column=14,pady=10,padx=0)
    
    Label(middle_frame,text="""
          """,bg="black").grid(row=10,column=14,padx=80,pady=2,sticky=EW)
    submit_btn=Button(middle_frame,text="submit",bg="black",fg="white",width=5,command=subtraction_input_grid)
    submit_btn.grid(row=11,column=14,columnspan=3)
    middle_frame.grid(rows=5,rowspan=10,column=2,columnspan=4,padx=200,pady=50)
    
def subtraction_input_grid():
        r1=row1.get()
        c1=col1.get()
        r2=row2.get()
        c2=col2.get()
        
        if r1==r2 and c1==c2 and r1!=0 and r2!=0 and c1!=0 and c2!=0:
            global right_frame
            middle_frame.grid_forget()
            right_frame.destroy()
            right_frame=Frame(root,bg="black")
            
            global dic1
            temp=[]
            dic1=[]
            for i in range (r1):
                for j in range (c1):
                    temp.append(IntVar())
                dic1.append(temp)
                temp=[]
            Label(right_frame,text="            Input Matrix 1",bg="black",fg="white",font=("ariel",15)).grid(row=0,column=1,columnspan=c1+c2,padx=10,pady=10)
            for i in range(1,r1+1):
                for j in range(1,c1+1):
                    ent=Entry(right_frame,width=4,textvariable=dic1[i-1][j-1])
                    ent.grid(row=i,column=j+2,padx=5,pady=5)
                    
            global dic2
            temp=[]
            dic2=[]
            for i in range (r2):
                for j in range (c2):
                    temp.append(IntVar())
                dic2.append(temp)
                temp=[]
            Label(right_frame,text="            Input Matrix 2",bg="black",fg="white",font=("ariel",15)).grid(row=r1+1,column=1,columnspan=c1+c2,padx=10,pady=10)
            for i in range(1,r2+1):
                for j in range(1,c2+1):
                    ent=Entry(right_frame,width=4,textvariable=dic2[i-1][j-1])
                    ent.grid(row=i+r1+2,column=j+2,padx=5,pady=5)
            
            Button(right_frame,text="submit",font=('ariel',15),bg='black',fg='white',width=5,command=subtraction_input_cmd).grid(row=r1+r2+4,column=2,columnspan=c1+c2,padx=10,pady=10)
            right_frame.grid(row=5,rowspan=100,column=50,columnspan=40)
            
        elif r1==0 or r2==0 or c1==0 or c2==0:
            messagebox.showerror("Input Error","Rows and Columns Can't be zero")
        else:
            messagebox.showerror("Input Error","Number of rows and Columns should be equal")

def subtraction_input_cmd():
    
    global sub1
    sub1=[]
    temp=[]
    for i in dic1:
        for j in i:
            temp.append(j.get())
        sub1.append(temp)
        temp=[]
        
    global sub2
    sub2=[]
    temp=[]
    for i in dic2:
        for j in i:
            temp.append(j.get())
        sub2.append(temp)
        temp=[]
    
    subtraction_result=subtraction_of_matrix(sub1,sub2)
    Label(result_frame,text="Result",fg="white",bg="black",font=('ariel',15)).grid(row=0,column=0,columnspan=len(subtraction_result[0]))
    for i in range(len(subtraction_result)):
        for j in range(len(subtraction_result[0])):
            Label(result_frame,text=subtraction_result[i][j],padx=6,pady=5,width=5,font=('ariel',15)).grid(row=i+1,column=j,padx=5,pady=5)
    result_frame.grid(row=7,column=300,padx=100)
            
            
def product_input_row_column():
    frame_destory()
    global row1,col1
    Label(middle_frame,text="Enter Number of Rows of First Matrix",bg="black",fg="white",borderwidth=3,relief="groove",font=('ariel',10),width=35).grid(row=4,column=11,pady=10,padx=0)
    Label(middle_frame,text="Enter Number of Column of First Matrix",bg="black",fg="white",borderwidth=3,relief="groove",font=('ariel',10),width=35).grid(row=5,column=11,pady=10,padx=0)
    row1=IntVar()
    Entry(middle_frame,width=4,textvariable=row1,borderwidth=3,bg="gray64",fg="black",relief="solid").grid(row=4,column=14,padx=0)
    col1=IntVar()
    Entry(middle_frame,width=4,textvariable=col1,borderwidth=3,bg="gray64",fg="black",relief="solid").grid(row=5,column=14,padx=0)
    
    global row2,col2
    Label(middle_frame,text="Enter Number of Rows of Second Matrix",bg="black",fg="white",borderwidth=3,relief="groove",font=('ariel',10),width=35).grid(row=8,column=11,pady=10,padx=0)
    Label(middle_frame,text="Enter Number of Column of Second Matrix",bg="black",fg="white",borderwidth=3,relief="groove",font=('ariel',10),width=35).grid(row=9,column=11,pady=10,padx=0)
    row2=IntVar()
    Entry(middle_frame,width=4,textvariable=row2,borderwidth=3,bg="gray64",fg="black",relief="solid").grid(row=8,column=14,pady=10,padx=0)
    col2=IntVar()
    Entry(middle_frame,width=4,textvariable=col2,borderwidth=3,bg="gray64",fg="black",relief="solid").grid(row=9,column=14,pady=10,padx=0)
    
    Label(middle_frame,text="""
          """,bg="black").grid(row=10,column=14,padx=80,pady=2,sticky=EW)
    submit_btn=Button(middle_frame,text="submit",bg="black",fg="white",width=5,command=product_input_grid)
    submit_btn.grid(row=11,column=14,columnspan=3)
    middle_frame.grid(rows=5,rowspan=10,column=2,columnspan=4,padx=200,pady=50)
    
def product_input_grid():
        r1=row1.get()
        c1=col1.get()
        r2=row2.get()
        c2=col2.get()
        
        if c1==r2 and r1!=0 and r2!=0 and c1!=0 and c2!=0:
            global right_frame
            middle_frame.grid_forget()
            right_frame.destroy()
            right_frame=Frame(root,bg="black")
            
            global dic1
            temp=[]
            dic1=[]
            for i in range (r1):
                for j in range (c1):
                    temp.append(IntVar())
                dic1.append(temp)
                temp=[]
            Label(right_frame,text="            Input Matrix 1",bg="black",fg="white",font=("ariel",15)).grid(row=0,column=1,columnspan=c1+c2,padx=10,pady=10)
            for i in range(1,r1+1):
                for j in range(1,c1+1):
                    ent=Entry(right_frame,width=4,textvariable=dic1[i-1][j-1])
                    ent.grid(row=i,column=j+2,padx=5,pady=5)
                    
            global dic2
            temp=[]
            dic2=[]
            for i in range (r2):
                for j in range (c2):
                    temp.append(IntVar())
                dic2.append(temp)
                temp=[]
            Label(right_frame,text="            Input Matrix 2",bg="black",fg="white",font=("ariel",15)).grid(row=r1+1,column=1,columnspan=c1+c2,padx=10,pady=10)
            for i in range(1,r2+1):
                for j in range(1,c2+1):
                    ent=Entry(right_frame,width=4,textvariable=dic2[i-1][j-1])
                    ent.grid(row=i+r1+2,column=j+2,padx=5,pady=5)
            
            Button(right_frame,text="submit",font=('ariel',15),bg='black',fg='white',width=5,command=product_input_cmd).grid(row=r1+r2+4,column=2,columnspan=c1+c2,padx=10,pady=10)
            right_frame.grid(row=5,rowspan=100,column=50,columnspan=40)
            
        elif r1==0 or r2==0 or c1==0 or c2==0:
            messagebox.showerror("Input Error","Rows and Columns Can't be zero")
        else:
            messagebox.showerror("Input Error","Number of rows and Columns should be equal")

def product_input_cmd():
    global pro1
    pro1=[]
    temp=[]
    for i in dic1:
        for j in i:
            temp.append(j.get())
        pro1.append(temp)
        temp=[]
        
    global pro2
    pro2=[]
    temp=[]
    for i in dic2:
        for j in i:
            temp.append(j.get())
        pro2.append(temp)
        temp=[]
    
    product_result=product_of_matrix(pro1,pro2)
    Label(result_frame,text="Result",fg="white",bg="black",font=('ariel',15)).grid(row=0,column=0,columnspan=len(product_result[0]))
    for i in range(len(product_result  )):
        for j in range(len(product_result[0])):
            Label(result_frame,text=product_result[i][j],padx=6,pady=5,width=5,font=('ariel',15)).grid(row=i+1,column=j,padx=5,pady=5)
    result_frame.grid(row=7,column=300,padx=100)
    
def transpose_input_row_column():
    frame_destory()
    global row,col
    Label(middle_frame,text="Enter Number of Rows",bg="black",fg="white",borderwidth=3,relief="groove",font=('ariel',10),width=35).grid(row=4,column=11,pady=10,padx=0)
    Label(middle_frame,text="Enter Number of Columns",bg="black",fg="white",borderwidth=3,relief="groove",font=('ariel',10),width=35).grid(row=5,column=11,pady=10,padx=0)
    row=IntVar()
    Entry(middle_frame,width=4,textvariable=row,borderwidth=3,bg="gray64",fg="black",relief="solid").grid(row=4,column=14,padx=0)
    col=IntVar()
    Entry(middle_frame,width=4,textvariable=col,borderwidth=3,bg="gray64",fg="black",relief="solid").grid(row=5,column=14,padx=0)
    submit_btn=Button(middle_frame,text="submit",bg="black",fg="white",width=5,command=transpose_input_grid)
    submit_btn.grid(row=11,column=14,columnspan=3)
    middle_frame.grid(rows=5,rowspan=10,column=2,columnspan=4,padx=200,pady=50)
    
def transpose_input_grid():
        r=row.get()
        c=col.get()
        
        if  r!=0 and c!=0:
            global right_frame
            middle_frame.grid_forget()
            right_frame.destroy()
            right_frame=Frame(root,bg="black")
            
            global dic1
            temp=[]
            dic1=[]
            for i in range (r):
                for j in range (c):
                    temp.append(IntVar())
                dic1.append(temp)
                temp=[]
            Label(right_frame,text="            Input Matrix",bg="black",fg="white",font=("ariel",15)).grid(row=0,column=1,columnspan=c,padx=10,pady=10)
            for i in range(1,r+1):
                for j in range(1,c+1):
                    ent=Entry(right_frame,width=4,textvariable=dic1[i-1][j-1])
                    ent.grid(row=i,column=j+2,padx=5,pady=5)
                    
            Button(right_frame,text="submit",font=('ariel',15),bg='black',fg='white',width=5,command=transpose_input_cmd).grid(row=r+1,column=c-1,columnspan=c,padx=10,pady=10)
            right_frame.grid(row=5,rowspan=100,column=50,columnspan=40)
        else:
            messagebox.showerror("Input Error","Number of rows and Columns should be equal")

def transpose_input_cmd():
    global transposematrix
    transposematrix=[]
    temp=[]
    for i in dic1:
        for j in i:
            temp.append(j.get())
        transposematrix.append(temp)
        temp=[]
    
    transpose_result=transpose(transposematrix)
    Label(result_frame,text="Result",fg="white",bg="black",font=('ariel',15)).grid(row=0,column=0,columnspan=len(transpose_result[0]))
    for i in range(len(transpose_result)):
        for j in range(len(transpose_result[0])):
            Label(result_frame,text=transpose_result[i][j],padx=6,pady=5,width=5,font=('ariel',15)).grid(row=i+1,column=j,padx=5,pady=5)
    result_frame.grid(row=7,column=300,padx=100)

                          
def back_btn():
    back.grid_forget()
    matrix_frame.grid_forget()
    middle_frame.grid_forget()
    right_frame.grid_forget()
    result_frame.grid_forget()
    main_frame.grid()
    
def close_main(event=None):
    if messagebox.askokcancel("Quit","Do You really want to quit?"):
        root.destroy()
        
root.protocol("DELETE_WINDOW",close_main)
    
lbl=Label(matrix_frame,text="Matrix",font=('Ariel',20),bg='black',fg='white')
lbl.grid(row=0,column=1,ipadx=20,ipady=10)
button1=Button(matrix_frame,text="Addition",bg="black",fg="white",padx=20,pady=30,command=addition_input_row_column)
button1.grid(row=5,column=0,padx=10,pady=10,sticky="nsew")
button1=Button(matrix_frame,text="Subtraction",bg="black",fg="white",padx=20,pady=30,command=subtraction_input_row_column)
button1.grid(row=5,column=2,padx=10,pady=10,sticky="nsew")
button1=Button(matrix_frame,text="Product",bg="black",fg="white",padx=20,pady=30,command=product_input_row_column)
button1.grid(row=6,column=0,padx=10,pady=10,sticky="nsew")
button1=Button(matrix_frame,text="Transpose",bg="black",fg="white",padx=20,pady=30,command=transpose_input_row_column)
button1.grid(row=6,column=2,padx=10,pady=10,sticky="nsew")
back=Button(matrix_frame,bg="black",fg="white",text="Quit",padx=10,pady=10,width=10,command=close_main)
back.grid(row=12,column=1,padx=10,pady=10,sticky="nsew")
matrix_frame.grid(row=0,column=0,columnspan=2,rowspan=6,sticky=W)



root.mainloop()