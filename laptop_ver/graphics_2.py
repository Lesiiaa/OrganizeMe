import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk #dodawanie zdjec
import tools
import time
import random

root = tk.Tk()
root.resizable(False, False) #brak mozliwosci zmiany okienka

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


#OKNO LOGOWANIA
def login_window(window, on_login_click, on_go_register_click):
    for content in window.winfo_children():
        content.destroy()
    
    #okienko wyskakuje na srodku ekranu
    window_width = int(screen_width * 0.337) #szerokosc okna i wysokosc dopasowana do ekranu uzytkownika
    window_height = int(screen_height * 0.39)
    x_window_place = (screen_width / 2) - (window_width /2)
    y_window_place = (screen_height / 2) - (window_height /2)
    root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_window_place, y_window_place))
    
    window.title("Log in")
    window.configure(bg="#F5F5F5")
    window.iconbitmap("graphic_elements/logo_icon.ico")


    label_login = tk.Label(
        window, 
        text = "E-mail", 
        bg="#F5F5F5",
        fg="#023047",
        font = ("Arial Rounded MT Bold", int(window_height * 0.047))
        )
    label_login.place(x=int(window_width*0.16), y=int(window_height*0.38))

    label_password = tk.Label(
        window, 
        text = "Password", 
        bg="#F5F5F5",
        fg="#023047",
        font=("Arial Rounded MT Bold", int(window_height * 0.047))
        )
    label_password.place(x=int(window_width*0.16), y=int(window_height*0.57))

    label_register = tk.Label(
        window, 
        text = "First time? Register here", 
        bg="#F5F5F5",
        font=("Arial Rounded MT Bold", int(window_height * 0.029)),
        fg = "#767676"
        )
    label_register.place(x=int(window_width*0.277), y=int(window_height*0.896))

    error_label = tk.Label(
        window,
        text="",
        bg="#F5F5F5",
        fg="#FF0000",
        font=("Arial Rounded MT Bold", int(window_height * 0.029) ),
        )
    error_label.place(x=int(window_width*0.35), y=int(window_height*0.37))

    #login i haslo, boxy do wpisywania
    element_width = int(window_width * 0.08)
    entry_font = ("Helvetica", int(window_height / 25))
    entry_login = tk.Entry(window, bg="#E4E4E4", width =element_width,  font = entry_font, border=0)
    entry_login.place(x = window_width * 0.17, y=window_height * 0.485)

    entry_password = tk.Entry(window, bg="#E4E4E4", width =element_width,  font = entry_font, border=0, show="*")
    entry_password.place(x = window_width * 0.17, y=window_height * 0.68)

    element_width = int(window_width * 0.7)

    #login i haslo, tlo boxow
    image = Image.open("graphic_elements/login_window/entry_bg.png")
    resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
    photo = ImageTk.PhotoImage(resized_image)
    login_label = tk.Label(root,image =photo, bd = 0, bg = "#F5F5F5")
    login_label.image = photo
    login_label.place(x = window_width * 0.15, y=window_height * 0.48)
    login_label.lower()

    image = Image.open("graphic_elements/login_window/entry_bg.png")
    resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
    photo = ImageTk.PhotoImage(resized_image)
    login_label = tk.Label(root,image =photo, bd = 0, bg = "#F5F5F5")
    login_label.image = photo
    login_label.place(x = window_width * 0.15, y=window_height * 0.67)
    login_label.lower()

    #przycisk logowania, tlo
    element_width = int(window_width * 0.13)
    image = Image.open("graphic_elements/login_window/login_btn.png")
    resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
    photo = ImageTk.PhotoImage(resized_image)
    login_label = tk.Label(root,image =photo, bd = 0, bg = "#F5F5F5")
    login_label.image = photo
    login_label.pack()
    login_label.place(x = window_width * 0.43, y=window_height * 0.79)
    login_label.lower()
    
    
    #przycisk logowania
    label_login_btn = tk.Button(
        window, 
        text = "Log in",
        bg="#E4E4E4",
        font=("Arial Rounded MT Bold", int(window_height * 0.027)),
        bd = 0,
        highlightthickness=0,
        activebackground="#E4E4E4",
        command=lambda:on_login_click(entry_login.get(), entry_password.get())
        )
    label_login_btn.place(x = window_width * 0.46, y=window_height * 0.79)

    #ikonka strzalka
    element_width = int(window_width * 0.05)
    image = Image.open("graphic_elements/login_window/arrow.png")
    resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
    photo = ImageTk.PhotoImage(resized_image)
    label = tk.Label(root, image =photo, bd = 0)
    label.image = photo
    label.pack()
    label.place(x = window_width * 0.57, y=window_height * 0.87)

    #ikonka rejestracji - button
    element_width = int(window_width * 0.07)
    image = Image.open("graphic_elements/login_window/register_icon.png")
    resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
    photo = ImageTk.PhotoImage(resized_image)
    register_button = tk.Button(window, image =photo, command=on_go_register_click, bd = 0, highlightthickness=0)
    register_button.image = photo
    register_button.pack()
    register_button.place(x = window_width * 0.64, y=window_height * 0.87)
    
    #logo
    element_width = int(window_width * 0.22)
    image = Image.open("graphic_elements/login_window/logo_complete.png")
    resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
    photo = ImageTk.PhotoImage(resized_image)
    label = tk.Label(root, image=photo, bd=0)
    label.image = photo
    label.pack()
    label.place(x = window_width * 0.39, y=window_height*0.02)


# OKNO REJESTRACJI
def register_window(window, back_to_login_click, on_register_click):
    for content in window.winfo_children():
        content.destroy()

    window_width = int(screen_width * 0.337) #szerokosc okna i wysokosc dopasowana do ekranu uzytkownika
    window_height = int(screen_height * 0.39)
    x_window_place = (screen_width / 2) - (window_width /2)
    y_window_place = (screen_height / 2) - (window_height /2)
    root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_window_place, y_window_place))
    
    window.title("Register window")
    window.configure(bg="#F5F5F5")
    window.iconbitmap("graphic_elements/logo_icon.ico")

    # napisy
    label_name = tk.Label(
        window,
        text="Name:",
        bg="#F5F5F5",
        fg="#023047",
        font=("Arial Rounded MT Bold", int(window_height * 0.04))
    )
    label_name.place(x=int(window_width*0.2), y=int(window_height*0.2))

    label_mail = tk.Label(
        window,
        text="Mail:",
        bg="#F5F5F5",
        fg="#023047",
        font=("Arial Rounded MT Bold", int(window_height * 0.04))
    )
    label_mail.place(x=int(window_width*0.2), y=int(window_height*0.35))

    label_password2 = tk.Label(
        window,
        text="Password:",
        bg="#F5F5F5",
        fg="#023047",
        font=("Arial Rounded MT Bold", int(window_height * 0.04))
    )
    label_password2.place(x=int(window_width*0.2), y=int(window_height*0.5))

    label_password3 = tk.Label(
        window,
        text="Confirm Password:",
        bg="#F5F5F5",
        fg="#023047",
        font=("Arial Rounded MT Bold", int(window_height * 0.04))
    )
    label_password3.place(x=int(window_width*0.2), y=int(window_height*0.65))

    error_label = tk.Label(
        window,
        text="",
        fg="#FF0000",
        bg="#F5F5F5",
        font=("Arial Rounded MT Bold", 6)
    )
    error_label.place(x=int(window_width*0.30), y=int(window_height*0.15))


    # imie, mail i haslo, boxy do wpisywania
    register_font = ("Helvetica", int(window_height * 0.0008))
    register_name = tk.Entry(window, bg="#E4E4E4", width =30,  font = register_font, border=0)
    register_name.place(x=int(window_width*0.215), y=int(window_height*0.285))

    register_mail = tk.Entry(window, bg="#E4E4E4", width =30,  font = register_font, border=0)
    register_mail.place(x=int(window_width*0.215), y=int(window_height*0.435))

    register_password = tk.Entry(window, bg="#E4E4E4", width =30,  font = register_font, border=0)
    register_password.place(x=int(window_width*0.215), y=int(window_height*0.585))

    register_password2 = tk.Entry(window, bg="#E4E4E4", width =30,  font = register_font, border=0)
    register_password2.place(x=int(window_width*0.215), y=int(window_height*0.735))


    # imie, mail i haslo, tlo do boxow
    def create_bg(x, y):
        element_width = int(window_width * 0.65)
        image = Image.open("graphic_elements/login_window/entry_bg.png")
        resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
        photo = ImageTk.PhotoImage(resized_image)
        entry_label = tk.Label(root, image=photo, bd=0, bg="#F5F5F5")
        entry_label.image = photo
        entry_label.place(x=x, y=y)
        entry_label.lower()
    create_bg(x=int(window_width*0.2), y=int(window_height*0.28))
    create_bg(x=int(window_width*0.2), y=int(window_height*0.43))
    create_bg(x=int(window_width*0.2), y=int(window_height*0.58))
    create_bg(x=int(window_width*0.2), y=int(window_height*0.73))

    # przycisk rejestracji i BACK, tlo
    def create_button_bg(image_path, x, y):
        element_width = int(window_width * 0.12)
        image = Image.open(image_path)
        resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
        photo = ImageTk.PhotoImage(resized_image)
        button_label = tk.Label(root, image=photo, bd=0, bg="#F5F5F5")
        button_label.image = photo
        button_label.place(x=x, y=y)
        button_label.lower()
    
    create_button_bg("graphic_elements/login_window/login_btn.png", x=int(window_width*0.33), y=int(window_height*0.9))
    create_button_bg("graphic_elements/login_window/login_btn.png", x=int(window_width*0.58), y=int(window_height*0.9))

    # przycisk rejestracji
    label_register_btn = tk.Button(
        window,
        text = "Register",
        bg="#E4E4E4",
        font=("Arial Rounded MT Bold", int(window_height * 0.025)),
        bd = 0,
        highlightthickness=0,
        activebackground="#E4E4E4",
        command = lambda:on_register_click(register_mail.get(),register_password.get(),register_name.get(),register_password2.get())
        )
    label_register_btn.place(x = window_width * 0.35, y=window_height * 0.9)

     # przycisk BACK
    label_back_btn = tk.Button(
        window,
        text = "Back",
        bg="#E4E4E4",
        font=("Arial Rounded MT Bold", int(window_height * 0.025)),
        bd = 0,
        highlightthickness=0,
        activebackground="#E4E4E4",
        command=back_to_login_click
        )
    label_back_btn.place(x = window_width * 0.61, y=window_height * 0.9)



#OKNO GLOWNE
def home_window(window, add_note_click, remove_note_click, name, logout):
# def home_window(window):
    for content in window.winfo_children():
        content.destroy()

    #okienko wyskakuje na srodku ekranu
    window_width = int(screen_width * 0.9) #szerokosc okna i wysokosc dopasowana do ekranu uzytkownika
    window_height = int(screen_height * 0.87)
    x_window_place = (screen_width / 2) - (window_width /2)
    y_window_place = (screen_height / 2) - (window_height /2)
    root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_window_place, y_window_place))
    
    window.title("Homepage")
    window.configure(bg="#F0F0F0")
    window.iconbitmap("graphic_elements/logo_icon.ico")


    #Ramka dla menu bocznego
    frame_menu = tk.Frame(window)
    frame_menu.grid(row=0, column=0, sticky="nw")

    #Ramka dla kalendarza
    frame_calendar = tk.Frame(window)
    frame_calendar.grid(row=0, column=0, sticky="nsew")

    #ramka dla miesiąca
    frame_month = tk.Frame(window)
    frame_month.grid(row=0, column=0, sticky="nsew")

    global view_number #widok kalendarza:  0 - rok,  1,2,3.. - dany miesiac
    view_number = 0

    new_size = (929,629) 
    
    
    def menu_open_clicked():
        print("Menu clicked!")
        frame_menu.lift()

    def menu_close_clicked():
        frame_menu.lower()

    def change_view(number):
        global view_number
        view_numbers = {0: 12,1: 1,2: 2,3: 3,4: 4,5: 5,6: 6,7: 7,8: 8,9: 9,10: 10,11: 11,12: 12, 13: 1}
        view(view_numbers.get(number, 1))
        if number == 0:
            view_number = 12
        elif number == 13:
            view_number = 1
        else:
            view_number = number
    
    def change_view_btn(number):
        global view_number
        if number == 0:
            view_number = 1
        else:
            view_number = 0
        view(view_number)


    #######MENU BOCZNE#######
    quotes = ["“I never dreamed about success. I worked for it.” —Estée Lauder",
                "“Goal setting is the secret to a compelling future.” —Tony Robbins",
                "“If you can dream it, you can do it.” ―Walt Disney",
                "“Opportunities don’t happen, you create them.” —Chris Grosser"]

    #logo
    element_width=int(window_width * 0.27)
    image = Image.open("graphic_elements/homepage/menu_bg.png")
    resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
    photo = ImageTk.PhotoImage(resized_image)
    menu_bg_label = tk.Label(frame_menu, image=photo, bd=0)
    menu_bg_label.image = photo
    menu_bg_label.place(x=0, y=0)

    #menu close- button
    element_width=int(window_width * 0.05)
    image = Image.open("graphic_elements/homepage/menu_close_btn.png")
    resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
    photo = ImageTk.PhotoImage(resized_image)
    menu_close_button = tk.Button(frame_menu, image=photo, bd=0, activebackground="#E2E2E2", highlightthickness=0, command=menu_close_clicked)
    menu_close_button.image = photo
    menu_close_button.grid(row=0, column=0, sticky="nw", padx=window_width*0.003, pady=window_height*0.006)
    
    #random quote
    quote_label = tk.Label(frame_menu,text= random.choice(quotes),bg="#E2E2E2",fg="#023047",font=("Arial Rounded MT Bold", 11), wraplength=250, justify='center')
    quote_label.grid(row=1, column=0, pady=(window_height*0.15,0))

    #Change view button
    view_button = tk.Button(frame_menu, width=20, text = "Change view", bg="#D1D1D1", bd=0, activebackground="#D1D1D1", highlightthickness=0 ,font = ("Arial Rounded MT Bold", 16), command=lambda:change_view_btn(view_number))
    view_button.grid(row=2,column=0, padx=window_width*0.038, pady=(window_height*0.12, 0))

    #Notes button
    notes_button = tk.Button(frame_menu, width=20, text = "Notes", bg="#D1D1D1", bd=0, activebackground="#D1D1D1", highlightthickness=0 ,font = ("Arial Rounded MT Bold", 16), command=open_notes_window)
    notes_button.grid(row=3,column=0, pady=(window_height*0.054, 0))
    
    #Log out button
    logout_button = tk.Button(frame_menu, width=20, text = "Log out", bg="#D1D1D1", fg="#DA4242", activeforeground="#DA4242", bd=0, activebackground="#D1D1D1", highlightthickness=0 ,font = ("Arial Rounded MT Bold", 16), command=logout)
    logout_button.grid(row=4,column=0, pady=window_height*0.3)



    #####WIDOK GLOWNY####
    def view(number):
        def show_date_label():
                today = time.strftime("%A, %d %B, %Y")
                date_label = tk.Label(frame_calendar, text=today, bg="#F0F0F0", font=20)
                date_label.grid(row=0, column=2, padx=(60,0), pady=30, columnspan=2)

        if number == 0:
            frame_calendar.lift()
            #NAPISY
                
            #welcome text and date
            welcome_label = tk.Label(frame_calendar, text=f"Welcome back {name}!", font=20, bg="#F0F0F0")
            welcome_label.grid(row=0, column=2, padx=(60,0), pady=30, columnspan=2)

            window.after(5000, lambda: welcome_label.config(text=""))
            window.after(5000, show_date_label)

            #menu- button
            element_width=int(window_width * 0.035)
            image_menu = Image.open("graphic_elements/homepage/menu_open_btn.png")
            resized_image_menu = image_menu.resize((element_width, int(element_width * image_menu.height / image_menu.width)))
            photo_menu = ImageTk.PhotoImage(resized_image_menu)
            menu_open_button = tk.Button(frame_calendar, image =photo_menu, bd = 0, highlightthickness=0, command=menu_open_clicked)
            menu_open_button.image = photo_menu
            menu_open_button.grid(row=0, column=0, padx=(14,0), pady=13, sticky="nw")

            #add note
            image = Image.open("graphic_elements/homepage/add_btn.png")
            element_width = int(window_width * 0.035)
            resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
            photo = ImageTk.PhotoImage(resized_image)
            add_button = tk.Button(frame_calendar, image=photo, bd = 0, highlightthickness=0, command=add_note_click)
            add_button.image = photo
            add_button.grid(row=3, column=6, padx=0, pady=15, sticky="se")
            add_button.lift()

            #remove note
            image = Image.open("graphic_elements/homepage/remove_btn.png")
            element_width = int(window_width * 0.035)
            resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
            photo = ImageTk.PhotoImage(resized_image)
            remove_button = tk.Button(frame_calendar, image=photo, bd = 0, highlightthickness=0, command=remove_note_click)
            remove_button.image = photo
            remove_button.grid(row=3, column=5, padx=40, pady=20, sticky="se")
            remove_button.lift()

            #Miesiace
            #01
            image = Image.open("graphic_elements/homepage/months/january.png")
            element_width = int(window_width * 0.13)
            resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
            photo = ImageTk.PhotoImage(resized_image)
            january = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(1))
            january.image = photo
            january.grid(row=1, column=1, padx=(150,0), pady=25)
            
            #02
            image = Image.open("graphic_elements/homepage/months/february.png")
            element_width = int(window_width * 0.13)
            resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
            photo = ImageTk.PhotoImage(resized_image)
            february = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(2))
            february.image = photo
            february.grid(row=1, column=2, padx=(50,0), pady=0)

            #03
            image = Image.open("graphic_elements/homepage/months/march.png")
            element_width = int(window_width * 0.13)
            resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
            photo = ImageTk.PhotoImage(resized_image)
            march = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(3))
            march.image = photo
            march.grid(row=1, column=3, padx=(50,0), pady=0)

            #04
            image = Image.open("graphic_elements/homepage/months/april.png")
            element_width = int(window_width * 0.13)
            resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
            photo = ImageTk.PhotoImage(resized_image)
            april = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(4))
            april.image = photo
            april.grid(row=1, column=4, padx=(50,0), pady=0)

            #05
            image = Image.open("graphic_elements/homepage/months/may.png")
            element_width = int(window_width * 0.13)
            resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
            photo = ImageTk.PhotoImage(resized_image)
            may = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(5))
            may.image = photo
            may.grid(row=2, column=1, padx=(135,0), pady=0)

            #06
            image = Image.open("graphic_elements/homepage/months/june.png")
            element_width = int(window_width * 0.13)
            resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
            photo = ImageTk.PhotoImage(resized_image)
            june = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(6))
            june.image = photo
            june.grid(row=2, column=2, padx=(50,0), pady=0)

            #07
            image = Image.open("graphic_elements/homepage/months/july.png")
            element_width = int(window_width * 0.13)
            resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
            photo = ImageTk.PhotoImage(resized_image)
            july = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(7))
            july.image = photo
            july.grid(row=2, column=3, padx=(50,0), pady=0)

            #08
            image = Image.open("graphic_elements/homepage/months/august.png")
            element_width = int(window_width * 0.13)
            resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
            photo = ImageTk.PhotoImage(resized_image)
            august = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(8))
            august.image = photo
            august.grid(row=2, column=4, padx=(50,0), pady=0)

            #09
            image = Image.open("graphic_elements/homepage/months/september.png")
            element_width = int(window_width * 0.13)
            resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
            photo = ImageTk.PhotoImage(resized_image)
            september = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(9))
            september.image = photo
            september.grid(row=3, column=1, padx=(135,0), pady=30)

            #10
            image = Image.open("graphic_elements/homepage/months/october.png")
            element_width = int(window_width * 0.13)
            resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
            photo = ImageTk.PhotoImage(resized_image)
            october = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(10))
            october.image = photo
            october.grid(row=3, column=2, padx=(50,0),pady=0)

            #11
            image = Image.open("graphic_elements/homepage/months/november.png")
            element_width = int(window_width * 0.13)
            resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
            photo = ImageTk.PhotoImage(resized_image)
            november = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(11))
            november.image = photo
            november.grid(row=3, column=3, padx=(50,0), pady=0)

            #12
            image = Image.open("graphic_elements/homepage/months/december.png")
            element_width = int(window_width * 0.13)
            resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
            photo = ImageTk.PhotoImage(resized_image)
            december = tk.Button(frame_calendar, image = photo, bd = 0, command=lambda:change_view(12))
            december.image = photo
            december.grid(row=3, column=4, padx=(50,0), pady=0)

        else:
            frame_month.lift()
            
            #menu- button
            element_width=int(window_width * 0.035)
            image_menu = Image.open("graphic_elements/homepage/menu_open_btn.png")
            resized_image_menu = image_menu.resize((element_width, int(element_width * image_menu.height / image_menu.width)))
            photo_menu = ImageTk.PhotoImage(resized_image_menu)
            menu_open_button = tk.Button(frame_month, image =photo_menu, bd = 0, highlightthickness=0, command=menu_open_clicked)
            menu_open_button.image = photo_menu
            menu_open_button.grid(row=0, column=0, padx=(14,0), pady=13, sticky="nw")

            #arrow back- button
            element_width=int(window_width * 0.035)
            image = Image.open("graphic_elements/homepage/arrow_back.png")
            resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
            photo = ImageTk.PhotoImage(resized_image)
            arrow_back_button = tk.Button(frame_month, image =photo, bd = 0, highlightthickness=0, command=lambda:change_view(view_number-1))
            arrow_back_button.image = photo
            arrow_back_button.grid(row=1, column=1, padx=(20,0), pady=(295,0), sticky="nsew")

            #arrow forward- button
            image = Image.open("graphic_elements/homepage/arrow_forward.png")
            resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
            photo = ImageTk.PhotoImage(resized_image)
            arrow_forward_button = tk.Button(frame_month, image =photo, bd = 0, highlightthickness=0, command=lambda:change_view(view_number+1))
            arrow_forward_button.image = photo
            arrow_forward_button.grid(row=1, column=2, padx=(1000,0), pady=(295,0), sticky="nsew")

            #add note
            image = Image.open("graphic_elements/homepage/add_btn.png")
            element_width = int(window_width * 0.035)
            resized_image = image.resize((element_width, int(element_width * image.height / image.width)))
            photo = ImageTk.PhotoImage(resized_image)
            add_button = tk.Button(frame_month, image=photo, bd = 0, highlightthickness=0, command=add_note_click)
            add_button.image = photo
            add_button.grid(row=2, column=3, padx=0, pady=180)


            if number == 1:
                image = Image.open("graphic_elements/homepage/months_2/january.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                january_m = tk.Label(window, image = photo)
                january_m.image = photo
                january_m.place(relx=0.129, rely=0.0405)

            elif number == 2:
                image = Image.open("graphic_elements/homepage/months_2/february.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                february_m = tk.Label(window, image = photo)
                february_m.image = photo
                february_m.place(relx=0.129, rely=0.04)
            
            elif number == 3:
                image = Image.open("graphic_elements/homepage/months_2/march.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                march_m = tk.Label(window, image = photo)
                march_m.image = photo
                march_m.place(relx=0.129, rely=0.04)

            elif number == 4:
                image = Image.open("graphic_elements/homepage/months_2/april.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                april_m = tk.Label(window, image = photo)
                april_m.image = photo
                april_m.place(relx=0.129, rely=0.04)

            elif number == 5:
                image = Image.open("graphic_elements/homepage/months_2/may.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                may_m = tk.Label(window, image = photo)
                may_m.image = photo
                may_m.place(relx=0.128, rely=0.04)

            elif number == 6:
                image = Image.open("graphic_elements/homepage/months_2/june.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                june_m = tk.Label(window, image = photo)
                june_m.image = photo
                june_m.place(relx=0.129, rely=0.04)

            elif number == 7:
                image = Image.open("graphic_elements/homepage/months_2/july.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                july_m = tk.Label(window, image = photo)
                july_m.image = photo
                july_m.place(relx=0.129, rely=0.04)

            elif number == 8:
                image = Image.open("graphic_elements/homepage/months_2/august.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                august_m = tk.Label(window, image = photo)
                august_m.image = photo
                august_m.place(relx=0.129, rely=0.04)

            elif number == 9:
                image = Image.open("graphic_elements/homepage/months_2/september.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                september_m = tk.Label(window, image = photo)
                september_m.image = photo
                september_m.place(relx=0.129, rely=0.04)

            elif number == 10:
                image = Image.open("graphic_elements/homepage/months_2/october.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                october_m = tk.Label(window, image = photo)
                october_m.image = photo
                october_m.place(relx=0.129, rely=0.04)

            elif number == 11:
                image = Image.open("graphic_elements/homepage/months_2/november.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                november_m = tk.Label(window, image = photo)
                november_m.image = photo
                november_m.place(relx=0.129, rely=0.04)

            else:
                image = Image.open("graphic_elements/homepage/months_2/december.png")
                resized_image = image.resize(new_size)
                photo = ImageTk.PhotoImage(resized_image)
                december_m = tk.Label(window, image = photo)
                december_m.image = photo
                december_m.place(relx=0.129, rely=0.04)

    view(view_number)


# Function to display notes
def display_notes(parent_window):
    notes = tools.get_notes_from_firebase()
    for widget in parent_window.winfo_children():
        widget.destroy()

    if notes:
        for note in notes:
            note_frame = tk.Frame(parent_window, bg="#E4E4E4", bd=1, relief="solid")
            note_frame.pack(pady=5, padx=10, fill="x", expand=True)

            title_label = tk.Label(note_frame, text=note['title'], bg="#E4E4E4", fg="#023047", font=("Arial Rounded MT Bold", 12), anchor="w")
            title_label.pack(anchor="w", padx=10, pady=5)

            content_label = tk.Label(note_frame, text=note['content'], bg="#E4E4E4", fg="#023047", font=("Helvetica", 10), wraplength=350, justify="left", anchor="w")
            content_label.pack(anchor="w", padx=10, pady=5)
    else:
        no_notes_label = tk.Label(parent_window, text="No notes available", bg="#F5F5F5", fg="#023047", font=("Arial Rounded MT Bold", 12))
        no_notes_label.pack(pady=20)


# Function to handle adding a new note
def add_note_click(parent_window):
    add_note_click = tk.Toplevel(parent_window)
    add_note_click.title("Add Note")
    add_note_click.configure(bg="#F5F5F5")
    add_note_click.iconbitmap("graphic_elements/logo_icon.ico")
    add_note_click.geometry("400x300")
    

    # Labels
    label_title = tk.Label(
        add_note_click,
        text="Enter the title of the note:",
        bg="#F5F5F5",
        fg="#023047",
        font=("Arial Rounded MT Bold", 10)
    )
    label_title.place(x=20, y=20)

    label_content = tk.Label(
        add_note_click,
        text="Enter the content of the note:",
        bg="#F5F5F5",
        fg="#023047",
        font=("Arial Rounded MT Bold", 10),
    )
    label_content.place(x=20, y=70)

    # Entry boxes
    note_font = ("Helvetica", 8)
    note_title = tk.Entry(add_note_click, bg="#E4E4E4", width=60, font=note_font, border=0)
    note_title.place(x=20, y=43)

    note_content = tk.Text(add_note_click, bg="#E4E4E4", width=60, height=10, font=note_font, border=0)
    note_content.place(x=20, y=93)

    # Save button
    save_button = tk.Button(
        add_note_click,
        text="Save",
        bg="#E4E4E4",
        font=("Arial Rounded MT Bold", 8),
        bd=0,
        highlightthickness=0,
        activebackground="#E4E4E4",
        command=lambda: save_note(add_note_click, note_title.get(), note_content.get("1.0", "end-1c")),
    )
    save_button.place(x=180, y=260)
    

# Function to save a note
def save_note(window, title, content):
    try:
        tools.add_note_to_firebase(title, content)
        window.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the note: {str(e)}")

# Function to open the notes window
def open_notes_window():
    notes_window = tk.Toplevel()
    notes_window.title("Notes")
    notes_window.configure(bg="#F5F5F5")
    notes_window.geometry("500x600")

    # Create a frame for the canvas and scrollbar
    frame_canvas = tk.Frame(notes_window, bg="#F5F5F5")
    frame_canvas.pack(fill="both", expand=True)

    # Add a canvas in that frame
    canvas = tk.Canvas(frame_canvas, bg="#F5F5F5")
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar to the canvas
    scrollbar = ttk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create another frame inside the canvas
    notes_frame = tk.Frame(canvas, bg="#F5F5F5")

    # Add that new frame to a window in the canvas
    canvas.create_window((0, 0), window=notes_frame, anchor="nw")

    display_notes(notes_frame)


def display_remove_notes(parent_window):
    notes = tools.get_notes_from_firebase()
    for widget in parent_window.winfo_children():
        widget.destroy()

    if notes:
        for note in notes:
            note_frame = tk.Frame(parent_window, bg="#E4E4E4", bd=1, relief="solid")
            note_frame.pack(pady=5, padx=10, fill="x", expand=True)

            # Dodajemy bind dla zdarzenia kliknięcia na note_frame
            note_frame.bind("<Button-1>", lambda e, note_id=note['id']: tools.delete_note_from_firebase(note_id))

            title_label = tk.Label(note_frame, text=note['title'], bg="#E4E4E4", fg="#023047", font=("Arial Rounded MT Bold", 12), anchor="w")
            title_label.pack(anchor="w", padx=10, pady=5)

            content_label = tk.Label(note_frame, text=note['content'], bg="#E4E4E4", fg="#023047", font=("Helvetica", 10), wraplength=350, justify="left", anchor="w")
            content_label.pack(anchor="w", padx=10, pady=5)

            # Opcjonalnie, możesz dodać bind dla zdarzenia kliknięcia na etykiety (title_label, content_label)
            title_label.bind("<Button-1>", lambda e, note_id=note['id']: tools.delete_note_from_firebase(note_id))
            content_label.bind("<Button-1>", lambda e, note_id=note['id']: tools.delete_note_from_firebase(note_id))
    else:
        no_notes_label = tk.Label(parent_window, text="No notes available", bg="#F5F5F5", fg="#023047", font=("Arial Rounded MT Bold", 12))
        no_notes_label.pack(pady=20)

def open_remove_notes_window():
    notes_window = tk.Toplevel()
    notes_window.title("Notes")
    notes_window.configure(bg="#F5F5F5")
    notes_window.geometry("500x600")

    # Create a frame for the canvas and scrollbar
    frame_canvas = tk.Frame(notes_window, bg="#F5F5F5")
    frame_canvas.pack(fill="both", expand=True)

    # Add a canvas in that frame
    canvas = tk.Canvas(frame_canvas, bg="#F5F5F5")
    canvas.pack(side="left", fill="both", expand=True)

    # Add a scrollbar to the canvas
    scrollbar = ttk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create another frame inside the canvas
    notes_frame = tk.Frame(canvas, bg="#F5F5F5")

    # Add that new frame to a window in the canvas
    canvas.create_window((0, 0), window=notes_frame, anchor="nw")

    display_remove_notes(notes_frame)