{% macro render() %}

{% import "components/quick-link.tpl" as c_quick_link %}
{% set quickLinks = [
    { title: 'Modern slavery act', desc: 'Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat vel illum dolore eu feugiat nulla. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie.', url: '#'},
    { title: 'Gender pay report', desc: 'Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat vel illum dolore eu feugiat nulla. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie.', url: '#'},
    { title: 'YouGov Cube', desc: 'Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat vel illum dolore eu feugiat nulla. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie.', url: '#'}
] %}

<div class="l-quick-links">
    <div class="l-quick-links__heading">
        <h2 class="t-headline-2 t-regular">
            Quick links
        </h2>
    </div>
    <div class="l-quick-links__content">
        <ul class="c-list c-list--big-spacing" style="color: #00B7B4;">
            {% for item in quickLinks %}
            <li class="c-list__item">
                {{
                    c_quick_link.render(
                        title=item.title,
                        desc=item.desc,
                        url=item.url
                    )
                }}
            </li>
        {%- endfor %}
        </ul>
    </div>
</div>
{% endmacro %}
