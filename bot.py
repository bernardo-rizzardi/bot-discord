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

carrinho = dict()

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

    if message.content.startswith('!adicionar'):
        mensagem = message.content.split()
        produtoId = int(mensagem[1])
        if message.author.id not in carrinho:
            carrinho[message.author.id] = []
        carrinho[message.author.id].append(produtoId)
        
        resposta = f"Produto {produtos[produtoId - 1]['nome']} adicionado ao seu carrinho!"
        await message.channel.send(resposta)
        
    if message.content == '!carrinho':
        userID = message.author.id
        if userID not in carrinho:
            await message.channel.send("Seu carrinho está vazio!\n")
            return

        valor = 0
        resposta = ""
        produto = {}
        lista = carrinho[message.author.id]
        for i in lista:
            produto = produtos[i - 1]
            resposta += f"{produto['nome']}: R$ {produto['preco']:.2f}\n"
            valor += produto['preco']

        resposta += f"Preço total: R$ {valor:.2f}\n"
        await message.channel.send(resposta)

client.run(TOKEN)