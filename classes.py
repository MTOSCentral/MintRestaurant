
class Table:
    def __init__(self,Persons,InTime,Orders):
        self.Person = Persons
        self.InTime = InTime
        self.Orders = Orders
class Selection:
    def __init__(self,name,price,max2):
        self.Name = name
        self.Price = price
        #Max Of The Same Item Selected
        self.Max = max2
class Option:
    def __init__(self,name,Selections:list,maxsel:None,minsel:0):
        self.Name = name
        self.Selections = Selections
        #Maximum Items
        self.MaxSel = maxsel
        #Minimum Items
        self.MinSel = minsel
class Options:
    def __init__(self,Options):
        self.Options = Options
class Ticket:
    def __init__(self,bytable,paidby,paid,items,price,Options=Options([])):
        self.ByTable = bytable
        self.PaidBy = paidby
        self.Paid = paid
        self.Items = items
        self.Price = price
        self.Options = Options
class Catergory:
    def __init__(self,ID,name,time):
        self.ID = ID
        self.Name = name
        self.Time = time
class Food:
    def __init__(self,id,name,caterogory,price,Options,Image=None):
        self.ID = id
        self.Name = name
        self.Catergory = caterogory
        self.Price = price
        self.Options = Options
        self.Image = Image