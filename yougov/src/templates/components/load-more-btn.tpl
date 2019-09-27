{% macro render(showLoadMore, btnText) %}
    {% if showLoadMore %}
        <button class="c-read-more-btn c-underline-link js-list-load-more">
            <span class="c-read-more-btn__span">
                {{ btnText }}
            </span>
            <span class="c-underline-link__icon o-icon-wrapper">
                <svg class="o-icon o-icon--cross">
                    <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-cross"></use>
                </svg>
            </span>
        </button>
    {% endif %}
{% endmacro %}
