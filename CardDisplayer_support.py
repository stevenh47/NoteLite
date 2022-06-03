#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    May 18, 2022 08:42:16 PM PDT  platform: Windows NT

import sys
import tkinter as tk
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
    _w1.labelCardId.configure(text="卡片ID：" + str(thisCard.cardId))
    _w1.textContent.insert(END, thisCard.content)
    
    root.mainloop()

def buttonSaveClick(*args):
    _thisCard.content = _w1.textContent.get("1.0",END)
    _thisCard.title = _w1.textTitle.get("1.0",END)
    dbHlper = DbHelper()
    newCard = dbHlper.insertOrUpdateCard(_thisCard)
    CardList_support.updateList(newCard, _index)