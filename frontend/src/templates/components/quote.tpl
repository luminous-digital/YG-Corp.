{% macro render(quote, author, position, url) %}
<div class="c-quote" style="color: #00B7B4;">
  <h4 class="c-quote__author t-headline-4 t-bold">
    {{ author }}
  </h4>
  <h5 class="c-quote__position t-headline-5">
    {{ position }}
  </h5>
  <h2 class="c-quote__quotation t-headline-2">
    {{ quote }}
  </h2>
  <div class="c-quote__action">
    <a href="{{ url }}" class="c-underline-link">
        Find out more
        <span class="c-underline-link__icon o-icon-wrapper">
            <svg class="o-icon o-icon--arrow-right">
                <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right"></use>
            </svg>
        </span>
    </a>
  </div>
</div>
{% endmacro %}
