def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    for gem in gems_list:
        for g in reqd_gems:
            if g==gem:
                index = gems_list.index(g)
                no_of_gems = reqd_quantity[reqd_gems.index(g)]
                price = price_list[index] * no_of_gems
                print(price)
                bill_amount += price
            if g not in gems_list:
                return -1
    if(bill_amount>30000):
        bill_amount-=bill_amount*5/100
    return bill_amount
#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to- 

price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have 

reqd_quantity=[4,2,5]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, 
reqd_quantity)

print(bill_amount)

