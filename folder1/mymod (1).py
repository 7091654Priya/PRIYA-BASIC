def countLines(f):
    with open(f,"r") as n:    
       print(f"Number of lines = {len(n.readlines())}")
def countChars(f):
    with open(f,"r") as n:
       print(f"Number of characters = {len(n.read())}")
def test(name):
    countLines(name)
    countChars(name) 


