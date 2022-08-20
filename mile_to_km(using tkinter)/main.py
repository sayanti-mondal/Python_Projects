from tkinter import *
#
window = Tk() #like screen in turtle
window.title("Mile to Km Converter")
#window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# #Label
# # creating a label component
# my_label = Label(text = "I am a label", font = ("Arial", 24, 'bold'))
# my_label.grid(row=0,column=0) # This would attach the component to the screen then only we can see it on the screen
#
# #update the properties of the component that we created
# # my_label['text'] = 'New Text'
# my_label.config(text = 'new text')
#
#
# def button_clicked():
#     print("click me")
#     entry_input = input.get()
#     my_label.config(text=entry_input)
#
#
# #Button
# button = Button(text='Click Me', command=button_clicked)
# button.grid(row=1,column=1)
#
# new_button = Button(text="New Button")
# new_button.grid(row=0, column=2)
#
# #Entry
# input = Entry(width=10)
# input.grid(row=2,column=3)
#
# # def add(*args):
# #     # for num in args:
# #     #     print(num)
# #     print(args)#(4, 5)
# #     print(sum(args))
# # add(5,6,7)















#This would keep the window open to listen  for any user interaction like turtle's exitonclick()

# it is an Entry

# program for miles to km converter

mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)


#Miles text
mile_text = Label(text="Miles")
mile_text.grid(column=2, row=0)

#is_equal_to; label
is_equal_to_text = Label(text="is equal to")
is_equal_to_text.grid(column=0, row=1)

#output label
output_label = Label(text="0")
output_label.grid(column=1, row=1)

#Km label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)


def mile_to_km():
    miles = float(mile_input.get())
    km = round(miles * 1.609)
    output_label.config(text=f"{km}")


#calculate button
calculate_button = Button(text='Calculate',command=mile_to_km)
calculate_button.grid(column=1, row=2)







window.mainloop()
