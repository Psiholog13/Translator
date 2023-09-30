
from googletrans import Translator

class git init
git add --all
git commit -m "M1L4 - my translator"
git branch -M main
git remote add origin https://github.com/Psiholog13/Perevod.git
git push -u origin main

:
    def __init__(self, word_obj):
        self.word = word_obj
        self.translator = Translator()
        self.russian_dict = {
            "я": "I",
            "яблоко": "apple",
            'банан': "banana",
            'город': 'city',
            'человек': 'human'
        }
        self.english_dict = {
                            'program': 'программа',
                            'technology': 'технология',
                            'innovation': 'инновация',
                            'super man': 'супермен'
        }

    def translator_text(self):
        if self.word in self.russian_dict:
            return self.russian_dict[self.word]
        elif self.word in self.english_dict:
            return self.english_dict[self.word]
        else:
            return "Слово не найдено"

translator1 = Translator("яблоко")
print(translator1.translator_text())
translator2 = Translator("technology")
print(translator2.translator_text())





















        # class Car:
#     speed = 250
#     mark = "Ford"
#     model = 'F23'
#
#     def __init__(self, color_car):
#         self.color = color_car
#
# obj1 = Car('Green')
# obj2 = Car('Yellow')
# obj3 = Car('Blue')
#
# print(obj1.model)





#from telegram import Bot, Update, ForceReply
#from telegram.ext import Updater, CommandHandler, MessageHandler, Application, ContextTypes
#from credits import bot_token



#class MyBot:
    #def __init__(self, bot_token):
        #self.application = Application.builder().token(bot_token).build()

        # Регистрируем обработчики команд
        #self.application.add_handler(CommandHandler("start", self.start))
        #self.application.add_handler(CommandHandler("help", self.help))
        #self.application.run_polling(allowed_updates=Update.ALL_TYPES)

    #async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        #"""Send a message when the command /start is issued."""
        #user = update.effective_user
        #print(user.mention_html())
       # await update.message.reply_html(
            #f"Hi {user.mention_html()}!",
            #reply_markup=ForceReply(selective=True),
        #)

    #async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
       # await update.message.reply_text(text="Это простой бот. Он может отвечать на текстовые сообщения.")
   # async def help_hello(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
            #await update.message.reply_text(text="Это простой бот. Он может отвечать на текстовые сообщения.")


#if __name__ == "__main__":
    #bot = MyBot(bot_token=bot_token)