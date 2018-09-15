
- [HTML parsing](#html-parsing)

### HTML parsing


```py
from bs4 import BeautifulSoup


class HtmlParser(object):

    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html5lib')

    @property
    def hrefs(self):
        # find all a tag which contains href attribute
        # for example:
        # yield mean
        a_tags = self.soup.find_all("a", {"href": True})
        for tag in a_tags:
            yield tag['href']

    @property
    def script_text(self):
        # find all script tag
        # return a list of text content in <script> tag.
        # for example: <script>text</script>
        # will return text
        scripts = self.soup.find_all('script')
        return [script.text for script in scripts]

```