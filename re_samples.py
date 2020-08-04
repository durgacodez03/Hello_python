from collections import Counter
import re

paragraph = "I love teaching. If you do not love teaching what else can you love.I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love"


items = re.findall("\w+",paragraph)

sorted_items = (Counter(items))

print(sorted_items.keys())
print(sorted_items)


