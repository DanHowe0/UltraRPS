from tkinter import *
import json

class Game:
  def __init__(self):
    self.window = Tk()
    
    self.name = StringVar()
    self.choice = StringVar()
    
    self.user_data = {}
    
  def show(self):
    Label(self.window, text="Ultra Rock Paper Scissors\nby Legacy Coding Studios\n").grid(row=0, column=0, columnspan=3)

    Label(self.window, text="Please enter your name and choice of weopan\nThen press NEXT to go to the next player or DONE when everyone has entered their weopan.\nREMEMBER THIS SELECTION AS YOU WILL ALL REVEAL YOUR CHOICES LIKE NORMAL ROCK PAPER SCISSORS").grid(row=1, column=0, columnspan=3)

    OPTIONS = ["Rock", "Gun", "Lightning", "Devil", "Dragon", "Water", "Air", "Paper", "Sponge", "Wolf", "Tree", "Human", "Snake", "Scissors", "Fire"]
    

    Label(self.window, text="Name: ").grid(row=2, column=0)
    Entry(self.window, textvariable=self.name).grid(row=2, column=1, columnspan=2)
    
    #OptionMenu(self.window, self.name, *PLAYERS).grid(row=2, column=1, columnspan=2)

    Label(self.window, text="Choice: ").grid(row=3, column=0)
    OptionMenu(self.window, self.choice, *OPTIONS).grid(row=3, column=1, columnspan=2)

    self.error = Label(self.window, text="")
    self.error.grid(row=4, column=0, columnspan=3)

    Button(self.window, text="NEXT", command=self.next).grid(row=5, column=1)
    Button(self.window, text="DONE", command=self.done).grid(row=5, column=2)

    self.window.mainloop()

  def next(self):
    name = self.name.get()
    choice = self.choice.get()

    print(name, choice)

    if name == "" or choice == "":
      self.error["text"] = "PLEASE ENTER A VALUE FOR ALL FIELDS!"
    else:
      self.error["text"] = ""
      self.name.set("")
      self.choice.set("")

      self.user_data.update({name: {"choice": choice, "score": 0}})
  
  def check(self, first, second):
    with open("data.json", "r") as f:
      data = json.load(f)
      
      first = first.lower()
      second=second.lower()
      
      if second in data[first]:
        return 1
      else:
        return 0

  def done(self):
    self.user_data.update({self.name.get(): {"choice": self.choice.get(), "score": 0}})
    self.window.destroy()

    choices = self.user_data

    for i in choices:
      for j in choices:
        if i == j:
          pass
        else:
          

          add = self.check(choices[i]["choice"], choices[j]["choice"])
          
          score = choices[i]["score"]
          score += add
          choices[i]["score"] = score
    
    window = Tk()

    Label(window, text="Ultra Rock Paper Scissors\nby Legacy Coding Studios\n").grid(row=0, column=0, columnspan=3)

    Label(window, text="Now play the Rock Paper Scissors using the hand signals so everyone knows what you all picked").grid(row=1, column=0, columnspan=3)

    Button(window, text="Done", command=window.destroy).grid(row=2, column=1)

    window.mainloop()

    window = Tk()

    Label(window, text="Ultra Rock Paper Scissors\nby Legacy Coding Studios\n").grid(row=0, column=0, columnspan=3)

    Label(window, text="NAME").grid(row=1, column=0)
    Label(window, text="CHOICE").grid(row=1, column=1)
    Label(window, text="SCORE").grid(row=1, column=2)

    row = 2

    for i in choices:
      Label(window, text=i).grid(row=row, column=0)
      Label(window, text=choices[i]["choice"]).grid(row=row, column=1)
      Label(window, text=choices[i]["score"]).grid(row=row, column=2)

      row += 1

    Button(window, text="Finish", command=window.destroy).grid(row=row, column=1)

    window.mainloop()


mainboard = Game()
mainboard.show()