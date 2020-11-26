import requests
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter.ttk import Combobox
from tkinter import messagebox

ulkelerUrl = "https://api.covid19api.com/countries"
ulkelerveriUrl = "https://api.covid19api.com/total/dayone/country/"
dunya = "https://api.covid19api.com/world/total"
spc="https://api.covid19api.com/total/country/china"


f = requests.get(ulkelerUrl)
d = f.json()

slug = []
confirmed = []
gConfirmed=[]
deaths = []
gDeaths=[]
recovered = []
gRecovered=[]
active = []
date = []
pie1 = []
pieworld1 = []


def appendslug():
    for x in range(0, len(d)):
        slug.append(d[x]["Slug"])


appendslug()
slug.sort()

form = tk.Tk()
form.title("COVİD-19 Uygulaması")
form.geometry("1000x600+150+60")


combobox = Combobox(form, values=slug, font=10)
combobox.pack()

lbl=tk.Label(form,text="Ülke Seç :", font=10)
lbl.place(relx=0.25,rely=0)

combobox23 = Combobox(form, values=date, font=10,width=15)
combobox23.place(relx=0.12, rely=0.9)

def sil():
    confirmed.clear()
    gConfirmed.clear()
    date.clear()
    deaths.clear()
    gDeaths.clear()
    recovered.clear()
    gRecovered.clear()
    active.clear()
    pie1.clear()
    pieworld1.clear()


class Veri:

    def confirmed1(self):
        c=requests.get(spc)
        h=c.json()
        f2 = requests.get(ulkelerveriUrl + combobox.get())
        d2 = f2.json()
        if combobox.get() == "china":
            for y in range (0,len(h)-1):
                confirmed.append(h[y]["Confirmed"])

        elif combobox.get() !="china":
            for x in range(0, len(d2)-1):
                confirmed.append(d2[x]["Confirmed"])

        if len(date) != 0:
            gConfirmed.append(confirmed[0])
        else:
            pass
        for g in range (1,len(confirmed)):
            gConfirmed.append(confirmed[g]-confirmed[g-1])





    def deaths1(self):
        c = requests.get(spc)
        h = c.json()
        f2 = requests.get(ulkelerveriUrl + combobox.get())
        d2 = f2.json()
        if combobox.get() == "china":
            for y in range(0, len(h) - 1):
                deaths.append(h[y]["Deaths"])


        elif combobox.get() != "china":
            for x in range(0, len(d2) - 1):
                deaths.append(d2[x]["Deaths"])

        if len(date) != 0 :
            gDeaths.append(deaths[0])
        else:
            pass
        for g in range(1, len(deaths) ):
            gDeaths.append(deaths[g] - deaths[g - 1])

    def recovered1(self):
        c = requests.get(spc)
        h = c.json()
        f2 = requests.get(ulkelerveriUrl + combobox.get())
        d2 = f2.json()
        if combobox.get() == "china":
            for y in range(0, len(h) - 1):
                recovered.append(h[y]["Recovered"])


        elif combobox.get() != "china":
            for x in range(0, len(d2) - 1):
                recovered.append(d2[x]["Recovered"])

        if len(date) != 0:
            gRecovered.append(recovered[0])
        else:
            pass

        for g in range(1, len(recovered)):
            gRecovered.append(recovered[g] - recovered[g - 1])

    def active1(self):
        c = requests.get(spc)
        h = c.json()
        f2 = requests.get(ulkelerveriUrl + combobox.get())
        d2 = f2.json()
        if combobox.get() == "china":
            for y in range(0, len(h) - 1):
                active.append(h[y]["Active"])


        elif combobox.get() != "china":
            for x in range(0, len(d2) - 1):
                active.append(d2[x]["Active"])

    def date1(self):
        c = requests.get(spc)
        h = c.json()
        f2 = requests.get(ulkelerveriUrl + combobox.get())
        d2 = f2.json()
        if combobox.get() == "china":
            for y in range(0, len(h) - 1):
                date.append(h[y]["Date"])


        elif combobox.get() != "china":
            for x in range(0, len(d2) - 1):
                date.append(d2[x]["Date"])

    def appenddate(self):
        combobox23.delete(0, 50)
        combobox23.config(values="")
        c = requests.get(spc)
        h = c.json()
        f3 = requests.get(ulkelerveriUrl + combobox22.get())  # Tablo combobox'undaki ülke listesi için.
        d3 = f3.json()
        sil()

        if combobox22.get() == "china":
            for y in range(0, len(h) - 1):
                date.append(h[y]["Date"])
                combobox23.config(values=date)
            
        else:

            for x in range(0, len(d3)-1):
                date.append(d3[x]["Date"])
                combobox23.config(values=date)
                
            if len(combobox22.get()) == 0:
                messageslug = messagebox.showinfo(title="Ülke seçmediniz" , message="Lütfen bir ülke seçiniz.")    

            elif len(date) == 0 :
                msg2=messagebox.showinfo(title="Hata", message="Ülke ile ilgili veri bulunamadı. Lütfen başka bir ülke seçiniz.")
                


veri = Veri()



class Ciz:
    def date_confirmed(self):
        sil()
        veri.date1()

        if len(combobox.get()) ==0:
            messageslug = messagebox.showinfo(title="Ülke seçmediniz" , message="Lütfen bir ülke seçiniz.")

        elif len(date) == 0:
            messagedate = messagebox.showinfo(title="Hata", message="Seçilen ülke ile ilgili veri bulunamadı. Lütfen başka bir ülke seçiniz.")

        else:
            veri.confirmed1()
            plt.plot(date, confirmed)
            plt.scatter(date, confirmed)
            plt.title(combobox.get().upper())
            plt.xlabel("Tarih")
            plt.ylabel("Toplam Vaka Sayısı")
            plt.xticks(range(0, len(date), 20))
            plt.xticks(rotation=20)
            plt.show()

    def date_deaths(self):
        sil()
        veri.date1()
        if len(combobox.get()) == 0:
            messageslug = messagebox.showinfo(title="Ülke seçmediniz", message="Lütfen bir ülke seçiniz.")

        elif len(date) == 0:
            messagedate = messagebox.showinfo(title="Hata", message="Seçilen ülke ile ilgili veri bulunamadı. Lütfen başka bir ülke seçiniz.")
        else:
            veri.deaths1()
            plt.plot(date, deaths)
            plt.scatter(date, deaths)
            plt.title(combobox.get().upper())
            plt.xlabel("Tarih")
            plt.ylabel("Toplam Vefat Sayısı")
            plt.xticks(range(0, len(date), 20))
            plt.xticks(rotation=10)
            plt.show()

    def date_recovered(self):
        sil()
        veri.date1()
        if len(combobox.get()) == 0:
            messageslug = messagebox.showinfo(title="Ülke seçmediniz", message="Lütfen bir ülke seçiniz.")

        elif len(date) == 0:
            messagedate = messagebox.showinfo(title="Hata", message="Seçilen ülke ile ilgili veri bulunamadı. Lütfen başka bir ülke seçiniz.")
        else:
            veri.recovered1()
            plt.plot(date, recovered)
            plt.scatter(date, recovered)
            plt.title(combobox.get().upper())
            plt.xlabel("Tarih")
            plt.ylabel("Toplam İyileşen Hasta Sayısı")
            plt.xticks(range(0, len(date), 20))
            plt.xticks(rotation=20)
            plt.show()

    def date_active(self):
        sil()
        veri.date1()
        if len(combobox.get()) == 0:
            messageslug = messagebox.showinfo(title="Ülke seçmediniz", message="Lütfen bir ülke seçiniz.")

        elif len(date) == 0:
            messagedate = messagebox.showinfo(title="Hata", message="Seçilen ülke ile ilgili veri bulunamadı. Lütfen başka bir ülke seçiniz.")
        else:
            veri.active1()
            plt.plot(date, active)
            plt.scatter(date, active)
            plt.title(combobox.get().upper())
            plt.xlabel("Tarih")
            plt.ylabel("Aktif Vaka Sayısı")
            plt.xticks(range(0, len(date), 20))
            plt.xticks(rotation=20)
            plt.show()

    def pie(self):
        f2 = requests.get(ulkelerveriUrl + combobox.get())
        d2 = f2.json()
        c = requests.get(spc)
        h = c.json()
        sil()
        veri.date1()

        if len(combobox.get()) == 0:
            messageslug = messagebox.showinfo(title="Ülke seçmediniz", message="Lütfen bir ülke seçiniz.")

        elif len(date) == 0:
            messagedate = messagebox.showinfo(title="Hata", message="Seçilen ülke ile ilgili veri bulunamadı. Lütfen başka bir ülke seçiniz.")

        else:
            if combobox.get()=="china":
                pie1.append(h[len(h) - 2]["Recovered"])
                pie1.append(h[len(h) - 2]["Deaths"])
                pie1.append(h[len(h) - 2]["Active"])
                plt.pie(pie1, labels=["İyileşen", "Vefat Eden", "Aktif Vaka"], colors=["green", "red", "orange"],autopct="%1.2f%%")
                plt.title(combobox.get().upper())
                plt.show()

            else:
                pie1.append(d2[len(d2) - 2]["Recovered"])
                pie1.append(d2[len(d2) - 2]["Deaths"])
                pie1.append(d2[len(d2) - 2]["Active"])
                plt.pie(pie1, labels=["İyileşen", "Vefat Eden", "Aktif Vaka"], colors=["green", "red", "orange"],autopct="%1.2f%%")
                plt.title(combobox.get().upper())
                plt.show()

    def pieworld(self):
        f10 = requests.get(dunya)
        d10 = f10.json()
        sil()

        pieworld1.append(d10["TotalRecovered"])
        pieworld1.append(d10["TotalDeaths"])
        plt.pie(pieworld1, labels=["İyileşen", "Vefat Eden"], colors=["green", "red"], autopct="%1.2f%%")
        plt.title("DÜNYA")
        plt.show()


ciz = Ciz()

label = tk.Label(form, text="Toplam Vefat Sayısı Grafiği", font=16)
label.place(relx=0.03, rely=0.1)
label2 = tk.Label(form, text="Toplam Vaka Sayısı Grafiği", font=16)
label2.place(relx=0.03, rely=0.2)
label3 = tk.Label(form, text="Toplam Aktif Vaka Sayısı Grafiği", font=16)
label3.place(relx=0.03, rely=0.4)
label4 = tk.Label(form, text="Toplam İyileşen Hasta Sayısı Grafiği", font=16)
label4.place(relx=0.03, rely=0.3)

button = tk.Button(form, text="Grafik çiz",font=10, command=ciz.date_deaths)
button.place(relx=0.35, rely=0.1, width=90)
button2 = tk.Button(form, text="Grafik çiz",font=10, command=ciz.date_confirmed)
button2.place(relx=0.35, rely=0.2, width=90)
button3 = tk.Button(form, text="Grafik çiz",font=10, command=ciz.date_active)
button3.place(relx=0.35, rely=0.4, width=90)
button4 = tk.Button(form, text="Grafik çiz",font=10, command=ciz.date_recovered)
button4.place(relx=0.35, rely=0.3, width=90)
button6 = tk.Button(form, text="Seçilen Ülke için Yüzdelik Dilim Oluştur",font=10,command=ciz.pie)
button6.place(relx=0.55, rely=0.38, width=300)
button7 = tk.Button(form, text="Dünya için Yüzdelik Dilim Oluştur",font=10,command=ciz.pieworld)
button7.place(relx=0.55, rely=0.47, width=300)

label20 = tk.Label(form,text="_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
label20.place(relx=0, rely=0.53)
l1 = tk.Label(form, text="Vefat Sayısı",fg="green",font= 10)
l1.place(relx=0.465, rely=0.75)
l2 = tk.Label(form, text="Vaka Sayısı",fg="green",font=10)
l2.place(relx=0.465, rely=0.82)
l3 = tk.Label(form, text="İyileşen Hasta Sayısı",fg="green",font=10)
l3.place(relx=0.465, rely=0.9)
l4=tk.Label(form,text="GÜNLÜK",fg="green",font=16)
l4.place(relx=0.65,rely=0.68)
l5=tk.Label(form,text="TOPLAM",fg="green",font=16)
l5.place(relx=0.8,rely=0.68)

e1 = tk.Entry(form)
e1.place(relx=0.65, rely=0.75, width=80)
e2 = tk.Entry(form)
e2.place(relx=0.65, rely=0.82, width=80)
e3 = tk.Entry(form)
e3.place(relx=0.65, rely=0.9, width=80)
e4=tk.Entry(form)
e4.place(relx=0.8, rely=0.75, width=80)
e5=tk.Entry(form)
e5.place(relx=0.8, rely=0.82, width=80)
e6=tk.Entry(form)
e6.place(relx=0.8, rely=0.9, width=80)





class Tablo():
    def tConfirmed(self):

        f5 = requests.get("https://api.covid19api.com/total/country/" + combobox22.get() +"?from="+date[0]+"&to="+combobox23.get())
        d5 = f5.json()
        f55 = requests.get("https://api.covid19api.com/total/country/" + combobox22.get() + "?from=" + combobox23.get() + "&to=" + date[len(date)-1])
        d55 = f55.json()

        e1.delete(0, 10)
        e2.delete(0, 10)
        e3.delete(0, 10)
        e4.delete(0, 10)
        e5.delete(0,10)
        e6.delete(0, 10)




        if combobox23.get() == date[0]:
            e1.insert(0, d55[0]["Deaths"])
            e2.insert(0, d55[0]["Confirmed"])
            e3.insert(0, d55[0]["Recovered"])
            e4.insert(0, d55[0]["Deaths"])
            e5.insert(0, d55[0]["Confirmed"])
            e6.insert(0, d55[0]["Recovered"])
            e1.config(font=70)
            e2.config(font=70)
            e3.config(font=70)
            e4.config(font=70)
            e5.config(font=70)
            e6.config(font=70)

        else:
            e1.insert(0, d5[len(d5) - 1]["Deaths"] - d5[len(d5) - 2]["Deaths"])
            e2.insert(0, d5[len(d5) - 1]["Confirmed"] - d5[len(d5) - 2]["Confirmed"])
            e3.insert(0, d5[len(d5) - 1]["Recovered"] - d5[len(d5) - 2]["Recovered"])

            e4.insert(0, d5[len(d5)-1]["Deaths"])
            e5.insert(0, d5[len(d5)-1]["Confirmed"])
            e6.insert(0, d5[len(d5)-1]["Recovered"])
            e1.config(font=70)
            e2.config(font=70)
            e3.config(font=70)
            e4.config(font=70)
            e5.config(font=70)
            e6.config(font=70)


class Gunluk:
    def gConfirmed1(self):
        sil()
        veri.date1()
        veri.confirmed1()
        if len(combobox.get()) == 0:
            messageslug = messagebox.showinfo(title="Ülke seçmediniz", message="Lütfen bir ülke seçiniz.")

        elif len(date) == 0:
            messagedate = messagebox.showinfo(title="Hata", message="Seçilen ülke ile ilgili veri bulunamadı. Lütfen başka bir ülke seçiniz.")
        else:
            plt.bar(date,gConfirmed, label="Vaka", color="orange")
            plt.title(combobox.get().upper())
            plt.xlabel("Tarih")
            plt.ylabel("Vaka Sayısı")
            plt.legend()
            plt.xticks(range(0, len(date), 20))
            plt.xticks(rotation=20)
            plt.show()

    def gRecovered1(self):
        sil()
        veri.date1()
        veri.recovered1()
        if len(combobox.get()) == 0:
            messageslug = messagebox.showinfo(title="Ülke seçmediniz", message="Lütfen bir ülke seçiniz.")

        elif len(date) == 0:
            messagedate = messagebox.showinfo(title="Hata", message="Seçilen ülke ile ilgili veri bulunamadı. Lütfen başka bir ülke seçiniz.")

        else:
            plt.bar(date,gRecovered, label="İyileşen", color="green")
            plt.title(combobox.get().upper())
            plt.xlabel("Tarih")
            plt.ylabel("İyileşen Hasta Sayısı")
            plt.legend()
            plt.xticks(range(0, len(date), 20))
            plt.xticks(rotation=20)
            plt.show()

    def gDeaths1(self):
        sil()
        veri.date1()
        veri.deaths1()
        if len(combobox.get()) == 0:
            messageslug = messagebox.showinfo(title="Ülke seçmediniz", message="Lütfen bir ülke seçiniz.")

        elif len(date) == 0:
            messagedate = messagebox.showinfo(title="Hata", message="Seçilen ülke ile ilgili veri bulunamadı. Lütfen başka bir ülke seçiniz.")
        else:
            plt.bar(date,gDeaths, label="Vefat", color="red")
            plt.title(combobox.get().upper())
            plt.xlabel("Tarih")
            plt.ylabel("Vefat Sayısı")
            plt.legend()
            plt.xticks(range(0, len(date), 20))
            plt.xticks(rotation=20)
            plt.show()


gunluk=Gunluk()





tablo=Tablo()

lbltablo=tk.Label(text="TABLO",fg="green",font=("BOLD", 18))
lbltablo.place(relx=0.72,rely=0.59)
def msgwar():
    messagewar = messagebox.showinfo(title="ÖNEMLİ BİLGİLENDİRME",message="Tablo oluşturmak için ilk olarak ülke seçip onaylayın, daha sonrasında tarih seçip onaylayın. Bu işlemlerden sonra yandaki tabloda veriler oluşacaktır. Ülke seçip onaylamadan tarih seçemezsiniz çünkü tarihler, ülkelere göre değişebildiği için ilk önce ülke seçip onaylamalısınız. Aksi takdirde ülke seçip onaylamazsanız tarihler zaten oluşmayacaktır. \nNot : Ülke veya tarih değiştirdiğinizde de onaylamayı unutmayınız.")

buttoninfo=tk.Button(form,text=" Tablo Nasıl Oluşturulur ? ",font=10, command=msgwar)
buttoninfo.place(relx=0.02,rely=0.59, width=200)

combobox22 = Combobox(form, values=slug, font=10,width=15)
combobox22.place(relx=0.12, rely=0.75)

button22 = tk.Button(form, text="Onayla", font=10, command=veri.appenddate)
button22.place(relx=0.3, rely=0.742,width=70)

button23 = tk.Button(form, text="Onayla",font=10, command=tablo.tConfirmed)
button23.place(relx=0.3, rely=0.892,width=70)

lbl1=tk.Label(form,text="Ülke Seç :",font=10)
lbl1.place(relx=0.01,rely=0.75)
lbl2=tk.Label(form,text="Tarih Seç :",font=10)
lbl2.place(relx=0.01,rely=0.9)

def tabloworld():

    f10 = requests.get(dunya)
    d10 = f10.json()
    e1.delete(0, 10)
    e2.delete(0, 10)
    e3.delete(0, 10)
    e4.delete(0, 10)
    e5.delete(0, 10)
    e6.delete(0, 10)
    e4.insert(0,d10["TotalDeaths"])
    e5.insert(0,d10["TotalConfirmed"])
    e6.insert(0,d10["TotalRecovered"])
    e4.config(font=70)
    e5.config(font=70)
    e6.config(font=70)



buttonworld=tk.Button(form,text="Dünya İçin Tablo Oluştur",command=tabloworld,font=10)
buttonworld.place(relx=0.4,rely=0.59)

labelconfirmed=tk.Label(form,text="Günlük Vaka Sayısı İstatistği", font=16)
labelconfirmed.place(relx=0.5,rely=0.2)
labeldeaths=tk.Label(form,text="Günlük Vefat Sayısı İstatistği", font=16)
labeldeaths.place(relx=0.5,rely=0.1)
labelrecovered=tk.Label(form,text="Günlük İyileşen Hasta Sayısı İstatistği", font=16)
labelrecovered.place(relx=0.5,rely=0.3)

buttonconfirmed=tk.Button(form,text="İstatistik Oluştur ",command=gunluk.gConfirmed1,font=16)
buttonconfirmed.place(relx=0.8, rely=0.2)
buttondeaths=tk.Button(form,text="İstatistik Oluştur ",command=gunluk.gDeaths1,font=16)
buttondeaths.place(relx=0.8, rely=0.1)
buttonrecovered=tk.Button(form,text="İstatistik Oluştur",command=gunluk.gRecovered1,font=16)
buttonrecovered.place(relx=0.8, rely=0.3)
form.mainloop()

