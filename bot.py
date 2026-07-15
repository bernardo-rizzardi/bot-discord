import discord
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
produtos = [
    {'id': 1, 'nome': 'Camiseta', 'preco': 49.90},
    {'id': 2, 'nome': 'Boné', 'preco': 29.90},
    {'id': 3, 'nome': 'Caneca', 'preco': 19.90},
]

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!produtos':
        resposta = '**Produtos disponíveis:**\n'
        for p in produtos:
            resposta += f"ID {p['id']} — {p['nome']} — R$ {p['preco']:.2f}\n"
        await message.channel.send(resposta)

client.run(TOKEN)