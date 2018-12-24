# DevOps Tools

DevOps tools are software that can be used to implement DevOps requirements. A great number of tools have been created since the mid-2000's for the purpose of managing infrastructure, as well as facilitating software development and testing. However, older Unix tools are still widely in use.

Typical use of DevOps tools in a [DevOps Toolchain][1] follow a few general stages of work:
 - Planning
 - Creating
 - Verifying
 - Packaging
 - Releasing
 - Configuring
 - Monitoring

**Note:** We have seeded the tool list here with [XebiaLabs' Periodic Table of DevOps Tools]. However, our own content may supersede or conflict with theirs, so please see their website if you would like to compare.

<ul class="tool-categories">
  {% for block in site.data.tools.categories %}
    <a href="{{ block.type | prepend: site.baseurl }}">
      <li>
        <div class="category-name">
          {{ block.category }}
        </div>
      </li>
    </a>
  {% endfor %}
</ul>

### Notes

[XebiaLabs' Periodic Table of DevOps Tools]: https://xebialabs.com/periodic-table-of-devops-tools/
[1]: https://en.wikipedia.org/wiki/DevOps_toolchain
