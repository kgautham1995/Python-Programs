from tkinter import *
import calendar
cal=Tk()
cal.title("calender by Gautam")
year=int(input("Enter the year to show the calender"))
MyCal=calendar.calendar(year)
cal_year=Label(cal, text=MyCal, font="Consolas 10 bold")
cal_year.pack()
cal.mainloop()