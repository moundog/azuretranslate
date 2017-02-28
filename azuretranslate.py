#!/usr/bin/env python

import argparse
import dotenv
import logging
import os
import requests
import sys
import time
import xml.etree.ElementTree

def main(inputText, fromLangCode, toLangCode):
  apiKey = getKey()
  logging.info('API key: ' + apiKey)

  tokenString = getToken(apiKey)
  logging.info('Temporary token: ' + tokenString)

  translationText = getTranslation(inputText, fromLangCode, toLangCode, tokenString)

  return translationText

def getKey():
  """ Retrieve the API key from the .env file """

  dotenvPath = os.path.join(os.path.dirname(__file__), '.env')

  if os.path.isfile(dotenvPath): # The .env file exists
    dotenv.load_dotenv(dotenvPath)
    apiKey = os.environ.get('API_KEY')
  else:
    sys.exit('Error: the .env file is missing')

  return apiKey

def getToken(apiKey):
  """ Request an access token (only valid for 10 minutes) """

  dottokenPath = os.path.join(os.path.dirname(__file__), '.token')

  if os.path.isfile(dottokenPath): # The .token file exists
    with open(dottokenPath) as tokenFile:
      fileData = tokenFile.read().split()
      tokenTime = int(fileData[0])
  else:
    tokenTime = 0

  epochTime = int(round(time.time()))

  if epochTime > tokenTime + 540: # The access token stored locally is older than 9 minutes
    logging.info('Requesting a new access token...')

    headers = {
      'Ocp-Apim-Subscription-Key': apiKey
    }

    issueTokenURL = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'

    try:
      authToken = requests.post(issueTokenURL, headers = headers).text
    except OSError:
      pass

    with open(dottokenPath, 'w') as tokenFile:
      tokenFile.write(str(epochTime) + ' ' + authToken)

    tokenString = 'Bearer ' + authToken
  else:
    tokenString = 'Bearer ' + fileData[1]

  return tokenString

def getTranslation(inputText, fromLangCode, toLangCode, tokenString):
  """ Translate the text """

  headers = {
    'Authorization': tokenString
  }

  # Force the call on the Dublin datacenter, refer to https://cognitive.uservoice.com/knowledgebase/articles/1128385-api-text-european-datacenter for more details
  #translateURL = 'https://api-db4.microsofttranslator.com/v2/http.svc/Translate?text={}&from={}&to={}'.format(inputText, fromLangCode, toLangCode)
  translateURL = 'https://api.microsofttranslator.com/v2/http.svc/Translate?text={}&from={}&to={}'.format(inputText, fromLangCode, toLangCode)

  try:
    translationData = requests.get(translateURL, headers = headers)
    translationText = xml.etree.ElementTree.fromstring(translationData.text.encode('utf-8')).text
  except OSError:
    pass

  return translationText

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description = 'This script uses the Microsoft Text Translation API to translate text')
  parser.add_argument('input_text', help = 'The text to translate (max 10k characters)')
  parser.add_argument('-f', '--from', default = 'fr', dest = 'from_lang_code', help = 'the language code of the translation text')
  parser.add_argument('-t', '--to', default = 'en', dest = 'to_lang_code', help = 'the language code to translate the text into')
  args = parser.parse_args()

  translationText = main(args.input_text, args.from_lang_code, args.to_lang_code)
  print(translationText)
