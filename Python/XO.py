from tkinter import*
import random

def next_turn (row , col) :
#function take number of row or col where put in it X , O
 global player 
 if game_buton[row][col]["text"] == "" and check_wineer()==False:
    if player == players[0]:
        game_buton[row][col]["text"]=player
        if check_wineer()==False:
            player = players[1]
            label.config(text=(players[1] + " turn"))
        elif check_wineer()==True:
            label.config(text=(players[0] + " wins!"))
        elif check_wineer()=="tie":
            label.config(text=("tie , No winner!"))
    elif player == players[1]:
        game_buton[row][col]["text"]=player
        if check_wineer()==False:
            player = players[0]
            label.config(text=(players[0] + " turn"))
        elif check_wineer()==True:
            label.config(text=(players[1] + " wins!"))
        elif check_wineer()=="tie":
            label.config(text=("tie , No winner!" )) 



           
def check_wineer():
#function check_wineer
    for row in range(3) :
        if game_buton[row][0]["text"] == game_buton[row][1]["text"] ==game_buton[row][2]["text"]!="":
             game_buton[row][0].config(bg="cyan")
             game_buton[row][1].config(bg="cyan")
             game_buton[row][2].config(bg="cyan")
             return True 
    for col in range(3) :
      if game_buton[0][col]["text"] == game_buton[1][col]["text"] ==game_buton[2][col]["text"]!="":
        game_buton[0][col].config(bg="cyan")
        game_buton[1][col].config(bg="cyan")
        game_buton[2][col].config(bg="cyan")
        return True
    if game_buton[0][0]['text'] == game_buton[1][1]['text'] == game_buton[2][2]['text'] != "":
        game_buton[0][0].config(bg="cyan")
        game_buton[1][1].config(bg="cyan")
        game_buton[2][2].config(bg="cyan")
        return True
    elif game_buton[0][2]['text'] == game_buton[1][1]['text'] == game_buton[2][0]['text'] != "":
        game_buton[0][2].config(bg="cyan")
        game_buton[1][1].config(bg="cyan")
        game_buton[2][0].config(bg="cyan")
        return True
    if check_empty_spacess()== False:
        for row in range (3):
            for col in range (3):
                game_buton[row][col].config(bg = "red")
        return"tie"
    else  :
        return False        




def check_empty_spacess():
#function check_empty_spacess
   space = 9
   for row in range (3):
       for col in range (3):
           if game_buton[row][col]["text"]!= "":
               space -=1
   if space == 0:
       return False
   else : 
       return True

def start_new_game():
#function to restart the game
    global player
    player = random.choice(players)
    for row in range (3):
       for col in range (3):
           game_buton[row][col].config(text= "",bg="#F0F0F0")
window = Tk()   # class to create window of the game
window.title("XO") 
players =["x" , "o"] #variable
player = random.choice(players) #choice random variable of playesrs to start the game
game_buton = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

label = Label(text=(player + " turn"), font=('consolas', 40))
label.pack(side="top")
restart_buton = Button(text = "restart" , font=('consolas', 20) , command=start_new_game)
restart_buton.pack(side = "top")
buton_frame = Frame (window)
buton_frame.pack()
for row in range(3):
    for col in range (3):
        game_buton[row][col] = Button( buton_frame , text = "" ,font=('consolas', 50) , width=4 , height= 1 , 
                                       command= lambda row= row , col= col  : next_turn (row , col) )
        game_buton[row][col].grid(row=row,column=col)
     

window.mainloop() #to make window open 

