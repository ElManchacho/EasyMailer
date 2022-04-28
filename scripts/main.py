from dataIntoMails import dataIntoMails
from cacheFlush import cacheFlush
import atexit
from sender import sender
from menuUI import *

if __name__ == "__main__":

  atexit.register(cacheFlush)

  menuUi()

 # mails = dataIntoMails()

 # sender(mails)
  