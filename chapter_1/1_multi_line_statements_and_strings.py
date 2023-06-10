a = [1, 2, 3]

a = [1, 2,
        3, 4]

a = [1, #comment is OK here.
    2,
    3] #and here


a = {"key1": "val1", #comment is allowed here
    "key2": "val2" #but we need to write the '}' into new line
    }

def a(b, #comment for b
      c): #comment for c need to be after those or you need to write them into new lines
    pass


multi_line_str = """this is first but i wrote it last, so hi from here          some white space
hi from here
        and here
                    hereeeeee
"""

# print(multi_line_str)


def func():
    multi_line_str = """this is single property for python

    so indentation is not the case inside qoutes
we cand break the indentation like this
                        or like this.
    """

    return multi_line_str

# print(func())