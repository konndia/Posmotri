import datetime as dt
import time, schedule, threading
from django.conf import settings
from django.core.mail import send_mail

# print(dt.datetime.now())
# def remind(time1, email_to):
#     time1 = time1.split('.')
#     print(dt.date())
#     time.sleep(send_time.timestamp() - dt.date())
#     send_mail("Посмотри - напоминание", "Здравствуйте, не забудьте про фильм, билет на который вы заказали", settings.EMAIL_HOST_USER, email_to)

def remind(email_to):
    now = dt.datetime.now()
    run_at = now + dt.timedelta(seconds=20)
    delay = (run_at - now).total_seconds()
    # threading.Timer(delay, self.update).start()
    time.sleep(delay)
    send_mail("Посмотри - напоминание", "Здравствуйте, не забудьте про фильм, билет на который вы заказали", settings.EMAIL_HOST_USER, email_to)
    # time.sleep(delay)
    # send_mail("Посмотри - напоминание", "Здравствуйте, не забудьте про фильм, билет на который вы заказали", settings.EMAIL_HOST_USER, email_to)

# async def main(email_to):
#     task = asyncio.create_task(remind(email_to))
#     await task