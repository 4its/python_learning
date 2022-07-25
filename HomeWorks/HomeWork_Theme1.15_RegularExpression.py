import re

print('=== Task #1 никнейм пользователя, имя домена и суффикс ===')
# Извлеките никнейм пользователя, имя домена и суффикс из данных email адресов.
emails = """zuck26@facebook.com  page33@google.com  jeff42@amazon.com"""
emails_pattern = '(\w+)@(\w+)(\S*)'  # make a template
a = re.findall(emails_pattern, emails)  # use findall to receive a list of tuples
print('Before extraction: ', emails, '\nAfter extraction:  ', a)

print('\n=== Task #2 слова, начинающиеся с ‘b’ или ‘B’ ===')
# Извлеките все слова, начинающиеся с ‘b’ или ‘B’ из данного текста.
text = """Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."""
text_pattern = '([bB]\w+)'  # make a template
a = re.findall(text_pattern, text)
print('We have a text:                          ', text, '\nWords started from letters b and B is:   ', a)

print('\n=== Task #3 символы пунктуации ===')
# Уберите все символы пунктуации из предложения
sentence = """A, very  very; irregular_sentence"""
sentence_pattern = '\W\s+'
s = re.sub('\_', ' ', re.sub(sentence_pattern, ' ', sentence))  # Only that construction works properly
print('Before change: ', sentence, '\nAfter change:  ', s)

print('\n=== Task #4 ===')
# Очистите следующий твит, чтобы он содержал только одно сообщение пользователя.
# То есть, удалите все URL, хэштеги, упоминания, пунктуацию, RT и CC.
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today https://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
print(tweet)
tweet = re.sub('RT\s@\w+:\s','',tweet)      # remove RT info etc "RT @ThNextWeb "
print(tweet)
tweet = re.sub('cc:\s@\w+\s','',tweet)      # remove cc info etc "cc: @garybernhardt "
print(tweet)
tweet = re.sub('(#\w+\s*)*','',tweet)      # remove hashtag etc "#rstats"
print(tweet)
tweet = re.sub('#\w+\s*','',tweet)      # remove cc info etc "cc: @garybernhardt "
print(tweet)

