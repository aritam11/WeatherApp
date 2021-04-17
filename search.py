from tkinter import *
from tkinter.ttk import *
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def weather_search(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    weather_final = weather+"°C"
    # print(location)
    # print(time)
    # print(info)
    # print(weather_final)
    report = (location, time, info, weather_final)
    return report


def check():
    city_final = city.get()
    city_final = city_final+" weather"
    detail = weather_search(city_final)
    locationlbl['text'] = '{}'.format(detail[0])
    timelbl['text'] = '{}'.format(detail[1])
    temperaturelbl['text'] = '{}'.format(detail[2])
    weatherlbl['text'] = '{}'.format(detail[3])


root = Tk()

root.title('Weather App')
root.geometry('700x350')
sto = Style()
sto.configure('TButton', font=('calibri', 10, 'bold'), foreground='Green')
city = StringVar()
city_input = Entry(root, textvariable=city, justify=CENTER)
city_input.pack(ipadx=30, ipady=6)


search = Button(root, text="search", command=check, style='TButton')
search.pack(pady=10)


locationlbl = Label(root, text="", font=('bold', 20))
timelbl = Label(root, text="", font=(10))
temperaturelbl = Label(root, text="", font=(10))
weatherlbl = Label(root, text="", font=(10))
locationlbl.pack(pady=10)
timelbl.pack(pady=10)
temperaturelbl.pack(pady=10)
weatherlbl.pack(pady=10)


root.mainloop()
