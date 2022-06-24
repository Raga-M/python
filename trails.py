class sp:
 '''supermarket'''
   def __init__(self, price, brand, discount=0):
       self.price = price
       self.brand = brand
       self.discount = discount


bread = sp(65, 'abd')
# bread.price=65
# bread.brand='abd'
rice = sp(76, 'sc', 16)
print(rice.__dict__)