# DevOps Glossary

**Note:** We have seeded the tool list with glossaries composed from several sources; [click here](./links.txt) to see those sources.

<!-- <ul class="glossary-sections"> -->
  {% comment %} {% assign index = site.data.glossary.index.letters | sort:'letter' %} {% endcomment %}
  {% for i in site.data.glossary.index.letters %}
<!--    <li class="glossary-letter"> {{ i.letter }} -->
---
## {{ i.letter }}

   <ul>
   {% comment %} {% assign terms = i.terms | sort:'term' %} {% endcomment %}
   {% for t in i.entries %}
   <li class="glossary-term h5"> <strong>{{ t.term }}</strong> <br />
   {{ t.desc }}
   </li> <br />
   {% endfor %}
   </ul>
<!--    </li> -->

  {% endfor %}
<!--</ul> -->


## Notes

[XebiaLabs' Periodic Table of DevOps Tools]: https://xebialabs.com/periodic-table-of-devops-tools/
[1]: https://en.wikipedia.org/wiki/DevOps_toolchain
