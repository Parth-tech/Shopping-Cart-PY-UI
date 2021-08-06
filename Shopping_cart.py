from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import ImageTk , Image
# make database and users (if not exists already) table at programme start up
with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
db.commit()
db.close()


class Window1:
    def __init__(self,master):
    	# Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            self.newWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow)
        else:
            ms.showerror('Oops!','Incorrect username or password.')
            
    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if(re.search(regex,self.n_username.get())):  
                ms.showinfo('Success','Account Created!')
                #Create New Account 
                insert = 'INSERT INTO user(username,password) VALUES(?,?)'
                c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
                db.commit()
            else:
                ms.showerror('Oops!','Invalid username.')

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',bg="#358597",fg="white",font = ('',35),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10,bg="#358597")
        Label(self.logf,text = 'Username : ',fg="white",bg="#358597",font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password  : ',fg="white",bg="#358597",font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',fg="black",bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Create Account ',fg="black",bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10,bg="#358597")
        Label(self.crf,text = 'Username: ',fg="white",bg="#358597",font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',fg="white",bg="#358597",font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',fg="black",bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',fg="black",bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=2,column=1)
        
class Window2:
    def __init__(self,master):
        self.master=master
        master.configure(bg="#358597")
        self.master.title("Shopping Cart")
        self.master.geometry("1145x1000")
        # text for string variable , count quantity variables
        qty = [0,0,0,0,0,0,0,0]
        p = [0,0,0,0,0,0,0,0]
        cost = StringVar()
        cost.set('TOTAL AMOUNT : --')
        
        price = [899,999,899,199,299,799,699,299]
        #global cart
        #cart = StringVar()
        TOTAL_COST=StringVar()
        #TOTAL_COST.set("TOTAL PRICE : $ ")
        txt1 = StringVar()
        txt2 = StringVar()
        txt3 = StringVar()
        txt4 = StringVar()
        txt5 = StringVar()
        txt6 = StringVar()
        txt7 = StringVar()
        txt8 = StringVar()

        txt1.set("QTY : 0")
        txt2.set("QTY : 0")
        txt3.set("QTY : 0")
        txt4.set("QTY : 0")
        txt5.set("QTY : 0")
        txt6.set("QTY : 0")
        txt7.set("QTY : 0")
        txt8.set("QTY : 0")

        # text initialized and will be updated in command function

        # VIEW CART AND COST FUNCTIONS

        #def vc():

        def tpf():
            for i in range(8):
                p[i]=price[i]*qty[i]
            tz = "TOTAL AMOUNT : $ "+ str(sum(p))
            TOTAL_COST.set(tz)
            cost.set(tz)
        
        #END

        #add to cart

        def add1():
            x = txt1.get()
            y = int(x[-1])
            qty[0] = y
            tpf()

        def add2():
            x = txt2.get()
            y = int(x[-1])
            qty[1] = y
            tpf()

        def add3():
            x = txt3.get()
            y = int(x[-1])
            qty[2] = y
            tpf()

        def add4():
            x = txt4.get()
            y = int(x[-1])
            qty[3] = y
            tpf()
        #end of 4
        def add5():
            x = txt5.get()
            y = int(x[-1])
            qty[4] = y
            tpf()

        def add6():
            x = txt6.get()
            y = int(x[-1])
            qty[5] = y
            tpf()

        def add7():
            x = txt7.get()
            y = int(x[-1])
            qty[6] = y
            tpf()

        def add8():
            x = txt8.get()
            y = int(x[-1])
            qty[7] = y
            tpf()
        #end add to cart


        #FUNCTION TO INCREMENT TEXT

        def dec1():
            xy = txt1.get()
            i = xy[-1]
            y = int(i)
            if(y!=0):
                y = y - 1
            else:
                y = 0
            i = str(y)
            xy = "QTY : " + i
            txt1.set(xy)
            x = txt1.get()
            y = int(x[-1])
            qty[0] = y
            tpf()
        

        def dec2():
            xy = txt2.get()
            i = xy[-1]
            y = int(i)
            if(y!=0):
                y = y - 1
            else:
                y = 0
            i = str(y)
            xy = "QTY : " + i
            txt2.set(xy)
            x = txt2.get()
            y = int(x[-1])
            qty[1] = y
            tpf()
        

        def dec3():
            xy = txt3.get()
            i = xy[-1]
            y = int(i)
            if(y!=0):
                y = y - 1
            else:
                y = 0
            i = str(y)
            xy = "QTY : " + i
            txt3.set(xy)
            x = txt3.get()
            y = int(x[-1])
            qty[2] = y
            tpf()
       

        def dec4():
            xy = txt4.get()
            i = xy[-1]
            y = int(i)
            if(y!=0):
                y = y - 1
            else:
                y = 0
            i = str(y)
            xy = "QTY : " + i
            txt4.set(xy)
            x = txt4.get()
            y = int(x[-1])
            qty[3] = y
            tpf()
        

        def dec5():
            xy = txt5.get()
            i = xy[-1]
            y = int(i)
            if(y!=0):
                y = y - 1
            else:
                y = 0
            i = str(y)
            xy = "QTY : " + i
            txt5.set(xy)
            x = txt5.get()
            y = int(x[-1])
            qty[4] = y
            tpf()
        

        def dec6():
            xy = txt6.get()
            i = xy[-1]
            y = int(i)
            if(y!=0):
                y = y - 1
            else:
                y = 0
            i = str(y)
            xy = "QTY : " + i
            txt6.set(xy)
            x = txt6.get()
            y = int(x[-1])
            qty[5] = y
            tpf()
        

        def dec7():
            xy = txt7.get()
            i = xy[-1]
            y = int(i)
            if(y!=0):
                y = y - 1
            else:
                y = 0
            i = str(y)
            xy = "QTY : " + i
            txt7.set(xy)
            x = txt7.get()
            y = int(x[-1])
            qty[6] = y
            tpf()
        
        def dec8():
            xy = txt8.get()
            i = xy[-1]
            y = int(i)
            if(y!=0):
                y = y - 1
            else:
                y = 0
            i = str(y)
            xy = "QTY : " + i
            txt8.set(xy)
            x = txt8.get()
            y = int(x[-1])
            qty[7] = y
            tpf()


            
        #inc below

            
        def inc1():
            xy = txt1.get()
            i = xy[-1]
            y = int(i)
            y = y + 1
            if y!=10 :
                y = y 
            if y==10:
                y=0
            i = str(y)
            xy = "QTY : " + i
            txt1.set(xy)
            

        def inc2():
            xy = txt2.get()
            i = xy[-1]
            y = int(i)
            y = y + 1
            if y!=10 :
                y = y 
            if y==10:
                y=0
            i = str(y)
            xy = "QTY : " + i
            txt2.set(xy)

        def inc3():
            xy = txt3.get()
            i = xy[-1]
            y = int(i)
            y = y + 1
            if y!=10 :
                y = y 
            if y==10:
                y=0
            i = str(y)
            xy = "QTY : " + i
            txt3.set(xy)

        def inc4():
            xy = txt4.get()
            i = xy[-1]
            y = int(i)
            y = y + 1
            if y!=10 :
                y = y 
            if y==10:
                y=0
            i = str(y)
            xy = "QTY : " + i
            txt4.set(xy)
        #5 onwards below
        def inc5():
            xy = txt5.get()
            i = xy[-1]
            y = int(i)
            y = y + 1
            if y!=10 :
                y = y 
            if y==10:
                y=0
            i = str(y)
            xy = "QTY : " + i
            txt5.set(xy)

        def inc6():
            xy = txt6.get()
            i = xy[-1]
            y = int(i)
            y = y + 1
            if y!=10 :
                y = y 
            if y==10:
                y=0
            i = str(y)
            xy = "QTY : " + i
            txt6.set(xy)

        def inc7():
            xy = txt7.get()
            i = xy[-1]
            y = int(i)
            y = y + 1
            if y!=10 :
                y = y 
            if y==10:
                y=0
            i = str(y)
            xy = "QTY : " + i
            txt7.set(xy)

        def inc8():
            xy = txt8.get()
            i = xy[-1]
            y = int(i)
            y = y + 1
            if y!=10 :
                y = y 
            if y==10:
                y=0
            i = str(y)
            xy = "QTY : " + i
            txt8.set(xy)

        #all function listed down                   #003399   #003399 #358597

        frame1 = Frame(master ,width = 50,height=50 ,bg="#F4A896"  ,relief=SUNKEN,highlightthickness=5,bd=5,pady=20,padx=20 ,highlightbackground="black")
        frame2 = Frame(master , width = 50,height=50 ,bg="#F4A896" ,relief=SUNKEN,highlightthickness=5,bd=5,pady=20,padx=20 ,highlightbackground="black")
        frame3 = Frame(master ,width = 50,height=50  ,bg="#F4A896" ,relief=SUNKEN,highlightthickness=5,bd=5,pady=20,padx=20 ,highlightbackground="black")
        frame4 = Frame(master , width = 50,height=50 ,bg="#F4A896" ,relief=SUNKEN,highlightthickness=5,bd=5,pady=20,padx=20 ,highlightbackground="black")
        frame5 = Frame(master , width = 50,height=50 ,bg="#F4A896" ,relief=SUNKEN,highlightthickness=5,bd=5,pady=20,padx=20 ,highlightbackground="black")
        frame6 = Frame(master , width = 50,height=50 ,bg="#F4A896" ,relief=SUNKEN,highlightthickness=5,bd=5,pady=20,padx=20 ,highlightbackground="black")
        frame7 = Frame(master , width = 50,height=50 ,bg="#F4A896" ,relief=SUNKEN,highlightthickness=5,bd=5,pady=20,padx=20 ,highlightbackground="black")
        frame8 = Frame(master , width = 50,height=50 ,bg="#F4A896" ,relief=SUNKEN,highlightthickness=5,bd=5,pady=20,padx=20 ,highlightbackground="black")

        #all images
        img1 = ImageTk.PhotoImage(Image.open('img1.jpg'))
        '''img1 = shrink(img1)'''
        imglabel_1 = Label(frame1,image=img1,bd=5,relief = "solid")
        imglabel_1.grid(row = 0,column=0,columnspan=2)

        img2 = ImageTk.PhotoImage(Image.open('foldable.jpg'))
        '''img1 = shrink(img1)'''
        imglabel_2 = Label(frame2,image=img2,bd=5,relief = "solid")
        imglabel_2.grid(row = 0,column=0,columnspan=2)

        img3 = ImageTk.PhotoImage(Image.open('googlepixel.jpg'))
        '''img1 = shrink(img1)'''
        imglabel_3 = Label(frame3,image=img3,bd=5,relief = "solid")
        imglabel_3.grid(row = 0,column=0,columnspan=2)

        img4 = ImageTk.PhotoImage(Image.open('lenevo.jpg'))
        '''img1 = shrink(img1)'''
        imglabel_4 = Label(frame4,image=img4,bd=5,relief = "solid")
        imglabel_4.grid(row = 0,column=0,columnspan=2)

        img5 = ImageTk.PhotoImage(Image.open('nokia6.jpg'))
        '''img1 = shrink(img1)'''
        imglabel_5 = Label(frame5,image=img5,bd=5,relief = "solid")
        imglabel_5.grid(row = 0,column=0,columnspan=2)

        img6 = ImageTk.PhotoImage(Image.open('note10.jpg'))
        '''img1 = shrink(img1)'''
        imglabel_6 = Label(frame6,image=img6,bd=5,relief = "solid")
        imglabel_6.grid(row = 0,column=0,columnspan=2)

        img7 = ImageTk.PhotoImage(Image.open('oneplus7pro.jpg'))
        '''img1 = shrink(img1)'''
        imglabel_7 = Label(frame7,image=img7,bd=5,relief = "solid")
        imglabel_7.grid(row = 0,column=0,columnspan=2)

        img8 = ImageTk.PhotoImage(Image.open('opporeno.jpg'))
        '''img1 = shrink(img1)'''
        imglabel_8 = Label(frame8,image=img8,bd=5,relief = "solid")
        imglabel_8.grid(row = 0,column=0,columnspan=2)
        #end of input

        #labels for discription (' d ')

        main_display = Label( master ,text = "Shopping Cart" ,fg = "white",bg="black" ,font="Helvetica 25",width=60)
        main_display.grid(columnspan=6,sticky="we")
        d1 = Label(frame1,text="APPLE XR",fg = "white",bg="#F4A896",font=(5))
        d1.grid(row = 1,column=0,columnspan=3)

        d1 = Label(frame2,text="SAMSUNG ZTX",fg = "white",bg="#F4A896",font=(5))
        d1.grid(row = 1,column=0,columnspan=3)

        d1 = Label(frame3,text="PIXEL 3A",fg = "white",bg="#F4A896",font=(5))
        d1.grid(row = 1,column=0,columnspan=3)

        d1 = Label(frame4,text="LENEVO K2 PRO",fg = "white",bg="#F4A896",font=(5))
        d1.grid(row = 1,column=0,columnspan=3)
        #5 onward below
        d1 = Label(frame5,text="NOKIA 6.1",fg = "white",bg="#F4A896",font=(3))
        d1.grid(row = 1,column=0,columnspan=3)

        d1 = Label(frame6,text="SAMSUNG NOTE 10",fg = "white",bg="#F4A896",font=(3))
        d1.grid(row = 1,column=0,columnspan=3)

        d1 = Label(frame7,text="ONEPLUS7 PRO",fg = "white",bg="#F4A896",font=(3))
        d1.grid(row = 1,column=0,columnspan=3)

        d1 = Label(frame8,text="OPPO MTK",fg = "white",bg="#F4A896",font=(3))
        d1.grid(row = 1,column=0,columnspan=3)
        #labels end

        #buttons && FRAME 

        #temp1.grid(row=0,column=1)

        frame1.grid(row=1,column=0,pady=20,padx=20)
        b11 = Button(frame1,text="PRICE : $899",state=DISABLED)
        bq11 = Button(frame1,text="QTY +1",command=inc1)
        bq12 = Button(frame1,text="QTY -1",command=dec1)
        b12 = Label(frame1,textvariable = txt1,width = 10,bd = 4)
        b11.grid(row = 2,column=0,pady=2)
        b12.grid(row=2,column=1)
        bq11.grid(row=3,column=0)
        bq12.grid(row=3,column=1)
        add1 = Button(frame1,text="ADD TO CART",command = add1)
        add1.grid(row=4,columnspan=3)

        frame2.grid(row=1,column=1,pady=20,padx=20)
        b21 = Button(frame2,text="PRICE : $999",state=DISABLED)
        bq21 = Button(frame2,text="QTY +1",command=inc2)
        bq22 = Button(frame2,text="QTY -1",command=dec2)
        b22 = Label(frame2,textvariable = txt2,width = 10,bd = 4)
        b21.grid(row = 2,column=0,pady=2)
        b22.grid(row=2,column=1)
        bq21.grid(row=3,column=0)
        bq22.grid(row=3,column=1)
        add2 = Button(frame2,text="ADD TO CART",command = add2)
        add2.grid(row=4,columnspan=3)

        frame3.grid(row=2,column=0,pady=20,padx=20)
        b31 = Button(frame3,text="PRICE : $899",state=DISABLED)
        bq31 = Button(frame3,text="QTY +1",command=inc3)
        bq32 = Button(frame3,text="QTY -1",command=dec3)
        b32 = Label(frame3,textvariable = txt3,width = 10,bd = 4)
        b31.grid(row = 2,column=0,pady=2)
        b32.grid(row=2,column=1)
        bq31.grid(row=3,column=0)
        bq32.grid(row=3,column=1)
        add3 = Button(frame3,text="ADD TO CART",command = add3)
        add3.grid(row=4,columnspan=3)

        frame4.grid(row=2,column=1,pady=20,padx=20)
        b41 = Button(frame4,text="PRICE : $199",state=DISABLED)
        bq41 = Button(frame4,text="QTY +1",command=inc4)
        bq42 = Button(frame4,text="QTY -1",command=dec4)
        b42 = Label(frame4,textvariable = txt4,width = 10,bd = 4)
        b41.grid(row = 2,column=0,pady=2)
        b42.grid(row = 2,column=1)
        bq41.grid(row=3,column=0)
        bq42.grid(row=3,column=1)
        add4 = Button(frame4,text="ADD TO CART",command = add4)
        add4.grid(row=4,columnspan=3)

        #initial set above

        frame5.grid(row=1,column=3,pady=20,padx=20)
        b51 = Button(frame5,text="PRICE : $299",state=DISABLED)
        bq51 = Button(frame5,text="QTY +1",command=inc5)
        bq52 = Button(frame5,text="QTY -1",command=dec5)
        b52 = Label(frame5,textvariable = txt5,width = 10,bd = 4)
        b51.grid(row = 2,column=0,pady=2)
        b52.grid(row = 2,column=1)
        bq51.grid(row=3,column=0)
        bq52.grid(row=3,column=1)
        add5 = Button(frame5,text="ADD TO CART",command = add5)
        add5.grid(row=4,columnspan=3)

        frame6.grid(row=1,column=4,pady=20,padx=20)
        b61 = Button(frame6,text="PRICE : $799",state=DISABLED)
        bq61 = Button(frame6,text="QTY +1",command=inc6)
        bq62 = Button(frame6,text="QTY -1",command=dec6)
        b62 = Label(frame6,textvariable = txt6,width = 10,bd = 4)
        b61.grid(row = 2,column=0,pady=2)
        b62.grid(row = 2,column=1)
        bq61.grid(row=3,column=0)
        bq62.grid(row=3,column=1)
        add6 = Button(frame6,text="ADD TO CART",command = add6)
        add6.grid(row=4,columnspan=3)

        frame7.grid(row=2,column=3,pady=20,padx=20)
        b71 = Button(frame7,text="PRICE : $699",state=DISABLED)
        bq71 = Button(frame7,text="QTY +1",command=inc7)
        bq72 = Button(frame7,text="QTY -1",command=dec7)
        b72 = Label(frame7,textvariable = txt7,width = 10,bd = 4)
        b71.grid(row = 2,column=0,pady=2)
        b72.grid(row = 2,column=1)
        bq71.grid(row=3,column=0)
        bq72.grid(row=3,column=1)
        add7 = Button(frame7,text="ADD TO CART",command = add7)
        add7.grid(row=4,columnspan=3)

        frame8.grid(row=2,column=4,pady=20,padx=20)
        b81 = Button(frame8,text="PRICE : $299",state=DISABLED)
        bq81 = Button(frame8,text="QTY +1",command=inc8)
        bq82 = Button(frame8,text="QTY -1",command=dec8)
        b82 = Label(frame8,textvariable = txt8,width = 10,bd = 4)
        b81.grid(row = 2,column=0,pady=2)
        b82.grid(row = 2,column=1)
        bq81.grid(row=3,column=0)
        bq82.grid(row=3,column=1)
        add8 = Button(frame8,text="ADD TO CART",command = add8)
        add8.grid(row=4,columnspan=3)

        #buttons end
        def buyCommand(cartWindow):
            cartWindow.destroy()    
            ms.showinfo(title="success",message="Purchase Completed Successfully")
            master.destroy()
            cartWindow.destroy()
            root.destroy()

        # viewCart -- checkout button event
        def viewCart():
            if sum(qty)==0:
                ms.showinfo(title="Empty Cart",message="Please Add Items To Cart")
                return
            cartWindow = Toplevel()
            cartWindow.configure(bg="#358597")
            cartWindow.title("CHECKOUT")
            cartWindow.grab_set()
          
            cartItemsLabelFrame = LabelFrame(cartWindow,text="Cart Items",bg="#358597",fg="white")
            cartItemsLabelFrame.grid(row=0,column=0)

            '''cartItemsFrame = LabelFrame(cartWindow,text="Cart Items")
            cartItemsFrame.grid(row=0,column=0)'''
            
            #all data here of products :
            if qty[0]!=0:
                n1 = Label(cartItemsLabelFrame,text="APPLE XR  x "+str(qty[0]) ,fg="white" ,bg="#358597",font=(20))
                n1.grid(row=1,column=0)
                p1 = Label(cartItemsLabelFrame,text="$899" , fg="orange",bg="#358597",font=(20))
                p1.grid(row=1,column=1)

            if qty[1]!=0:
                n2 = Label(cartItemsLabelFrame,text="SAMSUNG ZTX x "+str(qty[1]) ,fg="white",bg="#358597" ,font=(20))
                n2.grid(row=2,column=0)
                p2 = Label(cartItemsLabelFrame,text="$999" , fg="orange",bg="#358597",font=(20))
                p2.grid(row=2,column=1)
            
            if qty[2]!=0:
                n3 = Label(cartItemsLabelFrame,text="PIXEL 3A x "+str(qty[2]) ,fg="white" ,bg="#358597",font=(20))
                n3.grid(row=3,column=0)
                p3 = Label(cartItemsLabelFrame,text="$899" , fg="orange",bg="#358597",font=(20))
                p3.grid(row=3,column=1)
            if qty[3]!=0:
                n4 = Label(cartItemsLabelFrame,text="LENEVO K2 PRO x "+str(qty[3]) ,fg="white" ,bg="#358597",font=(20))
                n4.grid(row=4,column=0)
                p4 = Label(cartItemsLabelFrame,text="$199" , fg="orange",bg="#358597",font=(20))
                p4.grid(row=4,column=1)
            if qty[4]!=0:
                n5 = Label(cartItemsLabelFrame,text="NOKIA 6.1 x "+str(qty[4]) ,fg="white" ,bg="#358597",font=(20))
                n5.grid(row=5,column=0)
                p5 = Label(cartItemsLabelFrame,text="$299" , fg="orange",bg="#358597",font=(20))
                p5.grid(row=5,column=1)
            if qty[5]!=0:
                n6 = Label(cartItemsLabelFrame,text="SAMSUNG NOTE 10 x "+str(qty[5]) ,fg="white" ,bg="#358597",font=(20))
                n6.grid(row=6,column=0)
                p6 = Label(cartItemsLabelFrame,text="$799" , fg="orange",bg="#358597",font=(20))
                p6.grid(row=6,column=1)
            if qty[6]!=0:
                n7 = Label(cartItemsLabelFrame,text="ONEPLUS7 PRO x "+str(qty[6]) ,fg="white",font=(20) ,bg="#358597")
                n7.grid(row=7,column=0)
                p7 = Label(cartItemsLabelFrame,text="$699" , fg="orange",bg="#358597",font=(20))
                p7.grid(row=7,column=1)
            if qty[7]!=0:
                n8 = Label(cartItemsLabelFrame,text="OPPO MTK x "+str(qty[7]) ,fg="white" ,bg="#358597",font=(20))
                n8.grid(row=8,column=0)
                p8 = Label(cartItemsLabelFrame,text="$299" , fg="orange",bg="#358597",font=(20))
                p8.grid(row=8,column=1)
            b82 = Label(frame8,textvariable = txt8,width = 10,bd = 4)
            

            checkOutFrame = Frame(cartWindow, pady="10",bg="#358597")
            totalPriceLabel = Label(checkOutFrame, textvariable = TOTAL_COST, font=("Candara",15,"bold"),fg="orange" ,bg="#358597")
            totalPriceLabel.grid(row=10,column=0)
            
            buyBtn = Button(checkOutFrame, text="Buy Now", font=("Candara",15,"bold"),fg="green",bg="white",cursor="hand2", command=lambda : buyCommand(cartWindow))
            buyBtn.grid(row=10,column=1)
            checkOutFrame.grid(row=9,column=0)

            backToStoreBtn = Button(cartWindow, text="Back To Store", font=("Candara",15,"bold"),fg="red",bg="white",cursor="hand2",command=cartWindow.destroy)
            backToStoreBtn.grid(row=11,column=0)

            cartWindow.mainloop()


        #SEPERATE BUTTONS PRICE AND VIEW CART

        #vcart = Button(root,text="VIEW CART !",command = vc)
        tp = Button(master,text="VIEW CART !!",command =viewCart,font=(17))   
        #vcart.grid(row = 2 ,columnspan = 2)
        #vc = Label(root,textvariable = cart).grid(row=3,columnspan=2)
        tp.grid(row = 6,columnspan = 5)
        tx = Label(master,textvariable = cost,bg="#358597",font=(17),fg="white" ,highlightbackground="#F4A896",highlightthickness="3",bd="3").grid(row=4,columnspan=5)
        #END buttons

        master.mainloop()
            

#create window and application object
root = Tk()
root.geometry("500x350+300+300")
root.title("Login Form")
root.configure(bg="#358597")
Window1(root)
root.mainloop()

