from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# nr_letters = random.randint(8, 10)
# nr_symbols = random.randint(2, 4)
# nr_numbers = random.randint(2, 4)

# password_list = []

# for char in range(nr_letters):
#  password_list.append(random.choice(letters))

# for char in range(nr_symbols):
#   password_list += random.choice(symbols)
#
# for char in range(nr_numbers):
#   password_list += random.choice(numbers)

    # using list comprehension
    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list) # shuffling the elements in the list

    # password = ""
    # for char in password_list:
    #   password += char
    #
    # print(f"Your password is: {password}")
    password = ''.join(password_list)  # converting list to a string
    password_input.insert(0, password)  # reflecting data in entry widget
    pyperclip.copy(password)  # copying the password to clipboard so that the password can be used immediately 

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_input.get()  # get() takes the entry input and we can save it in a variable
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:  # checking if website and password entry is empty
        messagebox.showinfo("please make sure you haven't left any fields empty") # Then show a warning message

    else: # if website and password data given then save the data in data.txt

        #messagebox.askokcancel() returns a boolean either True or False
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                      f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:  # if True
            with open("data.txt", 'a') as data_file: # create the file and add data to it
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END) # after the data is saved we want the website entry to be blank again
                password_input.delete(0, END) # after the data is saved we want the password entry to be blank again






# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)  # increased the size of the window

#creating canvas widget on which we can put our image
canvas = Canvas(width=200, height=200)  # taking the canvas height and width same as image width and height
logo_img = PhotoImage(file="logo.png")  # converting the image into tkinter PhotoImage
canvas.create_image(100, 100, image=logo_img)  # bcz, canvas.create accepts Photoimage as image
canvas.grid(column=1, row=0) # placing canvas on the screen using grid() method

# labels
website_label = Label(text='Website')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username')
email_label.grid(column=0, row=2)

password_label = Label(text='Password')
password_label.grid(column=0, row=3)

#entry
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2) # for columnspan the entry widget would be spread upto 2 columns
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'sayantiju2014@gmail.com') # this would insert/show the text in entry widget

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

#button
generate_password = Button(text='Generate Password', command=password_generator)
generate_password.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
