from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import datetime

print('Inicializando o Bot')

#pip install python-telegram-bot

# Código de identificação do bot
TOKEN: Final = ''

BOT_USERNAME: Final = '@'

# Lets us use the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Olá, eu sou o NOME DO SEU BOT! Como posso ajudar?')

# Lets us use the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Se precisa de ajuda, selecione uma das seguintes opções: \n /start \n /help \n /monitoria \n /ps \n /site \n /instagram \n /GEPC')

# Lets us use the /custom command
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('teste')

# Lets us use the /monitoria command
async def monitoria_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Se você deseja solicitar uma monitoria acesse o link: \nNossas monitorias semanais acontecem na sala do Pet que fica no bloco 725. \nEm qual semestre você está: \n /primeiro \n /terceiro ')

# Lets us use the /primeiro command
async def primeiroSemestre_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Monitorias Disponíveis para o Primeiro Semestre:\nCálculo Fundamental: \nSegunda e Quarta (14h-16h)  \nFísica: \nTerça e Quinta (13h-15h) \nIndrodução à Programação: \nSexta (13h-14h)')

# Lets us use the /terceiro command
async def terceiroSemestre_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Monitorias Disponíveis para o Terceiro Semestre:\nCálculo Vetorial: \nQuarta (13h-14h) \nPOO: \nSexta (14h-16h)')

# Lets us use the /origens command
async def origens_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('eu vim daqui: https://www.youtube.com/watch?v=vZtm1wuA2yc&ab_channel=Indently')

# Lets us use the /ps command
async def ps_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('As inscrições para o processor seletivo começam no dia 22 de junho e se extenderão até o dia 02 de julho.\n\nPara mais detalhes, acesse o link do edital:')

# Lets us use the /site command
async def site_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Você pode acessar o nosso site pelo link:')

# Lets us use the /instagram command
async def insta_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Você pode acessar o nosso Instagram pelo link: ')

# Lets us use the /GEPC command
async def gepc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Você pode se inscrever no Grupo de Estudos em Programação Competitiva pelo link:')





#repostas
def handle_response(text: str) -> str:
    # Create your own response logic
    processed: str = text.lower()

    if 'oi' in processed:
        return 'Oi :)'

    if 'como vc tá bot?' in processed:
        return 'Estou bem, e você?'

    if 'também estou bem' in processed:
        return 'Que bom que você está bem, continue assim :)'

    if 'bom dia' in processed:
        return 'Bom dia! :)'

    if 'boa tarde' in processed:
        return 'Boa tarde! :)'

    if 'boa noite' in processed:
        return 'Boa noite! :)'

    if 'f' in processed:
        return 'Fui mlk... capotei o corsa'

    if 'data de hoje' in processed:
        current_date = datetime.datetime.now().strftime('%d-%m-%Y')
        return f'A data de hoje é {current_date}'

    return 'Desculpe, não entendi. Use o comando  /help para que eu possa ajuda-lo.'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    #Caso ele esteja em um grupo, ele só reagirá às mensagens caso seja mencionado
    if message_type == 'group':

        # Detectando se o bot foi mencionado
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)

        else:
            return  #não reage se não for mencionado

    else:
        response: str = handle_response(text)

    # Reply normal if the message is in private
    print('Bot:', response)
    await update.message.reply_text(response)


# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()


    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('monitoria', monitoria_command))
    app.add_handler(CommandHandler('origens', origens_command))
    app.add_handler(CommandHandler('ps', ps_command))
    app.add_handler(CommandHandler('site', site_command))
    app.add_handler(CommandHandler('instagram', insta_command))
    app.add_handler(CommandHandler('primeiro', primeiroSemestre_command))
    app.add_handler(CommandHandler('terceiro', terceiroSemestre_command))
    app.add_handler(CommandHandler('GEPC', gepc_command))


    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))


    # Log all errors
    app.add_error_handler(error)
    print('Verificando...')


    # Run the bot
    app.run_polling(poll_interval=5)
