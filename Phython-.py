from tkinter import *
from PIL import ImageTk,Image
import random
root=Tk()
root.title("Endless Pokemon Card Game")
root.geometry("700x600")
root.configure(background='#FEA500')
Abra=ImageTk.PhotoImage(Image.open ("abra.jpg"))
Bulbasour=ImageTk.PhotoImage(Image.open ("bulbasour.jpg"))
Charmender=ImageTk.PhotoImage(Image.open ("charmender.jpg"))
Iyvasour=ImageTk.PhotoImage(Image.open ("Iyvasour.jpg"))
Jigglypuff=ImageTk.PhotoImage(Image.open ("jigglypuff.jpg"))
Kadabra=ImageTk.PhotoImage(Image.open ("kadabra.jpg"))
Meowth=ImageTk.PhotoImage(Image.open ("meowth.jpg"))
Nidoking=ImageTk.PhotoImage(Image.open ("nidoking.jpg"))
Paras=ImageTk.PhotoImage(Image.open ("paras.jpg"))
Persion=ImageTk.PhotoImage(Image.open ("persion.jpg"))
Pikachu=ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
Ratata=ImageTk.PhotoImage(Image.open ("ratata.jpg"))
Squirtle=ImageTk.PhotoImage(Image.open ("squirtle.jpg"))
btn_img=ImageTk.PhotoImage(Image.open ("button.jpg"))

player1 = Label(root, text = "Player 1", bg = "red", fg = "white")
player1.place(relx = 0.1, rely = 0.3 , anchor =  CENTER)

player2 = Label(root, text = "Player 2", bg = "red", fg = "white")
player2.place(relx = 0.9, rely = 0.3 , anchor =  CENTER)

player_1_score_label = Label(root , bg = "royal blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4 , anchor =  CENTER)

player_2_score_label = Label(root , bg = "royal blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4 , anchor =  CENTER)

pokemon_list = [Pikachu,Bulbasour,Abra,Charmender,Iyvasour,Jigglypuff,Kadabra,Meowth,Nidoking,Paras,Persion,Pikachu,Ratata,Squirtle]
power_pokemon = [200,60,300,50,100,70,70,60,90,40,70,200,40,50]

random_card = Label(root)
random_card.place(relx = 0.5, rely = 0.5 , anchor =  CENTER)

player1_score = 0
def player1():
    global player1_score
    random_no = random.randint(1,14)
    random_card['image']=pokemon_list[random_no]
    player1_score=player1_score+power_pokemon[random_no]
    player_1_score_label['text']=str(player1_score)
    
player_1_btn = Button(root, image = btn_img, command = player1)
player_1_btn.place(relx = 0.1, rely = 0.6 , anchor =  CENTER)

player2_score = 0
def player2():
    global player2_score
    random_no = random.randint(1,14)
    random_card['image']=pokemon_list[random_no]
    player2_score=player2_score+power_pokemon[random_no]
    player_2_score_label['text']=str(player2_score)
    
player_2_btn = Button(root, image = btn_img, command = player2)
player_2_btn.place(relx = 0.9, rely = 0.6 , anchor =  CENTER)

root.mainloop()