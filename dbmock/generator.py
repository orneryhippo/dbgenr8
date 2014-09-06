__author__ = 'jesse'
import itertools,functools,dbproxy

"""Given a mock table structure (name and list of fields (including types) construct a generator that
   can be given parameters for ranges of values that can be inserted into such a table"""
def mk_generator(tbl_name,fields_dict,params_dict):
    """params_dict is a dict of field names and ranges like {f1: {min:0,max:100}, f2: {min:'a',max:'z'}}
    """
    t=dbproxy.Table(tbl_name,fields_dict)
    return lambda : 1
    pass