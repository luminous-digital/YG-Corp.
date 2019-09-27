<div class="l-inner">
    <div class="l-search-results js-search-list">
        <div class="l-search-results__heading">

            {% block results_heading %}
                {% import "../components/results-heading.tpl" as results_heading %}
                {{
                    results_heading.render(
                        searchQuery="query"
                    )
                }}
            {% endblock %}

        </div>
        <div class="l-search-results__list">

            {% block list %}
                {% import "../components/list.tpl" as list %}
                {{
                    list.render(
                        mapItems=[
                            {
                                url: '#',
                                section: 'Section 1',
                                page: 'Lorem ipsum 1'
                            },
                            {
                                url: '#',
                                section: 'Section 2',
                                page: 'Lorem ipsum 2'
                            },
                            {
                                url: '#',
                                section: 'Section 3',
                                page: 'Lorem ipsum 3'
                            },
                            {
                                url: '#',
                                section: 'Section 4',
                                page: 'Lorem ipsum 4'
                            },
                            {
                                url: '#',
                                section: 'Section 5',
                                page: 'Lorem ipsum 5'
                            },
                            {
                                url: '#',
                                section: 'Section 6',
                                page: 'Lorem ipsum 6'
                            },
                            {
                                url: '#',
                                section: 'Section 7',
                                page: 'Lorem ipsum 7'
                            },
                            {
                                url: '#',
                                section: 'Section 8',
                                page: 'Lorem ipsum 8'
                            },
                            {
                                url: '#',
                                section: 'Section 9',
                                page: 'Lorem ipsum 9'
                            },
                            {
                                url: '#',
                                section: 'Section 10',
                                page: 'Lorem ipsum 10'
                            },
                                                        {
                                url: '#',
                                section: 'Section 11',
                                page: 'Lorem ipsum 11'
                            },
                            {
                                url: '#',
                                section: 'Section 12',
                                page: 'Lorem ipsum 12'
                            },
                            {
                                url: '#',
                                section: 'Section 13',
                                page: 'Lorem ipsum 13'
                            },
                            {
                                url: '#',
                                section: 'Section 14',
                                page: 'Lorem ipsum 14'
                            },
                            {
                                url: '#',
                                section: 'Section 15',
                                page: 'Lorem ipsum 15'
                            },
                            {
                                url: '#',
                                section: 'Section 16',
                                page: 'Lorem ipsum 16'
                            },
                            {
                                url: '#',
                                section: 'Section 17',
                                page: 'Lorem ipsum 17'
                            },
                            {
                                url: '#',
                                section: 'Section 18',
                                page: 'Lorem ipsum 18'
                            },
                            {
                                url: '#',
                                section: 'Section 19',
                                page: 'Lorem ipsum 19'
                            },
                            {
                                url: '#',
                                section: 'Section 20',
                                page: 'Lorem ipsum 20'
                            },
                            {
                                url: '#',
                                section: 'Section 21',
                                page: 'Lorem ipsum 21'
                            },
                            {
                                url: '#',
                                section: 'Section 22',
                                page: 'Lorem ipsum 22'
                            }
                        ]
                    )
                }}
            {% endblock %}

        </div>
        <div class="l-search-results__cta">

            {% block load_more %}
                {% import "../components/load-more-btn.tpl" as load_more %}
                {{
                    load_more.render(
                        showLoadMore=true,
                        btnText='Load more'
                    )
                }}
            {% endblock %}

        </div>
    </div>
</div>
