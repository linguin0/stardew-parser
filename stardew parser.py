# stardew parser v 0.1

import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *

class MainMenu():
    def __init__(self, master):
        self.master = master
        self.master.title('Stardew Valley QuickSearch')

        self.WelcomeLabel = Label(self.master,text='WELCOME', font=("Helvetica", 20)).grid(row=0,column=0)
        self.Description = Label(self.master,text="This is the Stardew Valley Quick Search tool!", font=("Helvetica", 16)).grid(row=1,column=0)

        self.CharacterButton = Button(self.master,text="Character Info",command=self.CloseMenu,width=20).grid(row=2,column=0)
        self.ItemButton = Button(self.master,text="Item Info",command=self.CloseMenu,width=20).grid(row=3,column=0)
        self.FishButton = Button(self.master,text="Fish Info",command=self.CloseMenu,width=20).grid(row=4,column=0)
        self.CropButton = Button(self.master,text="Crop Info",command=self.CloseMenu,width=20).grid(row=5,column=0)

    def CloseMenu(self):
        self.master.destroy()
        Window = tk.Tk()
        GUI = InformationMenu(Window)
        
class InformationMenu():
    def __init__(self, master):
        self.master = master
        self.MenuTitle = ""
        self.Content = []
        
        self.Text = StringVar()
        self.EntryBox = Entry(self.master, textvariable=self.Text).grid(row=0,column=0)
        self.ConfirmButton = Button(self.master,text="Submit",command=self.Search,width=20).grid(row=1,column=0)

    def Search(self):
        self.InfoList = []
        Url_Beginning = 'https://stardewvalleywiki.com'

        result = requests.get(Url_Beginning + "/{}".format(self.Text.get().capitalize()))
        doc = BeautifulSoup(result.text, 'html.parser')

        info = doc.find_all(id="infoboxdetail")
        for I in info:
            parent = I.parent
            info = parent.find(id="infoboxdetail").get_text()
            self.InfoList.append(info.replace("\n", ""))

def main():
    Window = tk.Tk()
    GUI = MainMenu(Window)
    Window.mainloop()

if __name__ == '__main__':
    main()
