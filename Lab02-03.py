class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.cart = []
        self.past_orders = []

class OnlineShop:
    def __init__(self, name, url): 
        self.name = name
        self.url = url
        self.products = []  
    
    
    
    def addItemsToCart(self, customer, product, quantity):
        item = {
            'product': product,
            'quantity': quantity
        }
        customer.cart.append(item)
        print(f"เพิ่ม {product.name} จำนวน {quantity} ลงในตะกร้าแล้ว")
    
    def checkOut(self, customer):
        if not customer.cart:
            print("ตะกร้าสินค้าว่างเปล่า")
            return
        
        total = 0
        print(f"\n=== รายการสั่งซื้อของ {customer.name} ===")
        
 
        for item in customer.cart:
            product = item['product']
            quantity = item['quantity']
            subtotal = product.price * quantity
            total += subtotal
            print(f"{product.name} x {quantity} = {subtotal} บาท")
        
        print(f"ราคารวม: {total} บาท")
        
        order_id = f"ORD{len(customer.past_orders) + 1:03d}"
        
        order = {
            'order_id': order_id,
            'items': customer.cart.copy(),
            'total': total
        }
        customer.past_orders.append(order)
        

        customer.cart.clear()
        print(f"สั่งซื้อสำเร็จ! หมายเลขคำสั่งซื้อ: {order_id}")
    

    def orderTracking(self, customer, order_id):
        for order in customer.past_orders:
            if order['order_id'] == order_id:
                print(f"\nพบคำสั่งซื้อ {order_id}")
                print(f"ลูกค้า: {customer.name}")
                print(f"ราคารวม: {order['total']} บาท")
                print("รายการสินค้า:")
                for item in order['items']:
                    product = item['product']
                    quantity = item['quantity']
                    print(f"- {product.name} x {quantity}")
                return
        
        print(f"ไม่พบคำสั่งซื้อ {order_id}")


if __name__ == "__main__":

    shop = OnlineShop("Gadget World", "www.gadgetworld.com")
    
    mouse = Product("Gaming Mouse Pro X", "เมาส์เกมมิ่งคุณภาพสูง", 1500)
    keyboard = Product("Mechanical Keyboard", "คีย์บอร์ดกดโดนใจ", 2500)
    

    customer1 = Customer("phutana", "pphutna01@gmail.com", "123 นครปฐม")

    shop.addItemsToCart(customer1, mouse, 2)
    shop.addItemsToCart(customer1, keyboard, 1)

    shop.checkOut(customer1)

    shop.orderTracking(customer1, "ORD001")