__author__ = 'jesse'
"""
"""

class DbProxy():
    def __init__(self):
        pass
    def insert(self):
        pass
    def update(self):
        pass
    def select(self):
        pass
    def get_struct(self):
        pass
    def mk_table(self,tbl_name,field_dict):
        pass
    def write_sql(self,file_name):
        pass


    class Field():
        def __init__(self,name,type,max_width,**extras):
            pass

    class Table():
        def __init__(self,name,**fields):
            pass



    class Seq():
        from itertools import count
        def __init__(self,start=0):
            return count(start).__next__
        def next=count(start).__next__
            return next

    class ChildTable(Table):
        pass

    class RelatedTable(Table):
        pass