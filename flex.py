def mark(*args):
    add=0
    for i in args:
        add+=i
    print(add)
mark(80,70,90)
mark(65,55)
def details(**kwargs):
     for key,value in kwargs.items():
         print(key,":",value)
details(name="Arun", age=25, city="Chennai")
