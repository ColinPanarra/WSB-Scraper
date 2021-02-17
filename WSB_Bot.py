#DISCORD BOT
import os
import openpyxl
from openpyxl import load_workbook
import discord
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_NAME')

client = discord.Client()







workbook = load_workbook('listed_stocks.xlsx')
hourly_worksheet = workbook["hourly"]
daily_worksheet = workbook["daily"]
weekly_worksheet = workbook["weekly"]
open_closed_worksheet = workbook["open_closed"]

hourly_column_top_stock = hourly_worksheet['F']
daily_column_top_stock = daily_worksheet['F']
weekly_column_top_stock = weekly_worksheet['F']
open_closed_column_top_stock = open_closed_worksheet['F']

hourly_column_top_count = hourly_worksheet['G']
daily_column_top_count = daily_worksheet['G']
weekly_column_top_count = weekly_worksheet['G']
open_closed_column_top_count = open_closed_worksheet['G']

hourly_list_top_stock = [hourly_column_top_stock[x].value for x in range(1,len(hourly_column_top_stock))]
daily_list_top_stock = [daily_column_top_stock[x].value for x in range(1,len(daily_column_top_stock))]
weekly_list_top_stock = [weekly_column_top_stock[x].value for x in range(1,len(weekly_column_top_stock))]
market_list_top_stock = [open_closed_column_top_stock[x].value for x in range(1,len(open_closed_column_top_stock))]

hourly_list_top_count = [hourly_column_top_count[x].value for x in range(1,len(hourly_column_top_count))]
daily_list_top_count = [daily_column_top_count[x].value for x in range(1,len(daily_column_top_count))]
weekly_list_top_count = [weekly_column_top_count[x].value for x in range(1,len(weekly_column_top_count))]
market_list_top_count = [open_closed_column_top_count[x].value for x in range(1,len(open_closed_column_top_count))]

hourly_column_trending_stock = hourly_worksheet['I']
daily_column_trending_stock = daily_worksheet['I']
weekly_column_trending_stock = weekly_worksheet['I']
open_closed_column_trending_stock = open_closed_worksheet['I']

hourly_column_trending_count = hourly_worksheet['J']
daily_column_trending_count = daily_worksheet['J']
weekly_column_trending_count = weekly_worksheet['J']
open_closed_column_trending_count = open_closed_worksheet['J']

hourly_list_trending_stock = [hourly_column_trending_stock[x].value for x in range(1,len(hourly_column_trending_stock))]
daily_list_trending_stock = [daily_column_trending_stock[x].value for x in range(1,len(daily_column_trending_stock))]
weekly_list_trending_stock = [weekly_column_trending_stock[x].value for x in range(1,len(weekly_column_trending_stock))]
market_list_trending_stock = [open_closed_column_trending_stock[x].value for x in range(1,len(open_closed_column_trending_stock))]

hourly_list_trending_count = [hourly_column_trending_count[x].value for x in range(1,len(hourly_column_trending_count))]
daily_list_trending_count = [daily_column_trending_count[x].value for x in range(1,len(daily_column_trending_count))]
weekly_list_trending_count = [weekly_column_trending_count[x].value for x in range(1,len(weekly_column_trending_count))]
market_list_trending_count = [open_closed_column_trending_count[x].value for x in range(1,len(open_closed_column_trending_count))]



top_hourly_string = ''
trending_hourly_string = ''

top_daily_string = ''
trending_daily_string = ''

top_weekly_string = ''
trending_weekly_string =''

top_market_string = ''
trending_market_string = ''

for x in range(9):
    data=[hourly_list_top_stock[x],hourly_list_top_count[x], hourly_list_trending_stock[x],hourly_list_trending_count[x]]


    top_hourly_string = top_hourly_string + ( '{:<5} - {:<25} \n'.format(hourly_list_top_stock[x],hourly_list_top_count[x]))
    trending_hourly_string = trending_hourly_string + ( '{} : {}% \n'.format( hourly_list_trending_stock[x],hourly_list_trending_count[x] ))

    top_daily_string = top_daily_string + ( '{:<5} - {:<25} \n'.format(daily_list_top_stock[x],daily_list_top_count[x]))
    trending_daily_string = trending_daily_string + ( '{} : {}% \n'.format( daily_list_trending_stock[x],daily_list_trending_count[x] ))

    top_weekly_string = top_weekly_string + ( '{:<5} - {:<25} \n'.format(weekly_list_top_stock[x],weekly_list_top_count[x]))
    trending_weekly_string = trending_weekly_string + ( '{} : {}% \n'.format( weekly_list_trending_stock[x],weekly_list_trending_count[x] ))

    top_market_string = top_market_string + ( '{:<5} - {:<25} \n'.format(market_list_top_stock[x],market_list_top_count[x]))
    trending_market_string = trending_market_string + ( '{} : {}% \n'.format( market_list_trending_stock[x],market_list_trending_count[x] ))





@client.event
async def on_ready():
    #print(f'{client.user} has connected to Discord!')


    channel = client.get_channel(749370051714351214)
    await embed(channel)
    #await channel.send(title_string + top_hourly_string )
#    await channel.send(top_hourly_string)

    #await client.send_message(client.get_channel(channel), title_string)
    #await client.send_message(client.get_channel(channel), top_hourly_string)
    #await channel.send(hourly_trending_string)

@client.event
async def embed(channel):
    embed = discord.Embed(title="WSB Stock Info" , description="Beep Boop heres some stocks!\n____________", color=discord.Color.orange(), url = "https://www.reddit.com/r/wallstreetbets/")
    embed.set_author(name="WSB BOT", icon_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Farchive.is%2FrlllS%2Faf6b7b8c94765060701ca08cc34303a35c692a3f.png&f=1&nofb=1")

    embed.add_field(name="This Hour", value="______", inline =False)
    embed.add_field(name ="Top Mentioned", value =   top_hourly_string +'\n __________', inline=True)
    embed.add_field(name ="Trending", value =        trending_hourly_string +'\n __________', inline=True)

    embed.add_field(name="Today", value ="______",inline =False)
    embed.add_field(name ="Top Mentioned Today", value =    top_daily_string + '\n __________', inline=True)
    embed.add_field(name ="Trending Today", value =         trending_daily_string+ '\n __________',  inline=True)

    embed.add_field(name="This Week", value ="______",inline =False)
    embed.add_field(name ="Top Mentioned", value =   top_weekly_string+ '\n __________',  inline=True)
    embed.add_field(name ="Trending", value =        trending_weekly_string+ '\n __________',  inline=True)

    embed.add_field(name="Market", value ="______",inline =False)
    embed.add_field(name ="Top Mentioned Market", value = top_market_string+ '\n __________',  inline=True)
    embed.add_field(name ="Trending Market", value = trending_market_string+ '\n __________',  inline=True)



    await channel.send(embed=embed)
client.run(TOKEN)
