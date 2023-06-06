class Transaction:

  def __init__(self,name,id,price,amount,date):
    self.name = name
    self.id = id
    self.price = price
    self.amount = amount
    self.date = date
    
  def bought(self):
    print("This stock "+self.name+" is bought")
  def sold(self):
    print("This stock "+self.name+" is sold")
