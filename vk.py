from vk_api import VkApi, exceptions
from config import vk_token
from datetime import datetime, date, timedelta, timezone
from time import sleep


while True:
    try:
        def timedelta_to_hms(duration):
            days, seconds = duration.days, duration.seconds
            hours = days * 24 + seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = (seconds % 60)
            return hours, minutes, seconds


        vk = VkApi(token=vk_token)
        counted_friends = len(vk.method("friends.getOnline"))

        delta = timedelta(hours=3, minutes=0)
        now_date = datetime.now(timezone.utc) + delta
        format_date, format_date_ege = "%H:%M ● %d.%m.%Y", "%Y.%m.%d"

        now_date_ege, ege_date = now_date.strftime(format_date_ege).split('.'), date(int(2022), int(6), int(20))    #Вместо 2022, 6, 20 поставь свой день
        updated_date_ege = date(int(now_date_ege[0]), int(now_date_ege[1]), int(now_date_ege[2]))
        hours, minutes, seconds = timedelta_to_hms(ege_date-updated_date_ege)

        vk.method("status.set", {"text": f"""● Сейчас: {now_date.strftime(format_date)}
● Друзей онлайн: {str(counted_friends)}
● До ЕГЭ по Инфе {str(str(ege_date-updated_date_ege).split()[0])} дней
● Или {hours} часов {minutes+2} минут"""})
        sleep(30)
    except exceptions.Captcha as captcha:
        VkApi(token=vk_token).captcha_handler(captcha)
        # def captcha_handler(captcha):
        #     key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()
        #     return captcha.try_again(key)
        sleep(30)
