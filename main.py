from tkinter import *
from PIL import Image, ImageTk
import random

count_no = 0


def yes():

    global button_no

    label_image5.pack()

    button_no.place_forget()


def no():

    global count_no

    count_no += 1

    button_no_x = random.randint(10, 400)
    button_no_y = random.randint(10, 400)

    for i in range(count_no):
        button_no.place(x=button_no_x, y=button_no_y)

    if count_no == 3:
        label_image1.pack()
        label_image1.place(x=10, y=10)

    if count_no == 4:
        label_image3.pack()
        label_image3.place(x=230, y=200)
        label_hand_image.pack()
        label_hand_image.place(x=135, y=275)

    if count_no == 5:
        label_image2.pack()
        label_image2.place(x=80, y=340)

    if count_no == 6:
        label_image4.pack()
        label_image4.place(x=300, y=30)


# setting up the window -------------------------------------------------------------------
window = Tk()
window.geometry("500x500")
window.title("Confession")
window.config(background="white")
window.resizable(False, False)

# images ----------------------------------------------------------------------
# image 1 png
image1 = Image.open('image1.png')
img1 = image1.resize((180, 130))
my_img1 = ImageTk.PhotoImage(img1)
label_image1 = Label(window, image=my_img1)

# image 2 png
image2 = Image.open('image2.png')
img2 = image2.resize((150, 110))
my_img2 = ImageTk.PhotoImage(img2)
label_image2 = Label(window, image=my_img2)

# image 3 png
image3 = Image.open('image3.png')
img3 = image3.resize((170, 110))
my_img3 = ImageTk.PhotoImage(img3)
label_image3 = Label(window, image=my_img3)

# image 4 png
image4 = Image.open('image4.png')
img4 = image4.resize((180, 130))
my_img4 = ImageTk.PhotoImage(img4)
label_image4 = Label(window, image=my_img4)

# hand image
hand_image = Image.open('hand.png')
hand = hand_image.resize((70, 70))
hand_img = ImageTk.PhotoImage(hand)
label_hand_image = Label(window, image=hand_img)

# image 5 png
image5 = Image.open('image5.png')
my_img5 = ImageTk.PhotoImage(image5)
label_image5 = Label(window, image=my_img5)

# "Hi Crush" label -------------------------------------------------------------
label1 = Label(window,
               text="HI CRUSH",
               font=('Arial', 30),
               fg='red',
               bg="white",)
label1.pack()
# positing the label 1
label1.place(x=150, y=130)

# "I like you a lot, wanna go on a date?" label ----------------------------------------
label2 = Label(window,
               text="I like you a lot, wanna go on a date?",
               font=('Arial', 15),
               bg="white")
label2.pack()
# positing the label 2
label2.place(x=90, y=180)

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
                   command=no,
                   font=("Comic Sans", 16),
                   bg="white",
                   width=6,
                   height=1)
button_no.pack()
# positing the no button
button_no.place(x=280, y=240)

window.mainloop()