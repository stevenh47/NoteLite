#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    May 28, 2022 08:23:43 PM PDT  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import Card
import sqlite3 
import CardDisplayer_support


import CardList

def showList():
    conn = sqlite3.connect('d:\\NoteLiteRecords.db') 
    cur = conn.cursor()
    
    cur.execute("select * from cards")
    global _cards
    cardTuples = cur.fetchall()
    _cards = list()
    for cardTuple in cardTuples:
        card = Card.Card(cardTuple[0], cardTuple[1], cardTuple[2])
        _cards.append(card)
    
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = CardList.CardList(_top1)
    refreshList(_cards)
    
    root.mainloop()

def buttonDisplayCardClicked(*args):
    cardSelected = _w1.listboxCards.curselection()
    if len(cardSelected) == 0:
        return
    CardDisplayer_support.display(_cards[cardSelected[0]], cardSelected[0])

def updateList(card: Card.Card, index:int):
    _cards[index] = card
    refreshList(_cards)

def refreshList(cards: list[Card.Card]):
    _w1.listboxCards.delete(0, END)
    for card in cards:
        _w1.listboxCards.insert(END, card.title + ":" + card.content)
