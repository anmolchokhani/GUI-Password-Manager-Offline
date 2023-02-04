from tkinter import *
import string 
from tkinter import messagebox
import random


BLUE = "#86A3B8"
RED = "#F55050"
PINK = "#F48484"
YELLOW = "#E8D2A6"
WHITE = "#757575"
FONT_NAME = "Courier"



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def new_password_generator():
    all_alphabet= list(string.printable)
    new_password=""
    new_password=[ new_password+random.choice(all_alphabet) for i in range(12)]
    new_password="".join(new_password)
    password_input.insert(0, new_password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    web_name=website_input.get()
    email_name=email_input.get()
    pass_name=password_input.get()
    if len(web_name) !=0 and len(pass_name) !=0:
        is_ok=messagebox.askokcancel(title="Are you sure", message=f'These are the details entered\nWebsite: {web_name}\nEmail: {email_name}\nPassword: {pass_name}')


        if is_ok:
            with open("all_file_details.txt", mode="a+") as f:
                f.write(f'{web_name} | {email_name} | {pass_name}\n')
            web_name=website_input.delete(0,END)
            pass_name=password_input.delete(0,END)
    else:
        if len(web_name) == 0 and len(pass_name) ==0:
            messagebox.showerror(message=f"Website and Password is empty")
        elif len(web_name) == 0:
            messagebox.showerror(message=f"Website is empty")
        else:
            messagebox.showerror(message=f"Password is empty")
        



# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title('Password Manager')
window.config(padx=50, pady=20, bg=YELLOW)
window.minsize(width=70,height=70)

website_label= Label(text="Website:",bg=YELLOW, fg=BLUE, font=(FONT_NAME,20))
website_label.grid(column=0,row=1,pady=5)

website_input= Entry(width=42)
website_input.grid(column=1,row=1,columnspan=2)
website_input.focus()

email_label= Label(text="Email/Username:",bg=YELLOW, fg=BLUE, font=(FONT_NAME,20))
email_label.grid(column=0,row=2,pady=2)

email_input= Entry(width=42,bg=PINK)
email_input.insert(0, "anmol.chokhani123@gmail.com")

email_input.grid(column=1,row=2,columnspan=2)

password_label= Label(text="Password:",bg=YELLOW, fg=BLUE, font=(FONT_NAME,20))
password_label.grid(column=0,row=3,pady=2)

password_input= Entry(width=21)
password_input.grid(column=1,row=3)

password_button= Button(text="Generate Password",highlightbackground=YELLOW,command=new_password_generator,bg=YELLOW)
password_button.grid(column=2,row=3)

add_button= Button(text="Add",bg=YELLOW,command=add_password,highlightbackground=YELLOW)
add_button.grid(column=1,row=4)


canvas= Canvas(width=200,height=200,bg=YELLOW,highlightthickness=0)
lock_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(column=1,row=0)




window.mainloop()