#!/usr/bin/env python
from bs4 import BeautifulSoup
import sys
import json
import argparse

tool_chest_html = 'do-tool-chest.html'

class ToolChest:
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
            #d[f.encode('ascii', 'ignore').strip('.')] = text.encode('ascii', 'ignore')
            print("type f %s" % type(f))
            print("f %s" % f)
            d[f.strip('.')] = text.encode('ascii', 'ignore')

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
            categories = []
            for c_id, c_n in self.categories().items():
                if c_id in tool_classes: categories.append(c_n)
            #categories = [x for x, y in zip(self.categories().keys(), tool_classes) if y == x]
            #print("name %s id %s link %s img %s\nclass '%s'\ntext '%s'\n" % (tool_name, tool_id, link, img, tool_classes, text))
            d[tool_id] = {'name': tool_name, 'id': tool_id, 'class': tool_classes, 'link': link, 'img': img, 'text': text, 'category': categories }

        self.tool_list = d
        return self.tool_list

    def category(self, name):
        cat_list = [name]
        if type(name) == type([]):
            cat_list = name

        cat_id_list = []
        for type_id, c in self.categories().items():
            for name in cat_list:
                if name == c:
                    cat_id_list.append(type_id)

        tool_list = []
        for tool_id, d in self.tools().items():
            for cat_id in cat_id_list:
                if cat_id in d["class"]:
                    #print("tool %s" % d["name"])
                    tool_list.append(d)

        return tool_list

def main():
    page = ToolChest()

    parser = options()
    o = parser.parse_args()
    if o.categories == None and o.tools == None:
        parser.print_help()
        exit(1)

    if o.categories != None:
        if len(o.categories) > 0:
            print(json.dumps( page.category(o.categories) ))
        else:
            print(json.dumps(page.categories()))

    if o.tools != None:
        print("tools: %s" % page.tools() )
        print( json.dumps( page.tools() ) )

    return(0)

def options():
    parser = argparse.ArgumentParser(description='Decode the XebiaLabs DevOps tools page')
    parser.add_argument('--categories', nargs='*', help='List all categories of tools, or all tools in a category')
    parser.add_argument('--tools', nargs='*', help='List all the tools')
    return parser

if __name__ == "__main__":
    main()

