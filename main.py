from tkinter import*
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global reps

    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
    tick.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    reps += 1

    if reps <= 8:
        if reps % 8 == 0:
            label.config(text= "Long Break", font=(FONT_NAME, 30, "bold"), fg=GREEN)
            count_down_sec(LONG_BREAK_MIN )
        elif reps % 2 != 0:
            label.config(text="Work", font=(FONT_NAME, 50, "bold"), fg=RED)
            count_down_sec(WORK_MIN )
        else:
            label.config(text="Small Break", font=(FONT_NAME, 30, "bold"), fg=PINK)
            count_down_sec(SHORT_BREAK_MIN )
    else:
        reset_timer()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down_sec(sec):
    global reps
    global timer

    count_min = math.floor(sec / 60)
    count_sec = sec % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if sec > 0:
        timer = window.after(1000, count_down_sec, sec - 1) # after εκτελει τη function καθε ms(1000)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
        tick.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
# window/canvas
text_is_on = True
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png") #tkinter function, gets hold of image
canvas.create_image(100, 112, image=tomato)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

#label
label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

tick = Label(text="✓" , font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
tick.grid(column=1, row=3)

#buttons
button1 = Button(text="Start", command=start_timer)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", command=reset_timer)
button2.grid(column=2, row=2)

window.mainloop()