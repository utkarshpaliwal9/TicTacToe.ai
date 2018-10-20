from tkinter import *
import tkinter as tk
import tkinter.messagebox


# In[7]:


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
        print('1')


# In[8]:


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.master = master
        '''self.geometry('450x450')
        self.configure(background="coral")'''
        tk.Label(self, text="WELCOME TO THE GAME",bg="#ffffff").pack(side="top", fill="x", padx=70, pady=30)
        tk.Label(self,text="Input numbers of players",bg="#ffffff").pack(side="left",fill="x" ,padx=30,pady=30)
        global val,s
        s = tk.Entry(self,bd=1)
        s.pack(side="left",fill="x",pady=30)
       
        button1= tk.Button(self, text="Submit",bg="#ffffff",
                  command=self.get_s)
        button1.pack(padx="10",pady="15")
        print('2')
        #print(val,s)
        
    def get_s(self):
        print('In get func')
        global val
        val = int(s.get())
        '''print(f'In get_s, val = {val}')
        print(val, type(val))'''  #REMOVE THIS LINE (DEBUGGING)
        print('3')
        self.master.switch_frame(PageOne)
#print(val,s)


# In[13]:


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Button(self, text="Return to start page", command=lambda: master.switch_frame(StartPage)).pack()   
        var = "Welcome to TicTacToe.ai"
        #window.pack_propagate(0)
        welcome = Label(app, text= var)
        welcome.pack()
        print(val,s, "in init")
        
        frames = [0]*val
        for i in range(val):
            frames[i] = Frame(app)
            frames[i].pack()
        b = [[]*val for n in range(val)]

        for i in range(val):
            for j in range(val):
                b[i].append(Button(frames[i], text=str('  ')))

        for i in range(val):
            for j in range(val):
                #print(f'i = {i} and j = {j}')
                b[i][j].pack(side=LEFT)
        print('PageOne Ends')


# In[15]:


if __name__ == "__main__":
    app = SampleApp()
    app.geometry('450x450')
    app.configure(background="coral")
    app.mainloop()

