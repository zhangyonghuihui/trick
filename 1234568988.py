
import tkinter as tk
 
import random
 
import threading
 
import time
 
def dow():
    
 
    window = tk.Tk()
     
    width = window.winfo_screenwidth()
     
    height = window.winfo_screenheight()
     
    a = random.randrange(0, width/2)
     
    b = random.randrange(0, height)
     
    window.title('你是傻子')
     
    window.geometry("800x200" +"+" +str(a) +"+" +str(b))
     
    tk.Label(window,
     
    text='你就是个傻子！',
     
                bg='Red',
     
                font=('楷体',68),
     
                width=60,height=8
     
                ).pack()
     
    window.mainloop()
 
threads = []
 
for i in range(1000000000000000000000000000000):
     
    t = threading.Thread(target=dow)
 
    threads.append(t)
     
    time.sleep(0.00000001)
     
    threads[i].start()
