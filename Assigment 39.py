#PF-Assgn-39
#This verification is based on string match.     

#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,3,0]

'''This method accepts the item followed by the quantity required by a customer in the format item1, quantity_required, item2, quantity_required etc.'''
def place_order(*item_tuple):
    c=0
    m=0
    k=0
    item=list(item_tuple)
    for i in range(0,len(item) ,2):
        c=0
        for j in range(0,len(menu)):
            if(item[i]==menu[j]):
                c=1
                break
        if(c==0):
            print(item[i]+" is not available")
            break
        else:
            k=check_quantity_available(j,item[i+1])
            
        if(k==0):
            print(item[i]+" stock is over")
        else:
            print(item[i]+" is available")
            
            
    #Remove pass and write your logic here


    #Populate the item name in the below given print statements
    #Use it to display the output wherever applicable
    #Also, do not modify the text in it for verification to work
    
    #print("<item name>is not available")
    #print("<item name>stock is over")
    #print ("<item name>is available")
    
  


'''This method accepts the index position of the item requested by the customer in the quantity_available list, and the requested quantity of the item.'''
def check_quantity_available(index,quantity_requested):
    if(quantity_available[index]>=int(quantity_requested)):
        return 1
    else:
        return 0
    #Remove pass and write your logic here to return an appropriate boolean value.


#Provide different values for items ordered and test your program
place_order("Fried Rice",2,"Soup",1)
