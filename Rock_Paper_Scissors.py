'''
Created on Mar 5, 2019

@author: s271486
'''
#simple Gui
from tkinter import *
root = Tk()
import random

Label(root, text="Choose Rock, Paper, or Scissors.")
Label.pack()

#Create a random number
RockLabel1= Label(root, text="Congratulations!, Computer chose: Scissors")
RockLabel2= Label(root, text="Aww too bad!, Computer chose: Paper") 
RockLabel3= Label(root, text="It's a draw!!, Computer chose: Rock") 

def Rock():
    computer = random.randint(1,3)
    if computer ==1:
        RockLabel1.pack()
    if computer == 2:
        RockLabel2.pack()
    if computer == 3:
        RockLabel3.pack()

PaperLabel1= Label(root, text="Congratulations!, Computer chose: Rock")
PaperLabel2= Label(root, text="Aww too bad!, Computer chose: Scissors") 
PaperLabel3= Label(root, text="It's a draw!!, Computer chose: Paper") 
        
def Paper():
    computer = random.randint(1,3)
    if computer ==1:
        PaperLabel1.pack()
    if computer == 2:
        PaperLabel2.pack()
    if computer == 3:
        PaperLabel3.pack()    

ScissorsLabel1= Label(root, text="Congratulations!, Computer chose: Paper")
ScissorsLabel2= Label(root, text="Aww too bad!, Computer chose: Rock") 
ScissorsLabel3= Label(root, text="It's a draw!!, Computer chose: Scissors") 
        
def Scissors():
    computer = random.randint(1,3)
    if computer ==1:
        ScissorsLabel1.pack()
    if computer == 2:
        ScissorsLabel2.pack()
    if computer == 3:
        ScissorsLabel3.pack()    
        
SelectRock = Button(root, text="Rock", command=Rock)  
SelectPaper = Button(root, text="Paper", command=Paper)
SelectScissors = Button(root, text="Scissors", command=Scissors)

SelectRock.pack()
SelectPaper.pack()
SelectScissors.pack()
      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

#Kick the code
root.mainloop()