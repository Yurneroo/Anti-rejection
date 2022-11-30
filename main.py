from tkinter import *
from PIL import Image, ImageTk
import random

count_no = 0


# functions for YES BUTTON
def yes():

    global button_no

    # putting the image5 as a background
    canvas.create_image(0, 0, image=my_img5, anchor=NW)

    # removing the no button
    button_no.place_forget()


# functions for NO BUTTON
def no():

    global count_no

    count_no += 1

    # setting boundary for placing the no button randomly
    button_no_x = random.randint(10, 400)
    button_no_y = random.randint(10, 400)

    # randomly placing no button every time it is clicked
    button_no.place(x=button_no_x, y=button_no_y)


# putting and placing the images when no button is clicked
def image_add_no_button():
    if count_no == 2:
        canvas.create_image(10, 10, anchor=NW, image=my_img1)

    if count_no == 3:
        canvas.create_image(230, 230, anchor=NW, image=my_img3)
        canvas.create_image(135, 275, anchor=NW, image=hand_img)

    if count_no == 4:
        canvas.create_image(80, 360, anchor=NW, image=my_img2)

    if count_no == 5:
        canvas.create_image(300, 25, anchor=NW, image=my_img4)


# setting up the window -------------------------------------------------------------------
window = Tk()
window.geometry("500x500")
window.title("Confession")
window.config(background="white")
window.resizable(False, False)

# creating the canvas ------------------------------------------------------------------
canvas = Canvas(window, background="white", width=500, height=500)
canvas.pack(fill="both", expand=True)

# "Hi Crush" label -------------------------------------------------------------
canvas.create_text(150, 150,
                   anchor=NW,
                   text="HI CRUSH", fill="red",
                   font=('Arial', 30))

# "I like you a lot, Want to go on a date?" text ----------------------------------------
canvas.create_text(90, 200,
                   anchor=NW,
                   text="I like you a lot, wanna go on a date?",
                   font=('Arial', 15))

# opening, resizing and converting images ----------------------------------------------------------------------
image1 = Image.open('Resources/image1.png')
img1 = image1.resize((180, 130))
my_img1 = ImageTk.PhotoImage(img1)

image2 = Image.open('Resources/image2.png')
img2 = image2.resize((150, 110))
my_img2 = ImageTk.PhotoImage(img2)

image3 = Image.open('Resources/image3.png')
img3 = image3.resize((170, 110))
my_img3 = ImageTk.PhotoImage(img3)

image4 = Image.open('Resources/image4.png')
img4 = image4.resize((180, 130))
my_img4 = ImageTk.PhotoImage(img4)

hand_image = Image.open('Resources/hand.png')
hand = hand_image.resize((80, 70))
hand_img = ImageTk.PhotoImage(hand)

image5 = Image.open('Resources/image5.png')
img5 = image5.resize((500, 500))
my_img5 = ImageTk.PhotoImage(img5)

# the yes button ---------------------------------------------------------------------
button_yes = Button(window,
                    text="YES",
                    command=yes,
                    font=("Comic Sans", 16),
                    bg="white",
                    width=6,
                    height=1,)
button_yes.pack()
# positing the yes button
button_yes.place(x=130, y=240)

# the no button ---------------------------------------------------------------------------
button_no = Button(window,
                   text="NO",
                   command=lambda: [no(), image_add_no_button()],
                   font=("Comic Sans", 16),
                   bg="white",
                   width=6,
                   height=1)
button_no.pack()
# positing the no button
button_no.place(x=280, y=240)

window.mainloop()
