from tkinter import *
from tkinter import filedialog, PhotoImage
import webbrowser
from time import strftime
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt
from random import randint
import requests

# ---------------------------------------------------Weather Functionality-----------------------------------------------##

def open_weather():
    def fetch_weather():
        city = city_entry.get()
        api_key = "f0ed4770cfe6af621f5d921a30019a28"  # Replace with your OpenWeatherMap API key
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(base_url)
        data = response.json()

        if data["cod"] == 200:
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]

            weather_label.config(text=f"Weather: {weather}")
            temp_label.config(text=f"Temperature: {temp}°C")
            humidity_label.config(text=f"Humidity: {humidity}%")
            pressure_label.config(text=f"Pressure: {pressure} hPa")
        else:
            weather_label.config(text="City Not Found!")

    win_weather = Toplevel()
    win_weather.title("Weather Information")
    win_weather.geometry("400x300")
    win_weather.config(bg="lightblue")

    city_label = Label(win_weather, text="Enter City:", font=("Arial", 14), bg="lightblue")
    city_label.pack(pady=10)

    city_entry = Entry(win_weather, font=("Arial", 14))
    city_entry.pack(pady=5)

    get_weather_btn = Button(win_weather, text="Get Weather", font=("Arial", 14), command=fetch_weather)
    get_weather_btn.pack(pady=10)

    weather_label = Label(win_weather, text="", font=("Arial", 14), bg="lightblue")
    weather_label.pack(pady=5)

    temp_label = Label(win_weather, text="", font=("Arial", 14), bg="lightblue")
    temp_label.pack(pady=5)

    humidity_label = Label(win_weather, text="", font=("Arial", 14), bg="lightblue")
    humidity_label.pack(pady=5)

    pressure_label = Label(win_weather, text="", font=("Arial", 14), bg="lightblue")
    pressure_label.pack(pady=5)

    win_weather.mainloop()

## ------------------------------------------------------ Calculator, Notepad, Browser, Stopwatch, Game and Moon Emulator (same as before)-----------------------------------------------##
##--------------------------------------------------------------Calcilator Functionality-----------------------------------------------##

def open_calculator():
    win = Toplevel()  
    win.title("Simple Calculator")
    win['bg']="Black"
    mydata = Entry(win, justify='center', width = 12, borderwidth = 5,font=("Tahoma",35),bg="grey42",fg="Lightpink1")
    mydata.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = (10,40))

    def bclick(number):
        curr = mydata.get()
        mydata.delete(0, END)
        mydata.insert(0, str(curr) + str(number))

    def bclear():
        mydata.delete(0, END)

    def badd():
        fnum = mydata.get()
        global fn
        fn = int(fnum)
        mydata.delete(0, END)

    def bequal():
        snum = mydata.get()
        mydata.delete(0, END)
        mydata.insert(0, fn + int(snum))

    b0 = Button(win, text="0", padx=47, pady=20, command=lambda: bclick(0), font=("Tahoma",13,"bold"),bg="blue2", fg="cyan")
    b1 = Button(win, text="1", padx=47, pady=20, command=lambda: bclick(1), font=("Tahoma",13,"bold"),bg="blue2", fg="cyan")
    b2 = Button(win, text="2", padx=47, pady=20, command=lambda: bclick(2), font=("Tahoma",13,"bold"),bg="blue2", fg="cyan")
    b3 = Button(win, text="3", padx=47, pady=20, command=lambda: bclick(3), font=("Tahoma",13,"bold"),bg="blue2", fg="cyan")
    b4 = Button(win, text="4", padx=47, pady=20, command=lambda: bclick(4), font=("Tahoma",13,"bold"),bg="blue2", fg="cyan")
    b5 = Button(win, text="5", padx=47, pady=20, command=lambda: bclick(5), font=("Tahoma",13,"bold"),bg="blue2", fg="cyan")
    b6 = Button(win, text="6", padx=47, pady=20, command=lambda: bclick(6), font=("Tahoma",13,"bold"),bg="blue2", fg="cyan")
    b7 = Button(win, text="7", padx=47, pady=20, command=lambda: bclick(7), font=("Tahoma",13,"bold"),bg="blue2", fg="cyan")
    b8 = Button(win, text="8", padx=47, pady=20, command=lambda: bclick(8), font=("Tahoma",13,"bold"),bg="blue2", fg="cyan")
    b9 = Button(win, text="9", padx=47, pady=20, command=lambda: bclick(9), font=("Tahoma",13,"bold"),bg="blue2", fg="cyan")
    badd = Button(win, text="+", padx=45, pady=20, command=badd, font=("Tahoma",13,"bold"),bg="purple", fg="white")
    beq = Button(win, text="=", padx=106, pady=20, command=bequal, font=("Tahoma",13,"bold"),bg="orangered", fg="white")
    bclr = Button(win, text="Clear", padx=91, pady=20, command=bclear, font=("Tahoma",13,"bold"),bg="Seagreen2", fg="white")

    b1.grid(row=3, column=0)
    b2.grid(row=3, column=1)
    b3.grid(row=3, column=2)

    b4.grid(row=2, column=0)
    b5.grid(row=2, column=1)
    b6.grid(row=2, column=2)

    b7.grid(row=1, column=0)
    b8.grid(row=1, column=1)
    b9.grid(row=1, column=2)

    b0.grid(row=4, column=0)
    bclr.grid(row=4, column=1, columnspan=2)

    badd.grid(row=5, column=0)
    beq.grid(row=5, column=1, columnspan=2)

    win.mainloop()


##----------------------------------------------Notepad Functionality-----------------------------------------------##

def open_notepad():
    win1 = Toplevel()
    win1.geometry("1066x552")
    win1.title("Notepad")
    win1.config(bg="grey42")

    def save_file():
        open_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if open_file is None:
            return
        text = entry.get(1.0, END)
        open_file.write(text)
        open_file.close()

    def open_file():
        file = filedialog.askopenfile(mode="r", filetypes=[('text files', '*.txt')])
        if file is not None:
            content = file.read()
            entry.insert(INSERT, content)

    bl = Button(win1, width="12", height="1", bg="lightpink", fg="white" ,font=("lucida",18,"bold") ,text='Save File', command=save_file)
    b2 = Button(win1, width="12", height="1", bg="lightpink", fg="white" ,font=("lucida",18,"bold") ,text='Open File', command=open_file)

    entry = Text(win1, bg="LightYellow",font=("Times",13), height=23, width=115, wrap=WORD)
    entry.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
    bl.grid(row=1, column=0, padx=10, pady=15)
    b2.grid(row=1, column=2, padx=10, pady=15)

    win1.mainloop()

##----------------------------------------------------------Browser Functionality------------------------------------------------##

def open_browser():
        webbrowser.open("https://www.google.com")

##----------------------------------------------------------StopWatch Functionality------------------------------------------------##


def open_stopwatch():
    class Stopwatch(QWidget):
        def __init__(self):
            super().__init__()
            self.time = QTime(0, 0, 0, 0)
            self.time_label = QLabel("00:00:00.00", self)
            self.start_button = QPushButton("Start", self)
            self.stop_button = QPushButton("Stop", self)
            self.reset_button = QPushButton("Reset", self)
            self.timer = QTimer(self)
            self.initUI()

        def initUI(self):
            self.setWindowTitle("Stopwatch")
            vbox = QVBoxLayout()
            vbox.addWidget(self.time_label)
            self.setLayout(vbox)
            self.time_label.setAlignment(Qt.AlignCenter)

            hbox = QHBoxLayout()
            hbox.addWidget(self.start_button)
            hbox.addWidget(self.stop_button)
            hbox.addWidget(self.reset_button)
            vbox.addLayout(hbox)

            self.setStyleSheet("""
            QPushButton, QLabel
                {
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
                }
            QPushButton
               {
               font-size: 50px;
               }
            QLabel
               {
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 20px;
               }
              """)

            self.start_button.clicked.connect(self.start)
            self.stop_button.clicked.connect(self.stop)
            self.reset_button.clicked.connect(self.reset)
            self.timer.timeout.connect(self.update_display)

        def start(self):
            self.timer.start(10)

        def stop(self):
            self.timer.stop()

        def reset(self):
            self.timer.stop()
            self.time = QTime(0, 0, 0, 0)
            self.time_label.setText(self.format_time(self.time))

        def format_time(self, time):
            hours = time.hour()
            minutes = time.minute()
            seconds = time.second()
            milliseconds = time.msec() // 10
            return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

        def update_display(self):
            self.time = self.time.addMSecs(10)
            self.time_label.setText(self.format_time(self.time))

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        stopwatch = Stopwatch()
        stopwatch.show()
        sys.exit(app.exec_())
    
##---------------------------------------------------Guessing a Game Functionality----------------------------------------------##


def open_game():
    win2 = Toplevel()
    win2.geometry("500x300")
    win2.title("Number Guessing Game")
    win2.resizable(False,False)

    image_path=PhotoImage(file=r"C:\Users\nitin sharma\Downloads\Nitesh Work\ppproject\game_bg.png")
    bg_image=Label(win2,image=image_path)
    bg_image.place(relheight=1, relwidth=1)

    random_num = randint(1,100)

    def guess():
        entry_val = int(num_entry.get())
        try:
            if entry_val>random_num:
                msg["text"] = "Too High"
            elif entry_val<random_num:
                msg["text"] = "Too Low"
            else:
                msg ["text"] = "Correct"

        except:
            msg ["text"] = "please enter a number"


    lbl_intro = Label(win2, text="!Guess a number between 1 to 100!",font=("Times",12,"bold italic"), fg="PaleVioletRed2", bg = "lemon chiffon")
    lbl_intro.pack()

    lbl_number = Label(win2, text="Guess Number", font=("lucida",12,"bold"), fg="DeepSkyBlue2",bg="lawn green")
    lbl_number.pack()

    num_entry = Entry(win2, justify='center' ,font=("Impact",25,"bold"), bg="SeaGreen1",fg="OrangeRed3")
    num_entry.pack(pady=(80,5))

    cal_btn = Button(win2, text="Guess", width=8, height=1, bg="purple2", font=("lucida",20,"bold"),fg="tan1", relief=RIDGE, command=guess)
    cal_btn.pack()

    msg = Label(win2, text="", font=("Helvetica",15,"bold"))
    msg.pack()

    win2.mainloop()

    
root = Tk()
root.title("Moon Emulator")
root.geometry("1360x768")

# background image
image_path=PhotoImage(file=r"C:\Users\nitin sharma\Downloads\Nitesh Work\ppproject\test_bg.png")
bg_image=Label(root,image=image_path)
bg_image.place(relheight=1, relwidth=1)

# Clock Label
clock_label = Label(root, font=('calibri', 60, 'bold'), bg='LightYellow', fg="Orange")
clock_label.grid(row=0, column=3, padx=100, pady=20)

def update_clock():
    current_time = strftime('%I:%M:%S %p')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

update_clock()

# Load icons for buttons
calculator_icon = PhotoImage(file=r"C:\Users\nitin sharma\Downloads\Nitesh Work\ppproject\calculator_icon.png")
notepad_icon = PhotoImage(file=r"C:\Users\nitin sharma\Downloads\Nitesh Work\ppproject\notepad_icon.png")
browser_icon = PhotoImage(file=r"C:\Users\nitin sharma\Downloads\Nitesh Work\ppproject\browser_icon.png")
stopwatch_icon = PhotoImage(file=r"C:\Users\nitin sharma\Downloads\Nitesh Work\ppproject\stopwatch_icon.png")
game_icon = PhotoImage(file=r"C:\Users\nitin sharma\Downloads\Nitesh Work\ppproject\game_icon.png")
weather_icon = PhotoImage(file=r"C:\Users\nitin sharma\Downloads\Nitesh Work\ppproject\weather-icon.png")

# Calculator Button with Icon
btn_open_calculator = Button(root, text="Calculator", font=("Rockwell", 15, "bold"), image=calculator_icon, compound=TOP, command=open_calculator)
btn_open_calculator.grid(row=10, column=1, pady=50, padx=100)

# Notepad Button with Icon
btn_open_notepad = Button(root, text="Notepad", font=("Rockwell", 15, "bold"), image=notepad_icon, compound=TOP, command=open_notepad)
btn_open_notepad.grid(row=10, column=3, pady=50, padx=100)

# Browser Button with Icon
btn_open_browser = Button(root, text="Browser", font=("Rockwell", 15, "bold"), image=browser_icon, compound=TOP, command=open_browser)
btn_open_browser.grid(row=10, column=5, pady=50, padx=100)

# Stopwatch Button with Icon
btn_open_stopwatch = Button(root, text="Stopwatch", font=("Rockwell", 15, "bold"), image=stopwatch_icon, compound=TOP, command=open_stopwatch)
btn_open_stopwatch.grid(row=20, column=1, pady=100)

# Game Button with Icon
btn_open_game = Button(root, text="Guessify", font=("Rockwell", 15, "bold"), image=game_icon, compound=TOP, command=open_game)
btn_open_game.grid(row=20, column=3, pady=100)

# Weather Button with Icon
btn_open_weather = Button(root, text="Weather", font=("Rockwell", 15, "bold"), image=weather_icon, compound=TOP, command=open_weather)
btn_open_weather.grid(row=20, column=5, pady=100)

root.mainloop()
