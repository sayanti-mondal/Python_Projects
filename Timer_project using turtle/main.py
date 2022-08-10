import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer(): # stopping the timer and resetting it to 00:00 if reset button pressed
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer(): # call count_down function according to reps value
    global reps
    reps += 1  # increasing the reps every time start_timer getting called
    work_sec = WORK_MIN * 60  # converting minutes to second bcz window.after in function count_down only accepts second
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:  # for reps 2,4,6 => short break
        count_down(short_break_sec)
        timer_label.config(text='Break', fg=PINK) # changing the timer_label on the screen according to the task
    elif reps % 8 == 0:  # for rep 8 big break
        count_down(long_break_sec)
        timer_label.config(text='Break', fg=RED)
    else:
        count_down(work_sec)  # for reps 1,3,5 => work
        timer_label.config(text='Work', fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #



def count_down(count): # implementing timer and display it in min:sec format

    # code to display the timer text in min:sec format
    count_min = math.floor(count/60) # using floor bcz floor(3.7) = 3 whereas round(3.7) = 4
    count_sec = count % 60

    #used the concept of dynamic typing to convert variable count_sec from integer to string
    if count_sec < 10: # when the sec_timer decreases below 10, it was showing 4:9, but need to show 4:09
        count_sec = f"0{count_sec}" # using an f-string to append 0 before single digit sec
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") # canvas method to change the text of a widget

    # Exact code to decrease the timer by 1 sec
    if count > 0: # decrease the timer till it reaches 0 ; need 5,4,3,2,1,0 not -1,-2,...
        global timer
        timer = window.after(1000, count_down, count-1) # tkinter method to decrease the timer every 1 sec interval
                                                        # similar to time.sleep()

    else:  # after the timer reaches to 0 need to start_timer again for next task either work or short/long break
        start_timer()
        #after every 2 reps (i.e. 25 min work and 5 min break/20 min break) need to give 1 tick mark;i.e work_sessions
        marks = ""
        work_sessions = math.floor(reps/2) # if reps = 6, the 6/2 loop need to be 3 times to give 3 tick marks
        for _ in range(work_sessions):
            marks += '✔'
        tick_label.config(text=marks) # Displaying the tick marks in the screen

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)  # increased the size of the window

#creating canvas widget on which we can put our image
canvas = Canvas(width=200, height=224, bg=YELLOW)  # taking the canvas height and width same as image width and height
tomato_img = PhotoImage(file="tomato.png")  # converting the image into tkinter PhotoImage
canvas.create_image(102, 112, image=tomato_img)  # bcz, canvas.create accepts Photoimage as image
# creating a text on canvas
timer_text = canvas.create_text(102, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



timer_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME, 40, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

tick_label = Label(bg=YELLOW, fg=GREEN)
tick_label.grid(column=1, row=3)

window.mainloop()