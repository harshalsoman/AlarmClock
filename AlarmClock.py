
from tkinter import *
from datetime import datetime
import time
from tkinter import messagebox
import winsound

root=Tk()
root.title("Alarm Clock")
root.iconbitmap('alarm-clock.ico')
#root.iconbitmap(r'C:\Users\harsh\PycharmProjects\Python_Internship\alarm-clock.ico')
root.geometry("400x300")
#def refresh_Label4():



def update():
    global hours, minutes
    hours = hour.get()
    minutes = minute.get()
    name = Entry3.get()



    #Label4.configure( text=name + "-Alarm set for " + hours + ":" + minutes)


    #date=Entry5.get()
    #day=date[0:2]
   # month=date[3:5]
    #year= date[6:]



    #refresh_Label4()
    alarm_time= hours + ":" + minutes
    now = datetime.now()
    current_time = time.strftime("%H:%M")
    print(current_time)
    print(alarm_time)
    messagebox.askquestion(Entry3.get(), "Save Alarm for"+alarm_time)
    while current_time!= alarm_time:

        current_time = time.strftime("%H:%M")
        #print("Hi")
        time.sleep(1)

    if(current_time== alarm_time):
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        messagebox.showinfo(Entry3.get(), "Alarm!!!!!")




    #current_hour = current_time[0:2]
    #current_minute = current_time[3:5]
    #current_seconds = current_time[7:9]
   # hrs = int(hours) - int(current_hour)
    #mins = int(minutes) - int(current_minute)
    #secs = 0 - int(current_seconds)
    #duration = (hrs * 60 + mins) * 60 #
    #Label6 = Label(root, text=duration)
    #Label6.grid(row=5, column=1)
    #Label6.after(duration, refresh_Label4)

    #Button1.after(duration*1000,print("ALARM!"))
    now = datetime.now()
    current_date = str(now.date())
    current_day = current_date[0:4]
    current_month = current_date[5:7]
    current_year = current_date[8:10]




Label1= Label(root, text="Enter hours",padx=13)
Label1.grid(row=0,column=0,pady=10)

Label2= Label(root, text="Enter minutes",padx=10)
Label2.grid(row=0,column=2,pady=10)

Label3= Label(root, text="Alarm Name",padx=10)
Label3.grid(row=1,column=0)

Label4= Label(root,text="")
Label4.grid(row=4, column=1, columnspan=2)

#Label5= Label(root, text="Enter Date",padx=10,pady=12)
#Label5.grid(row=2,column=0)


hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24'
		)
hour.set(hours[0])

Entry1 = OptionMenu(root, hour, *hours)
Entry1.grid(row=0,column=1)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
minute.set(minutes[0])

Entry2= OptionMenu(root, minute, *minutes)
Entry2.grid(row=0,column=3)

Entry3=Entry(root,width=15)
Entry3.grid(row=1,column=1)

#Entry5=Entry(root,width=15)
#Entry5.grid(row=2,column=1)


Button1=Button(root,text="Set Alarm",width=20,command=update)
Button1.grid(row=2,column=1,columnspan=2,pady=10)



root.mainloop()