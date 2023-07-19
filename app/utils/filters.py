def format_date(date):
  return date.strftime('%m/%d/%y')

#test format_date() function by python app/utils/filters.py
# from datetime import datetime
# print(format_date(datetime.now()))

def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# test format_url() function python app/utils/filters.py
# print(format_url('http://google.com/test/'))
# print(format_url('https://www.google.com?q=test'))

def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word

# test format_plural() function python app/utils/filters.py
# print(format_plural(2, 'cat'))
# print(format_plural(1, 'dog'))