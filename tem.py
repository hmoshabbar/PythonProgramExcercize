from string import Template
def Main():
    cart=[]
    n=raw_input("Enter Your item:")
    p=int(input("Enter Your Price:"))
    q=int(input("Enter Your quantiuty:"))
    cart.append(dict(item=n,price=p,quantity=q))
    cart.append(dict(item=n,price=p,quantity=q))
    cart.append(dict(item=n,price=p,quantity=q))
    t=Template("$quantity*$item=$price")
    total=0
    print("cart:")
    for data in cart:
        print(t.substitute(data))
        total +=data["price"]
    print ("Total:"+str(total))
if __name__=="__main__":
    Main()
