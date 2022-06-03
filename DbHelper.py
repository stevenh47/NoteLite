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
            card = Card.Card(cardTuple[0], cardTuple[1], cardTuple[2])
            cards.append(card)  
        return cards  
    
    def insertOrUpdateCard(self, card: Card.Card) -> Card.Card:
        insertCard = f"insert into cards (title, content) values (?,?);"
        replaceCard = f"replace  into cards (cardId, title, content) values (?,?,?);"
        if card.cardId == 0:
            DbHelper.cur.execute(insertCard, (card.title, card.content))
        else:
            DbHelper.cur.execute(replaceCard, (card.cardId, card.title, card.content))
        DbHelper.conn.commit()
        card.cardId = DbHelper.cur.lastrowid
        return card
        