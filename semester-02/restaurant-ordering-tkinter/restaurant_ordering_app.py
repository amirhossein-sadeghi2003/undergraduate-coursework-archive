from tkinter import *
from tkinter import messagebox
win = Tk()
win.title("Inventory")
win.geometry("700x900+450-100")
win.resizable(False,False)
win.configure(background = "sky blue")

lbl_main = Label(master = win,text = "Main meals",font = ("Tahoma",15),background = "purple",width = 20,relief = "groove",borderwidth = 7)
lbl_main.grid(row = 0,column = 0,padx = 20,pady = 20)

lbl_number_meal = Label(master = win,text = "Number of meals",font = ("Tahoma",15),background = "yellow",relief = "groove",borderwidth = 7)
lbl_number_meal.grid(row = 0,column = 1,padx = 20,pady = 20)

lbl_food1 = Label(master = win,text = "Kubideh kebab",font = ("Tahoma",15),background = "teal")
lbl_food1.grid(row = 1,column = 0,padx = 20,pady = 20)

ent_food1 = Entry(master = win,font = ("Tahoma",15),background = "white")
ent_food1.grid(row = 1,column = 1,padx = 20,pady = 20)

lbl_food2 = Label(master = win,text = "Kebab chicken",font = ("Tahoma",15),background = "teal")
lbl_food2.grid(row = 2,column = 0,padx = 20,pady = 20)

ent_food2 = Entry(master = win,font = ("Tahoma",15),background = "white")
ent_food2.grid(row = 2,column = 1,padx = 20,pady = 20)

lbl_food3 = Label(master = win,text = "Barbecue leaves",font = ("Tahoma",15),background = "teal")
lbl_food3.grid(row = 3,column = 0,padx = 20,pady = 20)

ent_food3 = Entry(master = win,font = ("Tahoma",15),background = "white")
ent_food3.grid(row = 3,column = 1,padx = 20,pady = 20)

lbl_food4 = Label(master = win,text = "Te china",font = ("Tahoma",15),background = "teal")
lbl_food4.grid(row = 4,column = 0,padx = 20,pady = 20)

ent_food4 = Entry(master = win,font = ("Tahoma",15),background = "white")
ent_food4.grid(row = 4,column = 1,padx = 20,pady = 20)

lbl_food5 = Label(master = win,text = "Rice",font = ("Tahoma",15),background = "teal")
lbl_food5.grid(row = 5,column = 0,padx = 20,pady = 20)

ent_food5 = Entry(master = win,font = ("Tahoma",15),background = "white")
ent_food5.grid(row = 5,column = 1,padx = 20,pady =20)

lbl_food6 = Label(master = win,text = "Salad",font = ("Tahoma",15),background = "teal")
lbl_food6.grid(row = 6,column = 0,padx = 20,pady = 20)

ent_food6 = Entry(master = win,font = ("Tahoma",15),background = "white")
ent_food6.grid(row = 6,column = 1,padx = 20,pady = 20)

lbl_Drinks = Label(master = win,text = "Drinks and Salad",font = ("Tahoma",15),background = "purple",width = 20,relief = "groove",borderwidth = 7)
lbl_Drinks.grid(row = 7,column = 0,padx = 20,pady = 20)

lbl_number_meal = Label(master = win,text = "Number of meals",font = ("Tahoma",15),background = "yellow",relief = "groove",borderwidth = 7)
lbl_number_meal.grid(row = 7,column = 1,padx = 20,pady = 20)

lbl_Drink1 = Label(master = win,text = "Dough",font = ("Tahoma",15),background = "teal")
lbl_Drink1.grid(row = 8,column = 0,padx = 20,pady = 20)

ent_Drink1 = Entry(master = win,font = ("Tahoma",15),background = "white")
ent_Drink1.grid(row = 8,column = 1,padx = 20,pady =20)

lbl_Drink2 = Label(master = win,text = "Black soda",font = ("Tahoma",15),background = "teal")
lbl_Drink2.grid(row = 9,column = 0,padx = 20,pady = 20)

ent_Drink2 = Entry(master = win,font = ("Tahoma",15),background = "white")
ent_Drink2.grid(row = 9,column = 1,padx = 20,pady = 20)

lbl_Drink3 = Label(master = win,text = "Orange soda",font = ("Tahoma",15),background = "teal")
lbl_Drink3.grid(row = 10,column = 0,padx = 20,pady = 20)

ent_Drink3 = Entry(master = win,font = ("Tahoma",15),background = "white")
ent_Drink3.grid(row = 10,column = 1,padx = 20,pady = 20)

def btn_registration_pressed(event):
    with open("Food_number","w") as f:
        n_food1 = ent_food1.get()
        ent_food1.delete(0,END)
        f.write("Kubideh kebab: " + n_food1 + "\n")
        n_food2 = ent_food2.get()
        ent_food2.delete(0,END)
        f.write("Kebab chicken: " + n_food2 + "\n")
        n_food3 = ent_food3.get()
        ent_food3.delete(0,END)
        f.write("Barbecue leaves: " + n_food3 + "\n")
        n_food4 = ent_food4.get()
        ent_food4.delete(0,END)
        f.write("Te china: " + n_food4 + "\n")
        n_food5 = ent_food5.get()
        ent_food5.delete(0,END)
        f.write("Rice: " + n_food5 + "\n")
        n_food6 = ent_food6.get()
        ent_food6.delete(0,END)
        f.write("Salad: " + n_food6 + "\n")
        n_Drink1 = ent_Drink1.get()
        ent_Drink1.delete(0,END)
        f.write("Dough: " + n_Drink1 + "\n")
        n_Drink2 = ent_Drink2.get()
        ent_Drink2.delete(0,END)
        f.write("Black soda: " + n_Drink2 + "\n")
        n_Drink3 = ent_Drink3.get()
        ent_Drink3.delete(0,END)
        f.write("Orange soda: " + n_Drink3 + "\n")

btn_registration = Button(master = win,text = "Registration",font = ("Tahoma",15),background ="red")
btn_registration.grid(row = 11,column = 0,padx = 20,pady = 20)
btn_registration.config(bitmap = "questhead",compound = "top",cursor = "plus")
btn_registration.bind("<Button-1>",btn_registration_pressed)


def btn_Start_pressed(event):
    win.destroy()
    Food_list = {}
    with open("Food_number","r") as f:
        for line in f:
            food,number = line.split(": ")
            Food_list[food] = int(number)
    
    window = Tk()
    window.title("Food list")
    window.geometry("800x900+400-100")
    window.resizable(False,False)
    window.configure(background = "sky blue")
    
        

    lbl_main_course = Label(master = window,text = "Main meals",font = ("Tahoma",20),background = "purple",width = 20,relief = "groove",borderwidth = 7)
    lbl_main_course.grid(row = 0 ,column = 0,padx = 20,pady = 20)

    lbl_number = Label(master = window,text = "Number of meals",font = ("Tahoma",15),background = "white",width = 14,relief = "groove",borderwidth = 7)
    lbl_number.grid(row = 0,column = 2,padx = 20,pady = 20)



    lbl_price = Label(master = window,text ="Price",font = ("Tahoma",15),background = "orange",width = 8,relief = "groove",borderwidth = 7)
    lbl_price.grid(row = 0,column = 1,padx = 20,pady = 20)

    food_1 = Label(master = window,text = "Kubideh kebab",font = ("Tahoma",15),background = "teal",width = 12)
    food_1.grid(row = 1,column = 0,padx = 20,pady = 20)
    price_food_1 = Label(master = window,text = "25$",font =("Tahoma",15),background = "green",width = 4)
    price_food_1.grid(row = 1,column = 1)
    number_food_1 = Entry(master = window,background = "white",font =("Tahoma",15),width = 10)
    number_food_1.grid(row = 1,column = 2,padx = 20,pady = 20)


    food_2 = Label(master = window,text = "Kebab chicken",font = ("Tahoma",15),background = "teal",width = 12)
    food_2.grid(row = 2,column = 0,padx =20,pady = 20)
    price_food_2 = Label(master = window,text = "20$",font =("Tahoma",15),background = "green",width = 4)
    price_food_2.grid(row = 2,column = 1,padx = 20,pady = 20)
    number_food_2 = Entry(master = window,background = "white",font =("Tahoma",15),width = 10)
    number_food_2.grid(row = 2,column = 2,padx = 20,pady = 20)


    food_3 = Label(master = window,text = "Barbecue leaves",font = ("Tahoma",15),background = "teal",width = 14)
    food_3.grid(row = 3,column = 0,padx =20,pady = 20)
    price_food_3 = Label(master = window,text = "22$",font =("Tahoma",15),background = "green",width = 4)
    price_food_3.grid(row = 3,column = 1,padx = 20,pady = 20)
    number_food_3 = Entry(master = window,background = "white",font =("Tahoma",15),width = 10)
    number_food_3.grid(row = 3,column = 2,padx = 20,pady = 20)



    food_4 = Label(master = window,text = "Te china",font = ("Tahoma",15),background = "teal",width = 12)
    food_4.grid(row = 4,column = 0,padx =20,pady = 20)
    price_food_4 = Label(master = window,text = "15$",font =("Tahoma",15),background = "green",width = 4)
    price_food_4.grid(row = 4,column = 1,padx = 20,pady = 20)
    number_food_4 = Entry(master = window,background = "white",font =("Tahoma",15),width = 10)
    number_food_4.grid(row = 4,column = 2,padx = 20,pady = 20)



    food_5 = Label(master = window,text = "Rice",font = ("Tahoma",15),background = "teal",width = 14)
    food_5.grid(row = 5,column = 0,padx =20,pady = 20)
    price_food_5 = Label(master = window,text = "7$",font =("Tahoma",15),background = "green",width = 4)
    price_food_5.grid(row = 5,column = 1,padx = 20,pady = 20)
    number_food_5 = Entry(master = window,background = "white",font =("Tahoma",15),width = 10)
    number_food_5.grid(row = 5,column = 2,padx = 20,pady = 20)



    food_6 = Label(master = window,text = "Salad",font = ("Tahoma",15),background = "teal",width = 12)
    food_6.grid(row = 7,column = 0,padx =20,pady = 20)
    price_food_6 = Label(master = window,text = "5$",font =("Tahoma",15),background = "green",width = 4)
    price_food_6.grid(row = 7,column = 1,padx = 20,pady = 20)
    number_food_6 = Entry(master = window,background = "white",font =("Tahoma",15),width = 10)
    number_food_6.grid(row = 7,column = 2,padx = 20,pady = 20)




    lbl_Drinks = Label(master = window,text = "Drinks and Salad",font = ("Tahoma",15),background = "yellow",width = 26,relief = "groove",borderwidth = 7)
    lbl_Drinks.grid(row = 6,column = 0,padx = 20,pady = 20)

    lbl_price_Drinks = Label(master = window,text = "Price",font = ("Tahoma",15),background = "orange",width = 8,relief = "groove",borderwidth = 7)
    lbl_price_Drinks.grid(row = 6,column = 1,padx = 20,pady = 20)

    lbl_number_drinks = Label(master = window,text = "Number",font = ("Tahoma",15),background = "white",width = 14,relief = "groove",borderwidth = 7)
    lbl_number_drinks.grid(row = 6,column = 2,padx = 20,pady = 20)



    Drink_1 = Label(master = window,text = "Dough",font = ("Tahoma",15),background = "teal",width = 12)
    Drink_1.grid(row = 8,column = 0,padx =20,pady = 20)
    price_Drink_1 = Label(master = window,text = "2$",font =("Tahoma",15),background = "green",width = 4)
    price_Drink_1.grid(row = 8,column = 1,padx = 20,pady = 20)
    number_Drink_1 = Entry(master = window,background = "white",font =("Tahoma",15),width = 10)
    number_Drink_1.grid(row = 8,column = 2,padx = 20,pady = 20)



    Drink_2 = Label(master = window,text = "Black soda",font = ("Tahoma",15),background = "teal",width = 12)
    Drink_2.grid(row = 9,column = 0,padx =20,pady = 20)
    price_Drink_2 = Label(master = window,text = "3$",font =("Tahoma",15),background = "green",width = 4)
    price_Drink_2.grid(row = 9,column = 1,padx = 20,pady = 20)
    number_Drink_2 = Entry(master = window,background = "white",font =("Tahoma",15),width = 10)
    number_Drink_2.grid(row = 9,column = 2,padx = 20,pady = 20)



    Drink_3 = Label(master = window,text = "Orange soda",font = ("Tahoma",15),background = "teal",width = 12)
    Drink_3.grid(row = 10,column = 0,padx =20,pady = 20)
    price_Drink_3 = Label(master = window,text = "3$",font =("Tahoma",15),background = "green",width = 4)
    price_Drink_3.grid(row = 10,column = 1,padx = 20,pady = 20)
    number_Drink_3 = Entry(master = window,background = "white",font =("Tahoma",15),width = 10)
    number_Drink_3.grid(row = 10,column = 2,padx = 20,pady = 20)



    btn_phone = Button(master = window,text = "Name / Phone number",font = ("Tahoma",15),background = "green",width = 18,relief = "groove",borderwidth = 10)
    btn_phone.config(width = 220)
    btn_phone.grid(row = 11,column = 0,padx = 1,pady = 20)
    btn_phone.config(bitmap = "questhead",compound = "top",cursor = "plus")

    Food_ordered = {}

    def btn_confirm_pressed(event):
        if messagebox.askquestion("Confirmation","Are you sure?") == "yes":
            n_food1_ordered = number_food_1.get()
            number_food_1.delete(0,END)
            if n_food1_ordered.isdigit():
                if int(n_food1_ordered) > Food_list["Kubideh kebab"]:
                    n_Kubideh = Food_list["Kubideh kebab"]
                    messagebox.showwarning("Insufficient inventory",f"We have {n_Kubideh} Kubideh kebab presses.")
                    Food_ordered["Kubideh kebab"] = "Try again"
                else:         
                    Food_ordered["Kubideh kebab"] = int(n_food1_ordered)
                    Food_list["Kubideh kebab"] -= int(n_food1_ordered)
            else:
                Food_ordered["Kubideh kebab"] = "Try again"

            n_food2_ordered = number_food_2.get()
            number_food_2.delete(0,END)
            if n_food2_ordered.isdigit():
                if int(n_food2_ordered) > Food_list["Kebab chicken"]:
                    n_chicken = Food_list["Kebab chicken"]
                    messagebox.showinfo("Insufficient inventory",f"We have {n_chicken} Kebab chicken presses.")
                    Food_ordered["Kebab chicken"] = "Try again"
                else:    
                    Food_ordered["Kebab chicken"] = int(n_food2_ordered)
                    Food_list["Kebab chicken"] -= int(n_food2_ordered)
            else:
                Food_ordered["Kebab chicken"] = "Try again"        

            n_food3_ordered = number_food_3.get()
            number_food_3.delete(0,END)
            if n_food3_ordered.isdigit():
                if int(n_food3_ordered) > Food_list["Barbecue leaves"]:
                    n_Barbecue = Food_list["Barbecue leaves"]
                    messagebox.showinfo("Insufficient inventory",f"We have {n_Barbecue} Barbecue leaves presses.")
                    Food_ordered["Barbecue leaves"] = "Try again"
                else:
                    Food_ordered["Barbecue leaves"] = int(n_food3_ordered)
                    Food_list["Barbecue leaves"] -= int(n_food3_ordered)
            else:
                Food_ordered["Barbecue leaves"] = "Try again"

            n_food4_ordered = number_food_4.get()
            number_food_4.delete(0,END)
            if n_food4_ordered.isdigit():
                if int(n_food4_ordered) > Food_list["Te china"]:
                    n_Te = Food_list["Te china"]
                    messagebox.showinfo("Insufficient inventory",f"We have {n_Te} Te china presses.")
                    Food_ordered["Te china"] = "Try again"
                else:
                    Food_ordered["Te china"] = int(n_food4_ordered)        
                    Food_list["Te china"] -= int(n_food4_ordered)
            else:
                Food_ordered["Te china"] = "Try again"


            n_food5_ordered = number_food_5.get()
            number_food_5.delete(0,END)
            if n_food5_ordered.isdigit():
                if int(n_food5_ordered) > Food_list["Rice"]:
                    n_Rice = Food_list["Rice"]
                    messagebox.showinfo("Insufficient inventory",f"We have {n_Rice} Rice presses.")
                    Food_ordered["Rice"] = "Try again"
                else:
                    Food_ordered["Rice"] = int(n_food5_ordered)
                    Food_list["Rice"] -= int(n_food5_ordered)
            else:
                Food_ordered["Rice"] = "Try again"


            n_food6_ordered = number_food_6.get()
            number_food_6.delete(0,END)
            if n_food6_ordered.isdigit(): 
                if int(n_food6_ordered) > Food_list["Salad"]:
                    n_Salad = Food_list["Salad"]
                    messagebox.showinfo("Insufficient inventory",f"We have {n_Salad} Salad.")
                    Food_ordered["Salad"] = "Try again"
                else:
                    Food_ordered["Salad"] = int(n_food6_ordered)
                    Food_list["Salad"] -= int(n_food6_ordered)
            else:
                Food_ordered["Salad"] = "Try again"


            n_Drink1_ordered = number_Drink_1.get()
            number_Drink_1.delete(0,END)
            if n_Drink1_ordered.isdigit():
                if int(n_Drink1_ordered) > Food_list["Dough"]:
                    n_Dough = Food_list["Dough"]
                    messagebox.showinfo("Insufficient inventory",f"We have {n_Dough} cans of Dough.")
                    Food_ordered["Dough"] = "Try again"
                else:
                    Food_ordered["Dough"] = int(n_Drink1_ordered)
                    Food_list["Dough"] -= int(n_Drink1_ordered)
            else:
                Food_ordered["Dough"] = "Try again"


            n_Drink2_ordered = number_Drink_2.get()
            number_Drink_2.delete(0,END)
            if n_Drink2_ordered.isdigit():
                if int(n_Drink2_ordered) > Food_list["Black soda"]:
                    n_Black = Food_list["Black soda"]
                    messagebox.showinfo("Insufficient inventory",f"We have {n_Black} cans of Black soda.")
                    Food_ordered["Black soda"] = "Try again"
                else:
                    Food_ordered["Black soda"] = int(n_Drink2_ordered)
                    Food_list["Black soda"] -= int(n_Drink2_ordered)
            else:
                Food_ordered["Black soda"] = "Try again"


            n_Drink3_ordered = number_Drink_3.get()
            number_Drink_3.delete(0,END)
            if n_Drink3_ordered.isdigit():
                if int(n_Drink3_ordered) > Food_list["Orange soda"]:
                    n_Orange = Food_list["Orange soda"]
                    messagebox.showinfo("Insufficient inventory",f"We have {n_Orange} cans of Orange soda.")
                    Food_ordered["Orange soda"] = "Try again"
                else:
                    Food_ordered["Orange soda"] = int(n_Drink3_ordered)
                    Food_list["Orange soda"] -= int(n_Drink3_ordered)
            else:
                Food_ordered["Orange soda"] = "Try again"
            number_food_1.focus()

            with open("Ordered Food","a") as f:
                for item in Food_ordered.items():
                    food,number = item
                    if str(number).isdigit():
                        f.write(food + ": " + str(number) + "\n")
        else:
            messagebox.showinfo("Confirmation","Correct your order")

    
    btn_confirm = Button(master = window,text = "Confirmation",font = ("Tahoma",12),background = "red",width = 200,relief = "groove",borderwidth = 6)
    btn_confirm.config(bitmap = "questhead",compound = "top",cursor = "plus")
    btn_confirm.grid(row = 11,column = 2,padx = 20,pady = 20)
    btn_confirm.config(bitmap = "questhead",compound = "top",cursor = "plus")
    btn_confirm.bind("<Button-1>",btn_confirm_pressed)


    def btn_phone_pressed(event):
        window2 = Tk()
        window2.title("Phone number")
        window2.geometry("600x600+600-300")
        window2.resizable(False,False)
        window2.configure(background = "sky blue")

        lbl_name = Label(master = window2,text = "Name",font = ("Tahoma",15),background = "yellow")
        lbl_name.grid(row = 0,column = 0,padx = 20,pady = 20)

        ent_name = Entry(master = window2,background = "white",font = ("Tahoma",15))
        ent_name.grid(row = 0 ,column = 1,padx = 20,pady = 20)

        lbl_phone = Label(master = window2,text = "Phone number",font = ("Tahoma",15),background = "orange")
        lbl_phone.grid(row = 1,column = 0,padx = 20,pady = 20)

        ent_phone = Entry(master = window2,font = ("Tahoma",15),background = "white")
        ent_phone.grid(row = 1,column = 1,padx = 20,pady = 20)

        lbl_final_price = Label(master = window2,text = "Final price>>>>>>>",font = ("Tahoma",15),background = "green")
        lbl_final_price.grid(row = 2,column = 0,padx = 20,pady = 20)

        lbl_final_price2 = Label(master = window2,background = "green",width = 20)
        lbl_final_price2.grid(row = 2,column = 1,padx = 20,pady = 20)

        
        def btn_calculation_pressed(event):
            money = 0
            with open("Ordered Food","r") as f:
                for line in f:
                    food,number = line.split(": ")
                    if food == "Kubideh kebab":
                        money += (int(number) * 25)
                    elif food == "Kebab chicken":
                        money += (int(number) * 20)
                    elif food == "Barbecue leaves":
                        money += (int(number) * 22)
                    elif food == "Te china":
                        money += (int(number) * 15)
                    elif food == "Rice":
                        money += (int(number) * 7)
                    elif food == "Salad":
                        money += (int(number) * 5)
                    elif food == "Dough":
                        money += (int(number) * 2)
                    elif food == "Black soda":
                        money += (int(number) * 3)
                    elif food == "Orange soda":
                        money += (int(number) * 3)
            with open("Ordered Food","a") as f:
                f.write("Final price: " + str(money)+ "$" + "\n")

            lbl_final_price3 = Label(master = window2,text = f"{money}$",font = ("Tahoma",15),background = "green")
            lbl_final_price3.grid(row = 2,column = 1,padx = 20,pady = 20)

        btn_calculation = Button(master = window2,text = "Calculation",font = ("Tahoma",15),background = "yellow")
        btn_calculation.grid(row = 3,column = 0,padx = 20,pady = 20)
        btn_calculation.config(bitmap = "questhead",compound = "top",cursor = "plus")
        btn_calculation.bind("<Button-1>",btn_calculation_pressed)


        def btn_save_pressed(event):
            name = ent_name.get()
            ent_name.delete(0,END)
            phone_number = ent_phone.get()
            ent_phone.delete(0,END)
            with open("Ordered Food","a") as f:
                f.write("Name: " + name + "\n")
                f.write("Phone number: " + phone_number + "\n")

        btn_save = Button(master = window2,text = "Save",font = ("Tahoma",15),background = "red")
        btn_save.grid(row = 3,column = 1,padx = 20,pady = 20)
        btn_save.config(bitmap = "questhead",compound = "top",cursor = "plus")
        btn_save.bind("<Button-1>",btn_save_pressed)

        def btn_finish_pressed(event):
            with open("All orders","a") as f:
                with open("Ordered Food","r") as x:
                    for line in x:
                        inf,number = line.split(": ")
                        f.write(inf + ": " + number + "\n")
                    f.write("#################################" + "\n")
            with open("Ordered Food","w") as y:
                y.write("")
            window2.destroy() 


        btn_finish = Button(master = window2,text = "Finish",font = ("Tahoma",15),background = "gray")
        btn_finish.grid(row = 4,column = 0,padx = 20,pady = 20)
        btn_finish.config(bitmap = "questhead",compound = "top",cursor = "plus")
        btn_finish.bind("<Button-1>",btn_finish_pressed)


        def btn_Stop_pressed(event):
            if messagebox.askquestion("Stop Working","Are you sure?") == "yes":
                window.destroy()
                window2.destroy()
                with open("Left_foods","w") as f:   
                    for item in Food_list.items():
                        food,number = item
                        f.write(food + ": " + str(number) + "\n")
            else:
                messagebox.showinfo("Stop Working","Back to Work!!")
        
        btn_Stop = Button(master = window2,text = "Stop",font = ("Tahoma",15),background = "orange")
        btn_Stop.grid(row = 4,column = 1,padx = 20,pady = 20)
        btn_Stop.config(bitmap = "questhead",compound = "top",cursor = "plus")
        btn_Stop.bind("<Button-1>",btn_Stop_pressed)


        window2.mainloop()

    btn_phone.bind("<Button-1>",btn_phone_pressed)



    window.mainloop()

btn_Start = Button(master = win,text = "Start",font = ("Tahoma",15),background = "yellow")
btn_Start.grid(row = 11,column = 1,padx = 20,pady = 20)
btn_Start.config(bitmap = "questhead",compound = "top",cursor = "plus")
btn_Start.bind("<Button-1>",btn_Start_pressed)

win.mainloop()