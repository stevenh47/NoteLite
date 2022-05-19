'''
Created on Apr 29, 2022

@author: steve
'''
import sqlite3 
import tkinter
import test
import test_support

class Card:
    def __init__(self, cardId, title, content):
        self.cardId = cardId
        self.content = content
        self.title = title
        self.tags = set()
        self.relatedCards = set() # set of id
    
    def __str__(self):
        result = "Card id: {cardId}, title:{title}, content:{content}, tags:{tags}, relatedCards:{relatedCards}"
        return result.format(\
                             cardId = self.cardId, title = self.title, \
                             content = self.content, tags = self.tags, \
                             relatedCards = self.relatedCards)
        
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

if __name__ == '__main__':
    # conn = sqlite3.connect('d:\\NoteLiteRecords.db') 
    # cur = conn.cursor()
    
    # card1 = Card(0, "card 1", "card content")
    # writeCard = f"insert or replace  into cards (title, content) values (?,?);"
    # cur.execute(writeCard, (card1.title, card1.content))
    # conn.commit()
    
    # cur.execute("select * from cards")
    # print(cur.fetchall())
    test_support.main('test button')
    

    pass