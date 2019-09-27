{% macro render(searchQuery) %}

    <h2 class="c-results-heading">
        Search results for:
        {% if searchQuery %}
            <span class="c-results-heading__accent">{{ searchQuery }}</span>
        {% endif %}
    </h2>

{% endmacro %}
