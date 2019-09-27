{% extends "base/base.tpl" %}
{% block title %}
    Widget
{% endblock %}
{% set active_no = '' %}
{% set active_subnav_no = '' %}
{% block content %}

<div class="l-inner">
    <div class="c-widget">
        <div class="c-widget__row">
            <a href="#" class="c-widget-module" style="background-color: #00B7B4;">
                <div class="c-widget-module__main">
                    <h4 class="c-widget-module__title">
                        Latest report
                    </h4>
                    <p class="c-widget-module__desc">
                        Download our latest Annual Report & Accounts 2018
                    </p>
                    <div class="c-widget-module__action">
                        <span class="c-underline-link">
                            Downloads
                            <span class="c-underline-link__icon o-icon-wrapper">
                                <svg class="o-icon o-icon--arrow-right">
                                    <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right"></use>
                                </svg>
                            </span>
                        </span>
                    </div>
                </div>
                <div class="c-widget-module__media" style="background-image: url(./static/img/pic-widget-1.jpg);"></div>
            </a>
        </div>
    </div>
    <div class="c-widget c-widget--align-right">
        <div class="c-widget__row">
            <a href="#" class="c-widget-module" style="background-color: #00B7B4;">
                <div class="c-widget-module__main">
                    <h4 class="c-widget-module__title">
                        Latest report
                    </h4>
                    <p class="c-widget-module__desc">
                        Download our latest Annual Report & Accounts 2018
                    </p>
                    <div class="c-widget-module__action">
                        <span class="c-underline-link">
                            Downloads
                            <span class="c-underline-link__icon o-icon-wrapper">
                                <svg class="o-icon o-icon--arrow-right">
                                    <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right"></use>
                                </svg>
                            </span>
                        </span>
                    </div>
                </div>
                <div class="c-widget-module__media" style="background-image: url(./static/img/pic-widget-1.jpg);"></div>
            </a>
        </div>
    </div>
</div>

{% endblock %}
