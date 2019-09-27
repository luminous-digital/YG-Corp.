{% macro render(_active_no) %}
<nav class="c-nav">
    <ul class="c-nav__list">
        <li class="c-nav__item{% if _active_no == '1.1' %} is-active{% endif %}">
            <a href="#about-sub-nav" class="c-nav__link js-sub-nav-open-trigger">
                <span class="c-nav__name">
                    About
                </span>
                <span class="c-nav__icon o-icon-wrapper">
                    <svg class="o-icon o-icon--arrow-down">
                        <use xmlns:xlink="http://www.w3.org/1999/xlink"
                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-down"></use>
                    </svg>
                </span>
            </a>
        </li>
        <li class="c-nav__item{% if _active_no == '1.2' %} is-active{% endif %}">
            <a href="#investors-sub-nav" class="c-nav__link js-sub-nav-open-trigger">
                <span class="c-nav__name">
                    Investors
                </span>
                <span class="c-nav__icon o-icon-wrapper">
                    <svg class="o-icon o-icon--arrow-down">
                        <use xmlns:xlink="http://www.w3.org/1999/xlink"
                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-down"></use>
                    </svg>
                </span>
            </a>
        </li>
        <li class="c-nav__item{% if _active_no == '1.3' %} is-active{% endif %}">
            <a href="#governance-sub-nav" class="c-nav__link js-sub-nav-open-trigger">
                <span class="c-nav__name">
                    Governance
                </span>
                <span class="c-nav__icon o-icon-wrapper">
                    <svg class="o-icon o-icon--arrow-down">
                        <use xmlns:xlink="http://www.w3.org/1999/xlink"
                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-down"></use>
                    </svg>
                </span>
            </a>
        </li>
        <li class="c-nav__item{% if _active_no == '1.4' %} is-active{% endif %}">
            <a href="#compliance-sub-nav" class="c-nav__link js-sub-nav-open-trigger">
                <span class="c-nav__name">
                    Compliance
                </span>
                <span class="c-nav__icon o-icon-wrapper">
                    <svg class="o-icon o-icon--arrow-down">
                        <use xmlns:xlink="http://www.w3.org/1999/xlink"
                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-down"></use>
                    </svg>
                </span>
            </a>
        </li>
        <li class="c-nav__item{% if _active_no == '1.5' %} is-active{% endif %}">
            <a href="#press-sub-nav" class="c-nav__link js-sub-nav-open-trigger">
                <span class="c-nav__name">
                    Press
                </span>
                <span class="c-nav__icon o-icon-wrapper">
                    <svg class="o-icon o-icon--arrow-down">
                        <use xmlns:xlink="http://www.w3.org/1999/xlink"
                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-down"></use>
                    </svg>
                </span>
            </a>
        </li>
        <li class="c-nav__item{% if _active_no == '1.6' %} is-active{% endif %}">
            <a href="#contact-sub-nav" class="c-nav__link js-sub-nav-open-trigger">
                <span class="c-nav__name">
                    Contact
                </span>
                <span class="c-nav__icon o-icon-wrapper">
                    <svg class="o-icon o-icon--arrow-down">
                        <use xmlns:xlink="http://www.w3.org/1999/xlink"
                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-down"></use>
                    </svg>
                </span>
            </a>
        </li>
    </ul>
</nav>
{% endmacro %}
