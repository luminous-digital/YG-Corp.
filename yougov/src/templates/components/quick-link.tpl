{% macro render(title, desc, url) %}
<div class="c-quick-link">
    <h3 class="c-quick-link__title">
        {{ title }}
    </h3>
    <p class="c-quick-link__desc">
        {{ desc }}
    </p>
    <div class="c-quick-link__action">
        <a href="{{ url }}" class="c-underline-link">
            Read more
            <span class="c-underline-link__icon o-icon-wrapper">
                <svg class="o-icon o-icon--arrow-right">
                    <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right"></use>
                </svg>
            </span>
        </a>
    </div>
</div>
{% endmacro %}
