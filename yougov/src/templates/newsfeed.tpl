{% extends "base/base.tpl" %}
{% block title %}
    Newsfeed
{% endblock %}
{% block bodyClass %}has-subnav{% endblock %}
{% set active_no = '' %}
{% set active_subnav_no = '' %}
{% block content %}

<div class="l-inner">
    <div class="c-newsfeed">
        <h4 class="c-newsfeed__heading">
            Company Research
        </h4>
        <div class="c-newsfeed__content">
            <ul class="c-list">
                <li class="c-list__item">
                    <a href="#" class="c-excerpt">
                        <p class="c-excerp__subtitle">
                            Data: the connecting currency
                        </p>
                        <p class="c-excerp__text">
                            YouGov continues to develop its data, platform and tools to address significant opportunities to embed in clients’ workflows, particularly within…
                        </p>
                        <div class="c-excerp__btn-wrapper">
                            <span class="c-underline-link" target="_blank">
                                Read more
                                <span class="c-underline-link__icon o-icon-wrapper">
                                    <svg class="o-icon o-icon--arrow-right">
                                        <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right"></use>
                                    </svg>
                                </span>
                            </span>
                        </div>
                    </a>
                </li>
                <li class="c-list__item">
                    <a href="#" class="c-excerpt">
                        <p class="c-excerp__subtitle">
                            Activated data
                        </p>
                        <p class="c-excerp__text">
                            As indicated at January’s trading update, YouGov had a strong H119. 18% revenue growth (10% underlying) blends +34% from Products & Services…
                        </p>
                        <div class="c-excerp__btn-wrapper">
                            <span class="c-underline-link" target="_blank">
                                Read more
                                <span class="c-underline-link__icon o-icon-wrapper">
                                    <svg class="o-icon o-icon--arrow-right">
                                        <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right"></use>
                                    </svg>
                                </span>
                            </span>
                        </div>
                    </a>
                </li>
            </ul>
        </div>
        <div class="c-newsfeed__btn-wrapper">
            <a href="#" class="c-underline-link" target="_blank">
                See more company research
                <span class="c-underline-link__icon o-icon-wrapper">
                    <svg class="o-icon o-icon--arrow-right">
                        <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right"></use>
                    </svg>
                </span>
            </a>
        </div>
    </div>
</div>

{% endblock %}
