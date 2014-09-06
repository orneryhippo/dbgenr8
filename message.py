__author__ = 'jesse'

class Message:
    def __init__(self,text=None,*args,**kwargs):
        self.text=text
        self.entries={} if kwargs==None else kwargs

    def get_key(self):
        pass




