from dataIntoMails import dataIntoMails
from cacheFlush import cacheFlush
import atexit
from sender import sender

if __name__ == "__main__":

  atexit.register(cacheFlush)

  mails = dataIntoMails()

  sender(mails)
  