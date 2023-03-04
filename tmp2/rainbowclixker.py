import tkinter as tk
from art import *
def change_color(step=0):
    g = abs((step*8) % 512 - 255)
    b = 255 - g
    lbl.configure(fg=f"#00{g:0>2x}{b:0>2x}")

    button1.configure(fg=f"#00{g:0>2x}{b:0>2x}")

    btn1.configure(fg=f"#00{g:0>2x}{b:0>2x}")

    root.after(5000 * 8 // 256, lambda: change_color(step+1))

def click1():
    global i
    global count
    emojis = ['😭', '🥰', '😽', '😂', '😘', '😍']
    button1['text'] = emojis[i]
    Art = text2art(str(count), font='white_bubble', chr_ignore=True)
    lbl['text']=Art
    lbl['font']="-size 70"
    count+=1
    if i<5:
        i += 1
    else:
        i=0
if __name__=="__main__":
    i=0
    count=1
    root = tk.Tk()
    root.geometry('400x200')
    lbl = tk.Label(root, text="Hi pendosy", font="-size 50")
    lbl.pack(fill=tk.BOTH)
    root.after(1, change_color)
    button1 = tk.Button(root,text='push me', command=click1,font="-size 35")
    button1.pack()
    root.after(1, change_color)
    btn1 = tk.Button(root, text='Quit !',
                      command=root.destroy)

    btn1.pack()
    root.after(1, change_color)
    root.mainloop()
