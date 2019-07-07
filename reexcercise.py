import re
patterns=["this","that"]
text='this message has that output'

for pattern in patterns:
    print("looking for pattern {} in message {}".format(pattern,text))
    obj=re.compile(pattern)
    if obj.search(text):
        print('match found')
    else:
        print('match not found')
    match = obj.search(text)
    s = match.start()
    e = match.end()
    print("found {} in {} from {} to {} {}".format(match.re.pattern,match.string,s,e,text[s:e]))
