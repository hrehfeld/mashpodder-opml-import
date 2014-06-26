import opml

import re
import sys

regex = re.compile(r'[^A-Za-z0-9_]+')

outline = opml.parse('podcasts.opml')

i = 0
with open('mp.conf', 'w', encoding='utf-8') as out:
    for feed in outline:
        url = str(feed.xmlUrl)
        name = regex.sub('-', str(feed.title), 0)
        # name = name.decode(sys.stdout.encoding)
        # url = url.encode('utf-8')
        #name = name.encode('utf-8')
        out.write(url)
        out.write(' ')
#        out.write(' feed_' + str(i) + '_')
        out.write(name)
        out.write(' all')
        out.write('\n')
        i += 1
