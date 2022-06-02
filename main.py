'''
Created on Apr 29, 2022

@author: steve
'''
import sqlite3 
import tkinter
import Card
import CardList_support

    # cur.execute(''' create table cards (
    # cardId integer PRIMARY KEY   AUTOINCREMENT,
    # title text NOT NULL,
    # content text NOT NULL,
    # tagIds text
    # )''')
    # cur.execute(''' create table tags (
    # tagId integer PRIMARY KEY   AUTOINCREMENT,
    # tagName text NOT NULL
    # )''')
    # cur.execute(''' create table cardConnections (
    # connectionId integer PRIMARY KEY   AUTOINCREMENT,
    # a integer NOT NULL,
    # b integer NOT NULL
    # )''')
    
    
    # conn = sqlite3.connect('d:\\NoteLiteRecords.db') 
    # cur = conn.cursor()
    
    # card1 = Card.Card(0, "Card 1", "Card content")
    # writeCard = f"insert or replace  into cards (title, content) values (?,?);"
    # cur.execute(writeCard, (card1.title, card1.content))
    # conn.commit()
    
    # cur.execute("select * from cards")
    # print(cur.fetchall())

if __name__ == '__main__':
    CardList_support.showList()
    

    pass