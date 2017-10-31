import sys
import time
import schedule
import telepot
import telepot.namedtuple
from telepot.loop import MessageLoop

def job():
   bot.sendMessage(138615157, "Happy Ferd Fern Friday! It starts at 5 at 3rd Turn Brewery!")

schedule.every(1).minutes.do(job)
# schedule.every().friday.at("12:15").do(job)

bot = telepot.Bot('150228003:AAFgf0P8PNikpMBTKwoaNt7vAK-Yj8KX9C8')
# MessageLoop(bot, job).run_as_thread()
print 'Listening ...'

# Keep the program running.
while True:
   schedule.run_pending()
   time.sleep(1)