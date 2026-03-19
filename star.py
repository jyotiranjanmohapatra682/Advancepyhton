from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Student Form")
root.geometry('500x550')
root.configure(background='#1e1e2f')

# ===== Login Function =====
def login():
    email = email_entry.get()
    password = password_entry.get()

    if email == "" or password == "":
        messagebox.showerror("Error", "Please enter Email and Password")
    elif email == "admin@gmail.com" and password == "1234":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login Failed", "Invalid Email or Password")

# ===== Image =====
img = Image.open('star.png')
resize_img = img.resize((120,80))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root, image=img, bg="#1e1e2f")
img_label.pack(pady=20)

# ===== Title =====
title = Label(root,
              text="GIET BUCKS",
              font=('Arial',26,'bold'),
              bg='#1e1e2f',
              fg='#00FFAA')
title.pack(pady=10)

# ===== Email =====
email_label = Label(root,
                    text="Email",
                    font=('Arial',14,'bold'),
                    bg='#1e1e2f',
                    fg='white')
email_label.pack(pady=(20,5))

email_entry = Entry(root,
                    font=('Arial',14),
                    width=25,
                    bd=2)
email_entry.pack(pady=5)

# ===== Password =====
password_label = Label(root,
                       text="Password",
                       font=('Arial',14,'bold'),
                       bg='#1e1e2f',
                       fg='white')
password_label.pack(pady=(20,5))

password_entry = Entry(root,
                       font=('Arial',14),
                       width=25,
                       bd=2,
                       show="*")
password_entry.pack(pady=5)

# ===== Glow Frame (bulb light border) =====
glow_frame = Frame(root, bg="#00FFAA", padx=3, pady=3)
glow_frame.pack(pady=30)

# ===== Hover Effects =====
def on_enter(e):
    glow_frame.config(bg="#00FFFF")   # brighter glow
    login_btn.config(bg="#00cc88", fg="white")

def on_leave(e):
    glow_frame.config(bg="#00FFAA")   # normal glow
    login_btn.config(bg="#00FFAA", fg="black")

# ===== Stylish Login Button =====
login_btn = Button(glow_frame,
                   text="LOGIN",
                   font=("Arial",16,"bold"),
                   bg="#00FFAA",
                   fg="black",
                   width=15,
                   bd=0,
                   cursor="hand2",
                   command=login)

login_btn.pack()

login_btn.bind("<Enter>", on_enter)
login_btn.bind("<Leave>", on_leave)

root.mainloop()
