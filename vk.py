from vk_api import VkApi, exceptions
from config import vk_token
from datetime import datetime, date, timedelta, timezone
from time import sleep

while True:
    try:
        vk = VkApi(token=vk_token)
        counted_friends = len(vk.method("friends.getOnline"))

        delta = timedelta(hours=3, minutes=0)
        now_date = datetime.now(timezone.utc) + delta
        format_date, format_date_ege, format_minutes, format_hours = "%H:%M ● %d.%m.%Y", "%Y.%m.%d", "%M", "%H"
        
        now_date_ege, ege_date = now_date.strftime(format_date_ege).split('.'), date(2022, 6, 20)    #тут поменяй дату
        updated_date_ege = date(int(now_date_ege[0]), int(now_date_ege[1]), int(now_date_ege[2]))
        
        after_date = 'Удачи на Егэ Крабоед'     #тут текст по истечению даты
        ege = f'До ЕГЭ по Инфе {str(str(ege_date - updated_date_ege).split()[0])} дней'\
            if int((str(ege_date - updated_date_ege).split()[0])) > 0 else after_date

        hours = 24 * int((str(ege_date - updated_date_ege).split()[0])) - int(now_date.strftime(format_hours))
        minutes = 60 - (int(datetime.now().strftime(format_minutes))) if hours > 0 else 0
        
        vk.method("status.set", {"text": f"""● Сейчас: {now_date.strftime(format_date)}
● Друзей онлайн: {counted_friends}
● {ege}
● Или {hours} часов {minutes} минут"""})    
        sleep(30)
    except exceptions.Captcha as captcha:
        sleep(30)
