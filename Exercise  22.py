def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    if(no_of_passengers>5):
        count=no_of_passengers-4
    else:
        count=1
    while(count<=no_of_passengers):
        st=airline+":"+source[:3]+":"+destination[:3]+":"+str(count+100)
        ticket_number_list.append(st)
        count+=1
    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))

