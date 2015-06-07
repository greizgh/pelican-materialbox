#Materialbox

This [pelican](http://blog.getpelican.com/) plugin adds necessary tags to use _materialboxed_ images with [materialize](http://materializecss.com/) css framework.

See the demo from [materialize doc](http://materializecss.com/media.html#materialbox)

##Requirements

This plugin needs [beautifulsoup](http://www.crummy.com/software/BeautifulSoup/).
You can install it with pip:

    pip install beautifulsoup4

Of course, you need to use the materialize framework and make sure the materialboxed plugin is loaded:
```javascript
$(document).ready(function(){
  $('.materialboxed').materialbox();
});
```

##How to use

Simply add `materialbox` to your pelican plugins.

An image included like this:
```rst
.. figure:: https://127.0.0.1/my_awesome.gif
    :alt: cats

    This is image caption
```

Will result in this:
```html
<img alt="cats" class="materialboxed" data-caption="This is image caption" src="https://127.0.0.1/my_awesome.gif">
```
