import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot conectado')

    guild_id = 1116483813397241878
    category_name = 'Prueba_'

    guild = bot.get_guild(guild_id)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }
    category = await guild.create_category(category_name, overwrites=overwrites)
    print(f'Categoría creada: {category.name}')

bot.run(os.getenv('BOT_TOKEN'))


# import discord
# from discord.ext import commands
# from flask import Flask, render_template, request

# intents = discord.Intents.default()
# intents.guilds = True

# bot = commands.Bot(command_prefix='!', intents=intents)

# app = Flask(__name__, template_folder='.')

# async def create_category(guild, category_name):
#     overwrites = {
#         guild.default_role: discord.PermissionOverwrite(read_messages=False),
#         guild.me: discord.PermissionOverwrite(read_messages=True)
#     }
#     category = await guild.create_category(category_name, overwrites=overwrites)
#     print(f'Categoría creada: {category.name}')

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         guild_id = int(request.form['guild_id'])
#         category_name = request.form['category_name']

#         guild = bot.get_guild(guild_id)
#         bot.loop.create_task(create_category(guild, category_name))
#         return 'Categoría creada exitosamente'

#     return render_template('index.html')

# @bot.event
# async def on_ready():
#     print('Bot conectado')

# bot.run('TOKEN')

# if __name__ == '__main__':
#     app.run()


