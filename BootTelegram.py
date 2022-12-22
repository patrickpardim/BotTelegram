import telebot

Chave_API = "5948125413:AAG3mkjmpp9McoQbqk_fRdJMt22wV3qQGGU"

bot = telebot.TeleBot(Chave_API)

#Opção 1 - Para seleção de suporte via whatsapp ou ticket pelo site
#Nenhum suporte será feitpo se não aberto um ticket para atendimento

@bot.message_handler (commands = ["opcao1"])
def opcao1 (mensagem):
    textoOpcao1 = """
Entre em contato com nosso time de suporte via WhatsApp ou abra um Ticket por e-mail.

Whatsapp: 028 99275-5959
E-mail: suporte@pardim.com.br

Clique aqui para retornar ao início /iniciar."""
    bot.send_message(mensagem.chat.id, textoOpcao1)

#Opção 2 - Orçamentos de bot telegram, bot whatsapp ou criação de sites
#Orçamentos serão tratados via e-mail

@bot.message_handler (commands = ["opcao2"])
def opcao2 (mensagem):
    textoOpcao2 = """
Escolha uma das opções abaixo:
/telegram - Bot Telegram
/whatsapp - Bot WhatsApp
/sites - Sites

Clique aqui para retornar ao início /iniciar."""
    bot.send_message(mensagem.chat.id, textoOpcao2)

#Funções do menu de Orçamentos

@bot.message_handler (commands = ["telegram"])
def telegram (mensagem):
    textoTelegram = """
Bot Telegram:
    
Bot com 3 Menus - R$ 120,00
Bot com 4 Menus - R$ 160,00
Bot com 5 Menus - R$ 200,00

Clique aqui para retornar ao início /iniciar."""
    bot.send_message(mensagem.chat.id, textoTelegram)

@bot.message_handler(commands = ["whatsapp"])
def whatsapp (mensagem):
    textoWhatsapp = """
Bot WhatsApp:

Bot com 3 Menus - R$ 160,00
Bot com 4 Menus - R$ 190,00
Bot com 5 Menus - R$ 220,00

Clique aqui para retornar ao início /iniciar."""
    bot.send_message(mensagem.chat.id, textoWhatsapp)

@bot.message_handler(commands = ["sites"])
def sites (mensagem):
    textoSites = """
Sites:

Sites com 3 Menus - R$ 2.000,00
Sites com 4 Menus - R$ 2.400,00
Sites com 5 Menus - R$ 2.800,00
Upgrade FrontEnd - 1.300,00

Clique aqui para retornar ao início /iniciar."""
    bot.send_message(mensagem.chat.id, textoSites)

#Opção 3 - Meios de contatos para dúvidas e orçamentos.

@bot.message_handler(commands = ["opcao3"])
def opcao3 (mensagem):
    textoOpcao3 ="""
Entre em contato e tire suas dúvidas.

Whatsapp: 028 99275-5959
E-mail: patrick@pardim.com.br

Clique aqui para retornar ao início /iniciar."""

    bot.send_message(mensagem.chat.id, textoOpcao3 )

def verificar (mensagem):
    return True

#Mensagem do menu principal.

@bot.message_handler (func = verificar)
def responder (mensagem):
    textoBase = """
Olá! Me chamo Sexta Feira e estou aqui para te auxiliar. Como posso te ajudar?

Escolha uma das opções abaixo:
/opcao1 - Suporte
/opcao2 - Orçamentos
/opcao3 - Contatos

Obs: Mensagens fora as opções abordadas serão inválidas."""
    bot.reply_to (mensagem, textoBase)

bot.polling ()