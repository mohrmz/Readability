import requests
import lxml.html
import pprint

for version, url in [
     ('2.5', 'https://docs.python.org/2.5/lib/standard-encodings.html')
]:
    html = requests.get(url).text
    doc = lxml.html.fromstring(html)
    standard_encodings_table = doc.xpath(
        '//table[preceding::h2[.//text()[contains(., "Standard Encodings")]]][//th/text()="Codec"]'
    )[0]
    codecs = standard_encodings_table.xpath('.//td[1]/text()')
    print('<pre><code>' + pprint.pformat(codecs) + '</code></pre>')