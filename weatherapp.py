import tkinter as tk
import requests
import json
win=tk.Tk()
win.title("weather")
win.geometry("500x500")

api="your Api"
url="https://api.openweathermap.org/data/2.5/weather"
def weather():
    location=entry.get()
    answer=url+"?q="+location+"&APPID=16a9a2abebd6122eca397d1abd9af86d"
    response=requests.get(answer)
    res=response.json()
    if res["coord"]!="404":
        x=res["main"]
        temperature=x["temp"]
        pressure=x["pressure"]
        humidity=x["humidity"]
        y=res["weather"]
        weather_description=y[0]["description"]
        
        label1=tk.Label(win,text=f'temperature(k)={temperature},\n'
                                 f'atmospheric pressure(hpa)={pressure},\n'
                                 f'humidity(%)={humidity},\n'
                                 f'description={weather_description}')
        label1.grid(row=2,column=0)
    else:
        label2=tk.Label(win,text='enter correct city')
        label2.grid(row=2,column=0)
label=tk.Label(win,text="enter city name here:",bg='#add8e6')
label.grid(row=0,column=0)
label.config(font=("times",20,"bold"))

entry=tk.Entry(win)
entry.grid(row=1,column=0,padx=100)
button=tk.Button(win,text="search",command=weather)
button.grid(row=1,column=1)
win.mainloop()



