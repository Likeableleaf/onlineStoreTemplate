class Customer:
    def __init__(self, first_name, last_name, email, username, password) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
    
class Product:
    def __init__(self, name, info, price, stock, image_url, category) -> None:
        self.name = name
        self.info = info
        self.price = price
        self.stock = stock
        self.image_url = image_url
        self.category = category
    
        
class Order:
    def __init__(self, transaction_id, username, item_id, quantity,size, sale_date, cost) -> None:
        self.transaction_id = transaction_id
        self.username = username
        self.item_id = item_id
        self.quantity = quantity
        self.size = size
        self.sale_date = sale_date
        self.cost = 0
      
 