import discord 
from discord.ext import commands 
from hentai import Hentai, Format , Utils, Sort, Option, Tag
import random 
import requests 
from discord.ext.commands.cooldowns import BucketType
from discord import Embed 
import time
import asyncio
import os

client = commands.Bot(command_prefix=["^"]) 
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(name="Hentai with Senpai", type=discord.ActivityType.watching))
    print("im alive") 

#RANDOM HENTAI_ID 
@client.command(aliases = ["rhi" , "randomhentaiid"])
@commands.cooldown(1, 3, BucketType.user)
async def ranhenid(ctx):
    if ctx.message.channel.is_nsfw():
        async with ctx.typing():
            z = Utils.get_random_id()
            doujin = Hentai(z)  
            z = str(z) 
            c = 'https://nhentai.net/g/' + z + '/'
            x = (doujin.title(Format.Pretty))
            t = ([tag.name for tag in doujin.tag])
            o = " | ".join(str(elem) for elem in t)
            o = o.upper()
            p = (doujin.image_urls)
            p_ = p[0] 
            u = (doujin.upload_date)
            ar = str(doujin.artist)
            ar = ar.split("(")
            ar = ar[1]
            ar = ar.split(",")
            lol = [] 
            for i in ar:
                if i.endswith(")]"): 
                    i = i.split(")]")
                    i = " ".join(str(elem) for elem in i) 
                    i = i.split("=") 
                    lol.append(i)
                else:
                    i = i.split("=")
                    i = i[1] 
                    lol.append(i)
            lol[2] = lol[2].split("'")
            lol[3] = lol[3].split("'") 
            em = discord.Embed(title = x , url = c , description = f"` HENTAI ID ` - `{z}`\n`UPLOAD DATE` - `{u}`\n` Artist id ` - `{lol[0]}`\n`Artist Name` - `{lol[2][1].capitalize()}`\n[Artist Profile]({lol[3][1]})\n`Artist Rank` - `{lol[4][1]}`\n`   TAGS   ` - `{o}`" , colour = ctx.author.colour) 
            em.set_image(url = p_ ) 
            em.set_footer(text=f"Total pages - {len(p)} | Type ^henread {z} to read it")
            em.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url) 
            await ctx.send(embed = em)
    else:
        await ctx.send("``Please run this command in a NSFW Channel``") 

#HENSEARCH
@client.command()
@commands.cooldown(1, 3, BucketType.user)
async def hensearch(ctx, *, x=None):
    if ctx.message.channel.is_nsfw():
        if not x:
            await ctx.send("``Please Enter the HENTAI ID , if you dont have any in your mind then type '^ranhenid' to get one``")
            return 
        
        url = "https://nhentai.net/api/gallery/" + x
        r = requests.get(url)
        if r.status_code == 404:
            await ctx.send("``Sorry i cant find that hentai``")
            return 

        async with ctx.typing():
            doujin = Hentai(x)
            Hentai.exists(doujin.id)
            a = f"{doujin.title(Format.Pretty)}"
            b = ([tag.name for tag in doujin.tag])
            o = o = " | ".join(str(elem) for elem in b)
            o = o.upper()
            p = (doujin.image_urls)
            p_ = p[0] 
            c = 'https://nhentai.net/g/' + x + '/'
            u = (doujin.upload_date) 
            ar = str(doujin.artist)
            ar = ar.split("(")
            ar = ar[1]
            ar = ar.split(",")
            lol = [] 
            for i in ar:
                if i.endswith(")]"): 
                    i = i.split(")]")
                    i = " ".join(str(elem) for elem in i) 
                    i = i.split("=") 
                    lol.append(i)
                else:
                    i = i.split("=")
                    i = i[1] 
                    lol.append(i)
            lol[2] = lol[2].split("'")
            lol[3] = lol[3].split("'") 
            em = discord.Embed( 
                title=a , url = c , description=f"`UPLOAD DATE` - `{u}`\n` Artist id ` - `{lol[0]}`\n`Artist Name` - `{lol[2][1].capitalize()}`\n[Artist Profile]({lol[3][1]})\n`Artist Rank` - `{lol[4][1]}`\n`   TAGS    ` - `{o}`", colour=ctx.author.colour) 
            em.set_footer( 
                text=
            f"Total Pages - {len(p)} | Type ^henread {x} to read it"
            )
            em.set_author(name = ctx.author.name , icon_url = ctx.author.avatar_url) 
            em.set_image(url=p_)
            await ctx.send(embed = em)

    else:
        await ctx.send("``Please run this command in a NSFW Channel``") 

#HENREAD
@client.event
async def on_message(message):
    if client.user in message.mentions: 
        if message.author == client.user: 
            return
        
        if dic.get(message.author) == None:
            await message.channel.send("Hey there Baka! My prefixes are `^` , `,` , `e`\n:\)")
        else:
            x = dic.get(message.author)
            y = random.choice([f"<a:723276605035642942:787214257963794453>" , f"<:weird:775632025033506816>" , f"<a:696321747976454144:786442106474332221>"])
            a = random.choice(["heyy" , "hii" , "wassup" , "will yo-" , "yoo!" , "put it in-" , "ahem!" , "PERVERT" , "sup"])
            await message.channel.send(f"{a} {x} {y}")  

    if message.content.startswith('^henread'):
        if message.channel.is_nsfw():
            text = message.content 
            le = len(text)
            split = text.split()
            rm = (split[1:le]) 
            kek = ' '.join([str(elem) for elem in rm]) 
            
            url = "https://nhentai.net/api/gallery/" + kek 
            r = requests.get(url)
            if r.status_code == 404:
                await message.channel.send("``Sorry i cant find that hentai``")
                return
            doujin = Hentai(kek)
            Hentai.exists(doujin.id)
            p = (doujin.image_urls)
            a = f"{doujin.title(Format.Pretty)}" 
            l = len(p)
            page_counter = 1 
            c = 'https://nhentai.net/g/' + kek + '/' 
            first_embed = Embed(
                    title=a , url = c , colour=message.author.colour)
            first_embed.set_image(url = p[0])
            first_embed.set_footer(text = f"{page_counter}/{l}") 
            first_embed.set_author(name = message.author.name , icon_url = message.author.avatar_url) 
            emto = Embed(title = "`TIMED OUT`")
            flush_embed = Embed(
                    title="FLUSHING THE EMBED" , colour=message.author.colour)
            
            new_embed = Embed(title = a , url = c , colour=message.author.colour)
            new_embed.set_author(name = message.author.name , icon_url = message.author.avatar_url)  
            msg = await message.channel.send(embed=first_embed) 
            await msg.add_reaction(f"↖️")  
            await msg.add_reaction(f"⬅️")  
            await msg.add_reaction(f"➡️")
            await msg.add_reaction(f"↘️") 
            await msg.add_reaction(f"🚽") 
            
            def reac_check(r, u):
                return msg.id == r.message.id and u != client.user and r.emoji in ['↖️','⬅️','➡️','↘️','🚽']
            
            while True:
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout= 72000 , check=reac_check)
                    em = str(reaction.emoji) 
                except asyncio.exceptions.TimeoutError:
                    await msg.edit(embed=emto) 
                    break
                
                if user != client.user: 
                    await msg.remove_reaction(emoji=em, member=user) 

                if em == '➡️': 
                    if user == message.author:
                        if page_counter == l:
                            page_counter = page_counter
                        else:
                            page_counter += 1
                            new_embed.set_image(url = p[page_counter - 1])
                            new_embed.set_footer(text = f"{page_counter}/{l}")
                            await msg.edit(embed=new_embed) 
                
                if em == '⬅️':
                    if user == message.author:
                        if page_counter == 1:
                            page_counter = page_counter
                        else:
                            page_counter -= 1 
                            new_embed.set_image(url = p[page_counter - 1]) 
                            new_embed.set_footer(text = f"{page_counter}/{l}")
                            await msg.edit(embed=new_embed)

                if em == '↘️':
                    if user == message.author:
                        if page_counter == l:
                            page_counter = page_counter
                        else:
                            page_counter = l 
                            new_embed.set_image(url = p[page_counter - 1])
                            new_embed.set_footer(text = f"{page_counter}/{l}")
                            await msg.edit(embed=new_embed) 
                
                if em == '↖️':
                    if user == message.author:
                        if page_counter == 1:
                            page_counter == page_counter
                        
                        else:
                            page_counter = 1 
                            new_embed.set_image(url = p[page_counter - 1]) 
                            new_embed.set_footer(text = f"{page_counter}/{l}")
                            await msg.edit(embed=new_embed)
                            

                if em == '🚽':
                    await msg.edit(embed=flush_embed)
                    await msg.remove_reaction(emoji="↖️" , member=client.user)
                    await msg.remove_reaction(emoji="➡️" , member=client.user)
                    await msg.remove_reaction(emoji="⬅️" , member=client.user)
                    await msg.remove_reaction(emoji="↘️" , member=client.user)
                    await msg.remove_reaction(emoji="🚽" , member=client.user)
                    await msg.delete() 
                    break 
        else:
            await message.channel.send("``Please run this command in a NSFW Channel``")

    await client.process_commands(message)

#PING 
@client.command(pass_context=True, brief="Shows the pings of this bot")
async def ping(ctx):
    x = random.choice([range(100)]) 
    if x == 69:
        msg = await ctx.send("``Please run this command in a NSFW Channel``")
        await asyncio.sleep(2)
        x = f"lol jk!\nits {round(client.latency * 1000)} ms" 
        await msg.edit(content =x ) 
    
    else:
        em = Embed(description="aaah~~", colour=ctx.author.colour)
        ea = Embed(description=f"<a:696321747976454144:786442106474332221> **{round(client.latency * 1000)} ms**", colour=ctx.author.colour)
        msg = await ctx.send(embed=em)
        await asyncio.sleep(1) 
        await msg.edit(embed = ea)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            f"`BAKA! Resources are limited , you may retry after {error.retry_after:.2f} seconds`"
        )
        return

client.run('__your-token__')