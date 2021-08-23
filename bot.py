import os
import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

from voice import text_to_file

f = open('token.txt', 'r')
TOKEN = f.read()

def hello(update, context):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def help_handler(update, context):
    help_text = "Наш бот косит под политика начала прошлого века в ответ на ваше сообщение"
    update.message.reply_text(help_text)

def reply(update, context):
    """Generate reply message."""
    source_1 = ['Товарищи!', 'С другой стороны, ', 'Равным образом, ', 'Не следует, однако, забывать, что ', 'Таким образом, ', 'Повседневная практика показывает, что ', 'Уважаемые коллеги! ', 'Позвольте Вам напомнить, что ', 'Также, как ', 'В целом, конечно, ']
    source_2 = [' реализация намеченных плановых заданий', ' рамки и место обучения кадров', ' 	постоянный количественный рост и сфера нашей активности', ' сложившаяся структура организации', ' новая модель организационной деятельности', ' дальнейшее развитие различных форм деятельности', ' перспективное планирование', ' оптимизация основных целей ', ' экономическая повестка сегоднящнего дня', ' внедрение современных подходов']
    source_3 = [' играет важную роль в формировании ', ' требуют от нас анализа ', ' требуют определения и уточнения ', ' способствует подготовке и реализации ', ' обеспечивает широкому кругу (специалистов) участие в формировании ', ' позволяет выполнить важные задания по разработке ', ' не дает нам иного выбора, кроме определения ', ' вынуждает нас объективно потребовать ', ' играет определяющее значение для  ', ' выявляет срочную потребность ']
    source_4 = [' существенных финансовых и административных условий', ' дальнейших направлений развития', ' системы массового участия', ' позиций, занимаемых участниками в отношении поставленных задач', ' новых предложений', ' направлений прогрессивного развития', ' стандартных подходов', ' нестандартных решений', ' экономических и неэкономических факторов и перспектив', ' инновационных методов управления процессами']
    text_to_reply = random.sample (source_1, 1) + random.sample (source_2, 1) + random.sample (source_3, 1) + random.sample (source_4, 1) 
    update.message.text = "".join(text_to_reply)
    file_name = text_to_file(update.message.text)
    #update.message.reply_text(update.message.text)
    update.message.reply_voice(voice = open(file_name, 'rb'))
    os.remove(file_name)

    

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', help_handler))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

updater.start_polling()
updater.idle()
