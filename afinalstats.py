import os
import discord
from discord.ext import commands
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

client = commands.Bot(command_prefix=">",intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
        activity=discord.Game(">commands"))
    
@client.command()
async def commands(ctx):
    embed = discord.Embed(title='Help menu')
    embed.add_field(name='YouTube statistics',value='>state channel')
    embed.add_field(name='Invite bot',value='>invite')
    await ctx.send(embed=embed)
@client.command()
async def invite(ctx):
    embed = discord.Embed(title='Invite this Bot')
    link = 'https://discord.com/api/oauth2/authorize?client_id=906173863413551154&permissions=8&scope=bot'
    embed.add_field(name='Invite bot link',value='[click](' + link + ')')
    await ctx.send(embed=embed)
    
@client.command()
async def state(ctx,*,channel = 'UCWzK3Y8YMBNuCpNLyI2afpQ'):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    browser.get(f'https://socialblade.com/youtube/channel/{channel}')
    elems = browser.find_elements_by_xpath('//p')
    info = browser.find_element_by_id('YouTubeUserTopInfoWrap')
    mass,mass2,mass3 = [],[],[]
    avatars = browser.find_elements_by_xpath("//img[@src]")
    for avatar in avatars:
        ava = avatar.get_attribute('src')
        if ava[0:len('https://yt3.ggpht.com/')] == 'https://yt3.ggpht.com/':
            found_ava = ava   
    for elem in elems:
        mass.append(elem.text)
    mass2 = info.text.split()
    name = ''
    for elem in mass2:
        if elem == 'UPLOADS':
            break
        name += elem + ' '
        mass3.append(elem)
    for in_mass3 in mass3: 
        mass2.remove(in_mass3)###
    created = ''
    flag = True
    for elem in mass2:
        if elem == 'CREATED':
            flag = False
            continue
        if flag:
            if elem != 'CREATED':
                continue
        if elem == 'APPLY':
            break
        created += elem + ' '       
    browser.quit()

    embed = discord.Embed(title=f'{name}')
    embed.add_field(name='Created',value=created,inline=False)
    #embed.add_field(name='Status',value=status,inline=False)#style
    embed.set_thumbnail(url=found_ava)
    embed.add_field(name=mass2[0],value=mass2[1],inline=False)
    embed.add_field(name=mass2[2],value=mass2[3],inline=False)
    embed.add_field(name=mass2[5],value=mass2[6],inline=False)
    embed.add_field(name=mass2[7],value=mass2[8],inline=False)
    embed.add_field(name=mass[10],value=mass[9],inline=False)
    embed.add_field(name=mass[12],value=mass[11],inline=False)
    embed.add_field(name=mass[14],value=mass[13],inline=False)
    embed.add_field(name=mass[16],value=mass[15],inline=False)
    await ctx.send(embed=embed)

    
client.run(os.environ['token'])
