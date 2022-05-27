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