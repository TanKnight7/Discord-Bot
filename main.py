import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

from apikeys import *

client = commands.Bot(command_prefix="!",intents=discord.Intents.all(),owner_id=owner_id)

@client.event
async def on_ready():
    print("Bot nyala")
    channel = client.get_channel(admin_channel_id)
    await channel.send(f"Bot nyala!")

@client.event
async def on_member_join(member):
    channel = client.get_channel(member_join_id)
    await channel.send(f"```Selamat datang {member}!```")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(member_leave_id)
    await channel.send(f"```Selamat tinggal {member}!```")


@client.command(pass_context=True,description="Command ini digunakan untuk memasukkan bot ke dalam voice channel")
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        await ctx.send("Gua dah masuk vc!")
    else:
        await ctx.send("Masuk vc dlu!")

@client.command(pass_context=True, description ="Command ini digunakan untuk mengeluarkan bot dari voice channel")
async def leave(ctx):
    if (ctx.voice_client):
        channel = ctx.guild.voice_client
        await channel.disconnect()
    else:
        await ctx.send("Join vc dlu baru kick aku woi!")

@client.command(pass_context=True, description ="Command ini digunakan untuk memainkan lagu, berikut adalah penulisannya:\n!play <lagu>")
async def play(ctx,*arg):
    if (ctx.voice_client):
        list_lagu = ["dream","windah","cinematic"]
        if arg[0] in list_lagu:
            voice = discord.utils.get(client.voice_clients,guild = ctx.guild)
            if voice.is_playing():
                voice.stop()
            source = FFmpegPCMAudio("music\\"+arg[0] + ".mp3")
            player = ctx.guild.voice_client.play(source)
            await ctx.send(f"Playing {arg[0]}!")
        else:
            await ctx.send("Lagunya gak ada!")
            await ctx.send(f"Ini list lagunya:")
            nomor = 0
            for lagu in list_lagu:
                nomor +=1
                print(nomor,lagu)
                await ctx.send(f"{nomor}. {lagu}")
                           
    else:
        await ctx.send("masukin aku ke vc dlu, baru req lagu")

@client.command(pass_context=True, description="Command ini digunakan untuk men-stop lagu")
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    voice.stop()

@client.command(pass_context=True, description="Command ini digunakan untuk melanjutkan lagu")
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    voice.resume()

@client.command(pass_context=True, description="Command ini digunakan untuk mem-pause lagu")
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    voice.pause()

@client.command(description="This command is used to shutdown the bot (OWNER ONLY)")
@commands.has_permissions(administrator=True)
async def shutdown(ctx):
    await ctx.send("Aku dimatikan :(")
    await client.close()


## PELAJARAN
@client.command(description="Command ini digunakan untuk menunjukkan list-list pelajaran")
async def pelajaran(ctx):
    list_pelajaran = ["Python"]
    nomor = 0
    for i in list_pelajaran:
        nomor += 1
        await ctx.send(f"{nomor}. {i}")












## PYTHON
@client.command(description="Command ini digunakan untuk menunjukkan list-list materi pada python, berikut adalah penulisannya:\n!python <list materi> <opsi lain>")
async def python(ctx,*arg):    
    print(arg)
    list_pelajaran_python = ["tipe_data", "for_loop"]
    opsi_lain = ["penjelasan"]

    if len(arg) == 0:
        await ctx.send(f"```!python <list materi> <opsi lain>```")
        await ctx.send(f"```List materi: \n\t1) Tipe_data \n\t2) For_loop \nOpsi lain: \n\t1) Penjelasan```")   

    elif len(arg) == 1:
        # 1. Tipe data
        if arg[0].lower() == "tipe_data":
            await ctx.send(f"``` Tipe data ada 9, yaitu:\n\t1) Integer\n\t2) Float\n\t3) String\n\t4) Boolean\n\t5) List\n\t6) Tuple\n\t7) Dictionary\n\t8) Complex\n\t9) Hexadecimal```")
            await ctx.send(f"```Apakah kamu ingin penjelasan lebih lanjut? Ketik ini:\n!python tipe_data penjelasan```")

        # 2. For loop
        elif arg[0].lower() == "for_loop":
            await ctx.send(f"masih dikembangkan")
        
        #################################################
        else:
            await ctx.send(f"Maaf, kami mengalami eror dari input anda, cobakan tuliskan berdasarkan yang saya ketik disini!")
            await ctx.send(f"```!python <list materi> <opsi lain>```")
            await ctx.send(f"```List materi: \n\t1) Tipe_data \n\t2) For_loop \nOpsi lain: \n\t1) Penjelasan```")
    


    elif len(arg) == 2:
        if arg[0] in list_pelajaran_python:
            if arg[1].lower() == "penjelasan":
                await ctx.send(file=discord.File("Images\python(1).jpg"))
            #####################################
            else:
                await ctx.send(f'```Maaf, opsi lainnya hanya berupa:\n1) Penjelasan```')
        #########################################
        else:
            await ctx.send(f"Maaf, kami mengalami eror dari input anda, cobakan tuliskan berdasarkan yang saya ketik disini!")
            await ctx.send(f"```!python <list materi> <opsi lain>```")
            await ctx.send(f"```List materi: \n\t1) Tipe_data \n\t2) For_loop \nOpsi lain: \n\t1) Penjelasan```")

    ####################################
    else:
        await ctx.send(f"Maaf, kami mengalami eror dari input anda, cobakan tuliskan berdasarkan yang saya ketik disini!")
        await ctx.send(f"```!python <list materi> <opsi lain>```")
        await ctx.send(f"```List materi: \n\t1) Tipe_data \n\t2) For_loop \nOpsi lain: \n\t1) Penjelasan```")




client.run(botToken)