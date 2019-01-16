# DevOps Glossary

**Note:** We have seeded the tool list with glossaries composed from several sources; [click here](./links.txt) to see those sources. However, we have modified some descriptions, so please refer back to those sites for the originals.

If there is a term you don't see here, it may be in the [tools section](../tools/).

<!-- <ul class="glossary-sections"> -->
  {% comment %} {% assign index = site.data.glossary.index.letters | sort:'letter' %} {% endcomment %}
  {% for i in site.data.glossary.index.letters %}
<!--    <li class="glossary-letter"> {{ i.letter }} -->
---
## {{ i.letter }}

   <ul>
   {% comment %} {% assign terms = i.terms | sort:'term' %} {% endcomment %}
   {% for t in i.entries %}
   <li class="glossary-term h5" id="{{ t.term | slugify }}"> <strong>{{ t.term }}</strong> <br />
   {{ t.desc }}
   </li> <br />
   {% endfor %}
   </ul>
<!--    </li> -->

  {% endfor %}
<!--</ul> -->


[1]: https://en.wikipedia.org/wiki/DevOps_toolchain
