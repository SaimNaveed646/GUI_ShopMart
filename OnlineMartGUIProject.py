from tkinter.messagebox import showinfo
from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import ttk
from tkinter import messagebox
from datetime import date


root = Tk()
root.title("Online Shopping Market")
root.geometry('920x670+290+15')
root.resizable(False, False)


# def rotate_image():
#     global l
#     l = 1
#     img6_label.config(image=img_array[l % len(img_array)])
#     l += 1

def save():
    f = open(f'customer_bills\\{customer_entry.get()} Bill', "w")
    f.write(f'Customer Name:{customer_entry.get()}\n')
    f.write(f'Total price:{total_price}\n')
    f.write(f'Customer Name:{date.today()}')
    f.close()
    messagebox.showinfo(title="Saved", message="Bill has been saved.")
def pay():
    global total_price
    price_list = [1200, 1000, 2000, 5000, 6000, 5500]
    if (customer_entry.get() == ""):
        messagebox.showwarning(title="Error", message="Please enter you Name")
    else:
        total_price = int(quantity1_combobox.get()) * price_list[0] + int(quantity2_combobox.get()) * \
                      price_list[1] + int(quantity3_combobox.get()) * price_list[2] + int(
            quantity4_combobox.get()) * price_list[3] + int(quantity5_combobox.get()) * price_list[4] + int(
            quantity6_combobox.get()) * price_list[5]
        name_label = Label(bill_frame, text=f'Customer Name:{customer_entry.get()}',
                           font=('Microsoft YaHei UI Light', 12), fg="#FFFFFF", bg="#090b17", width=320,
                           anchor=W)
        name_label.place(x=0, y=100)
        bill_label = Label(bill_frame, text=f'Total Price:{total_price}',
                           font=('Microsoft YaHei UI Light', 12), bg="#090b17", fg="#FFFFFF", width=320,
                           anchor=W)
        bill_label.place(x=0, y=170)
        date_label = Label(bill_frame, text=f'Bill Date:{date.today()}',
                           font=('Microsoft YaHei UI Light', 12), bg="#090b17", fg="#FFFFFF", width=320,
                           anchor=W)
        date_label.place(x=0, y=240)


def new():
    customer_entry.delete(0, END)
    quantity1_combobox.set(0)
    quantity2_combobox.set(0)
    quantity3_combobox.set(0)
    quantity4_combobox.set(0)
    quantity5_combobox.set(0)
    quantity6_combobox.set(0)

def signup():
    fh = open("accounts.txt", "a")
    fhh = open("account holders name.txt", "a")

    first_name = FName.get()
    last_name = LName.get()
    username = UName.get()
    # print("NOTE: Password must be between 7 and 12 characters and should also include at least one digit.")
    password = Password.get()

    # Password validity check for digit
    number = 0
    for i in password:
        if i.isdigit():
            number += 1

    # Password validity check for length
    if (first_name and last_name) and (first_name and password) and (first_name and username):
        if len(password) >= 7 and len(password) <= 12 and number >= 1:
            # Saving username and password
            user_pass = {username: password}
            fh.write(f'{user_pass}\n')
            fhh.write(f'- {first_name} {last_name}\n')
            showinfo(message="Account created successfully. You can shop now")
            fh.flush()
            fhh.flush()

        else:
            showinfo(message="Your password does not meet the requirements. Try again!")

    else:
        showinfo(message="Fill all the instructions")
    fh.close()
    fhh.close()
    ONLINE_PAGE()


def signin():
    try:
        with open('accounts.txt', 'r') as file:
            login_user = user.get()
            login_password = password.get()

            # Creating a dictionary from the input
            user_pass = {login_user: login_password}

            for line in file:
                try:
                    # Assuming each line in the file is a string representation of a dictionary
                    line = line.strip()
                    if line == str(user_pass):
                        showinfo(message="Login successful. You can shop now :)")
                        ONLINE_PAGE()
                        file_name = f"{login_user}"
                        with open(f"{file_name}.txt", 'a'):
                            pass  # Open and immediately close the file
                        return
                except Exception as e:
                    pass  # Handle any other potential errors gracefully

            showinfo(message="ERROR: Either account does not exist or invalid username/password. Try again!")

    except FileNotFoundError:
        showinfo(message="ERROR: Accounts file not found!")
    except Exception as e:
        showinfo(message=f"ERROR: An unexpected error occurred: {e}")

def PRODUCTS():
    global bill_frame,customer_entry,quantity1_combobox,quantity2_combobox,quantity3_combobox,quantity4_combobox
    global quantity5_combobox,quantity6_combobox,img_array,img6_label
    frame = Frame(root, width=920, height=670, bg="#25283b")
    frame.place(x=0, y=0)

    bill_frame = Frame(frame, width=300, height=670, bg="#545457")
    bill_frame.place(x=650, y=0)

    menu_label = Label(root, text="StepUp  Mart   ", font=('Microsoft YaHei UI Light', 25,), fg="#FFFFFF",
                       bg="#25283b")
    menu_label.place(x=230, y=5)
    ##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    img1 = Image.open(r"shoe\louboutin heels.jpeg")
    resized_img1 = img1.resize((140, 120))
    img1 = ImageTk.PhotoImage(resized_img1)
    img1_label = Label(frame, image=img1, text="Louboutin Heels\n Price:1200 Rs",
                       font=('Microsoft YaHei UI Light', 12), fg="#FFFFFF", bg="#090b17", width=150, height=205,
                       compound=TOP, anchor=N)
    img1_label.place(x=30, y=70)

    img2 = Image.open(r"shoe\women flat.jpg")
    resized_img2 = img2.resize((140, 120))
    img2 = ImageTk.PhotoImage(resized_img2)
    img2_label = Label(frame, image=img2, text="Flat Heels\n Price:1000 Rs",
                       font=('Microsoft YaHei UI Light', 12),
                       fg="#FFFFFF", bg="#090b17", width=150, height=205, compound=TOP, anchor=N)
    img2_label.place(x=250, y=70)

    img3 = Image.open(r"shoe\Women oxford.jpeg")
    resized_img3 = img3.resize((140, 120))
    img3 = ImageTk.PhotoImage(resized_img3)
    img3_label = Label(frame, image=img3, text="Women Oxford\n Price:2000 Rs",
                       font=('Microsoft YaHei UI Light', 12), fg="#FFFFFF", bg="#090b17", width=150, height=205,
                       compound=TOP, anchor=N)
    img3_label.place(x=470, y=70)

    quantity1_combobox = ttk.Combobox(frame, width=10, font=('Microsoft YaHei UI Light', 12),
                                      values=('0', '1', '2'), state="readonly")
    quantity1_combobox.place(x=52, y=242)
    quantity1_combobox.set(0)

    quantity2_combobox = ttk.Combobox(frame, width=10, font=('Microsoft YaHei UI Light', 12),
                                      values=('0', '1', '2'), state="readonly")
    quantity2_combobox.place(x=272, y=242)
    quantity2_combobox.set(0)

    quantity3_combobox = ttk.Combobox(frame, width=10, font=('Microsoft YaHei UI Light', 12),
                                      values=('0', '1', '2'), state="readonly")
    quantity3_combobox.place(x=492, y=242)
    quantity3_combobox.set(0)

    img4 = Image.open(r"shoe\Adidas Man.jpeg")
    resized_img4 = img4.resize((140, 120))
    img4 = ImageTk.PhotoImage(resized_img4)
    img4_label = Label(frame, image=img4, text="Adidas\n Price:5000 Rs", font=('Microsoft YaHei UI Light', 12),
                       fg="#FFFFFF", bg="#090b17", width=150, height=205, compound=TOP, anchor=N)
    img4_label.place(x=30, y=300)

    img5 = Image.open(r"shoe\Bata Enna Oxford.jpeg")
    resized_img5 = img5.resize((140, 120))
    img5 = ImageTk.PhotoImage(resized_img5)
    img5_label = Label(frame, image=img5, text="Bata Enna Oxford\n Price:6000 Rs",
                       font=('Microsoft YaHei UI Light', 12), fg="#FFFFFF", bg="#090b17", width=150, height=205,
                       compound=TOP, anchor=N)
    img5_label.place(x=250, y=300)

    img6 = Image.open(r"shoe\Nike Men's Roshe.jpeg")
    resized_img6 = img6.resize((140, 120))
    img6 = ImageTk.PhotoImage(resized_img6)
    img6_label = Label(frame, image=img6, text="Men's Nike\n Price:5500 Rs",
                       font=('Microsoft YaHei UI Light', 12),
                       fg="#FFFFFF", bg="#090b17", width=150, height=205, compound=TOP, anchor=N)
    img6_label.place(x=470, y=300)

    quantity4_combobox = ttk.Combobox(frame, width=10, font=('Microsoft YaHei UI Light', 12),
                                      values=('0', '1', '2'), state="readonly")
    quantity4_combobox.place(x=52, y=472)
    quantity4_combobox.set(0)

    quantity5_combobox = ttk.Combobox(frame, width=10, font=('Microsoft YaHei UI Light', 12),
                                      values=('0', '1', '2'), state="readonly")
    quantity5_combobox.place(x=272, y=472)
    quantity5_combobox.set(0)

    quantity6_combobox = ttk.Combobox(frame, width=10, font=('Microsoft YaHei UI Light', 12),
                                      values=('0', '1', '2'), state="readonly")
    quantity6_combobox.place(x=492, y=472)
    quantity6_combobox.set(0)

    customer_label = Label(frame, text="Customer Name", font=('Microsoft YaHei UI Light', 12), fg="#FFFFFF",
                           bg="#25283b")
    customer_label.place(x=272, y=520)

    customer_entry = Entry(frame, font=('Microsoft YaHei UI Light', 12), bg="#FFFFFF", width=15)
    customer_entry.place(x=262, y=550)

    pay_button = Button(frame, text="Pay bill", font=('Microsoft YaHei UI Light', 12), fg="#FFFFFF",
                        bg="#090b17",
                        width=15, command=pay)
    pay_button.place(x=32, y=600)

    save_button = Button(frame, text="Save bill", font=('Microsoft YaHei UI Light', 12), fg="#FFFFFF",
                         bg="#090b17",
                         width=15, command=save)
    save_button.place(x=260, y=600)

    new_button = Button(frame, text="New  bill", font=('Microsoft YaHei UI Light', 12), fg="#FFFFFF",
                        bg="#090b17",
                        width=15, command=new)
    new_button.place(x=472, y=600)

    root.mainloop()


def WELCOME_PAGE():
    frame2 = Frame(root, width=920, height=670, bg="white")  # white color (whole screen)
    frame2.place(x=0, y=0)

    label2 = Label(frame2, width=135, height=9, bg="#0f1a2b")  # dark blue color
    label2.place(x=0, y=0)

    heading2 = Label(frame2, text="StepUp  Mart", fg="white", bg="#0f1a2b",

                     font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading2.place(x=270, y=90)

    img5 = Image.open(r"picture\shopping-online 11.jpg")
    resized_img5 = img5.resize((140, 120))
    img5 = ImageTk.PhotoImage(resized_img5)
    img_label5 = Label(frame2, image=img5, bg="white")
    img_label5.place(x=90, y=30)

    files = os.listdir('bakery wallpaper')
    img_array = []
    for i in files:
        img6 = Image.open(os.path.join('bakery wallpaper', i))
        resized_img6 = img6.resize((600, 450))
        img_array.append(ImageTk.PhotoImage(resized_img6))

    img6_label = Label(frame2, image=img_array[0], width=600)
    img6_label.place(x=160, y=150)

    img4 = Image.open(r"picture\arrow.jpg")
    resized_img4 = img4.resize((20, 40))
    img4 = ImageTk.PhotoImage(resized_img4)
    img_label4 = Button(frame2, image=img4, bg="white")#, command=rotate_image)
    img_label4.place(x=870, y=350)
    #
    img8 = Image.open(r"picture\OIP (4).jpeg")
    photo8 = ImageTk.PhotoImage(img8)
    stop_button = Button(frame2, image=photo8, bg="white", bd=0, command=PRODUCTS)
    stop_button.place(x=400, y=605)

    root.mainloop()

def ONLINE_PAGE():
    frame = Frame(root, width=920, height=670, bg="white")  # white color (whole screen)
    frame.place(x=0, y=0)

    label = Label(frame, width=135, height=9, bg="#0f1a2b")  # dark blue color
    label.place(x=0, y=0)

    heading = Label(frame, text="StepUp  Mart", fg="white", bg="#0f1a2b",
                    # Likhai  color white ,back ground color dark blue
                    font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=270, y=90)

    img1 = Image.open(r"picture\D.jpg")  # display main screen
    resized_img1 = img1.resize((920, 450))
    img1 = ImageTk.PhotoImage(resized_img1)
    img1_label = Label(frame, image=img1, bg="white", )
    img1_label.place(x=0, y=220)

    img = Image.open(r"picture\shopping-online 11.jpg")  # logo
    resized_img = img.resize((140, 140))
    img = ImageTk.PhotoImage(resized_img)
    img_label = Label(frame, image=img, bg="white")
    img_label.place(x=90, y=40)

    img2 = Image.open(r"picture\OIP (4).jpeg")  # button photo
    photo4 = ImageTk.PhotoImage(img2)
    stop_button = Button(root, image=photo4, bg="white", bd=0, command=WELCOME_PAGE)
    stop_button.place(x=670, y=365)
    root.mainloop()


def SIGNUP_PAGE():
    global FName , LName , UName , Password


    frame = Frame(root, width=920, height=670, bg="white")
    frame.place(x=0, y=0)

    photo = PhotoImage(file=r'picture\login (3).png')
    lab1 = Label(frame, image=photo, bg="white")
    lab1.place(x=50, y=150)

    frame1 = Frame(frame, width=350, height=400, bg="white")
    frame1.place(x=500, y=120)

    heading = Label(frame1, text="Sign up", fg="#57a1f8", bg="white",
                    font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    ##----------------------------------------------------------

    def on_enter(e):
        FName.delete(0, "end")

    def on_leave(e):
        name = FName.get()
        if name == "":
            FName.insert(0, "First Name")

    FName = Entry(frame1, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    FName.place(x=30, y=80)
    FName.insert(0, "First Name")
    FName.bind("<FocusIn>", on_enter)
    FName.bind("<FocusOut>", on_leave)

    user1 = Frame(frame1, width=295, height=2, bg="black")
    user1.place(x=25, y=107)

    ##----------------------------------------------------------

    def on_enter(e):
        LName.delete(0, "end")

    def on_leave(e):
        name = LName.get()
        if name == "":
            LName.insert(0, "Last Name")

    LName = Entry(frame1, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    LName.place(x=30, y=140)
    LName.insert(0, "Last Name")
    LName.bind("<FocusIn>", on_enter)
    LName.bind("<FocusOut>", on_leave)

    user2 = Frame(frame1, width=295, height=2, bg="black")
    user2.place(x=25, y=167)

    # ##----------------------------------------------------------

    def on_enter(e):
        UName.delete(0, "end")

    def on_leave(e):
        name = UName.get()
        if name == "":
            UName.insert(0, "Username")

    UName = Entry(frame1, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    UName.place(x=30, y=200)
    UName.insert(0, "Username")
    UName.bind("<FocusIn>", on_enter)
    UName.bind("<FocusOut>", on_leave)

    user2 = Frame(frame1, width=295, height=2, bg="black")
    user2.place(x=25, y=227)

    # ##-----------------------------------------------------
    def on_enter(e):
        Password.delete(0, "end")

    def on_leave(e):
        name = Password.get()
        if name == "":
            Password.insert(0, "Password")

    Password = Entry(frame1, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    Password.place(x=30, y=260)
    Password.insert(0, "Password")
    Password.bind("<FocusIn>", on_enter)
    Password.bind("<FocusOut>", on_leave)

    user3 = Frame(frame1, width=295, height=2, bg="black")
    user3.place(x=25, y=287)
    # ##----------------------------------------------------------
    sign_up = Button(frame1, width=39, pady=3, text="Sign up", bg="#57a1f8", fg="white", border=0, command=signup)
    sign_up.place(x=25, y=327)

    label3 = Label(frame1, text="I have an account", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
    label3.place(x=75, y=360)

    sign_up = Button(frame1, width=6, text="Sign in", border=0, bg="white", cursor='hand2', fg='#57a1f8')
                     #command=signin)
    sign_up.place(x=185, y=360)
    root.mainloop()
def SIGNIN_PAGE(root):
    global user, password  # Declare the variables as global so they can be accessed in signin()

    frame = Frame(root, width=920, height=670, bg="white")
    frame.place(x=0, y=0)

    photo = PhotoImage(file=r'picture\login (2).png')
    lab1 = Label(frame, image=photo, bg="white")
    lab1.place(x=50, y=150)

    frame1 = Frame(frame, width=350, height=350, bg="white")
    frame1.place(x=500, y=120)

    heading = Label(frame1, text="Sign in", fg="#57a1f8", bg="white",
                    font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    def on_enter_user(e):
        user.delete(0, "end")

    def on_leave_user(e):
        if not user.get():
            user.insert(0, "Username")

    user = Entry(frame1, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=90)
    user.insert(0, "Username")
    user.bind("<FocusIn>", on_enter_user)
    user.bind("<FocusOut>", on_leave_user)

    user1 = Frame(frame1, width=295, height=2, bg="black")
    user1.place(x=25, y=117)

    def on_enter_password(e):
        password.delete(0, "end")
        password.config(show="*")  # Hide the password with asterisks

    def on_leave_password(e):
        if not password.get():
            password.insert(0, "Password")
            password.config(show="")  # Show the placeholder text

    password = Entry(frame1, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    password.place(x=30, y=160)
    password.insert(0, "Password")
    password.bind("<FocusIn>", on_enter_password)
    password.bind("<FocusOut>", on_leave_password)

    user1 = Frame(frame1, width=295, height=2, bg="black")
    user1.place(x=25, y=187)

    sign_in = Button(frame1, width=39, pady=3, text="Sign in", bg="#57a1f8", fg="white", border=0,
                     command=signin)
    sign_in.place(x=25, y=254)

    label = Label(frame1, text="Don't have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
    label.place(x=75, y=285)

    sign_up = Button(frame1, width=6, text="Sign up", border=0, bg="white", cursor='hand2', fg='#57a1f8',command=SIGNUP_PAGE)
    sign_up.place(x=215, y=285)

    root.mainloop()

SIGNIN_PAGE(root)

