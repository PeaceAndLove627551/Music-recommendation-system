from __future__ import division
from tkinter import *
import tkinter.ttk
from recommend import *
import threading
import time

class GUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create()
    def progress(self,count1,count2):
        self.len1.set(count1)
        self.len2.set(count2)
    def search(self):
        musicTitle = self.musicTitle.get()
        if musicTitle == '':
            print("Please input the music title!")
        else:
            self.len1 = StringVar()
            self.len2 = StringVar()
            self.scale1 = Scale(self,from_ = 0,
                    to = 100,
                    resolution = 0.1,
                    orient = HORIZONTAL,
                    variable = self.len1,
                    length = 500
                ).grid(row = 2,column=0, columnspan=4, padx = 5)
            self.scale2 = Scale(self,from_ = 0,
                    to = 100,
                    resolution = 0.1,
                    orient = HORIZONTAL,
                    variable = self.len2,
                    length = 500
                ).grid(row = 3,column=0, columnspan=4, padx = 5)
            threading.Thread(target = self.musicRecom).start()
    def musicRecom(self):
        self.searchButton.destroy()
        musicTitle = self.musicTitle.get()
        res = dict()
        songId = musicRecom().getSongId(musicTitle)
        time.sleep(1)
        comment = NetEaseAPI().getComment(songId)
        time.sleep(1)
        count1 = 0
        for user in comment:
            count1 = count1 + 1
            uid = user['user']['userId']
            playlist = NetEaseAPI().getPlaylist(uid)
            time.sleep(1)
            count2 = 0
            for table in playlist:
                count2 = count2 + 1
                musicDetail = NetEaseAPI().getPlaylistDetail(table['id'])
                time.sleep(1)
                self.progress(count1/len(comment)*100,count2/len(playlist)*100)
                for music in musicDetail:
                    res[music['id']]={'id':music['id'],'name':music['name'],'singer':music['singer'],'musicPlayCount':int(music['playCount']),'listCount':int(table['playCount']),'listSubscribedCount':int(table['subscribedCount'])}
        self.res = musicRecom().musicRank(res)
        self.maxPage = 4
        self.page = 1
        self.nextButton = Button(self, text='Pre', command=self.Pre)
        self.nextButton.grid(row = 4,column = 1, padx=5, pady=5)
        self.nextButton = Button(self, text='Next', command=self.Next)
        self.nextButton.grid(row = 4,column = 2, padx=5, pady=5)
        self.frame = Frame(self)
        self.frame.grid(row = 5,columnspan=4)
        self.getCont()
    def getCont(self):
        index = 1
        num = 0
        self.frame.destroy()
        self.frame = Frame(self)
        self.frame.grid(row = 5,columnspan=4)
        for item in self.res:
            num = num + 1
            if num > self.page * 15:
                break
            if num <= self.page * 15 and num > (self.page - 1) * 15:
                Label(self.frame, text=index + (self.page - 1) * 15).grid(row = index + 4,column=0)
                Label(self.frame, text=item[1]['name'].encode('utf8')).grid(row = index + 4,column=1)
                Label(self.frame, text=item[1]['id']).grid(row = index + 4,column=2)
                Label(self.frame, text=item[1]['singer'].encode('utf8')).grid(row = index + 4,column=3)
                index = index + 1
    def Next(self):
        if self.page < self.maxPage:
            self.page = self.page + 1
        else:
            self.page = 1
        self.getCont()
    def Pre(self):
        if self.page > 1:
            self.page = self.page - 1
        else:
            self.page = self.maxPage
        self.getCont()
    def create(self):
        self.labelName = Label(self, text = "Please input the music name:")
        self.labelName.grid(row = 0, column = 0)
        self.musicTitle = StringVar()
        self.inputName = Entry(self, textvariable = self.musicTitle, width=50)
        self.inputName.grid(row = 0, column = 1, columnspan=3, padx=5, pady=5)
        self.searchButton = Button(self, text='Search', command=self.search)
        self.searchButton.grid(row = 1,column = 1, padx=5, pady=5)
