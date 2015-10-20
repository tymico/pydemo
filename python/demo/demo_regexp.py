# Filename: using_regexp.py

#   ^ 匹配字符串开始位置。
#   $ 匹配字符串结束位置。
#   \b 匹配一个单词边界。
#   \d 匹配一个数字。
#   \D 匹配一个任意的非数字字符。
#   x? 匹配可选的x字符。换句话说，就是0个或者1个x字符。
#   x* 匹配0个或更多的x。
#   x+ 匹配1个或者更多x。
#   x{n,m} 匹配n到m个x，至少n个，不能超过m个。
#   (a|b|c) 匹配单独的任意一个a或者b或者c。
#   (x) 这是一个组，它会记忆它匹配到的字符串。你可以用re.search返回的匹配对象的groups()函数来获取到匹配的值。

import re

phonexp = r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$'
phonePattern = re.compile(phonexp)

print(phonePattern.search('800-555-1212').groups())
print(phonePattern.search('work 1-(800) 555.1212 #1234').groups())
