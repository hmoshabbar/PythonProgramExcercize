from string import Template
def Main():
    cart=[]
    cart.append(dict(item="Mango",price=23,quantity=2))
    cart.append(dict(item="Fish",price=42,quantity=3))
    cart.append(dict(item="Onion",price=23,quantity=2))
    t=Template("$quantity  $item=$price")
    total=0
    print("cart:")
    for data in cart:
        print(t.substitute(data))
        total +=data["price"]
    print ("Total:"+str(total))
if __name__=="__main__":
    Main()
    
