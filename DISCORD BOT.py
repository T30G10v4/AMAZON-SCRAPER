import discord
from discord.ext import commands, tasks
from discord import client
import database
import asyncio
import requests

canale_twitch = "Twitch Channel Here"
is_live = 0
token = "Discord Token Here"
client = commands.Bot(command_prefix=("$"))
link_twitch = "https://twitch.tv/"+canale_twitch

print('Bot in avvio...')

@client.event
async def on_ready():
    print(client.user," è ora ONLINE")
    advice.start(837414507927830571)
    

@client.event
async def on_message(message):
    if message.content == "$help":
        await message.channel.send("Lista comandi:\n$list Lista di prezzi\n$add \[link amazon\] Aggiungi un articolo alla lista")
    
    if message.content == "$list":
      
        lista="Ecco i prezzi che stai monitorando:\n"
        
        for record in database.readFromDatabase():
            lista=lista+str(record[2])+"\nPrezzo: "+str(record[5])+" €\n"+str(record[1])+"\n\n"
        
        await message.channel.send(lista)
    
    if message.content.startswith("$add"):
        command=message.content
        command=command.split(" ")[1]
        
        print("Inserendo in database il link amazon...")
        await message.channel.send("Inserendo in database il link amazon...")
        
        title=database.getTitleAmazon(command)
        price=database.getPriceAmazonStr(command)
        
        database.writeOnDatabase(command, title, price)
           
        result="    Inserito il link amazon "+command+"\nTitolo "+title+"\nPrezzo = "+price+"." 
        
        print(result)
        await message.channel.send(result)    
    
    """
    elif message.content.startswith("$"):
        await message.channel.send("Comando non valido, digitare \"$help\" per i comandi disponibili")
    """   
        

@tasks.loop(hours=24)
async def advice(canale):
    
    channel = client.get_channel(canale)
    for record in database.readFromDatabase():

        print('Updating price of record '+str(record[0])+'...')
        #await channel.send('Updating price of record '+str(record[0])+'...')
        
        database.updateDatabase(record[0], database.getPriceAmazonFloat(database.getLinkFromId(record[0]))) #

        print('        Price updated of record '+str(record[0])+'\n')
        #await channel.send('        Price updated of record '+str(record[0])+'\n')

    for record in database.readFromDatabase():    
        print('Checking price of record '+str(record[0])+'...')
        #await channel.send('Checking price of record '+str(record[0])+'...')
        if (record[5] < record[4])&(record[5]!=-1):
            Messaggio = 'PREZZO SCONTATO!\n'+record[2]+'\nPREZZO: '+str(record[5])+'€!\n'+record[1]
            print(Messaggio)
            await channel.send(Messaggio)

        else:
            print('        No discounts for record '+str(record[0])+'\n')
            #await channel.send('        No discounts for record '+str(record[0])+'\n')
        

   

   
    
client.run(token)
