import telebot


TOKEN = "667031004:AAGNmIEUqL1KGvCUntaxuISLFrt54Y68rfo"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.from_user.id, "Добро пожаловать в DEVOTION BOT.\n\n")
    bot.register_next_step_handler(sent, hello)
    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.row("✈ТУРИЗМ✈","🚕ЗАКАЗ ТАКСИ🚕")
    markup.row("💷КОШЕЛЬКИ💷","💳ДЕБЕТОВЫЕ КАРТЫ💳")
    markup.row("🚁РАЗВЛЕЧЕНИЯ🚁","🔍ПРОБИВ🔍")
    markup.row("📁ДОКУМЕНТЫ📁","⚙СОФТ НА ЗАКАЗ⚙")
    markup.row("💡ДРУГИЕ УСЛУГИ💡")
    bot.send_message(message.from_user.id,"Введите Ваше имя", reply_markup=markup)


def hello(message):
    bot.send_message(message.chat.id, "Приветствую, {name}. Пожалуйста прочтите пользовательское соглашение между Telegram Bot'ом ","DEVOTION BOT"," и пользователем {name}:\n\n"
'1. DEVOTION BOT - (далее бот) является информационным ресурсом.\n'
'2. Бот, владельцы, разработчики и администраторы бота не несут ответственности за ваши действия по использованию сервисов, а также за сделки финансового и иного характеров. Исключением являются сделки проводимые администрацией ресурса.\n'
'3. Сервисы, продавцы и услуги вне бота не имеют никакого отношения к боту. Лица, выдающие себя за сервисы, администраторов, владельцев бота, могут таковыми не являются.\n'
'4. С актуальным списком сервисов вы можете ознакомиться в соответствующем разделе бота.\n'
'5. При заключении сделки с продавцом, размещенном в боте, ответственность полностью ложиться на Вас. Бот, администрация, модераторы не несут ответственности за ваши действия.\n'
'6. В случае возникновения спорных ситуаций необходимо решать напрямую с сервисом, при невозможности решения ситуации рекомендуем обратиться к Администрации бота.\n'
'7. С правилами, условиями, ценами и другими нюансами работы сервисов (продавцов), вы можете ознакомится, запросив информацию у любого из представленных сервисов (продавцов)/\n'
'8. Вы можете обезопасить свою сделку используя "Гарант-сервис". Как покупатель, так и продавец в праве предложить провести сделку через удобный ему "Гарант-сервис".\n'
'9. Продавцы допускаются к размещению в боте только при наличии "проверенной" темы и/или депозита на "проверенном*" форуме.\n'
'10. Проверенный форум - форум, который по мнению администрации бота является надежным (администрация учитывает следующие факторы: известность форума, репутация форума, наличие положительных/негативных отзывов и многи другие факторы).\n'
'11. Услуги сервисов (продавцов), размещенных в боте, могут нарушать настоящее законодательство РФ. Администрация сервиса не несет отвественности за возможные последствия.\n'
'12. Подписываясь на данный Бот, вы даете свое согласие с данными правилами.\n'
'13. Данное соглашение может быть изменено в одностороннем порядке и без уведомления.\n\n'
'Для того что бы увидеть список сервисов (продавцов) выберите интересующую вас категорию.'.format(name=message.text))


@bot.message_handler(content_types=["text"])
def category(message):
    if message.text == "✈ТУРИЗМ✈":
            bot.send_message(message.from_user.id, "🏨 Отели по всему миру за 30% от кассы.\n"
"📱Добавить в Telegram 👉@FunnyFish7👈\n\n"
"✈️ Авиабилеты/Отели за 50/30% от кассы.\n"
"🏖 Договор от турфирмы в подарок!\n"
"📱Добавить в Telegram 👉@patriarh👈\n\n"
"🏨Отели по всему миру от Leto.\n"
"❤️Скидки и бонусы постоянным клиентам.\n"
"📱Добавить в Telegram 👉@LetoTravel👈\n\n"
"✈️ Авиа/Отели по всему миру от Трикстера.\n"
"📱Добавить в Telegram 👉@travelx👈\n\n"
"🏨 Bon Voyage Travel Отели с депозитом за 30%.\n"
"📱Добавить в Telegram 👉@bvoyage👈\n\n"
"✈️Авиа и отели от Alekmsk Travel.\n"
"📱Добавить в Telegram 👉@AlekmskTravel👈\n\n"
"🏨Авиа и отели от Hannibal.\n"
"📱Добавить в Telegram 👉@drhlecter👈".format(name=message.text))


    elif message.text == "🚕ЗАКАЗ ТАКСИ🚕":
            bot.send_message(message.from_user.id, "🚕Длинные и короткие поездки по всему миру.\n"
"📱Добавить в Telegram 👉@Vip_Taxist👈\n\n"
"🚕Сервис заказа такси от UberTENb\n"
"📱Добавить в Telegram 👉@UberTENb👈\n\n"
"🚕 VIP Такси от Патриарха 24/7\n"
"📱Добавить в Telegram 👉@patriarh👈\n\n"
"🚕 Дешевый серви такси от Sumon.\n"
"📱Добавить в Telegram 👉@free_taxi👈\n\n"
"🚕 Премиум Такси от Binelli88 без слетов.\n"
"📱Добавить в Telegram 👉@Binelli88👈\n\n"
"🚕@Taxi_London - такси по всему миру!\n"
"📱Добавить в Telegram 👉@Taxi_London👈\n\n"
'🚕 Хороший сервис такси от mahrez_msk.\n'
'📱Добавить в Telegram 👉@mahrez_msk👈\n\n'
'🚕 Длинные поезди от такси сервиса "Комрад"\n'
'📱Добавить в Telegram 👉@kamradtaxi👈\n\n'
'🚕 Такси сервис, работает по всему миру (Uber/Gett)\n'
'📱Добавить в Telegram 👉@LuxTaxiWorld👈\n\n'
'🚕 Услуги личных водителей Uber за бесценок.\n'
'📱Добавить в Telegram 👉@SteelEffective👈'.format(name=message.text))


    elif message.text == "💷КОШЕЛЬКИ💷":
        bot.send_message(message.from_user.id, "💷Идентификация QIWI/Яндекс кошельков.\n"
'📱Добавить в Telegram 👉@balabanovs👈\n\n'
'💷Идентификация кошельков QIWI и Yandex 24\7.\n'
'📱Добавить в Telegram 👉@etcshop_2010👈\n\n'
'💷Идентификация кошельков QIWI/YANDEX/ЦУПИС/PayPal.\n'
"📱Добавить в Telegram 👉@Darkeyerus👈".format(name=message.text))


    elif message.text == "💳ДЕБЕТОВЫЕ КАРТЫ💳":
        bot.send_message(message.from_user.id, '💳Дебетовые карты на дропов и на ваши сканы.\n'
'📱Добавить в Telegram 👉@parono👈\n\n'
'💳Дебетовые карты банков России под любые нужды.\n'
'📱Добавить в Telegram 👉@centrocc👈\n\n'
'💳Надежные дебетовые карты РФ, только качественный материал!\n'
'📱Добавить в Telegram 👉@korney1👈\n\n'
'💳 Дебетовые карты по низким ценам.\n'
'📱Добавить в Telegram 👉 @Cherep1488👈\n\n'
'💳 Продажа дебетовых карт РФ.\n'
'📱Добавить в Telegram 👉 @Cardsmarket👈\n\n'
'💳Надежные дебетовые карты РФ, только качественный материал.\n'
'📱Добавить в Telegram 👉 @BEREAL👈\n\n'
'💳Продажа Дебетовых Карт с Сохранностью денежных средств!\n'
'📱Добавить в Telegram 👉 @Georgi_Grup👈)'.format(name=message.text))


    elif message.text == "🚁РАЗВЛЕЧЕНИЯ🚁":
        bot.send_message(message.from_user.id, '🎢Экскурсии и Еда по всему миру.\n'
'📱Добавить в Telegram 👉@FoodAndTickets👈\n\n'
'🎭Билеты в театры Москвы за 50%.\n'
'📱Добавить в Telegram 👉@One_Entertainment 👈'.format(name=message.text))


    elif message.text == "🔍ПРОБИВ🔍":
        bot.send_message(message.from_user.id, '🔍Комплексный поиск информации по физическим и юридическим лицам.\n'
'📱Добавить в Telegram 👉@Monte_Cristo777👈\n\n'
'🔍Пробив/детализация сотов. операторов РФ.\n'
'📱Добавить в Telegram 👉@online250👈\n\n'
'🔍Проверка Кредитной Истории 90 руб.\n'
'📱Добавить в Telegram 👉@CreditReport👈\n\n'
'🔍Пробив по любым базам МИРА.\n'
'📱Добавить в Telegram 👉@DaVinci_Support👈\n\n'
'🔍Пробив, поиск, местоположение, детализация МТС, ТЕЛЕ2, Билайн, Мегафон,Yota. Государственный и банковский пробив!\n'
'📱Добавить в Telegram 👉@buro_info👈\n\n'
'🔍Комплексный пробив и поиск данных по РФ\n'
'📱Добавить в Telegram 👉@PhoenixFen👈'.format(name=message.text))


    elif message.text == "📁ДОКУМЕНТЫ📁":
        bot.send_message(message.from_user.id, '📑Изготовление дипломов и аттестатов.\n'
'📱Добавить в Telegram 👉@diplomist👈\n\n'
'📑 Изготовление: СТС РФ, СТС РБ, ГРЗ РФ, ГРЗ РБ, ВУ, ПТС.\n'
'📱Добавить в Telegram 👉@vovabirukov👈\n\n'
'📑 ПТС и СТС. Автодокументы Киргизия, республика Казахстан, республика Беларусь, РФ.\n'
'📱Добавить в Telegram 👉@zelezniychelovekk👈\n\n'
'📑Изготовление VIN маркировок, табличек, наклеек.\n'
'📱Добавить в Telegram 👉@zelezniychelovekk👈'.format(name=message.text))


    elif message.text == "⚙СОФТ НА ЗАКАЗ⚙":
        bot.send_message(message.from_user.id, '⚒ Скрытый FUD MINER BY SMM RID на заказ.\n'
'📱Добавить в Telegram 👉@turtk👈\n\n'
'⚒Nocturnal Stealer - 22+ браузеров, 28 крипто-кошельков [1500 руб.]\n'
'📱Добавить в Telegram 👉@neutentg👈\n\n'
'⚒Megumin Botnet | Clipper (6000 рублей)\n'
'📱Добавить в Telegram 👉@ddanijj👈\n\n'
'⚒[GPU+CPU] Скрытый майнер с админ-панелью от gladoff\n'
'📱Добавить в Telegram 👉@glad0ff​👈'.format(name=message.text))


    elif message.text == "💡ДРУГИЕ УСЛУГИ💡":
        bot.send_message(message.from_user.id, '🛒REFUND Средств за покупки в зарубежных интернет магазинах (ASOS, AMAZON, Victoriasecret и др.).\n'
'📱Добавить в Telegram 👉@ganglar👈\n\n'
'📡Подмена исходящего номера на +77777777777 (анонимная связь).\n'
'📱Добавить в Telegram 👉@JesusChristTheBestPersonInTheWeb👈\n\n'
'💡Профессиональный взлом ВКонтанкте от 1500 рублей.\n'
'📱Добавить в Telegram 👉@ccracck👈'.format(name=message.text))


@bot.message_handler(commands=['off'])
def off(message):
    bot.send_message(message.from_user.id,'Вы отписались от бота')

while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception:
        pass
