"""
Materialbox
-----------

This plugin adds necessary attributes to img tags to work with
the materialboxed class from materialize css framework.
"""
from pelican import signals
from bs4 import BeautifulSoup

def materialbox(instance):
    if instance._content is not None:
        content = instance._content
        soup = BeautifulSoup(content, 'html.parser')
        for figure in soup.find_all("div", class_="figure"):
            caption = figure.find('p', class_="caption").string
            img = figure.find('img')
            img['data-caption'] = caption
            if 'class' not in img.attrs:
                img['class'] = "materialboxed responsive-img"
            else:
                img['class'].append("materialboxed")
        instance._content = soup.decode()

def register():
    signals.content_object_init.connect(materialbox)
