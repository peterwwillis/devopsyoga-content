# Tools

DevOps tools are software that can be used to implement DevOps requirements. A great number of tools have been created since the mid-2000's for the purpose of managing infrastructure, as well as facilitating software development and testing. However, older Unix tools are still widely in use.

<ul class="job-listing">
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

Notes
 - Some of the tool list derived from https://xebialabs.com/periodic-table-of-devops-tools/

