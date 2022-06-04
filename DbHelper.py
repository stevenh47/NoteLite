'''
Created on Jun 2, 2022

@author: steve
'''

import sqlite3 
import Card

class DbHelper():
    conn = sqlite3.connect('d:\\NoteLiteRecords.db') 
    cur = conn.cursor()

    def readAllCards(self) -> list[Card.Card]:
        DbHelper.cur.execute("select * from cards")
        cardTuples = DbHelper.cur.fetchall()
        cards = list()
        for cardTuple in cardTuples:
            card = Card.Card(cardTuple[0], cardTuple[1], cardTuple[2], cardTuple[3])
            cards.append(card)  
        return cards  
    
    def insertOrUpdateCard(self, card: Card.Card) -> Card.Card:
        insertCard = f"insert into cards (title, content, tagNames) values (?,?,?);"
        replaceCard = f"replace  into cards (cardId, title, content, tagNames) values (?,?,?,?);"
        if card.cardId == 0:
            DbHelper.cur.execute(insertCard, (card.title, card.content, card.tags))
        else:
            DbHelper.cur.execute(replaceCard, (card.cardId, card.title, card.content, card.tags))
        DbHelper.conn.commit()
        card.cardId = DbHelper.cur.lastrowid
        
        tags = card.tags.split(",")
        for tag in tags:
            tag = tag.strip()
            self.addTag(tag)
        
        return card
    
    def addTag(self, tag:str):
        if (tag == None or len(tag) == 0):
            return
        insertTag = f"insert or replace into tags (tagName) values (?);"
        DbHelper.cur.execute(insertTag, (tag,))
        DbHelper.conn.commit()
        
    def getAllTags(self): # return list of tuple [('tag2',), ('tag1',)]
        DbHelper.cur.execute("select * from tags")
        return DbHelper.cur.fetchall()