
# coding: utf-8

# In[1]:


import numpy as np
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter.font import Font


# In[16]:


SYMBOLS = ['X', 'O', '*', '$', '#', '@', '&', '^','A','B','C','D','E','F','G','H','I']
player = 1
k = 1
sym = 'X'
btn_text = []


# In[12]:


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        #print('1')


# In[13]:


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
    
        self.master = master
        self.configure(background="spring green")
        tk.Label(self, text="WELCOME TO THE GAME",bg="spring green", fg="#ffffff",font=("Courier",24,'bold')).pack(side="top", fill="x", padx=70, pady=60)
        tk.Label(self,text="Input numbers of players",bg="spring green", fg="#ffffff", font=("Courier",18, 'bold')).pack(side="left",fill="x" ,padx=10,pady=60)
        global val,s
        s = tk.Entry(self,bd=2)
        s.pack(side="left",fill="x",pady=60)
       
        button1= tk.Button(self, text="Submit",bg="springgreen4", fg="#ffffff",font=("Courier",16),
                  command=self.get_s)
        button1.pack(padx="20", pady=60)
        lr = tk.Label(self, text='Created By- Utkarsh Paliwal & Nitya Kumari',bg="spring green", fg="#ffffff",font=("Helvetica",13))
        lr.place(relx=1.0, rely=1.0, anchor='se')
        
    def get_s(self):
        #print('In get func')
        global val
        val = int(s.get())
        #val = val+1
        if val == 1:
            import tictactoe_ai as TTT
            TTT.GUI().mainloop()
        else:
            global mat
            global symbols
            #global player
            global players
            #global k
            global size
            size = val + 1
            symbols = SYMBOLS[:size-1]
            players = list(range(1,size))
            mat = np.zeros((size,size), dtype = int)
            #print(f"ALL VARIABLES ASSIGNED and player = {player}")
            self.master.switch_frame(PageOne)


# In[17]:


class PageOne(tk.Frame):

    def __init__(self, master):
       
        tk.Frame.__init__(self, master)
        
        #tk.Button(self, text="Return to start page", command=lambda: master.switch_frame(StartPage)).pack()   
        #var = "Welcome to TicTacToe.ai"
        global welcome, b
        #window.pack_propagate(0)
        welcome = Label(app, text="Welcome to TicTacToe.ai", font= Font(family="Helvetica", size=30))
        welcome.pack()
        #print(val,s, "in init")
        
        frames = [0]*(val+1)
        for i in range(val+1):
            frames[i] = Frame(app)
            frames[i].pack()
        b = [[]*val for n in range(val+1)]
        button_pos = 1
        global btn_text
        btn_text = [[] for n in range(val+1)]
        for i in range(val+1):
            for j in range(val+1):
                btn_text[i].append(tk.StringVar())
        for i in range(val+1):
            for j in range(val+1):
                b[i].append(Button(frames[i], textvariable=btn_text[i][j], padx=15, pady=15, bg="#ffffff", command = lambda i=i,j=j: place(i,j), font=Font(family="Helvetica", size=32), width=2, height=1))
                '''button = Button(self, textvariable=btn_text, padx=15, pady=15, bg="#ffffff", command = lambda i=i,j=j: place(i,j), font=Font(family="Helvetica", size=32), width=2, height=1)
                button.grid(row=i, column=j)'''
                #print(f'row and column are = {i}, {j}')
                #b[i][j].grid(row=i, column=j)
                button_pos += 1

        for i in range(val+1):
            for j in range(val+1):
                #print(f'i = {i} and j = {j}')
                b[i][j].pack(side=LEFT)
        #print('PageOne Ends')


# In[6]:


def next_player(p):
    p-=1
    if p+1 == len(players):
        return players[0], symbols[0]
    else:
        return players[p+1], symbols[p+1]


# In[7]:


def check_board():
    for r in range(size):
        for c in range(size):
            try:
                if mat[r,c] == mat[r,c+1] == mat[r,c+2] != 0 and c+2<size:
                    return mat[r,c]
            except:
                pass
            try:
                if  mat[r,c] == mat[r+1,c] == mat[r+2,c] != 0 and r+2<size:
                    return mat[r,c]
            except:
                pass
            try:
                if mat[r,c] == mat[r+1,c+1] == mat[r+2,c+2] != 0 and r+2<size and c+2<size:
                    return mat[r,c]
            except:
                pass
            try:
                if mat[r,c] == mat[r+1,c-1] == mat[r+2,c-2] != 0 and r+2<size and c-2>=0:
                    return mat[r,c]
            except:
                pass
    return None

def win_buttons():
    for r in range(size):
        for c in range(size):
            try:
                if mat[r,c] == mat[r,c+1] == mat[r,c+2] != 0 and c+2<size:
                    return (r,c), (r,c+1), (r,c+2)
            except:
                pass
            try:
                if  mat[r,c] == mat[r+1,c] == mat[r+2,c] != 0 and r+2<size:
                    return (r,c), (r+1,c), (r+2,c)
            except:
                pass
            try:
                if mat[r,c] == mat[r+1,c+1] == mat[r+2,c+2] != 0 and r+2<size and c+2<size:
                    return (r,c), (r+1,c+1), (r+2,c+2)
            except:
                pass
            try:
                if mat[r,c] == mat[r+1,c-1] == mat[r+2,c-2] != 0 and r+2<size and c-2>=0:
                    return (r,c), (r+1,c-1), (r+2,c-2)
            except:
                pass
    return None

# In[15]:


def place(r,c):
        #pos = int(input("Enter position of your wish "))
        #print(f'player = {player}')
        #r = (pos-1)//size
        #c = (pos-1)%size
        #print(f'r,c are = {r}, {c}')
        global player,k, sym, btn_text
        if mat[r][c] == 0:
            mat[r][c] = player
            #b[r][c].config(text=sym)
            #print(f'r and c are = {r}, {c}')
            b[r][c]['state'] = 'disabled'
            #b[r][c]['text'] = sym
            btn_text[r][c].set(sym)
            player, sym = next_player(player)
            winner = check_board()
            if winner != None:
                welcome.config(text= '{} wins !'.format(symbols[winner-1]))
                for x,y in win_buttons():
                        b[x][y]['disabledforeground'] = 'red'
                for i in range(size):
                	for j in range(size):
                		if b[i][j]['state'] != 'disabled':
                			b[i][j]['state'] = 'disabled'
            elif k<size**2:
                welcome.config(text= "{}'s turn".format(sym))
            k+=1
        if k==(size**2)+1 and winner == None:
            welcome.config(text= 'Match Drawn')


# In[18]:

if __name__ == "__main__":
	app = SampleApp()
	app.title("TicTacToe.ai")
	app.geometry('700x700')
	app.configure(background="spring green")
	app.mainloop()