import random
from tkinter import *
import random
import time
from tkinter import filedialog,messagebox
import requests

#Functions

#Function To Reset
def to_reset():
    textarea.delete(1.0,END)

    #Setting All values of the entry field to be zero
    e_babycornchilli.set('0')
    e_chilollipop.set('0')
    e_chikurkure.set('0')
    e_americancorn.set('0')
    e_paneertikka.set('0')
    e_chisoup.set('0')
    e_fishfinger.set('0')
    e_frenchfry.set('0')
    e_omlette.set('0')

    e_chillymushroom.set('0')
    e_chibiriyani.set('0')
    e_chimasala.set('0')
    e_prawanmalai.set('0')
    e_chillypaneer.set('0')
    e_vegbiriyani.set('0')
    e_butternan.set('0')
    e_eggcurry.set('0')
    e_mixveg.set('0')

    e_chocolateshake.set('0')
    e_jaljeerapani.set('0')
    e_oreoshake.set('0')
    e_masalacola.set('0')
    e_kalakhatta.set('0')
    e_gulabjamun.set('0')
    e_rassgolla.set('0')
    e_rassmalaii.set('0')
    e_jalebi.set('0')

    # To disable the entry fields
    text_Baby_Corn_Chilli.config(state=DISABLED)
    text_Chicken_lollipop.config(state=DISABLED)
    text_Chicken_Kurkure.config(state=DISABLED)
    text_americancorn.config(state=DISABLED)
    text_PaneerTikka.config(state=DISABLED)
    text_Chicken_Soup.config(state=DISABLED)
    text_Fishfinger.config(state=DISABLED)
    text_French_Fry.config(state=DISABLED)
    text_omlette.config(state=DISABLED)

    textchillymushroom.config(state=DISABLED)
    textchickenbiriyani.config(state=DISABLED)
    textchickenmasala.config(state=DISABLED)
    textprawanmalai.config(state=DISABLED)
    textchillypaneer.config(state=DISABLED)
    textvegbiriyani.config(state=DISABLED)
    textbutternan.config(state=DISABLED)
    texteggcurry.config(state=DISABLED)
    textmixveg.config(state=DISABLED)

    text_chocolateshake.config(state=DISABLED)
    text_jaljeerapani.config(state=DISABLED)
    text_oreoshake.config(state=DISABLED)
    text_masalacola.config(state=DISABLED)
    text_kalakhatta.config(state=DISABLED)
    text_gulabjamun.config(state=DISABLED)
    text_rassgolla.config(state=DISABLED)
    text_rassmalaii.config(state=DISABLED)
    text_jalebi.config(state=DISABLED)

    #Unchecking the check box by setting them to 0
    var1.set('0')
    var2.set('0')
    var3.set('0')
    var4.set('0')
    var5.set('0')
    var6.set('0')
    var7.set('0')
    var8.set('0')
    var9.set('0')
    var10.set('0')
    var11.set('0')
    var12.set('0')
    var13.set('0')
    var14.set('0')
    var15.set('0')
    var16.set('0')
    var17.set('0')
    var18.set('0')
    var19.set('0')
    var20.set('0')
    var21.set('0')
    var22.set('0')
    var23.set('0')
    var24.set('0')
    var25.set('0')
    var26.set('0')
    var27.set('0')

    # Making The Entry Field 0 when all are reset
    costofstarter.set('')
    costofmaincourse.set('')
    costofdrinks.set('')
    e_subtotal.set('')
    e_gst.set('')
    e_totalcost.set('')


def to_send():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror("Send Error","Hotel Bill Not Found")
    else:
        def sendmessage():
            message = textarea.get(1.0, END)
            number = mobilenumber_entry.get()
            url = "https://www.fast2sms.com/dev/bulkV2"
            querystring = {"authorization": "QbM54lpj8n7FaxCgw6iDNRhHYdoeyrPkKGZEvOscJWI9AT0ufUuyAU1p0Mz96ngGiHaBWqL2FJlIrT8v", "message": message, "language": "english",
                           "route": "q", "numbers": number}
            headers = {
                'cache-control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)
            dic = response.json()
            result = dic.get('return')
            if result == True:
                messagebox.showinfo('Send Successfully', 'Message sent succesfully')

            else:
                messagebox.showerror('Error', 'Something went wrong')

        app=Toplevel()
        app.geometry("500x700+40+40")
        app.title("SEND BILL")
        app.config(bg="aquamarine")

        #Adding The Title Bar Icon
        send_icon=PhotoImage(file="sendicon.png")
        app.iconphoto(False,send_icon)

        #Adding The photo
        p3=PhotoImage(file="logo-3.png")
        sendimage=Label(app,image=p3)
        sendimage.pack()

        #Adding The label for the text
        mobile_numberlabel=Label(app,text="CONTACT NUMBER",font=("Times New Roman",22,"bold","underline"),fg="black",bg="aquamarine")
        mobile_numberlabel.pack(pady=35)

        #Adding an entry field for the contact number
        mobilenumber_entry=Entry(app,font=("Times New Roman",20,"bold"),fg="black",width=30,bd=4,relief=SUNKEN)
        mobilenumber_entry.pack()

        #Adding Label for Bill Details
        billdetails=Label(app,text="Bill Details",font=("Times New Roman",22,"bold","underline"),fg="black",bg="aquamarine")
        billdetails.pack(pady=15)

        #Adding Textarea for the reciept in the toplevel
        textreciept=Text(app,font=("Times New Roman",13,"bold"),bd=4,width=35,height=8,relief=SUNKEN)
        textreciept.pack()
        textreciept.delete(1.0,END)
        y=random.randint(100,20000)
        hotelbill="Bill No:-"+str(y)
        todaydate=time.strftime("%d/%m/%Y")
        textreciept.insert(END,"RK HOTELS"+"   "+hotelbill+"   "+todaydate+"\n\n")
        textreciept.insert(END,"***********************************\n")

        if costofstarter.get()!='Rs0':
            textreciept.insert(END,f"Price of Starter:\t\t\tRs {priceofstarter}\n\n")

        if costofmaincourse.get()!="Rs0":
            textreciept.insert(END,f"Price Of Main Course:\t\t\tRs {priceofmaincourse}\n\n")

        if costofdrinks.get()!="Rs0":
            textreciept.insert(END,f"Price of Drinks & Sweets:\t\t\tRs {priceofdrinksandsweets}\n\n")

        textreciept.insert(END,f"Subtotal:\t\t\tRs {subtotal}\n\n")
        textreciept.insert(END,f"GST:\t\t\tRs {100}\n\n")
        textreciept.insert(END,f"Total Price:\t\t\tRs {subtotal+100}\n\n")
        textreciept.insert(END,"***********************************\n")

        #Adding A send button
        sendbutton=Button(app,text="SEND",font=("Times New Roman",18,"bold"),bg="white",fg="black",bd=5,command=sendmessage)
        sendbutton.pack(pady=8)

        app.mainloop()

def to_save():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror("Save Error","Hotel Bill Not Found")
    else:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if url == None:
            pass
        else:

            bill_data = textarea.get(1.0, END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information', 'Your Bill Is Succesfully Saved')

def get_reciept():
    global billnumber,date
    if costofstarter.get()!='' or costofmaincourse.get()!='' or costofdrinks.get()!='':
        textarea.delete(1.0,END)
        x=random.randint(100,15000)
        billnumber="Bill No:-"+str(x)
        date=time.strftime("%d/%m/%Y")#Getting the time and writing in the normal date and time format
        textarea.insert(END,"RK HOTELS"+"       "+billnumber+"      "+date+"\n")
        textarea.insert(END,"****************************************\n")
        textarea.insert(END,"Items:\t\t Cost Of Items (in Rs)\n")
        textarea.insert(END,"****************************************\n")

        # Receipt For Starters
        if e_babycornchilli.get()!="0":
            textarea.insert(END,f"BabyCorn Chilli\t\t\t{int(e_babycornchilli.get())*150}\n\n")
        if e_chilollipop.get()!="0":
            textarea.insert(END,f"Chicken Lollipop\t\t\t{int(e_chilollipop.get())*200}\n\n")
        if e_chikurkure.get()!="0":
            textarea.insert(END,f"Chicken Kurkure\t\t\t{int(e_chikurkure.get())*250}\n\n")
        if e_americancorn.get()!="0":
            textarea.insert(END,f"American Corn\t\t\t{int(e_americancorn.get())*100}\n\n")
        if e_paneertikka.get()!="0":
            textarea.insert(END,f"Paneer Tikka\t\t\t{int(e_paneertikka.get())*180}\n\n")
        if e_chisoup.get()!="0":
            textarea.insert(END,f"Chicken Soup\t\t\t{int(e_chisoup.get())*180}\n\n")
        if e_fishfinger.get()!="0":
            textarea.insert(END,f"Fish Finger\t\t\t{int(e_fishfinger.get())*169}\n\n")
        if e_frenchfry.get()!="0":
            textarea.insert(END,f"French Fry\t\t\t{int(e_frenchfry.get())*129}\n\n")
        if e_omlette.get()!="0":
            textarea.insert(END,f"Omlette\t\t\t{int(e_omlette.get())*50}\n\n")

        # Receipt For Maincourses
        if e_chillymushroom.get()!="0":
            textarea.insert(END,f"Chilly Mushroom\t\t\t{int(e_chillymushroom.get())*150}\n\n")
        if e_chibiriyani.get()!="0":
            textarea.insert(END,f"Chicken Biriyani\t\t\t{int(e_chibiriyani.get())*300}\n\n")
        if e_chimasala.get()!="0":
            textarea.insert(END,f"Chicken Masala\t\t\t{int(e_chimasala.get())*180}\n\n")
        if e_prawanmalai.get()!="0":
            textarea.insert(END,f"Prawan Malai\t\t\t{int(e_prawanmalai.get())*180}\n\n")
        if e_chillypaneer.get()!="0":
            textarea.insert(END,f"Chilly Paneer\t\t\t{int(e_chillypaneer.get())*120}\n\n")
        if e_vegbiriyani.get()!="0":
            textarea.insert(END,f"Veg Biriyani\t\t\t{int(e_vegbiriyani.get())*200}\n\n")
        if e_butternan.get()!="0":
            textarea.insert(END,f"Butternan\t\t\t{int(e_butternan.get())*40}\n\n")
        if e_eggcurry.get()!="0":
            textarea.insert(END,f"Egg Curry\t\t\t{int(e_eggcurry.get())*80}\n\n")
        if e_mixveg.get()!="0":
            textarea.insert(END,f"Mix Veg\t\t\t{int(e_mixveg.get())*120}\n\n")

        #Receipt For Drinks & Sweets
        if e_chocolateshake.get()!="0":
            textarea.insert(END,f"Chocolate Shake\t\t\t{int(e_chocolateshake.get())*90}\n\n")
        if e_jaljeerapani.get()!="0":
            textarea.insert(END,f"Jaljeera Pani\t\t\t{int(e_jaljeerapani.get())*30}\n\n")
        if e_oreoshake.get()!="0":
            textarea.insert(END,f"Oreo Shake\t\t\t{int(e_oreoshake.get())*40}\n\n")
        if e_masalacola.get()!="0":
            textarea.insert(END,f"Masala Cola\t\t\t{int(e_masalacola.get())*69}\n\n")
        if e_kalakhatta.get()!="0":
            textarea.insert(END,f"Kala Khatta\t\t\t{int(e_kalakhatta.get())*25}\n\n")
        if e_gulabjamun.get()!="0":
            textarea.insert(END,f"Gulabjamun\t\t\t{int(e_gulabjamun.get())*15}\n\n")
        if e_rassgolla.get()!="0":
            textarea.insert(END,f"Rasgola\t\t\t{int(e_rassgolla.get())*20}\n\n")
        if e_rassmalaii.get()!="0":
            textarea.insert(END,f"Rasmalaii\t\t\t{int(e_rassmalaii.get())*15}\n\n")
        if e_jalebi.get()!="0":
            textarea.insert(END,f"Jalebi\t\t\t{int(e_jalebi.get())*10}\n\n")

        textarea.insert(END,"****************************************\n")
        if costofstarter.get()!='Rs0':
            textarea.insert(END,f"Price of Starter:\t\t\tRs {priceofstarter}\n\n")

        if costofmaincourse.get()!="Rs0":
            textarea.insert(END,f"Price Of Main Course:\t\t\tRs {priceofmaincourse}\n\n")

        if costofdrinks.get()!="Rs0":
            textarea.insert(END,f"Price of Drinks & Sweets:\t\t\tRs {priceofdrinksandsweets}\n\n")

        textarea.insert(END,f"Subtotal:\t\t\tRs {subtotal}\n\n")
        textarea.insert(END,f"GST:\t\t\tRs {100}\n\n")
        textarea.insert(END,f"Total Price:\t\t\tRs {subtotal+100}\n\n")
        textarea.insert(END, "****************************************\n")
    else:
        messagebox.showerror("Reciept Error","No Items are selected.")


#Functions of the buttons

def totalprice():
    global priceofstarter,priceofmaincourse,priceofdrinksandsweets,subtotal
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
            var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or \
            var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
            var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
            var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or \
            var26.get() != 0 or var27.get() != 0:
        item1=int(e_babycornchilli.get())
        item2=int(e_chilollipop.get())
        item3=int(e_chikurkure.get())
        item4=int(e_americancorn.get())
        item5=int(e_paneertikka.get())
        item6=int(e_chisoup.get())
        item7=int(e_fishfinger.get())
        item8=int(e_frenchfry.get())
        item9=int(e_omlette.get())

        item10 =int(e_chillymushroom.get())
        item11=int(e_chibiriyani.get())
        item12=int(e_chimasala.get())
        item13=int(e_prawanmalai.get())
        item14=int(e_chillypaneer.get())
        item15=int(e_vegbiriyani.get())
        item16=int(e_butternan.get())
        item17=int(e_eggcurry.get())
        item18=int(e_mixveg.get())

        item19=int(e_chocolateshake.get())
        item20=int(e_jaljeerapani.get())
        item21=int(e_oreoshake.get())
        item22=int(e_masalacola.get())
        item23=int(e_kalakhatta.get())
        item24=int(e_gulabjamun.get())
        item25=int(e_rassgolla.get())
        item26=int(e_rassmalaii.get())
        item27=int(e_jalebi.get())

        priceofstarter=(item1*150)+(item2*200)+(item3*250)+(item4*100)+(item5*180)+(item6*180)+(item7*169)\
                       +(item8*120)+(item9*50)
        priceofmaincourse=(item10*150)+(item11*300)+(item12*180)+(item13*180)+(item14*120)+(item15*200)+(item16*40)\
                          +(item17*80)+(item18*120)
        priceofdrinksandsweets=(item19*90)+(item20*30)+(item21*40)+(item22*69)+(item23*25)+(item24*15)+(item25*20)\
                               +(item26*15)+(item27*10)

        costofstarter.set("Rs"+" "+str(priceofstarter))
        costofmaincourse.set("Rs"+" "+str(priceofmaincourse))
        costofdrinks.set("Rs"+" "+str(priceofdrinksandsweets))

        subtotal=priceofstarter+priceofmaincourse+priceofdrinksandsweets
        e_subtotal.set("Rs"+" "+str(subtotal))

        e_gst.set("Rs"+" "+"100")

        totalcost=subtotal+100
        e_totalcost.set("Rs"+" "+str(totalcost))
    else:
        messagebox.showerror("Total Cost Error","No Food Items are Selected.")

#Functions for starter

def babycornchilly():
    if var1.get()==1:
        text_Baby_Corn_Chilli.config(state=NORMAL)
        text_Baby_Corn_Chilli.delete(0,END)
        text_Baby_Corn_Chilli.focus()
    else:
        text_Baby_Corn_Chilli.config(state=DISABLED)
        e_babycornchilli.set('0')

def chilollipop():
    if var2.get()==1:
        text_Chicken_lollipop.config(state=NORMAL)
        text_Chicken_lollipop.delete(0,END)
        text_Chicken_lollipop.focus()
    else:
        text_Chicken_lollipop.config(state=DISABLED)
        e_chilollipop.set('0')

def chikurkure():
    if var3.get()==1:
        text_Chicken_Kurkure.config(state=NORMAL)
        text_Chicken_Kurkure.delete(0,END)
        text_Chicken_Kurkure.focus()
    else:
        text_Chicken_Kurkure.config(state=DISABLED)
        e_chikurkure.set('0')

def corn():
    if var4.get()==1:
        text_americancorn.config(state=NORMAL)
        text_americancorn.delete(0,END)
        text_americancorn.focus()
    else:
        text_americancorn.config(state=DISABLED)
        e_americancorn.set('0')

def paneertikka():
    if var5.get()==1:
        text_PaneerTikka.config(state=NORMAL)
        text_PaneerTikka.delete(0,END)
        text_PaneerTikka.focus()
    else:
        text_PaneerTikka.config(state=DISABLED)
        e_paneertikka.set('0')

def chisoup():
    if var6.get()==1:
        text_Chicken_Soup.config(state=NORMAL)
        text_Chicken_Soup.delete(0,END)
        text_Chicken_Soup.focus()
    else:
        text_Chicken_Soup.config(state=DISABLED)
        e_chisoup.set('0')

def fishfinger():
    if var7.get()==1:
        text_Fishfinger.config(state=NORMAL)
        text_Fishfinger.delete(0,END)
        text_Fishfinger.focus()
    else:
        text_Fishfinger.config(state=DISABLED)
        e_fishfinger.set('0')

def frenchfry():
    if var8.get()==1:
        text_French_Fry.config(state=NORMAL)
        text_French_Fry.delete(0,END)
        text_French_Fry.focus()
    else:
        text_French_Fry.config(state=DISABLED)
        e_frenchfry.set('0')

def omlette():
    if var9.get()==1:
        text_omlette.config(state=NORMAL)
        text_omlette.delete(0,END)
        text_omlette.focus()
    else:
        text_omlette.config(state=DISABLED)
        e_omlette.set('0')

#Functions for maincourse

def chillymushroom():
    if var10.get()==1:
        textchillymushroom.config(state=NORMAL)
        textchillymushroom.delete(0,END)
        textchillymushroom.focus()
    else:
        textchillymushroom.config(state=DISABLED)
        e_chillymushroom.set('0')

def chibiriyani():
    if var11.get()==1:
        textchickenbiriyani.config(state=NORMAL)
        textchickenbiriyani.delete(0,END)
        textchickenbiriyani.focus()
    else:
        textchickenbiriyani.config(state=DISABLED)
        e_chibiriyani.set('0')

def chimasala():
    if var12.get()==1:
        textchickenmasala.config(state=NORMAL)
        textchickenmasala.delete(0,END)
        textchickenmasala.focus()
    else:
        textchickenmasala.config(state=DISABLED)
        e_chimasala.set('0')

def prawan():
    if var13.get()==1:
        textprawanmalai.config(state=NORMAL)
        textprawanmalai.delete(0,END)
        textprawanmalai.focus()
    else:
        textprawanmalai.config(state=DISABLED)
        e_prawanmalai.set('0')

def chipaneer():
    if var14.get()==1:
        textchillypaneer.config(state=NORMAL)
        textchillypaneer.delete(0,END)
        textchillypaneer.focus()
    else:
        textchillypaneer.config(state=DISABLED)
        e_chillypaneer.set('0')

def vegbiriyani():
    if var15.get()==1:
        textvegbiriyani.config(state=NORMAL)
        textvegbiriyani.delete(0,END)
        textvegbiriyani.focus()
    else:
        textvegbiriyani.config(state=DISABLED)
        e_vegbiriyani.set('0')

def butternan():
    if var16.get()==1:
        textbutternan.config(state=NORMAL)
        textbutternan.delete(0,END)
        textbutternan.focus()
    else:
        textbutternan.config(state=DISABLED)
        e_butternan.set('0')

def egg():
    if var17.get()==1:
        texteggcurry.config(state=NORMAL)
        texteggcurry.delete(0,END)
        texteggcurry.focus()
    else:
        texteggcurry.config(state=DISABLED)
        e_eggcurry.set('0')

def mixveg():
    if var18.get()==1:
        textmixveg.config(state=NORMAL)
        textmixveg.delete(0,END)
        textmixveg.focus()
    else:
        textmixveg.config(state=DISABLED)
        e_mixveg.set('0')

#Functions for drinks and sweets

def chocolateshake():
    if var19.get()==1:
        text_chocolateshake.config(state=NORMAL)
        text_chocolateshake.delete(0,END)
        text_chocolateshake.focus()
    else:
        text_chocolateshake.config(state=DISABLED)
        e_chocolateshake.set('0')

def jaljeera():
    if var20.get()==1:
        text_jaljeerapani.config(state=NORMAL)
        text_jaljeerapani.delete(0,END)
        text_jaljeerapani.focus()
    else:
        text_jaljeerapani.config(state=DISABLED)
        e_jaljeerapani.set('0')

def oreo():
    if var21.get()==1:
        text_oreoshake.config(state=NORMAL)
        text_oreoshake.delete(0,END)
        text_oreoshake.focus()
    else:
        text_oreoshake.config(state=DISABLED)
        e_oreoshake.set('0')

def masalacola():
    if var22.get()==1:
        text_masalacola.config(state=NORMAL)
        text_masalacola.delete(0,END)
        text_masalacola.focus()
    else:
        text_masalacola.config(state=DISABLED)
        e_masalacola.set('0')

def kalakhatta():
    if var23.get()==1:
        text_kalakhatta.config(state=NORMAL)
        text_kalakhatta.delete(0,END)
        text_kalakhatta.focus()
    else:
        text_kalakhatta.config(state=DISABLED)
        e_kalakhatta.set('0')

def gulab():
    if var24.get()==1:
        text_gulabjamun.config(state=NORMAL)
        text_gulabjamun.delete(0,END)
        text_gulabjamun.focus()
    else:
        text_gulabjamun.config(state=DISABLED)
        e_gulabjamun.set('0')

def rasgola():
    if var25.get()==1:
        text_rassgolla.config(state=NORMAL)
        text_rassgolla.delete(0, END)
        text_rassgolla.focus()
    else:
        text_rassgolla.config(state=DISABLED)
        e_rassgolla.set('0')

def rasmalii():
    if var26.get()==1:
        text_rassmalaii.config(state=NORMAL)
        text_rassmalaii.delete(0, END)
        text_rassmalaii.focus()
    else:
        text_rassmalaii.config(state=DISABLED)
        e_rassmalaii.set('0')

def jalebi():
    if var27.get()==1:
        text_jalebi.config(state=NORMAL)
        text_jalebi.delete(0,END)
        text_jalebi.focus()
    else:
        text_jalebi.config(state=DISABLED)
        e_jalebi.set('0')

root=Tk()
root.title("Restaurant Management System")
root.geometry("1300x700+0+0")
root.config(bg="firebrick4")
p2=PhotoImage(file="icon-1.png")
root.iconphoto(False,p2)

topframe=Frame(root,bd=10,relief=SUNKEN,bg='white')
topframe.pack(side=TOP,pady=12)

labeltitle_frame=Label(topframe,font=("Times New Roman",30,"underline","bold"),
                       text="RESTAURANT MANAGEMENT SYSTEM",width=45,fg="black",bg="white")
labeltitle_frame.grid(row=0,column=0,pady=10)

#frmaes

#Frame containing the menu part
menuframe=Frame(root,bd=9,relief=RIDGE,bg="green")
menuframe.pack(side=LEFT,padx=11)

#Frame containing the price of the foods part
costframe=Frame(menuframe,bd=6,relief=RIDGE)
costframe.pack(side=BOTTOM)

#Frame containing the starter part
starterframe=LabelFrame(menuframe,text="Starter",font=("Times New Roman",20,"bold","underline"),bd=11,relief=RIDGE,fg="green")
starterframe.pack(side=LEFT,padx=10,pady=10)

#Frame containing the maincourse part
maincourseframe=LabelFrame(menuframe,text="Main Course",font=("Times New Roman",20,"bold","underline"),bd=11,relief=RIDGE,fg="green")
maincourseframe.pack(side=LEFT,padx=10,pady=10)

#Frame containing the drinks part
drinksframe=LabelFrame(menuframe,text="Drinks & Sweets",font=("Times New Roman",20,"bold","underline"),bd=11,relief=RIDGE,fg="green")
drinksframe.pack(side=LEFT,padx=10,pady=10)

#Frame containing the rightframe containing calculator & recipet part
rightframe=Frame(root,bd=15,relief=SUNKEN,bg="firebrick4")
rightframe.pack(side=RIGHT)

#Frame containing the recipt part
calculatorframe=LabelFrame(rightframe,bd=6,relief=SUNKEN,bg="firebrick4")
calculatorframe.pack(side=TOP)

#Frame containing the recipt part
recieptframe=Frame(rightframe,bd=2,relief=SUNKEN,bg="firebrick4")
recieptframe.pack(pady=4)

#Frame containing all the buttons
buttonframe=Frame(rightframe,bd=4,relief=SUNKEN,bg="firebrick4")
buttonframe.pack()

#All Varibales
var1=IntVar()#Method of declaring integer type variable in Tkinter
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()

var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()

var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
e_mobileno=IntVar()

e_babycornchilli=StringVar()
e_chilollipop=StringVar()
e_chikurkure=StringVar()
e_americancorn=StringVar()
e_paneertikka=StringVar()
e_chisoup=StringVar()
e_fishfinger=StringVar()
e_frenchfry=StringVar()
e_omlette=StringVar()

e_chillymushroom=StringVar()
e_chibiriyani=StringVar()
e_chimasala=StringVar()
e_prawanmalai=StringVar()
e_chillypaneer=StringVar()
e_vegbiriyani=StringVar()
e_butternan=StringVar()
e_eggcurry=StringVar()
e_mixveg=StringVar()

e_chocolateshake=StringVar()
e_jaljeerapani=StringVar()
e_oreoshake=StringVar()
e_masalacola=StringVar()
e_kalakhatta=StringVar()
e_gulabjamun=StringVar()
e_rassgolla=StringVar()
e_rassmalaii=StringVar()
e_jalebi=StringVar()

costofstarter=StringVar()
costofmaincourse=StringVar()
costofdrinks=StringVar()
e_subtotal=StringVar()
e_gst=StringVar()
e_totalcost=StringVar()

#Setting the values of quantity for every item

e_babycornchilli.set('0')
e_chilollipop.set('0')
e_chikurkure.set('0')
e_americancorn.set('0')
e_paneertikka.set('0')
e_chisoup.set('0')
e_fishfinger.set('0')
e_frenchfry.set('0')
e_omlette.set('0')

e_chillymushroom.set('0')
e_chibiriyani.set('0')
e_chimasala.set('0')
e_prawanmalai.set('0')
e_chillypaneer.set('0')
e_vegbiriyani.set('0')
e_butternan.set('0')
e_eggcurry.set('0')
e_mixveg.set('0')

e_chocolateshake.set('0')
e_jaljeerapani.set('0')
e_oreoshake.set('0')
e_masalacola.set('0')
e_kalakhatta.set('0')
e_gulabjamun.set('0')
e_rassgolla.set('0')
e_rassmalaii.set('0')
e_jalebi.set('0')

#Adding Foods for first Starter frame

Baby_Corn_Chilli=Checkbutton(starterframe,text="BabyCorn Chilly",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var1,command=babycornchilly)
Baby_Corn_Chilli.grid(row=0,column=0,sticky=W)

Chicken_lollipop=Checkbutton(starterframe,text="Chicken Lollipop",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var2,command=chilollipop)
Chicken_lollipop.grid(row=1,column=0,sticky=W)

Chicken_Kurkure=Checkbutton(starterframe,text="Chicken Kurkure",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var3,command=chikurkure)
Chicken_Kurkure.grid(row=2,column=0,sticky=W)

American_Corn=Checkbutton(starterframe,text="American Corn",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var4,command=corn)
American_Corn.grid(row=3,column=0,sticky=W)

PaneerTikka=Checkbutton(starterframe,text="Paneer Tikka",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var5,command=paneertikka)
PaneerTikka.grid(row=4,column=0,sticky=W)

Chicken_Soup=Checkbutton(starterframe,text="Chicken Soup",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var6,command=chisoup)
Chicken_Soup.grid(row=5,column=0,sticky=W)

Fishfinger=Checkbutton(starterframe,text="Fish Finger",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var7,command=fishfinger)
Fishfinger.grid(row=6,column=0,sticky=W)

French_Fry=Checkbutton(starterframe,text="French Fry",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var8,command=frenchfry)
French_Fry.grid(row=7,column=0,sticky=W)

omlete=Checkbutton(starterframe,text="Omlette",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var9,command=omlette)
omlete.grid(row=8,column=0,sticky=W)

#STARTER

text_Baby_Corn_Chilli=Entry(starterframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_babycornchilli)
text_Baby_Corn_Chilli.grid(row=0,column=1)

text_Chicken_lollipop=Entry(starterframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_chilollipop)
text_Chicken_lollipop.grid(row=1,column=1)

text_Chicken_Kurkure=Entry(starterframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_chikurkure)
text_Chicken_Kurkure.grid(row=2,column=1)

text_americancorn=Entry(starterframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_americancorn)
text_americancorn.grid(row=3,column=1)

text_PaneerTikka=Entry(starterframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_paneertikka)
text_PaneerTikka.grid(row=4,column=1)

text_Chicken_Soup=Entry(starterframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_chisoup)
text_Chicken_Soup.grid(row=5,column=1)

text_Fishfinger=Entry(starterframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_fishfinger)
text_Fishfinger.grid(row=6,column=1)

text_French_Fry=Entry(starterframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_frenchfry)
text_French_Fry.grid(row=7,column=1)

text_omlette=Entry(starterframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_omlette)
text_omlette.grid(row=8,column=1)

#Add foods for Maincourse

chillymushroom=Checkbutton(maincourseframe,text="Chilly Mushroom",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var10,command=chillymushroom)
chillymushroom.grid(row=0,column=0,sticky=W)

Chicken_Biriyani=Checkbutton(maincourseframe,text="Chicken Biriyani",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var11,command=chibiriyani)
Chicken_Biriyani.grid(row=1,column=0,sticky=W)

chickenmasala=Checkbutton(maincourseframe,text="Chicken Masala",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var12,command=chimasala)
chickenmasala.grid(row=2,column=0,sticky=W)

Prawan_Malai=Checkbutton(maincourseframe,text="Prawan Malai",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var13,command=prawan)
Prawan_Malai.grid(row=3,column=0,sticky=W)

paneer=Checkbutton(maincourseframe,text="Chilly Paneer",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var14,command=chipaneer)
paneer.grid(row=4,column=0,sticky=W)

Veg_Biriyani=Checkbutton(maincourseframe,text="Veg Biriyani",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var15,command=vegbiriyani)
Veg_Biriyani.grid(row=5,column=0,sticky=W)

Butternan=Checkbutton(maincourseframe,text="Butter Nan",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var16,command=butternan)
Butternan.grid(row=6,column=0,sticky=W)

eggcurry=Checkbutton(maincourseframe,text="Egg Curry",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var17,command=egg)
eggcurry.grid(row=7,column=0,sticky=W)

mixveg=Checkbutton(maincourseframe,text="Mix Veg",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var18,command=mixveg)
mixveg.grid(row=8,column=0,sticky=W)

#Adding text fields for maincourse frame

# text_Chicken_lollipop=Entry(starterframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=7,textvariable=e_chilollipop)
# text_Chicken_lollipop.grid(row=1,column=1)
textchillymushroom=Entry(maincourseframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_chillymushroom)
textchillymushroom.grid(row=0,column=1)

textchickenbiriyani=Entry(maincourseframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_chibiriyani)
textchickenbiriyani.grid(row=1,column=1)

textchickenmasala=Entry(maincourseframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_chimasala)
textchickenmasala.grid(row=2,column=1)

textprawanmalai=Entry(maincourseframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_prawanmalai)
textprawanmalai.grid(row=3,column=1)

textchillypaneer=Entry(maincourseframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_chillypaneer)
textchillypaneer.grid(row=4,column=1)

textvegbiriyani=Entry(maincourseframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_vegbiriyani)
textvegbiriyani.grid(row=5,column=1)

textbutternan=Entry(maincourseframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_butternan)
textbutternan.grid(row=6,column=1)

texteggcurry=Entry(maincourseframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_eggcurry)
texteggcurry.grid(row=7,column=1)

textmixveg=Entry(maincourseframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,state=DISABLED,bd=7,width=6,textvariable=e_mixveg)
textmixveg.grid(row=8,column=1)

#Adding Foods For Drinks And Sweets
chocolateshake=Checkbutton(drinksframe,text="Chocolate Shake",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var19,command=chocolateshake)
chocolateshake.grid(row=0,column=0,sticky=W)

jaljeerapani=Checkbutton(drinksframe,text="Jal Jeera Pani",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var20,command=jaljeera)
jaljeerapani.grid(row=1,column=0,sticky=W)

oreoshake=Checkbutton(drinksframe,text="OREO Shake",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var21,command=oreo)
oreoshake.grid(row=2,column=0,sticky=W)

masalacola=Checkbutton(drinksframe,text="Masala Cola",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var22,command=masalacola)
masalacola.grid(row=3,column=0,sticky=W)

kalakhata=Checkbutton(drinksframe,text="Kala Khatta",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var23,command=kalakhatta)
kalakhata.grid(row=4,column=0,sticky=W)

gulabjamun=Checkbutton(drinksframe,text="Gulabjamun",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var24,command=gulab)
gulabjamun.grid(row=5,column=0,sticky=W)

rassgolla=Checkbutton(drinksframe,text="Ras Golla",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var25,command=rasgola)
rassgolla.grid(row=6,column=0,sticky=W)

rasmalaii=Checkbutton(drinksframe,text="Rasmalii",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var26,command=rasmalii)
rasmalaii.grid(row=7,column=0,sticky=W)

jalebi=Checkbutton(drinksframe,text="Jalebi",font=("Times New Roman",17,"bold"),onvalue=1,offvalue=0,variable=var27,command=jalebi)
jalebi.grid(row=8,column=0,sticky=W)

#Adding Textfields for drinks

text_chocolateshake=Entry(drinksframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,bd=7,width=6,textvariable=e_chocolateshake)
text_chocolateshake.grid(row=0,column=1)

text_jaljeerapani=Entry(drinksframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,bd=7,width=6,textvariable=e_jaljeerapani)
text_jaljeerapani.grid(row=1,column=1)

text_oreoshake=Entry(drinksframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,bd=7,width=6,textvariable=e_oreoshake)
text_oreoshake.grid(row=2,column=1)

text_masalacola=Entry(drinksframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,bd=7,width=6,textvariable=e_masalacola)
text_masalacola.grid(row=3,column=1)

text_kalakhatta=Entry(drinksframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,bd=7,width=6,textvariable=e_kalakhatta)
text_kalakhatta.grid(row=4,column=1)

text_gulabjamun=Entry(drinksframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,bd=7,width=6,textvariable=e_gulabjamun)
text_gulabjamun.grid(row=5,column=1)

text_rassgolla=Entry(drinksframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,bd=7,width=6,textvariable=e_rassgolla)
text_rassgolla.grid(row=6,column=1)

text_rassmalaii=Entry(drinksframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,bd=7,width=6,textvariable=e_rassmalaii)
text_rassmalaii.grid(row=7,column=1)

text_jalebi=Entry(drinksframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,bd=7,width=6,textvariable=e_jalebi)
text_jalebi.grid(row=8,column=1)

#costoflabels & entryfields

labelcostofstarter=Label(costframe,text="Price Of Starter",relief=RAISED,font=("Times New Roman",17,"bold","underline"),bg="firebrick4",fg="yellow")
labelcostofstarter.grid(row=0,column=0,padx=41)

textstarter=Entry(costframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,bd=6,width=14,state="readonly",textvariable=costofstarter)
textstarter.grid(row=0,column=1,padx=41)

labelcostofdrinks=Label(costframe,text="Price Of Maincourse",font=("Times New Roman",17,"bold","underline"),bg="firebrick4",fg="yellow",relief=RAISED)
labelcostofdrinks.grid(row=1,column=0,padx=41)

textdrinks=Entry(costframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,bd=6,width=14,state="readonly",textvariable=costofmaincourse)
textdrinks.grid(row=1,column=1,padx=41)

labelcostofmaincourse=Label(costframe,text="Price Of Drinks",font=("Times New Roman",17,"bold","underline"),bg="firebrick4",fg="yellow",relief=RAISED)
labelcostofmaincourse.grid(row=2,column=0,padx=41)

textmaincourse=Entry(costframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,bd=6,width=14,state="readonly",textvariable=costofdrinks)
textmaincourse.grid(row=2,column=1,padx=41)

labelsubtotal=Label(costframe,text="SubTotal",font=("Times New Roman",17,"bold","underline"),relief=RAISED,bg="firebrick4",fg="yellow")
labelsubtotal.grid(row=0,column=2,padx=41)

textsubtotal=Entry(costframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,bd=6,width=14,state="readonly",textvariable=e_subtotal)
textsubtotal.grid(row=0,column=3,padx=41)

labelGST=Label(costframe,text="GST",font=("Times New Roman",17,"bold","underline"),relief=RAISED,bg="firebrick4",fg="yellow")
labelGST.grid(row=1,column=2,padx=41)

textsubtotal=Entry(costframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,bd=6,width=14,state="readonly",textvariable=e_gst)
textsubtotal.grid(row=1,column=3,padx=41)

labeltotalcost=Label(costframe,text="Total Price",font=("Times New Roman",17,"bold","underline"),relief=RAISED,bg="firebrick4",fg="yellow")
labeltotalcost.grid(row=2,column=2,padx=41)

texttotalcost=Entry(costframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,bd=6,width=14,state="readonly",textvariable=e_totalcost)
texttotalcost.grid(row=2,column=3,padx=41)

#Buttons

totalbutton=Button(buttonframe,text="Total",font=("Times New Roman",17,"bold","underline"),fg="yellow",bg="firebrick4",bd=4,command=totalprice)
totalbutton.grid(row=0,column=0)

reciept=Button(buttonframe,text="Reciept",font=("Times New Roman",17,"bold","underline"),fg="yellow",bg="firebrick4",bd=4,command=get_reciept)
reciept.grid(row=0,column=1,padx=3,pady=3)

send=Button(buttonframe,text="Send",font=("Times New Roman",17,"bold","underline"),fg="yellow",bg="firebrick4",bd=4,command=to_send)
send.grid(row=0,column=2,padx=3,pady=3)

save=Button(buttonframe,text="Save",font=("Times New Roman",17,"bold","underline"),fg="yellow",bg="firebrick4",bd=4,command=to_save)
save.grid(row=0,column=3,padx=3,pady=3)

reset=Button(buttonframe,text="Reset",font=("Times New Roman",17,"bold","underline"),fg="yellow",bg="firebrick4",bd=4,command=to_reset)
reset.grid(row=0,column=4,padx=3,pady=3)

#Adding The Textarea

textarea=Text(recieptframe,font=("Times New Roman",15,"bold"),relief=SUNKEN,width=40,height=11)
textarea.grid(row=0,column=0)

#Adding The Calculator

operator=''
def buttonClick(numbers): #9
    global operator
    operator=operator+numbers
    entryofcalculator.delete(0,END)
    entryofcalculator.insert(END,operator)

def clear():
    global operator
    operator=''
    entryofcalculator.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    entryofcalculator.delete(0,END)
    entryofcalculator.insert(0,result)
    operator=''

entryofcalculator=Entry(calculatorframe,font=("Times New Roman",17,"bold"),relief=SUNKEN,width=33,bd=3)
entryofcalculator.grid(row=0,column=0,columnspan=4)

#Making The Buttons of the calculator

b1=Button(calculatorframe,text="1",font=("Times New Roman",17,"bold"),bd=6,
          fg="white",bg="black",width=6,command=lambda:buttonClick('1'))
b1.grid(row=1,column=0)

b2=Button(calculatorframe,text="2",font=("Times New Roman",17,"bold"),bd=6,
          fg="white",bg="black",width=6,command=lambda:buttonClick('2'))
b2.grid(row=1,column=1)

b3=Button(calculatorframe,text="3",font=("Times New Roman",17,"bold"),bd=6,
          fg="white",bg="black",width=6,command=lambda:buttonClick('3'))
b3.grid(row=1,column=2)

plusbutton=Button(calculatorframe,text="+",font=("Times New Roman",17,"bold"),bd=6,
                  fg="white",bg="black",width=6,command=lambda:buttonClick('+'))
plusbutton.grid(row=1,column=3)

b4=Button(calculatorframe,text="4",font=("Times New Roman",17,"bold"),bd=6,
          fg="white",bg="black",width=6,command=lambda:buttonClick('4'))
b4.grid(row=2,column=0)

b5=Button(calculatorframe,text="5",font=("Times New Roman",17,"bold"),bd=6,
          fg="black",bg="white",width=6,command=lambda:buttonClick('5'))
b5.grid(row=2,column=1)

b6=Button(calculatorframe,text="6",font=("Times New Roman",17,"bold"),bd=6,
          fg="black",bg="white",width=6,command=lambda:buttonClick('6'))
b6.grid(row=2,column=2)

minusbutton=Button(calculatorframe,text="-",font=("Times New Roman",17,"bold"),bd=6,
                   fg="white",bg="black",width=6,command=lambda:buttonClick('-'))
minusbutton.grid(row=2,column=3)

b7=Button(calculatorframe,text="7",font=("Times New Roman",17,"bold"),bd=6,
          fg="white",bg="black",width=6,command=lambda:buttonClick('7'))
b7.grid(row=3,column=0)

b8=Button(calculatorframe,text="8",font=("Times New Roman",17,"bold"),bd=6,
          fg="black",bg="white",width=6,command=lambda:buttonClick('8'))
b8.grid(row=3,column=1)

b9=Button(calculatorframe,text="9",font=("Times New Roman",17,"bold"),bd=6,
          fg="black",bg="white",width=6,command=lambda:buttonClick('9'))
b9.grid(row=3,column=2)

multiplybutton=Button(calculatorframe,text="*",font=("Times New Roman",17,"bold"),bd=6,
                      fg="white",bg="black",width=6,command=lambda:buttonClick('*'))
multiplybutton.grid(row=3,column=3)

ansbutton=Button(calculatorframe,text="Ans",font=("Times New Roman",17,"bold"),bd=6,
                 fg="white",bg="black",width=6,command=answer)
ansbutton.grid(row=4,column=0)

clearbutton=Button(calculatorframe,text="Clear",font=("Times New Roman",17,"bold"),bd=6,
                   fg="white",bg="black",width=6,command=clear)
clearbutton.grid(row=4,column=1)

b0=Button(calculatorframe,text="0",font=("Times New Roman",17,"bold"),bd=6,
          fg="white",bg="black",width=6,command=lambda:buttonClick('0'))
b0.grid(row=4,column=2)

divisonbutton=Button(calculatorframe,text="/",font=("Times New Roman",17,"bold"),bd=6,
                     fg="white",bg="black",width=6,command=lambda:buttonClick('/'))
divisonbutton.grid(row=4,column=3)

root.mainloop()