PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#E7F0DC"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0

def reset_timer():
    
    windows.after_cancel(timer)
    canvas.itemconfig(timer_txt,text="00:00")
    timer_label.config(text="Timer")
    check_box.config(text="")
    global reps
    reps=0




def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    short_break_sec=SHORT_BREAK_MIN

    if reps%8==0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=PINK)
    elif reps%2==0:
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=RED)
    else:
        count_down(work_sec)
        timer_label.config(text="Work",fg=GREEN)

    # count_down(5*60)



def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_txt,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=windows.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_session=math.floor(reps/2)
        for _ in range(work_session):
            marks+="✔️"
        check_box.config(text=marks)
    
        




import math
from tkinter import *
windows=Tk()
windows.minsize(width=700,height=400)
windows.title("Pomdaro Timer")
windows.config(padx=60,pady=60,bg=YELLOW)


timer_label=Label(text="Timer",bg=YELLOW,fg=PINK,font=(FONT_NAME,40))
timer_label.pack()


canvas=Canvas(width=210,height=240,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(110,120,image=tomato_img)
timer_txt=canvas.create_text(110,130,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
canvas.pack()

start_timer=Button(text="START",command=start_timer)
start_timer.pack()

check_box=Label()
check_box.pack()

reset_timer=Button(text="RESET",command=reset_timer)
reset_timer.pack()

windows.mainloop()