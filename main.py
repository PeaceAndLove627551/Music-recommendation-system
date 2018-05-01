#!/usr/bin/env python  
# -*- coding: UTF-8 -*-  

# from Crawler import *
import sys
from show_window import *

default_encoding = 'utf-8'
# if sys.getdefaultencoding() != default_encoding:
#     reload(sys)
#     sys.setdefaultencoding(default_encoding)


def main():
    root = tkinter.Tk()
    app = GUI(root)
    root.geometry('640x560')
    root.resizable(False, False)
    app.master.title('music_recommendation')
    app.mainloop()


if __name__ == "__main__":
    main() 
