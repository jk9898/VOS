## VOS ##
#-------------------------------------------------------------------------------#
# Name:        Exodus VOS                                                       #
# Purpose:     Provide a sleek interface using Tkinter                          #
#                                                                               #
# Author:      JG Technologies                                                  #
#                                                                               #
# Created:     18/01/2015                                                       #
# Copyright:   (c) JG Technologies                                              #
# Licence:     GNU General Public License                                       #
#-------------------------------------------------------------------------------#

import math, time, os, sys, Tkinter, shutil, urllib2

from urllib2 import Request, urlopen, URLError, HTTPError

from Tkinter import *
from os import walk

sys.path.append('./data/login/users')
sys.path.append('./data/bin')
sys.path.append('./data/bin/icons')
sys.path.append('./data/bin/')
sys.path.append('.')
f = []
import optionsWin

class OS:
    def callback(self, event):
        if self.var1 == True:
            pass
        else:
            self.deskclickList = Listbox(self.desktopWindow, height = 1)
            self.deskclickList.insert(END, "= Options =")
            self.x, self.y = event.x, event.y
            self.deskclickList.place(x = self.x, y = self.y)
            self.deskclickList.lift()
            self.deskclickList.bind("<<ListboxSelect>>", lambda x: OS.rightclickSelect(self))
            self.var1 = True

    def rightstartDestroy(self):
        if self.var1 == True:
            self.deskclickList.destroy()
            self.var1 = False
        elif self.var1 == False:
            pass
        if self.var2 == True:
            self.startList.lower()
        else:
            pass

    def usercreate1(self):
        PATH = './data/login/users/' + str(self.userBox3.get()) + ".dll"
        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            print "Account already exists"
        else:
            fle = open(PATH, 'w+')
            fle.write(str(self.passBox3.get()))
            fle.close()
            self.warnWin11 = Tk()
            self.warnWin11.iconbitmap("./data/bin/icons/tick.ico")
            self.warnWin11.title("Notification")
            self.warnWin11.geometry("390x150")

            self.warnLabel9 = Label(self.warnWin11, text = "Settings saved." + "\n" + "You may now login using the new credentials.")
            self.warnLabel9.place(x = 70, y = 30)

            os.mkdir('./data/bin/system/' + str(self.userBox3.get()))

            PATH1 = ("./data/bin/system/" + self.userBox3.get() + "/background")
            if os.path.isfile(PATH1) and os.access(PATH1, os.R_OK):
                pass
            else:
                os.mkdir(PATH1)

            self.warnBut9 = Button(self.warnWin11, text = "Okay", width = 10, command = lambda: (self.accCreateScreen.destroy(), self.createWindow.destroy(), self.warnWin11.destroy(), OS.osLogin(self)))
            self.warnBut9.place(x = 150, y = 100)

    def accCreateUs(self):
        self.accCreateScreen = Tk()
        self.accCreateScreen.title("New Account")
        self.accCreateScreen.geometry("200x200")
        self.accCreateScreen.iconbitmap("./data/bin/icons/plus.ico")
        self.accCreateScreen.resizable(width = FALSE, height = FALSE)

        self.userLabel3 = Label(self.accCreateScreen, text = "New Username:")
        self.userLabel3.place(x = 55, y = 15)

        self.userBox3 = Entry(self.accCreateScreen)
        self.userBox3.place(x = 40, y = 40)
        self.userBox3.focus_set()

        self.passLabel3 = Label(self.accCreateScreen, text = "New Password:")
        self.passLabel3.place(x = 55, y = 70)

        self.passBox3 = Entry(self.accCreateScreen, show = "*")
        self.passBox3.place(x = 40, y = 100)

        self.loginButton3 = Button(self.accCreateScreen, text = "Okay", width = 15, command = lambda: OS.usercreate1(self))
        self.loginButton3.place(x = 43, y = 150)


    def delacc(self):
        PATH = "./data/login/users/" + str(self.userBox2.get()) + ".dll"
        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            fle = open('./data/login/users/' + str(self.userBox2.get()) + ".dll")
            password = fle.readlines()[0]
            fle.close()
            if password == self.passBox2.get():
                os.remove("./data/login/users/" + self.userBox2.get() + ".dll")
                PATH1 = "./data/bin/system/" + self.userBox2.get()
                shutil.rmtree(PATH1)
                self.warnWin10 = Tk()
                self.warnWin10.iconbitmap("./data/bin/icons/tick.ico")
                self.warnWin10.title("Notification")
                self.warnWin10.geometry("290x100")

                self.warnLabel8 = Label(self.warnWin10, text = "Deleted." + "\n" + "This command cannot be undone.")
                self.warnLabel8.place(x = 20, y = 10)

                self.warnBut8 = Button(self.warnWin10, text = "Okay", width = 10, command = lambda: self.warnWin10.destroy())
                self.warnBut8.place(x = 105, y = 60)
            else:
                print "Wrong password"
        else:
            self.warnWin9 = Tk()
            self.warnWin9.iconbitmap("./data/bin/icons/error.ico")
            self.warnWin9.title("Notification")
            self.warnWin9.geometry("290x100")

            self.warnLabel7 = Label(self.warnWin9, text = "Cannot delete." + "\n" + "Reason: Account does not exist.")
            self.warnLabel7.place(x = 60, y = 10)

            self.warnBut7 = Button(self.warnWin9, text = "Okay", width = 10, command = lambda: self.warnWin9.destroy())
            self.warnBut7.place(x = 105, y = 60)

    def userAccDel(self):
        self.useracc = Tk()
        self.useracc.title("Details")
        self.useracc.iconbitmap("./data/bin/icons/minus.ico")
        self.useracc.geometry("200x200")

        self.userLabel2 = Label(self.useracc, text = "Username:")
        self.userLabel2.place(x = 70, y = 15)

        self.userBox2 = Entry(self.useracc)
        self.userBox2.place(x = 40, y = 40)
        self.userBox2.focus_set()

        self.passLabel2 = Label(self.useracc, text = "Password:")
        self.passLabel2.place(x = 70, y = 70)

        self.passBox2 = Entry(self.useracc, show = "*")
        self.passBox2.place(x = 40, y = 100)

        self.okayButton2 = Button(self.useracc, text = "Okay", width = 15, command = lambda: OS.delacc(self))
        self.okayButton2.place(x = 43, y = 150)
        self.useracc.focus_force()

    def createWindow1(self):
        self.createWindow1.destroy()
        self.createWindow1 = Tk()
        self.createWindow1.iconbitmap("./data/bin/icons/accountmanager.ico")
        self.createWindow1.title("Account Manager")
        self.createWindow1.geometry("400x400")

        self.createWindow1.resizable(width = FALSE, height = FALSE)
        self.newUserLabel = Label(self.createWindow1, text = "Current Users:")
        self.newUserLabel.place(x = 10, y = 10)
        self.accountsPath = './data/login/users'

        self.userList1 = Listbox(self.createWindow1)
        for f in os.listdir(self.accountsPath):
            a = f.split(".")[0]
            self.userList1.insert(END, a)
            self.userList1.place(x = 12, y = 30)
        self.userList1.bind("<<ListboxSelect>>")

        self.userOkay2 = Button(self.createWindow1, text = "Okay", width = 12, height = 1, command = lambda: (self.createWindow1.destroy(), OS.osLogin(self)))
        self.userOkay2.place(x = 70, y = 360),

        self.userCancel1 = Button(self.createWindow1, text = "Cancel", width = 12, height = 1, command = lambda: OS.changeCancel1(self))
        self.userCancel1.place(x = 225, y = 360)

        self.newUser1Label = Label(self.createWindow1, text = "New Username:")
        self.newUser1Label.place(x = 150, y = 10)

        self.newUser1Entry = Entry(self.createWindow1)
        self.newUser1Entry.place(x = 153, y = 40)
        self.newUser1Entry.focus_set()

        self.newPassLabel = Label(self.createWindow1, text = "New Password:")
        self.newPassLabel.place(x = 150, y = 70)

        self.newPass1Entry = Entry(self.createWindow1, show = "*")
        self.newPass1Entry.place(x = 153, y = 100)

        self.newPass2Label = Label(self.createWindow1, text = "Confirm Password:")
        self.newPass2Label.place(x = 150, y = 130)

        self.newPass2Entry = Entry(self.createWindow1, show = "*")
        self.newPass2Entry.place(x = 153, y = 160)

        self.newUserPassButt = Button(self.createWindow1, text = "Save Changes", width = 16, command = lambda: OS.passSave(self))
        self.newUserPassButt.place(x = 153, y = 190)
        self.newUserPassButt.bind("<Return>", lambda x: OS.passSave(self))

        self.textVar1 = "This is the User Accounts control panel." + "\n" + "From this screen you can change an accounts credentials," + "\n" + "Or create a new account."
        self.textVar2 = "Once you have finished," + "\n" + "click 'Okay' to save your changes."

        self.infoLabel1 = Label(self.createWindow1, text = self.textVar1)
        self.infoLabel1.place(x = 50, y = 230)

        self.infoLabel2 = Label(self.createWindow1, text = self.textVar2)
        self.infoLabel2.place(x = 115, y = 300)

        self.createWindow1.focus_force()
        self.userOkay1.focus_force()

    def passSave(self):
        if self.newPass1Entry.get() == self.newPass2Entry.get():
            os.rename("./data/login/users/" + str(self.userList1.selection_get()) + ".dll", "./data/login/users/" + str(self.newUser1Entry.get()) + ".dll")
            fle = open("./data/login/users/" + str(self.newUser1Entry.get()) + ".dll", "w")
            fle.write(str(self.newPass1Entry.get()))
            fle.close()

            self.warnWin6 = Tk()
            self.warnWin6.title("Notification")
            self.warnWin6.geometry("390x150")
            self.warnWin6.iconbitmap("./data/bin/icons/tick.ico")

            self.warnLabel4 = Label(self.warnWin6, text = "Settings saved." + "\n" + "You may now login using the new credentials.")
            self.warnLabel4.place(x = 90, y = 30)

            self.warnBut4 = Button(self.warnWin6, text = "Okay", width = 10, command = lambda: self.warnWin6.destroy())
            self.warnBut4.place(x = 150, y = 90)
        else:
            self.warnWin7 = Tk()
            self.warnWin7.title("Notification")
            self.warnWin7.geometry("390x150")
            self.warnWin7.iconbitmap("./data/bin/icons/error.ico")

            self.warnLabel5 = Label(self.warnWin7, text = "Passwords must match!")
            self.warnLabel5.place(x = 150, y = 10)

            self.warnBut5 = Button(self.warnWin7, text = "Okay", width = 10, command = lambda: self.warnWin7.destroy())
            self.warnBut5.place(x = 130, y = 70)

    def changeCancel1(self):
        self.createWindow1.destroy()
        OS().osLogin()

    def changeCancel(self):
        self.createWindow.destroy()
        OS().osLogin()

    def createUser1(self):
        self.userPass.destroy()
        self.x = 1
        self.userOkay1 = Tk()
        self.userOkay1.title("Notification")
        self.userOkay1.geometry("290x100")
        self.userOkay1.iconbitmap("./data/bin/icons/tick.ico")

        self.userOkay1Label = Label(self.userOkay1, text = "You may now manage your account.")
        self.userOkay1Label.place(x = 40, y = 10)

        self.userOkay1Button = Button(self.userOkay1, width = 10, text = "Okay", command = lambda: self.userOkay1.destroy())
        self.userOkay1Button.place(x = 100, y = 40)

        OS.createWindow1(self)

    def passCheck(self):
        self.userPassvar = open('./data/login/users/' + self.userList.selection_get() + ".dll")
        self.password = self.userPassvar.readlines()[0]
        if self.userPassBox.get() == self.password:
            OS.createUser1(self)
            self.userPassvar.close()
        else:
            self.warnWin5 = Tk()
            self.warnWin5.title("Notification")
            self.warnWin5.geometry("390x100")
            self.userPass.destroy()
            self.warnWin5.iconbitmap("./data/bin/icons/error.ico")

            self.warnWin5Label = Label(self.warnWin5, text = "Incorrect password, please try again.")
            self.warnWin5Label.place(x = 100, y = 10)
            self.warnWin5Button = Button(self.warnWin5, text = "Okay", width = 10, command = lambda: self.warnWin5.destroy())
            self.warnWin5Button.place(x = 155, y = 60)
            self.userPassvar.close()

    def changeUser(self):
        self.userPass = Tk()
        self.userPass.title("Notification")
        self.userPass.geometry("390x150")
        self.userPass.iconbitmap("./data/bin/icons/error.ico")

        self.userPassLabel = Label(self.userPass, text = "You must enter the account password to configure the account.")
        self.userPassLabel.place(x = 20, y = 10)

        self.userPassBox = Entry(self.userPass, show = "*")
        self.userPassBox.place(x = 130, y = 40)

        self.userPassButton = Button(self.userPass, text = "Enter", width = 10, anchor = "n", command = lambda: OS.passCheck(self))
        self.userPassButton.place(x = 150, y = 70)
        self.userPassBox.bind("<Return>", lambda x: OS.passCheck(self))

    def createUser(self):
        self.loginScreen.destroy()
        self.createWindow = Tk()
        self.createWindow.iconbitmap("./data/bin/icons/accountmanager.ico")
        self.createWindow.title("Account Manager")
        self.createWindow.geometry("400x400")

        self.createWindow.resizable(width = FALSE, height = FALSE)
        self.newUserLabel = Label(self.createWindow, text = "Current Users:")
        self.newUserLabel.place(x = 10, y = 10)
        self.accountsPath = './data/login/users'

        self.userList = Listbox(self.createWindow)
        for f in os.listdir(self.accountsPath):
            a = f.split(".")[0]
            self.userList.insert(END, a)
            self.userList.place(x = 12, y = 30)
        self.userList.bind("<<ListboxSelect>>", lambda x: OS.changeUser(self))

        self.textVar1 = "This is the User Accounts control panel." + "\n" + "From this screen you can change an accounts credentials," + "\n" + "Or create a new account."
        self.textVar2 = "Once you have finished," + "\n" + "click 'Okay' to save your changes."

        self.infoLabel1 = Label(self.createWindow, text = self.textVar1)
        self.infoLabel1.place(x = 50, y = 210)

        self.infoLabel2 = Label(self.createWindow, text = self.textVar2)
        self.infoLabel2.place(x = 115, y = 280)

        self.accCreate = Label(self.createWindow, text = "Create Account:")
        self.accCreate.place(x = 230, y = 30)

        self.createNewAccB = Button(self.createWindow, text = "Create New Account", width = 20, command = lambda: OS.accCreateUs(self))
        self.createNewAccB.place(x = 200, y = 50)

        self.accDel = Label(self.createWindow, text = "Delete An Account:")
        self.accDel.place(x = 225, y = 100)

        self.createNewAccB1 = Button(self.createWindow, text = "Delete Account", width = 20, command = lambda: OS.userAccDel(self))
        self.createNewAccB1.place(x = 200, y = 120)

        self.userOkay2 = Button(self.createWindow, text = "Okay", width = 12, height = 1, command = lambda: (self.createWindow.destroy(), OS.osLogin(self)))
        self.userOkay2.place(x = 70, y = 360)

        self.userCancel1 = Button(self.createWindow, text = "Cancel", width = 12, height = 1, command = lambda: OS.changeCancel(self))
        self.userCancel1.place(x = 225, y = 360)

    def timeUpdate(self):
        now = time.strftime("%H:%M:%S")
        date = time.strftime("%d/%m/%Y")
        self.dateTime.configure(text = now)
        self.currentDateLabel.configure(text = date)
        self.timeDateBox.after(1000, self.timeUpdate)

    def timeClick(self):
        self.timeDateBox = Tk()
        self.timeDateBox.title("Time and Date")
        self.timeDateBox.geometry("400x300")

        self.timeDateLabel1 = Label(self.timeDateBox, text = "This is the current date/time," + "\n" + "You can set your time zone in the options menu.")
        self.timeDateLabel1.place(x = 65, y = 10)

        self.dateTimeOptions = Button(self.timeDateBox, text = "Settings", height = 1,command = lambda: OS.optionsClick(self))
        self.dateTimeOptions.place(x = 345, y = 273)

        self.timeLabel = Label(self.timeDateBox, text = "Current Time:", font = "20")
        self.timeLabel.place(x = 145, y = 50)

        self.dateTimeOkay = Button(self.timeDateBox, text = "Okay", height = 1, command = lambda: self.timeDateBox.destroy())
        self.dateTimeOkay.place(x = 0, y = 273)

        self.dateTime = Label(self.timeDateBox, text = "", font = "100")
        self.dateTime.place(x = 160, y = 80)

        self.dateLabel = Label(self.timeDateBox, text = "Current Date:", font = "20")
        self.dateLabel.place(x = 145, y = 110)

        self.currentDateLabel = Label(self.timeDateBox, text = "", font = "20")
        self.currentDateLabel.place(x = 153, y = 140)
        OS.timeUpdate(self)

        self.timeDateBox.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        hour = time.strftime("%H")
        self.taskBarTime.configure(text="Time: " + now)
        self.desktopWindow.after(1000, self.update_clock)

    def createUser4(self):
        self.createWindow1 = Tk()
        self.createWindow1.iconbitmap("./data/bin/icons/accountmanager.ico")
        self.createWindow1.title("Account Manager")
        self.createWindow1.geometry("400x400")

        self.createWindow1.resizable(width = FALSE, height = FALSE)
        self.newUserLabel = Label(self.createWindow1, text = "Current Users:")
        self.newUserLabel.place(x = 10, y = 10)
        self.accountsPath = './data/login/users'

        self.userList = Listbox(self.createWindow1)
        for f in os.listdir(self.accountsPath):
            a = f.split(".")[0]
            self.userList.insert(END, a)
            self.userList.place(x = 12, y = 30)
        self.userList.bind("<<ListboxSelect>>", lambda x: OS.changeUser(self))

        self.textVar1 = "This is the User Accounts control panel." + "\n" + "From this screen you can change an accounts credentials," + "\n" + "Or create a new account."
        self.textVar2 = "Once you have finished," + "\n" + "click 'Okay' to save your changes."

        self.infoLabel1 = Label(self.createWindow1, text = self.textVar1)
        self.infoLabel1.place(x = 50, y = 210)

        self.infoLabel2 = Label(self.createWindow1, text = self.textVar2)
        self.infoLabel2.place(x = 115, y = 280)

        self.accCreate = Label(self.createWindow1, text = "Create Account:")
        self.accCreate.place(x = 230, y = 30)

        self.createNewAccB = Button(self.createWindow1, text = "Create New Account", width = 20, command = lambda: OS.accCreateUs(self))
        self.createNewAccB.place(x = 200, y = 50)

        self.accDel = Label(self.createWindow1, text = "Delete An Account:")
        self.accDel.place(x = 225, y = 100)

        self.createNewAccB1 = Button(self.createWindow1, text = "Delete Account", width = 20, command = lambda: OS.userAccDel(self))
        self.createNewAccB1.place(x = 200, y = 120)

        self.userOkay2 = Button(self.createWindow1, text = "Okay", width = 12, height = 1, command = lambda: self.createWindow1.destroy())
        self.userOkay2.place(x = 70, y = 360)

        self.userCancel1 = Button(self.createWindow1, text = "Cancel", width = 12, height = 1, command = lambda: self.createWindow1.destroy())
        self.userCancel1.place(x = 225, y = 360)


    def startSelection(self):
        startChoice = self.startList.selection_get()
        if startChoice == "= Settings =":
            self.startList.lower()
            OS.optionsClick(self)
        elif startChoice == "= Shutdown =":
            self.warnWin4 = Tk()
            self.warnWin4.iconbitmap("./data/bin/icons/error.ico")
            self.warnWin4.title("WARNING")
            self.warnWin4.geometry("390x150")

            self.warnLabel3 = Label(self.warnWin4, text = "Are you sure you want to shutdown?")
            self.warnLabel3.place(x = 95, y = 15)

            self.warnBut2 = Button(self.warnWin4, text = "Yes", width = 10, command = lambda: (self.warnWin4.destroy(), self.desktopWindow.destroy()))
            self.warnBut2.place(x = 100, y = 80)

            self.warnBut2 = Button(self.warnWin4, text = "No", width = 10, command = lambda: self.warnWin4.destroy())
            self.warnBut2.place(x = 200, y = 80)

            self.warnWin4.mainloop()
        elif startChoice == "=  Logout  =":
            self.desktopWindow.destroy()
            OS.osLogin(self)

        elif startChoice == "- Account Manager":
            OS.createUser4(self)

    def startClick(self):
        self.var2 = True
        self.startList = Listbox(self.desktopWindow, height = 7, relief = GROOVE)
        self.startList.insert(END, "- Search")
        self.startList.insert(END, "- Account Manager")
        self.startList.insert(END, " ")
        self.startList.insert(END, "-------------------------")
        self.startList.insert(END, "= Settings =")
        self.startList.insert(END, "=  Logout  =")
        self.startList.insert(END, "= Shutdown =")
        self.startList.bind("<<ListboxSelect>>", lambda x: OS.startSelection(self))
        if self.reader == "resolution: 640x480":
            self.startList.place(x = 1, y = 335)
        if self.reader == "resolution: 1024x768":
            self.startList.place(x = 1, y = 623)
        if self.reader == "resolution: 1280x720":
            self.startList.place(x = 1, y = 575)
        self.startList.lift()

    @staticmethod
    def desktopSplash(self):
        self.var2 = False
        self.var1 = False
        self.desktopWindow = Tk()
        self.desktopWindow.iconbitmap("./data/bin/icons/desktop.ico")
        self.desktopWindow.title("Exodus Virtual Operating System - (C) JG Technologies")
        conf = open('./data/config.dll')
        res = str(self.desktopwidth) + "x" + str(self.desktopheight)
        self.desktopWindow.geometry(res)
        self.desktopWindow.resizable(width = FALSE, height = FALSE)

        self.startImage = PhotoImage(file = "data/bin/system/starticon.gif")

        self.startButton = Button(self.desktopWindow, compound = LEFT, image = self.startImage , text = " Start", command = lambda: OS.startClick(self))

        self.taskBarLabel = Label(self.desktopWindow, text = (u"\u2015") * 200, bg = "#000", anchor = "n")

        self.taskBarTime = Label(self.desktopWindow, text = "")
        OS.update_clock(self)

        self.taskBarTime.bind("<Double-Button-1>", lambda x: OS.timeClick(self))

        self.searchLabel = Label(self.desktopWindow, text = "Search:")

        self.searchBox = Entry(self.desktopWindow)

        self.taskbarBack = Label(self.desktopWindow, text = " " * 500, height = 2)

        self.searchButton = Button(self.desktopWindow, text = u"\U0001F50E", command = lambda: OS.search(self))

        self.taskbarBack.lower()

        self.backgroundLabel = Label(self.desktopWindow, image = "", height = self.desktopheight + 2, width = self.desktopwidth)
        self.backgroundLabel.bind("<Button-1>", lambda x: OS.rightstartDestroy(self))
        self.backgroundLabel.bind("<Button-3>", self.callback)
        self.backgroundLabel.place(x = -3, y = -3)

        PATH1 = './data/bin/system/' + self.userVar1 + "/background/background.gif"
        if os.path.isfile(PATH1) and os.access(PATH1, os.R_OK):
            backImage = PhotoImage(file = "data/bin/system/" + self.userVar1 + "/background/background.gif")
            self.backgroundLabel.configure(image = backImage)
        else:
            backImage = PhotoImage(file = "data/bin/system/default/background/default.gif")
            self.backgroundLabel.configure(image = backImage)

        self.taskBarLabel.lower()
        self.backgroundLabel.lower()

        if self.reader == "resolution: 640x480":
            self.startButton.place(x = 0, y = 452)
            self.taskBarLabel.place(x = -2, y = 451)
            self.taskBarTime.place(x = 556, y = 457)
            self.searchLabel.place(x = 60, y = 455)
            self.searchBox.place(x = 110, y = 457)
            self.taskbarBack.place(x = 0, y = 452)
            self.searchButton.place(x = 240, y = 454)

        elif self.reader == "resolution: 1024x768":
            self.startButton.place(x = 0, y = 740)
            self.taskBarLabel.place(x = -2, y = 739)
            self.taskBarTime.place(x = 940, y = 745)
            self.searchLabel.place(x = 60, y = 743)
            self.searchBox.place(x = 110, y = 745)
            self.taskbarBack.place(x = 30, y = 740)
            self.searchButton.place(x = 240, y = 742)

        elif self.reader == "resolution: 1280x720":
            self.startButton.place(x = 0, y = 692)
            self.taskBarLabel.place(x = -2, y = 691)
            self.taskBarTime.place(x = 1196, y = 697)
            self.searchLabel.place(x = 60, y = 695)
            self.searchBox.place(x = 110, y = 697)
            self.taskbarBack.place(x = 10, y = 692)
            self.searchButton.place(x = 240, y = 694)

        self.desktopWindow.mainloop()

    def optionsClick(self):
        optionsWin.OptionsWin().optionsWindow()

    def continueClick(self):
        self.loginSuccess.destroy()
        self.warnWin1 = Tk()
        self.warnWin1.iconbitmap("./data/bin/icons/error.ico")
        self.warnWin1.geometry("390x150")
        self.warnWin1.title("Notification")

        self.warnLabel1 = Label(self.warnWin1, text = ("The resolution of this OS is set by default to 1024x768," + "\n" + "you can change this in the config.dll"))
        self.warnLabel1.place(x = 50, y = 15)

        self.warnLabel2 = Label(self.warnWin1, text = ("(config.dll located in './data')"))
        self.warnLabel2.place(x = 120, y = 60)

        self.warnBut1 = Button(self.warnWin1, text = "Okay", command = lambda: OS.warnClick(self))
        self.warnBut1.place(x = 175, y = 100)

        self.warnWin1.mainloop()

    def warnClick(self):
        self.warnWin1.destroy()
        self.desktopSplash(self)

    @staticmethod
    def loginClick(self):
        PATH = "./data/login/users/" + str(self.userBox.get()) + ".dll"
        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            fle = open('./data/login/users/' + str(self.userBox.get()) + ".dll")
            password = fle.readlines()[0]
            fle.close()

            if password == self.passBox.get():
                self.userVar1 = self.userBox.get()
                self.loginScreen.destroy()
                fle = open('./data/config.dll', 'r')
                print ("DEBUG INFO:")
                print ("-----------")
                print (" ")
                print "Time: " + str(time.strftime("%H:%M:%S"))
                print "Date: " + str(time.strftime("%d/%m/%Y"))
                print "Username: " + str(self.userVar1)
                print "Password: " + password
                self.reader = fle.readlines()[0]
                try:
                    if self.reader == "resolution: 640x480":
                        self.desktopwidth = 640
                        print "Width: " + str(self.desktopwidth)
                        self.desktopheight = 480
                        print "Height: " + str(self.desktopheight)
                    if self.reader == "resolution: 1024x768":
                        self.desktopwidth = 1024
                        print "Width: " + str(self.desktopwidth)
                        self.desktopheight = 768
                        print "Height: " + str(self.desktopheight)
                    if self.reader == "resolution: 1280x720":
                        self.desktopwidth = 1280
                        print "Width: " + str(self.desktopwidth)
                        self.desktopheight = 720
                        print "Height: " + str(self.desktopheight)
                    if self.reader == "resolution: 1360x768":
                        self.desktopwidth = 1360
                        print "Width: " + str(self.desktopwidth)
                        self.desktopheight = 768
                        print "Height: " + str(self.desktopheight)
                except:
                    print ("VOS ERROR: Config file does not exist or is unreadable.")
                fle.close()
                self.loginSuccess = Tk()
                self.loginSuccess.iconbitmap("./data/bin/icons/tick.ico")
                self.loginSuccess.title("Login Success")
                self.loginSuccess.minsize(width = 25, height = 25)
                self.loginSuccess.resizable(width = FALSE, height = FALSE)

                self.sucLabel = Label(self.loginSuccess, text = "You logged in succesfully.")
                self.sucLabel.place(x = 30, y = 40)

                self.optionsButton = Button(self.loginSuccess, text = u"\u2699", width = 2, height = 1,command = lambda: OS.optionsClick(self))
                self.optionsButton.place(x = 170, y = 170)

                self.sucButton = Button(self.loginSuccess, text = "Continue", command = lambda: OS.continueClick(self))
                self.sucButton.place(x = 70, y = 80)

                self.loginSuccess.mainloop()
            else:
                self.warnWin8 = Tk()
                self.warnWin8.iconbitmap("./data/bin/icons/error.ico")
                self.warnWin8.title("Notification")
                self.warnWin8.geometry("290x100")

                self.warnLabel6 = Label(self.warnWin8, text = "Login failed." + "\n" + "Password incorrect or account does not exist.")
                self.warnLabel6.place(x = 20, y = 10)

                self.warnBut6 = Button(self.warnWin8, text = "Okay", width = 10, command = lambda: self.warnWin8.destroy())
                self.warnBut6.place(x = 105, y = 60)

        else:
            self.warnWin8 = Tk()
            self.warnWin8.iconbitmap("./data/bin/icons/error.ico")
            self.warnWin8.title("Notification")
            self.warnWin8.geometry("290x100")

            self.warnLabel6 = Label(self.warnWin8, text = "Login failed." + "\n" + "Password incorrect or account does not exist.")
            self.warnLabel6.place(x = 20, y = 10)

            self.warnBut6 = Button(self.warnWin8, text = "Okay", width = 10, command = lambda: self.warnWin8.destroy())
            self.warnBut6.place(x = 105, y = 60)

    def loginShut(self):
        self.warnWin12 = Tk()
        self.warnWin12.iconbitmap("./data/bin/icons/error.ico")
        self.warnWin12.title("WARNING")
        self.warnWin12.geometry("390x150")

        self.warnLabel9 = Label(self.warnWin12, text = "Are you sure you want to shutdown?")
        self.warnLabel9.place(x = 95, y = 15)

        self.warnBut9 = Button(self.warnWin12, text = "Yes", width = 10, command = lambda: (self.warnWin12.destroy(), self.loginScreen.destroy()))
        self.warnBut9.place(x = 100, y = 80)

        self.warnBut9 = Button(self.warnWin12, text = "No", width = 10, command = lambda: self.warnWin12.destroy())
        self.warnBut9.place(x = 200, y = 80)

        self.warnWin12.mainloop()

    def osUpdate(self):
        url = "http://exodusvos.weebly.com/uploads/2/7/5/2/27527567/version.txt"
        req = Request(url)

        try:
            f = urlopen(req)
            print "[Update Checker]: Checking your current version..."
            fileread = f.read()
            fileread1 = fileread[0:100]
            versionVar1 = fileread1[16:100]

            currentVer = open("./data/version.dll")
            cVersion = currentVer.readlines()[0]
            versionVar = cVersion[16:100]

            if fileread1 == cVersion:
                print "[Update Checker]: VOS is up to date"
                print "[Notification]: You are running version: " + versionVar
                self.updateWindow = Tk()
                self.updateWindow.title("Notification")
                self.updateWindow.iconbitmap("./data/bin/icons/note1.ico")
                self.updateWindow.geometry("290x100")

                self.updateWindowLabel = Label(self.updateWindow, text = "Your current version is up to date." + "\n" + "You are running version: " + versionVar)
                self.updateWindowLabel.place(x = 50, y = 10)

                self.updateWindowButton = Button(self.updateWindow, text = "Okay", width = 10, command = lambda: (self.updateWindow.destroy(), OS.osLogin(self)))
                self.updateWindowButton.place(x = 100, y = 60)
                self.updateWindow.mainloop()
            else:
                print "[Notification]: Out of date."
                self.updateWindow1 = Tk()
                self.updateWindow1.title("Notification ")
                self.updateWindow1.geometry("290x100")
                self.updateWindow1.iconbitmap("./data/bin/icons/note1.ico")

                self.updateWindowLabel1 = Label(self.updateWindow1, text = "Update Available." + " New version: " + versionVar1 + "\n" + "You are running version: " + versionVar)
                self.updateWindowLabel1.place(x = 35, y = 10)

                self.updateWindowButton1 = Button(self.updateWindow1, text = "Okay", width = 10, command = lambda: (self.updateWindow1.destroy(), OS.osLogin(self)))
                self.updateWindowButton1.place(x = 100, y = 60)
                self.updateWindow1.mainloop()

                print "[Notification]: New update available, updates contain useful new features, please download the new version from our site."

        except HTTPError, e:
            print "VOS Error: " + str(e.code) + " Site Not found:", str(url)
        except URLError, e:
            print "VOS Error #46: " + str(e.reason), str(url)
        except:
            print "VOS Error #2: An unknown error occured, please make sure you have an internet connection."


    def osLogin(self):
        self.loginScreen = Tk()
        self.loginScreen.title("Login")
        self.loginScreen.iconbitmap("./data/bin/icons/systemlogin.ico")
        self.loginScreen.minsize(width = 200, height = 200)
        self.loginScreen.resizable(width = FALSE, height = FALSE)

        self.userLabel = Label(self.loginScreen, text = "Username:")
        self.userLabel.place(x = 70, y = 15)

        self.userBox = Entry(self.loginScreen)
        self.userBox.place(x = 40, y = 40)
        self.userBox.focus_set()

        self.passLabel = Label(self.loginScreen, text = "Password:")
        self.passLabel.place(x = 70, y = 70)

        self.passBox = Entry(self.loginScreen, show = "*")
        self.passBox.place(x = 40, y = 100)

        self.createAccount = Button(self.loginScreen, text = "Manage Accounts", width = 15, command = lambda: OS.createUser(self))
        self.createAccount.place(x = 43, y = 130)

        self.loginButton = Button(self.loginScreen, text = "Login", width = 15, command = lambda: OS.loginClick(self))
        self.loginButton.place(x = 43, y = 170)

        self.shutImage = PhotoImage(file = "data/bin/icons/power.gif")
        self.shutButton = Button(self.loginScreen, image = self.shutImage, width = 21, height = 20, command = lambda: OS.loginShut(self))
        self.shutButton.place(x = 170, y = 170)

        self.passBox.bind("<Return>", lambda x: OS.loginClick(self))
        self.loginScreen.mainloop()

OS().osUpdate()
