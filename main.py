
from googletrans import Translator

class Translator:
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
        self.arabik_dict = {
            'البرنامج': 'программа',
            'التكنولوجيا': 'технология',
            'الابتكار': 'инновация',
            'سوبرمان': 'супермен'
        }
        self.China_dict = {
            '计划': 'программа',
            '科技': 'технология',
            '创新科技': 'инновация',
            '超人': 'супермен'
        }
        self.Japanese_dict = {
            'プログラム': 'программа',
            '技術': 'технология',
            'イノベーション': 'инновация',
            'スーパーマン': 'супермен'
        }
        self.Belarus_dict = {
            'праграма': 'программа',
            'тэхналогія': 'технология',
            'інавацыя': 'инновация',
            'супермэн': 'супермен'
        }
        self.German_dict = {
            'das Programm': 'программа',
            'Technologie': 'технология',
            'Innovation': 'инновация',
            'Superman': 'супермен'
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
translator2 = Translator("я")
print(translator2.translator_text())
translator3 = Translator("банан")
print(translator3.translator_text())
translator4 = Translator("город")
print(translator4.translator_text())
translator5 = Translator("человек")
print(translator5.translator_text())
translator6 = Translator("technology")
print(translator6.translator_text())
translator7 = Translator("program")
print(translator7.translator_text())
translator8 = Translator("innovation")
print(translator8.translator_text())
translator9 = Translator("super man")
print(translator9.translator_text())
translator10 = Translator("البرنامج")
print(translator10.translator_text())
translator11 = Translator("التكنولوجيا")
print(translator11.translator_text())
translator12 = Translator("الابتكار")
print(translator12.translator_text())
translator13 = Translator("سوبرمان")
print(translator13.translator_text())
translator14 = Translator("计划")
print(translator14.translator_text())
translator15 = Translator("科技")
print(translator15.translator_text())
translator16 = Translator("创新科技")
print(translator16.translator_text())
translator17 = Translator("超人")
print(translator17.translator_text())
translator18 = Translator("プログラム")
print(translator18.translator_text())
translator19 = Translator("技術")
print(translator19.translator_text())
translator20 = Translator("イノベーション")
print(translator20.translator_text())
translator21 = Translator("スーパーマン")
print(translator21.translator_text())
translator22 = Translator("праграма")
print(translator22.translator_text())
translator23 = Translator("тэхналогія")
print(translator23.translator_text())
translator24 = Translator("інавацыя")
print(translator24.translator_text())
translator25 = Translator("супермэн")
print(translator25.translator_text())
translator26 = Translator("das Programm")
print(translator26.translator_text())
translator27 = Translator("Technologie")
print(translator27.translator_text())
translator28 = Translator("Innovation")
print(translator28.translator_text())
translator29 = Translator("Superman")
print(translator29.translator_text())



#кгврпгщпщвщ




















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