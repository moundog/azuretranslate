# azuretranslate

## Description

This Python module uses the [Microsoft Text Translation API](https://azure.microsoft.com/en-us/services/cognitive-services/translator-text-api/) to translate text. It supports more than 50 languages and offers a free tier with 2 million characters per month.

![alt text](https://raw.githubusercontent.com/moundog/azuretranslate/master/img/translator.png "Microsoft Translator")

Requires Python 2.7 or greater (tested with Python 2.7 on Mac OS X).

## Installation

1. Setup the Text Translation API from the [Microsoft Azure Portal](https://portal.azure.com/), please refer to http://docs.microsofttranslator.com/text-translate.html for more details
2. Clone this repository, install the dependencies, and copy your API key to a `.env` file
```shell
$ pip install -r requirements.txt
$ echo 'API_KEY="<YOUR_API_KEY>"' > .env
```
3. Translate some text 🙂
  * As a Python module
  ```python
  import azuretranslate
  translationText = azuretranslate.main('Success consists of going from failure to failure without loss of enthusiasm', 'en', 'fr')
  ```
  * As a Python script
  ```shell
  $ python azuretranslate.py 'Success consists of going from failure to failure without loss of enthusiasm' -f 'en' -t 'fr'
  ```

## License

Copyright 2017 Mounir Krichane

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
