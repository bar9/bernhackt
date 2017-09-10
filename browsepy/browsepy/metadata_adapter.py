import random
import datetime
import hashlib

class MetadataAdapter:

    def getBlockchainStatus(self, path):
      return 1

    def getVerificationStatus(self, path):
      return random.randint(0, 1)

    def getConfirmationDate(self, path):
      return datetime.datetime.now().strftime("%d %b %Y %H:%M:%S")

    def getTransactionId(self, path):
      return 1

    def isTracked(self, path):
      return random.randint(0, 1)

    def verifiedHash(self, path):
      return hashlib.sha224("Nobody inspects the spammish repetition").hexdigest()

    def calculatedHash(self, path):
      return hashlib.sha224("Nobody inspects the spammish repetition").hexdigest()
