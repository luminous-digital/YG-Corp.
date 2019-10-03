{% macro render() %}
<div class="l-cookies js-cookie">
    <div class="l-inner">
        <div class="c-cookies">
            <p class="c-cookies__text">YouGov uses cookies to give you the best experience on our site. By continuing to browse, you are agreeing to our use of cookies.</p>
            <div class="c-cookies__actions">
                <a href="#" class="c-underline-link js-cookie-accept">
                    Accept cookies
                    <span class="c-underline-link__icon o-icon-wrapper">
                        <svg class="o-icon o-icon--arrow-right">
                            <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right"></use>
                        </svg>
                    </span>
                </a>
                <a href="#" class="c-underline-link js-cookie-decline">
                    Reject
                    <span class="c-underline-link__icon o-icon-wrapper">
                        <svg class="o-icon o-icon--arrow-right">
                            <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right"></use>
                        </svg>
                    </span>
                </a>
            </div>
        </div>
    </div>
</div>
{% endmacro %}
