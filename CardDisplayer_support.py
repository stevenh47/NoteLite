#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    May 18, 2022 08:42:16 PM PDT  platform: Windows NT

import sys
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter.constants import *
import Card

import CardDisplayer
import CardList_support
from DbHelper import DbHelper

def display(thisCard: Card.Card, index:int):
    '''Main entry point for the application.'''
    global root, _top1, _w1, _thisCard, _index
    _thisCard = thisCard
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    _top1 = root
    _w1 = CardDisplayer.CardDisplayer(_top1)
    _index = index
    
    _w1.textTitle.insert(END, thisCard.title)
    updateIdLabel(thisCard.cardId)
    _w1.textContent.insert(END, thisCard.content)
    _w1.textTag.insert(END, thisCard.tags)
    
    root.mainloop()

def buttonSaveClick(*args):
    if _w1.textContent.get("1.0",END).strip() == "":
        messagebox.showerror("错误", "内容不能为空")
        return
    if _w1.textTitle.get("1.0",END).strip() == "":
        messagebox.showerror("错误", "标题不能为空")
        return
    global _thisCard, _index
    _thisCard.content = _w1.textContent.get("1.0",END).strip()
    _thisCard.title = _w1.textTitle.get("1.0",END).strip()
    _thisCard.tags = _w1.textTag.get("1.0", END).strip()
    dbHlper = DbHelper()
    _thisCard = dbHlper.insertOrUpdateCard(_thisCard)
    _index = CardList_support.updateList(_thisCard, _index)
    updateIdLabel(_thisCard.cardId)
    messagebox.showinfo("保存成功", "保存成功")
    
def updateIdLabel(cardId: int):
    _w1.labelCardId.configure(text="卡片ID：" + str(cardId))

def buttonShowTagsClicked(*args):
    print('CardDisplayer_support.buttonShowTagsClicked')
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()