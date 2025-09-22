from tkinter import *
from PIL import Image, ImageTk
import speech_conversion
import action
root = Tk()
root.title("U-Phoria the AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#89CFF0")

def ask():
    user_value = speech_conversion.speech_conversion()
    bot_value = action.action(user_value)
    chatbox.insert(END, "User ------> " + str(user_value) + "\n")
    if bot_value is not None:
        chatbox.insert(END, "BOT <------ " + str(bot_value) + "\n")

def send():
    send = entry.get()
    bot = action.action(send)
    chatbox.insert(END, "User ------> " + str(send) + "\n")
    if bot is not None:
        chatbox.insert(END, "BOT <------ " + str(bot) + "\n")

def delete():
    chatbox.delete('1.0' , "end")

#frame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#89CFF0")
frame.grid(row=0, column=1, padx=55, pady=10)

#title
text_label = Label(frame, text="U-Phoria the AI Assistant", font=("Times New Roman", 14, "bold"), bg="#F4C2C2")
text_label.grid(row=0, column=0, padx=20, pady=10)

#image
img=ImageTk.PhotoImage(Image.open("image/assistant.png"))
image_label = Label(frame, image=img)
image_label.grid(row=1, column=0, pady=10)

#chatbox
chatbox = Text(root, font=("Garamond", 8, "bold"), bg="#F4C2C2", wrap="word")
chatbox.grid(row=2, column=0)
chatbox.place(x=100, y=375, width=375, height=100)

#entry
entry = Entry(root, justify=CENTER)
entry.place(x=100, y=500, width=350, height=30)

#button1
button_one = Button(root, text="ASK", bg="#F4C2C2", padx=40, pady=16, borderwidth=3, relief=SOLID, command=ask)
button_one.place(x=70, y=575)

#button2
button_two = Button(root, text="SEND", bg="#F4C2C2", padx=40, pady=16, borderwidth=3, relief=SOLID, command=send)
button_two.place(x=400, y=575)

#button3
button_three = Button(root, text="DELETE", bg="#F4C2C2", padx=40, pady=16, borderwidth=3, relief=SOLID, command=delete)
button_three.place(x=225, y=575)

root.mainloop()