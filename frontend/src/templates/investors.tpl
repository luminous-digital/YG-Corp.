{% extends "base/base.tpl" %}
{% block title %}
Investors
{% endblock %}
{% set active_no = '1.2' %}
{% set active_subnav_no = '' %}
{% block content %}

{% import "components/quote.tpl" as c_quote %}
{% import "components/quick-links.tpl" as c_quick_links %}
{% include "components/rich-editor.tpl" %}
<div class="l-inner">
    <div class="l-decor-wrapper l-decor-wrapper--mobile-bottom">
        <div class="l-two-cols l-two-cols--grid">
            <div class="l-two-cols__box l-two-cols__box--socials">
                <ul class="c-social-media c-social-media--horizontal c-social-media--start">
                    <li class="c-social-media__list">
                        <a href="#" class="c-icon-with-decor c-icon-with-decor--light" target="_blank"
                            rel="noopener noreferrer">
                            <span class="o-icon-wrapper">
                                <svg class="o-icon o-icon--twitter">
                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-twitter"></use>
                                </svg>
                            </span>
                        </a>
                    </li>
                    <li class="c-social-media__list">
                        <a href="#" class="c-icon-with-decor c-icon-with-decor--light" target="_blank"
                            rel="noopener noreferrer">
                            <span class="o-icon-wrapper">
                                <svg class="o-icon o-icon--linkedin">
                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-linkedin"></use>
                                </svg>
                            </span>
                        </a>
                    </li>
                </ul>
            </div>
            <div class="l-two-cols__box l-two-cols__box--with-decor-left">
                <div class="c-widget">
                    <div class="c-widget__row">
                        <div class="c-widget__col">
                            <a href="#" class="c-widget-module" style="background-color: #241D36;">
                                <div class="c-widget-module__main">
                                    <h4 class="c-widget-module__title">
                                        Corporate responsibility
                                    </h4>
                                    <div class="c-widget-module__action">
                                        <span class="c-underline-link">
                                            Read more
                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                <svg class="o-icon o-icon--arrow-right">
                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                    </use>
                                                </svg>
                                            </span>
                                        </span>
                                    </div>
                                </div>
                            </a>
                        </div>
                        <div class="c-widget__col">
                            <a href="#" class="c-widget-module" style="background-color: #00B7B4;">
                                <div class="c-widget-module__main">
                                    <h4 class="c-widget-module__title">
                                        Gender pay gap
                                    </h4>
                                    <p class="c-widget-module__desc">
                                        Download our latest gender pay gap report
                                    </p>
                                    <div class="c-widget-module__action">
                                        <span class="c-underline-link">
                                            Downloads
                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                <svg class="o-icon o-icon--arrow-right">
                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                    </use>
                                                </svg>
                                            </span>
                                        </span>
                                    </div>
                                </div>
                            </a>
                        </div>
                    </div>
                    <div class="c-widget__row">
                        <a href="#" class="c-tile" style="background-image: url(./static/img/pic-widget-1.jpg);">
                            <div class="c-tile__content">
                                <h4 class="c-tile__title t-headline-4 t-bold">
                                    Board of Directors
                                </h4>
                                <div class="c-tile__action">
                                    <span class="c-underline-link">
                                        Read more
                                        <span class="c-underline-link__icon o-icon-wrapper">
                                            <svg class="o-icon o-icon--arrow-right">
                                                <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                    xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                </use>
                                            </svg>
                                        </span>
                                    </span>
                                </div>
                            </div>
                        </a>
                    </div>
                </div>
                <div class="l-quote">
                    {{ c_quote.render(
                        quote='Access to permissioned data is a key differentiator, allowing for faster responses and increased automation and efficiency.',
                        author='Name Surname',
                        position='Edison Investment Research',
                        url='#'
                        )
                    }}
                </div>
            </div>
            <div class="l-two-cols__box l-two-cols__box--simple-widget">
                <div class="c-widget">
                    <div class="c-widget__row" style="background-color: #241d36;">
                        <iframe class="c-iframe c-iframe--pad"
                            src="https://polaris.brighterir.com/public/yougov/tool_group/share_price_widget_and_chart"
                            frameborder="0" scrolling="no"></iframe>
                    </div>
                    <div class="c-widget__row">
                        <div class="c-widget__col">
                            <a href="#" class="c-widget-module" style="background-color: #9078D7;">
                                <div class="c-widget-module__main">
                                    <h4 class="c-widget-module__title">
                                        Why invest?
                                    </h4>
                                    <p class="c-widget-module__desc">
                                        Read our investment case
                                    </p>
                                    <div class="c-widget-module__action">
                                        <span class="c-underline-link">
                                            Read more
                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                <svg class="o-icon o-icon--arrow-right">
                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                    </use>
                                                </svg>
                                            </span>
                                        </span>
                                    </div>
                                </div>
                            </a>
                        </div>
                        <div class="c-widget__col">
                            <a href="#" class="c-widget-module" style="background-color: #605A70;">
                                <div class="c-widget-module__main">
                                    <h4 class="c-widget-module__title">
                                        Latest announcements
                                    </h4>
                                    <div class="c-widget-module__action">
                                        <span class="c-underline-link">
                                            See all announcements
                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                <svg class="o-icon o-icon--arrow-right">
                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                    </use>
                                                </svg>
                                            </span>
                                        </span>
                                    </div>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>
                <div class="l-callouts">
                    <div class="l-callouts__content">
                        <section class="l-heading">
                            <div class="c-heading c-heading--small">
                                <h2 class="c-heading__title t-headline-2 t-regular">
                                    Summary of financial results
                                </h2>
                            </div>
                        </section>
                        <ul class="c-list c-list--horizontal-wrap">
                            <li class="c-list__item">
                                <div class="c-callouts">
                                    <h4 class="c-callouts__heading">
                                        Turnover
                                    </h4>
                                    <h2 class="c-callouts__price">
                                        £116.6m
                                    </h2>
                                    <div class="c-callouts__info">
                                        <time datetime="2017" class="c-callouts__date">
                                            2017:
                                        </time>
                                        <span class="c-callouts__previous-price">
                                            £107.0m
                                        </span>
                                    </div>
                                </div>
                            </li>
                            <li class="c-list__item">
                                <div class="c-callouts">
                                    <h4 class="c-callouts__heading">
                                        Operating cash generation
                                    </h4>
                                    <h2 class="c-callouts__price">
                                        £23.6m
                                    </h2>
                                    <div class="c-callouts__info">
                                        <time datetime="2017" class="c-callouts__date">
                                            2017:
                                        </time>
                                        <span class="c-callouts__previous-price">
                                            £18.9m
                                        </span>
                                    </div>
                                </div>
                            </li>
                            <li class="c-list__item">
                                <div class="c-callouts">
                                    <h4 class="c-callouts__heading">
                                        Adjusted earnings per share
                                    </h4>
                                    <h2 class="c-callouts__price">
                                        £16.6p
                                    </h2>
                                    <div class="c-callouts__info">
                                        <time datetime="2017" class="c-callouts__date">
                                            2017:
                                        </time>
                                        <span class="c-callouts__previous-price">
                                            £10.9m
                                        </span>
                                    </div>
                                </div>
                            </li>
                            <li class="c-list__item">
                                <div class="c-callouts">
                                    <h4 class="c-callouts__heading">
                                        Adjusted operating profit
                                    </h4>
                                    <h2 class="c-callouts__price">
                                        £19.7m
                                    </h2>
                                    <div class="c-callouts__info">
                                        <time datetime="2017" class="c-callouts__date">
                                            2017:
                                        </time>
                                        <span class="c-callouts__previous-price">
                                            £14.5m
                                        </span>
                                    </div>
                                </div>
                            </li>
                            <li class="c-list__item">
                                <div class="c-callouts">
                                    <h4 class="c-callouts__heading">
                                        Adjusted operating profit
                                    </h4>
                                    <h2 class="c-callouts__price">
                                        £19.7m
                                    </h2>
                                    <div class="c-callouts__info">
                                        <time datetime="2017" class="c-callouts__date">
                                            2017:
                                        </time>
                                        <span class="c-callouts__previous-price">
                                            £14.5m
                                        </span>
                                    </div>
                                </div>
                            </li>
                            <li class="c-list__item">
                                <div class="c-callouts">
                                    <h4 class="c-callouts__heading">
                                        Adjusted operating profit
                                    </h4>
                                    <h2 class="c-callouts__price">
                                        £19.7m
                                    </h2>
                                    <div class="c-callouts__info">
                                        <time datetime="2017" class="c-callouts__date">
                                            2017:
                                        </time>
                                        <span class="c-callouts__previous-price">
                                            £14.5m
                                        </span>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% include "components/video-module.tpl" %}
<div class="l-inner">
    <div class="l-decor-wrapper l-decor-wrapper--top">
        <div class="l-two-cols l-two-cols--with-decor-top">
            <div class="l-two-cols__col">
                <div class="l-two-cols__row">
                    <div class="c-widget">
                        <div class="c-widget__row">
                            <div class="c-newsfeed" style="background: #AD97ED;">
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
                                                    YouGov continues to develop its data, platform and tools to address
                                                    significant opportunities to embed in clients’ workflows,
                                                    particularly within…
                                                </p>
                                                <div class="c-excerp__btn-wrapper">
                                                    <span class="c-underline-link" target="_blank">
                                                        Read more
                                                        <span class="c-underline-link__icon o-icon-wrapper">
                                                            <svg class="o-icon o-icon--arrow-right">
                                                                <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                    xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                </use>
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
                                                    As indicated at January’s trading update, YouGov had a strong H119.
                                                    18% revenue growth (10% underlying) blends +34% from Products &
                                                    Services…
                                                </p>
                                                <div class="c-excerp__btn-wrapper">
                                                    <span class="c-underline-link" target="_blank">
                                                        Read more
                                                        <span class="c-underline-link__icon o-icon-wrapper">
                                                            <svg class="o-icon o-icon--arrow-right">
                                                                <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                    xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                </use>
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
                                                <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                    xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                </use>
                                            </svg>
                                        </span>
                                    </a>
                                </div>
                            </div>
                        </div>
                        <div class="c-widget__row">
                            <a href="#" class="c-widget-module" style="background-color: #DC4C81;">
                                <div class="c-widget-module__media"
                                    style="background-image: url(./static/img/pic-widget-1.jpg);"></div>
                                <div class="c-widget-module__main">
                                    <h4 class="c-widget-module__title">
                                        Factsheet
                                    </h4>
                                    <p class="c-widget-module__desc">
                                        Add later
                                    </p>
                                    <div class="c-widget-module__action">
                                        <span class="c-underline-link">
                                            Downloads
                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                <svg class="o-icon o-icon--arrow-right">
                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                    </use>
                                                </svg>
                                            </span>
                                        </span>
                                    </div>
                                </div>

                            </a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="l-two-cols__col l-two-cols__col--center">
                <div class="l-two-cols__row">
                    {{ c_quick_links.render() }}
                </div>
            </div>
        </div>
    </div>
</div>

{% endblock %}
