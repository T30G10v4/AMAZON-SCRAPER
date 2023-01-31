from requests_html import HTMLSession
import sqlite3

def getTitleAmazon(link):
    s = HTMLSession()
    r = s.get(link)
    title = r.html.xpath('//*[@id="productTitle"]/text()')
    print(price)
    if title == []:
        return -1
    else:
        title = title[0]
        title=title.replace("\n", "")
        return title

def getPriceAmazonFloat(link):
    s = HTMLSession()
    r = s.get(link)
    price = r.html.xpath('//*[@id="priceblock_ourprice"]/text()')
    print(price)
    if price == []:
        return -1
    else:
        price = price[0]
        price = price.split("\xa0")
        price = price[0]
        price = price.replace(",",".")
        price = float(price)
        return price

def getPriceAmazonStr(link):
    s = HTMLSession()
    r = s.get(link)
    price = r.html.xpath('//*[@id="priceblock_ourprice"]/text()')
    print(price)
    if price == []:
        return -1
    else:
        price = price[0]
        price = price.split("\xa0")
        price = price[0]
        price = price.replace(",",".")
        return price

def createTable():

    connection = sqlite3.connect('discounts.db')

    cursor = connection.cursor()

    command =  """
            CREATE TABLE PRODOTTI (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT,
            descr TEXT,
            min_price REAL,
            old_price REAL,
            new_price REAL)

                """
    cursor.execute(command)

    connection.commit()

    connection.close()

def writeOnDatabase(link, descr, price):
    
    connection = sqlite3.connect('discounts.db')

    cursor = connection.cursor()

    command =  """
            INSERT INTO PRODOTTI (link, descr, min_price, old_price, new_price)
            VALUES('"""+link+"""', '"""+descr+"""',"""+price+""","""+price+""","""+price+""")

                """
    cursor.execute(command)

    connection.commit()

    connection.close()

def readFromDatabase():
    
    connection = sqlite3.connect('discounts.db')

    cursor = connection.cursor()

    command =   """
                SELECT * FROM PRODOTTI
                    
                """

    result = cursor.execute(command).fetchall()
    
    connection.commit()

    connection.close()

    return result

def updateDatabase(id_db, new_price):

    connection = sqlite3.connect('discounts.db')

    cursor = connection.cursor()

    #save new price in old
    command =   """
                SELECT new_price FROM PRODOTTI
                WHERE id = """+str(id_db)+"""
                    
                """

    result = cursor.execute(command).fetchall()

    command =   """
                UPDATE PRODOTTI
                SET old_price = """+str(result[0][0])+"""
                WHERE id = """+str(id_db)

    cursor.execute(command)

    command =   """
                UPDATE PRODOTTI
                SET new_price = """+str(new_price)+"""
                WHERE id = """+str(id_db)
    
    cursor.execute(command)

    #controls the minimun price of all time
    command =   """
                SELECT min_price FROM PRODOTTI
                WHERE id = """+str(id_db)+"""
                    
                """

    result = cursor.execute(command).fetchall()

    if float(result[0][0])>float(new_price):
        command =   """
                UPDATE PRODOTTI
                SET min_price = """+str(new_price)+"""
                WHERE id = """+str(id_db)

        cursor.execute(command)
    
    connection.commit()

    connection.close()


def getLinkFromId(id_db):
    
    connection = sqlite3.connect('discounts.db')

    cursor = connection.cursor()

    command =   """
                SELECT link FROM PRODOTTI
                where id = """+str(id_db)+"""
                    
                """

    result = cursor.execute(command).fetchall()
    
    connection.commit()

    connection.close()

    return result[0][0]


