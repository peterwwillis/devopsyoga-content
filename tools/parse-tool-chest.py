#!/usr/bin/env python
from bs4 import BeautifulSoup

tool_chest_html = 'do-tool-chest.html'

class PageContent:
    soup = None

    def body(self):
        if self.soup == None:
            with open(tool_chest_html) as f:
                self.soup = BeautifulSoup(f, 'html.parser')
        return self.soup.body

    def section(self, section_id):
        sections = self.body().find_all('section')
        for section in sections:
            if section.has_attr('id') and section_id in section.get('id'):
                return section

    def categories(self):
        # The 'tool-chest' section of the HTML contains categories as well as
        # tool content
        section = self.section("tool-chest")

        # The 'dropdown-menu' ul class has the categories
        ul = section.find('ul', attrs={"class": "dropdown-menu"} )
        links = ul.find_all("a", attrs={"class": "filter"} )

        d = {}
        for link in links:
            # The 'data-filter' attribute in the HTML is the ID for the category
            f = link['data-filter']
            text = link.get_text()
            d[f.encode('ascii', 'ignore')] = text.encode('ascii', 'ignore')
        return d


def main():
    page = PageContent()
    print page.categories()

if __name__ == "__main__":
    main()

