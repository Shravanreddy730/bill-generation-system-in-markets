from datetime import datetime

name=input("enter your name:")
#list of items
lists='''
rice    rs 20/kg
suger   rs 30/kg
salt    rs 20/kg
oil     rs 80/kg
paneer  rs 110/kg
maggi   rs 50/kg
boost   rs 90/each
colgate rs 85/each
'''
#declaring the variables
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[] #items list
qlist=[] #quantity list
plist=[] #price list

#rates for item
items={'rice':20,
	'suger':30,
	'salt':20,
	'oil':80,
	'paneer':110,'maggi':50,'boost':90,'colgate':85}
option=int(input("for list of items press 1"))
if option==1:
	print(lists)
for i in range(len(items)):
	inp1=int(input("if you want to buy press 1 or 2 for exit"))
	if inp1==2:
		break
	if inp1==1:
	    item=input('enter the items:')
	    quantity=int(input("enter quantity"))
	    if item in items.keys():
	     price=quantity*(items[item])
             pricelist.append(item,quantity,items,price)
             totalprice+=price
             ilist.append(item)
             qlist.append(quantity)
             plist.append(price)
             gst=(totalprice*5)/100
             finalamount=gst+totalprice
        else:
             print("sorry the item is not available")
    else:
         print("you entered the wrong option")
         inp=input("can i bill the the items yes or no:")
         if inp=='yes':
         	pass
            if finalamount!=0:
            	print("datetime:"datetime.now())
            	for i in range(len(pricelist)):
            		print(i,ilist[i],plist[i])
                print("totalprice:" totalprice)
                print("gst:" gst)
                print("finalamount:" finalamount)


