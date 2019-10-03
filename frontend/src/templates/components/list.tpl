{% macro render(mapItems) %}

    <ul class="c-list c-list--load-more">
        {% for mapItem in mapItems %}

            <li class="c-list__item">
                <div class="c-list__decor">
                    <a href="{{ mapItem.url }}" class="c-redirect-cta" target="_blank">
                        <h5 class="c-redirect-cta__section t-headline-5">
                            {{ mapItem.section }}
                        </h5>
                        <h5 class="c-redirect-cta__title t-headline-5">
                            {{ mapItem.page }}
                        </h5>
                        <div class="c-redirect-cta__icon" target="_blank">
                            <span class="o-icon-wrapper">
                                <svg class="o-icon o-icon--arrow-right-bold">
                                    <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right-bold"></use>
                                </svg>
                            </span>
                        </div>
                    </a>
                </div>
            </li>

        {% endfor %}
    </ul>

{% endmacro %}
