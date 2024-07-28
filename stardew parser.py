# stardew parser v 0.1

import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
import re

class MainMenu():
    def __init__(self, master):
        self.master = master
        self.master.title('Stardew Valley QuickSearch')

        self.WelcomeLabel = Label(self.master,text='WELCOME', font=("Helvetica", 20)).grid(row=0,column=0)
        self.Description = Label(self.master,text="This is the Stardew Valley Quick Search tool!", font=("Helvetica", 16)).grid(row=1,column=0)

        self.CharacterButton = Button(self.master,text="Character Info",command=self.CH,width=20).grid(row=2,column=0)
        self.ItemButton = Button(self.master,text="Item Info",command=self.CloseMenu,width=20).grid(row=3,column=0)
        self.FishButton = Button(self.master,text="Fish Info",command=self.CloseMenu,width=20).grid(row=4,column=0)
        self.CropButton = Button(self.master,text="Crop Info",command=self.CloseMenu,width=20).grid(row=5,column=0)

    def CloseMenu(self):
        self.master.destroy()
        Window = tk.Tk()
        return Window

    def CH(self):
        CharacterMenu(self.CloseMenu())
        
class InformationMenu():
    def __init__(self, master):
        self.master = master
        self.Content = []

        self.InfoLabel = Label(self.master,text='Enter the name of the villager you would like to search for', font=("Helvetica", 16)).grid(row=0,column=0)
        self.Text = StringVar()
        self.EntryBox = Entry(self.master, textvariable=self.Text, width=30).grid(row=1,column=0)
        self.ConfirmButton = Button(self.master,text="Submit",command=self.Search,width=20).grid(row=2,column=0)

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

        print(self.CleanText(self.InfoList[0]))

    def CleanText(self, Text):
        # https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
        RE_Tag = re.compile(r'<[^>]+>')
        return RE_Tag.sub('', Text)

class CharacterMenu(InformationMenu):
    def __init__(self, master):
        InformationMenu.__init__(self, master)
        self.master = master
        self.master.title("Character Information")
        self.Content = ["Birthday", "Lives In", "Address", "Marriage", "Loved Gifts"]
 
def main():
    Window = tk.Tk()
    GUI = MainMenu(Window)
    Window.mainloop()

if __name__ == '__main__':
    main()
