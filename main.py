from tkinter import Tk, Canvas, Label, Entry, Button, font as tkFont
import math

COUNT = 2  # time in seconds
timer = None


# time counting function
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    global timer
    if int(count_sec) < 10:
        count_sec = f"0{str(count_sec)}"
    canvas.itemconfig(time_display, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = app.after(1000, count_down, count - 1)
    else:
        texts = []
        for letter in text_entry.get():
            if letter == " ":
                pass
            else:
                texts.append(letter)

        speed = len(texts) / COUNT
        canvas.itemconfig(time_display, text=f"{speed:.2f}\n letters per sec", width=100)
        text_entry.config(state="disabled")


def start_count(*args):
    global timer
    if timer is None:  # To ensure the timer starts only once
        count_down(COUNT)


def restart():
    global timer
    if timer:
        app.after_cancel(timer)  # Cancel the ongoing timer if any
    timer = None  # Reset timer

    text_entry.config(state="normal")  # Enable text entry for typing
    text_entry.delete(0, "end")  # Clear the text entry
    text_entry.focus()  # Focus on the text entry widget
    canvas.itemconfig(time_display, text="00:00")  # Reset time display
    text_entry.bind("<KeyPress>", start_count)


app = Tk()
app.title("Typing_speed_test")
app.minsize(300, 200)
canvas = Canvas(width=300, height=100, bg="yellow", highlightthickness=0)

# content
content = Label(text="Check your typing speed. Start typing and time will count down")
content.grid(column=1, row=1)

# typing area
text_entry = Entry(width=60, font=tkFont.Font(size=14))
text_entry.grid(column=1, row=2)
text_entry.bind("<KeyPress>", start_count)

# time display
time_display = canvas.create_text(150, 50, text="00:00", font=tkFont.Font(size=20, weight="bold"), fill="white")
canvas.grid(column=1, row=3)

# restart button
restart = Button(text="Restart", command=restart, bg="green", fg="white", font=tkFont.Font(size=12), padx=20, pady=10)
restart.grid(column=1, row=4)

if text_entry.get() == "":
    canvas.itemconfig(time_display, text="00:00")
else:
    count_down(COUNT)

app.mainloop()
