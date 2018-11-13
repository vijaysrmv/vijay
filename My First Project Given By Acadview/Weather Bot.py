from tkinter import *
master=Tk()
import requests

master.geometry("250x400")
master.title("Weather Gui Application")
w=Canvas(master,width=250,height=400)
my_image=PhotoImage(file='C:\\Users\\vvch5\\PycharmProjects\\vijay1.png')
w.create_image(0,0,anchor=NW,image=my_image)
w.pack()
w.create_line(0,205,250,205)
w.create_line(110,235,110,335)
w.create_line(0,235,250,235)
w.create_line(0,285,250,285)
w.create_line(0,335,250,335)
class weather:
   def today(self):
       inputvalue = textBox.get("1.0", "end-1c")
       print(inputvalue)
       api_address = 'https://api.openweathermap.org/data/2.5/weather?appid=d0e953670ffe68b6a6d0a32c919007a1&q='
       url = api_address + inputvalue
       json_data = requests.get(url).json()
       formatedata = json_data['main']['temp']
       string = int(formatedata)
       print(formatedata)
       label_4 = Label(master, text=(string - 273), bg="#47A8E5", font=("Times new Roman", 20, 'bold')).place(x=10, y=5)
       label4 = Label(master, text="o", bg="#47A8E5", font=("Times new Roman", 10, 'bold')).place(x=40, y=5)
       label2 = Label(master, text="C", bg="#47A8E5", font=("Times new Roman", 14, 'bold')).place(x=50, y=10)
       city_Name = json_data['name']
       weather = json_data['weather'][0]['main']
       label3 = Label(master, text=city_Name, bg="#47A8E5", font=("Times new Roman", 10, 'bold')).place(x=10, y=40)
       label6 = Label(master, text=weather, bg="#47A8E5", font=("Times New Roman", 10, 'bold')).place(x=10, y=60)
       labe_6 = Label(master, text="Details", bg="#47A8E5", font=("Times New Roman", 10)).place(x=10, y=210)
       text = json_data['wind']['speed']
       covert_string = str(text)
       string_data_wind = covert_string + " Km/hr NW"
       labe_7 = Label(master, text="WIND", bg="#47A8E5", font=("Times New Roman", 7)).place(x=10, y=250)
       labe_8 = Label(master, text=string_data_wind, bg="#47A8E5", font=("Times New Roman", 7)).place(x=12, y=265)
       labe_9 = Label(master, text="REAL FEEL", bg="#47A8E5", font=("Times New Roman", 7)).place(x=120, y=250)
       labe_10 = Label(master, text=string - 274, bg="#47A8E5", font=("Times New Roman", 7)).place(x=120, y=265)
       labe_11 = Label(master, text="UV INDEX", bg="#47A8E5", font=("Times New Roman", 7)).place(x=10, y=290)
       labe_12 = Label(master, text="PRESSURE", bg="#47A8E5", font=("Times New Roman", 7)).place(x=120, y=290)
       labe_13 = Label(master, text="2", bg="#47A8E5", font=("Times New Roman", 7)).place(x=10, y=305)
       pressure = json_data['main']['pressure']
       convert_into_string = str(pressure)
       string_data = convert_into_string + " mb"
       labe_14 = Label(master, text=string_data, bg="#47A8E5", font=("Times New Roman", 7)).place(x=120, y=305)
       label_5 = Label(master, bg="#47A8E5", fg="white", text="Data Provided By OpenWeatherMap", font=("cambria",10,
                                                                                                       'bold')).place(
           x=10,y=340)


   def tommarrow(self):
       inputvalue = textBox.get("1.0", "end-1c")
       api_address = 'https://api.openweathermap.org/data/2.5/forecast?' \
                     '&appid=d0e953670ffe68b6a6d0a32c919007a1&q='
       url = api_address + inputvalue
       json_data = requests.get(url).json()
       json_data1 = json_data['list'][4]
       formatedata = json_data1['main']['temp']
       string = int(formatedata)
       print(formatedata)
       label_4 = Label(master, text=(string - 273), bg="#47A8E5", font=("Times new Roman", 20, 'bold')).place(x=10, y=5)
       label4 = Label(master, text="o", bg="#47A8E5", font=("Times new Roman", 10, 'bold')).place(x=40, y=5)
       label2 = Label(master, text="C", bg="#47A8E5", font=("Times new Roman", 14, 'bold')).place(x=50, y=10)
       #city_Name = json_data['name']
       weather = json_data1['weather'][0]['main']
       #label3 = Label(master, text=city_Name, bg="#47A8E5", font=("Times new Roman", 10, 'bold')).place(x=10, y=40)
       label6 = Label(master, text=weather, bg="#47A8E5", font=("Times New Roman", 10, 'bold')).place(x=10, y=60)
       labe_6 = Label(master, text="Details", bg="#47A8E5", font=("Times New Roman", 10)).place(x=10, y=210)
       text = json_data1['wind']['speed']
       covert_string = str(text)
       string_data_wind = covert_string + " Km/hr NW"
       labe_7 = Label(master, text="WIND", bg="#47A8E5", font=("Times New Roman", 7)).place(x=10, y=250)
       labe_8 = Label(master, text=string_data_wind, bg="#47A8E5", font=("Times New Roman", 7)).place(x=12, y=265)
       labe_9 = Label(master, text="REAL FEEL", bg="#47A8E5", font=("Times New Roman", 7)).place(x=120, y=250)
       labe_10 = Label(master, text=string - 274, bg="#47A8E5", font=("Times New Roman", 7)).place(x=120, y=265)
       labe_11 = Label(master, text="UV INDEX", bg="#47A8E5", font=("Times New Roman", 7)).place(x=10, y=290)
       labe_12 = Label(master, text="PRESSURE", bg="#47A8E5", font=("Times New Roman", 7)).place(x=120, y=290)
       labe_13 = Label(master, text="2", bg="#47A8E5", font=("Times New Roman", 7)).place(x=10, y=305)
       pressure = json_data1['main']['pressure']
       convert_into_string = str(pressure)
       string_data = convert_into_string + " mb"
       labe_14 = Label(master, text=string_data, bg="#47A8E5", font=("Times New Roman", 7)).place(x=120, y=305)
       label_5 = Label(master, bg="#47A8E5", fg="white", text="Data Provided By OpenWeatherMap", font=("cambria", 10,
                                                                                                       'bold')).place(
           x=10, y=340)



g=weather()
label_0=Label(master,text="Weather",font=("Times New Roman",20,'bold','underline'),bg='#47A8E5')
label_0.place(x=90,y=10)
label_0=Label(master,text=" City :-",width=4,bd=3,padx=2,font=("Times New Roman",10,'bold','underline'),bg="#47A8E5")
label_0.place(x=10,y=80)
textBox=Text(master,height=1,width=15,bd=4,font=("Times new roman",10,'bold'))
textBox.place(x=60,y=80)
buttoncommit=Button(master,text="Show",command=lambda:g.today())
buttoncommit.place(x=200,y=78)
buttoncommit1=Button(master,height=1,text="Next",command=lambda :g.tommarrow()).place(x=10,y=360)
mainloop()


