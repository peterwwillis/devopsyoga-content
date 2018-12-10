#!/usr/bin/env python
from bs4 import BeautifulSoup

tool_chest_html = 'do-tool-chest.html'

class PageContent:
    def __init__(self):
        self.soup = None
        self.tool_list = None
        self.categories_list = None

    def body(self):
        if self.soup == None:
            with open(tool_chest_html) as f:
                self.soup = BeautifulSoup(f, 'html.parser', from_encoding="ascii")
        return self.soup.body

    def section(self, section_id):
        sections = self.body().find_all('section')
        for section in sections:
            if section.has_attr('id') and section_id in section.get('id'):
                return section

    def categories(self):
        if self.categories_list != None: return self.categories_list

        # The 'tool-chest' section of the HTML contains categories as well as
        # tool content
        section = self.section("tool-chest")

        # The 'dropdown-menu' ul class has the categories
        ul = section.find('ul', attrs={"class": "dropdown-menu"} )
        links = ul.find_all("a", attrs={"class": "filter"} )

        d = {}
        for link in links:
            # The 'data-filter' attribute in the HTML is the ID for the category
            text = link.get_text()
            # Strip leading '.' from category id
            f = link['data-filter']
            d[f.encode('ascii', 'ignore').strip('.')] = text.encode('ascii', 'ignore')

        self.categories_list = d
        return self.categories_list

    def tools(self):
        if self.tool_list != None: return self.tool_list

        section = self.section("tool-chest")
        div = section.find('div', attrs={"id": "mixitup", "class": "panel"} )
        tools = div.find_all('div')

        d = {}
        for tool in tools:
            # data-name is the tool title
            # data-id is the id of the tool
            # class contains the classes applying to this tool, including categories
            tool_name, tool_id = tool.get("data-name").encode('ascii','ignore'), tool.get("data-id").encode('ascii','ignore')
            tool_classes = [l.encode('ascii', 'ignore') for l in tool.get("class")]
            link, img = tool.a.get("href").encode('ascii','ignore'), tool.img.get("src").encode('ascii','ignore')
            text = tool.p.get_text().encode('ascii', 'ignore')
            #print "name %s id %s link %s img %s\nclass '%s'\ntext '%s'\n" % (tool_name, tool_id, link, img, tool_classes, text)
            d[tool_id] = {'name': tool_name, 'id': tool_id, 'class': tool_classes, 'link': link, 'img': img, 'text': text }

        self.tool_list = d
        return self.tool_list

    def category(self, name):
        cat_id = None
        for type_id, cat in self.categories().items():
            if name == cat:
                cat_id = type_id

        tool_list = []
        for tool_id, d in self.tools().items():
            if cat_id in d["class"]:
                print "tool %s" % d["name"]
                tool_list.append(d)

        return tool_list

def main():
    page = PageContent()
    #print page.categories()
    #print page.tools()
    print page.category("Testing")

if __name__ == "__main__":
    main()

