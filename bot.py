import database
import time

wait = 60

while(1):

    for record in database.readFromDatabase():

        print('Updating price of record '+str(record[0])+'...')

        database.updateDatabase(record[0], database.getPriceAmazonFloat(database.getLinkFromId(record[0]))) #

        print('        Price updated of record '+str(record[0])+'\n')
    

    for record in database.readFromDatabase():    
        print('Checking price of record '+str(record[0])+'...')
        if record[5] < record[4]:
            Messaggio = '        Discount for product: ('+record[2]+') New Price: '+str(record[5])+'€!\n'
            print(Messaggio)
        else:
            print('        No discounts for record '+str(record[0])+'\n')
        #print('Price checked\n')



    print('Sleep for '+str(wait)+' seconds...\n\n\n\n')
    time.sleep(wait)
