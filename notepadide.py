from tkinter import*
from PIL import ImageTk,Image
root=Tk()

root.minsize(650,650)
root.maxsize(1000,1000)
root.title("Notepad")

open_img=ImageTk.PhotoImage(Image.open("open.png"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))
exit_img=ImageTk.PhotoImage(Image.open("exit.jpg"))  

file_name=Label(root,text="File Name")          
file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name=Entry(root)
input_file_name.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text=Text(root,width=80,height=35)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

def open_file():
    print("opening file")

open_btn=Button(root,text="open",command=open_file,image=open_img)
open_btn.place(relx=0.05,rely=0.03,anchor=CENTER)

def save_file():
    print("saving file")

save_btn=Button(root,text="save",image=save_img,command=save_file)
save_btn.place(relx=0.12,rely=0.03,anchor=CENTER)

def exit_file():
    print("exiting file")

exit_btn=Button(root,text="exit",image=exit_img,command=exit_file)
exit_btn.place(relx=0.19,rely=0.03,anchor=CENTER)

root.mainloop()                

