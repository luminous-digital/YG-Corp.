{% extends "base/base.tpl" %}
{% block title %}
Homepage
{% endblock %}
{% set active_no = '1.6' %}
{% set active_subnav_no = '6.2' %}
{% block content %}

<div class="l-inner js-map-container" data-json="/src/js/modules/offices-map/locations.json">
    <section class="l-heading">
        <div class="c-heading">
            <h1 class="c-heading__title t-headline-2">
                Global offices
            </h1>
        </div>
    </section>
    <section class="l-filters">
        <form class="f-form f-form--filters">
            <div class="f-form__col">
                <h5 class="f-form__title t-headline-5">
                    Filter by:
                </h5>
            </div>
            <div class="f-form__col f-form__col--big">
                <div class="f-field f-field--select">
                    <select class="f-field__control js-select" name="country" data-placeholder="All" required=''>
                        <option value="All">All</option>
                    </select>
                    <span class="o-icon-wrapper">
                        <svg class="o-icon o-icon--arrow-simple">
                            <use xmlns:xlink="http://www.w3.org/1999/xlink"
                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right-bold">
                            </use>
                        </svg>
                    </span>
                </div>
            </div>
            <div class="f-form__col">
                <button type="button" class="c-clear-btn t-caption js-clear-filters">
                    Clear filters
                    <span class="c-clear-btn__icon o-icon-wrapper">
                        <svg class="o-icon o-icon--cross">
                            <use xmlns:xlink="http:www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-cross"></use>
                        </svg>
                    </span>
                </button>
            </div>
        </form>
    </section>
    <section class="l-locations">
        <div class="l-locations__row l-locations__row--no-padding">
            <div class="c-map">
                <div class="c-map__popup js-map-popup-container">
                    <button class="c-map__popup__close js-map-popup-close">
                        <span class="o-icon-wrapper">
                            <svg class="o-icon o-icon--cross">
                                <use xmlns:xlink="http:www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-cross"></use>
                            </svg>
                        </span>
                    </button>
                    <div class="c-map__popup__content"></div>
                </div>
                <div class="c-map__main js-map" aria-label="google map" data-zoom="2.4" data-lat="0" data-lng="0">
                    Offices map
                </div>
                <div class="c-map__legend">
                    <ul class="c-list c-list--horizontal">
                        <li class="c-list__item">
                            <div class="c-marker-box">
                                <span class="c-marker-box__icon o-icon-wrapper">
                                    <svg class="o-icon o-icon--map-pin">
                                        <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-map-pin">
                                        </use>
                                    </svg>
                                </span>
                                Corporate Headquarters
                            </div>
                        </li>
                        <li class="c-list__item">
                            <div class="c-marker-box">
                                <span class="c-marker-box__icon">
                                    <span class="c-marker-box__small-marker"></span>
                                </span>
                                Office location
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="js-locations-container"></div>
    </section>
</div>

{% endblock %}
