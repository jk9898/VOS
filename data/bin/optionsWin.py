#-------------------------------------------------------------------------------
# Name:        Options Module For VOS
# Purpose:
#
# Author:      jguy
#
# Created:     20/01/2015
# Copyright:   (c) jguy 2015
# Licence:     GNU General Public License
#-------------------------------------------------------------------------------

import Tkinter
from Tkinter import *

import os, sys, time
sys.path.append("../")

class OptionsWin():

    def setResolution(self):
        fle = open("./data/config.dll", 'w+')
        fle.write("resolution: " + self.resVar.get())
        fle.close()
        self.warnWin2 = Tk()
        self.warnWin2.title("Notification")
        self.warnWin2.geometry("290x100")

        self.warnWin2Lab = Label(self.warnWin2, text = "You must restart for the new resolution" + "\n" + "To take effect.")
        self.warnWin2Lab.place(x = 30, y = 10)

        self.warnWin2But = Button(self.warnWin2, text = "Okay", width = 10, command = lambda: self.warnWin2.destroy())
        self.warnWin2But.place(x = 105, y = 60)

    @staticmethod
    def yesClick1(self):
        if not os.path.exists(self.configPath):
            os.makedirs(self.configPath)
        else:
            pass

        fle = open(self.configPath + "/config.dll", 'w+')
        fle.writelines("resolution:")
        fle.writelines("\n")
        fle.writelines("1024x768")
        fle.close()

        warnWin3 = Tk()
        warnWin3.iconbitmap("./data/bin/icons/tick.ico")
        warnWin3.geometry("290x100")
        warnWin3.title("Notification")

        warnWinLabel2 = Label(warnWin3, text = "File has been created" + "\n" + "New Directory:")
        warnWinLabel2.place(x = 30, y = 10)

        warnWinButton2 = Button(warnWin3, text = "Okay", width = 10, command = lambda: OptionsWin.yesClick1.warnWin3.destroy())
        warnWinButton2.place(x = 50, y = 60)
        warnWin3.mainloop()

    @staticmethod
    def noClick1(self):
        self.warnWin2.destroy()

    @staticmethod
    def optionsButton1Set(self):
        self.configPath = str(self.optionsBox1.get())
        sys.path.append(self.configPath)
        if os.path.isfile(self.configPath + '/config.dll') and os.access(self.configPath + '/config.dll', os.R_OK):
            print "File already set."
        else:
            self.warnWin2 = Tk()
            self.warnWin2.geometry("290x100")
            self.warnWin2.iconbitmap("./data/bin/icons/error.ico")
            self.warnWin2.title("Notification")

            self.warnWinLabel1 = Label(self.warnWin2, text = "No config file exists in the given directory!" + "\n" + "Should the system create one?")
            self.warnWinLabel1.place(x = 30, y = 10)

            self.warnWinButton1 = Button(self.warnWin2, text = "Yes", width = 10, command = lambda: OptionsWin.yesClick1(self))
            self.warnWinButton1.place(x = 50, y = 60)

            self.warnWinButton1 = Button(self.warnWin2, text = "No", width = 10, command = lambda: OptionsWin.noClick1(self))
            self.warnWinButton1.place(x = 150, y = 60)

            self.warnWin2.mainloop()

    def optionsWindow(self):
        self.optionsWind = Tk()
        self.optionsWind.title("Options")
        self.optionsWind.geometry("200x200")
        self.optionsWind.iconbitmap("./data/bin/icons/options.ico")
        self.optionsWind.resizable(width = FALSE, height = FALSE)

        self.optionsLabel1 = Label(self.optionsWind, text = "Configuration File:")
        self.optionsLabel1.place(x = 5, y = 10)

        self.optionsBox1 = Entry(self.optionsWind, width = 13)
        self.optionsBox1.place(x = 110, y = 12)

        self.optionsButton1 = Button(self.optionsWind, text = "Set Directory", width = 20, command = lambda: OptionsWin.optionsButton1Set(self))
        self.optionsButton1.place(x = 25, y = 40)

        self.optionsLabel2 = Label(self.optionsWind, text = "Resolution:")
        self.optionsLabel2.place(x = 5, y = 70)

        self.resVar = StringVar(self.optionsWind)

        fle = open("./data/config.dll", "r")
        resVar1 = fle.readlines()[0]
        self.resVar.set(resVar1.split(" ")[1])

        self.optionsBox2 = OptionMenu(self.optionsWind, self.resVar, "640x480", "1024x768", "1280x720", "1360x768")
        self.optionsBox2.place(x = 110, y = 67)

        self.optionsButton2 = Button(self.optionsWind, text = "Set Resolution", width = 20, command = lambda: OptionsWin.setResolution(self))
        self.optionsButton2.place(x = 25, y = 100)

        self.timeOptions = Label(self.optionsWind, text = "Zone (GMT+00):")
        self.timeOptions.place(x = 5, y = 130)

        self.timeEntry = Entry(self.optionsWind, width = 13)
        self.timeEntry.place(x = 110, y = 132)

        self.timeClick = Button(self.optionsWind, text = "Set TimeZone", width = 20)
        self.timeClick.place(x = 25, y = 160)

        self.optionsWind.mainloop()
