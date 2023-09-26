from telegram import Bot

# Reemplaza 'TOKEN' por tu token de API obtenido del BotFather
bot = Bot('5868349882:AAHPKuCBlOzaueLPAEBbXfsWIGb-hnhwdNY')

# Reemplaza 'CHAT_ID' por el ID de chat al que deseas enviar el mensaje
chat_id = '1643312165'

# Reemplaza 'Tu mensaje aquí' por el contenido del mensaje que deseas enviar
message = 'Tu mensaje aquí'

# Envía el mensaje utilizando el método 'send_message' del bot
bot.send_message(chat_id=chat_id, text=message)
