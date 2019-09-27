{% extends "base/base.tpl" %} {% block title %} Example page {% endblock %} {% block bodyClass %}has-subnav{% endblock %} {% set active_no = '1.1' %} {% set active_subnav_no = '1.1' %} {% block content %} {% import
"components/quick-links.tpl" as c_quick_links %}

{# <div class="l-inner">
    <div class="l-two-cols l-two-cols--grid l-two-cols--grid-alt">
        <div class="l-two-cols__box l-two-cols__box--simple-widget">
            <div class="c-widget">
                <div class="c-widget__row">
                    <div class="c-newsfeed" style="background-color:#DC4C81">
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
                <div class="c-widget__row">
                    <div class="c-widget__col">
                        <a href="#" class="c-widget-module" style="background-color: #241D36;">
                            <div class="c-widget-module__main">
                                <h4 class="c-widget-module__title">
                                    Our data
                                </h4>
                                <p class="c-widget-module__desc">
                                    Link to solutions site
                                </p>
                                <div class="c-widget-module__action">
                                    <span class="c-underline-link">
                                        Read more
                                        <span class="c-underline-link__icon o-icon-wrapper">
                                            <svg class="o-icon o-icon--arrow-right">
                                                <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right"></use>
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
                                    Have a question?
                                </h4>
                                <p class="c-widget-module__desc">
                                    Visit our press office page to find out more
                                </p>
                                <div class="c-widget-module__action">
                                    <span class="c-underline-link">
                                        Read more
                                        <span class="c-underline-link__icon o-icon-wrapper">
                                            <svg class="o-icon o-icon--arrow-right">
                                                <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right"></use>
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
        <div class="l-two-cols__box l-two-cols__box--simple-widget-alt">
            {{ c_quick_links.render() }}
        </div>
    </div>
</div> #}
{# <div class="l-inner l-inner--small">
    <div class="c-newsfeed c-newsfeed--invert-colors-alt c-newsfeed--no-padding">
        <div class="c-newsfeed__content">
            <ul class="c-list c-list--odd">
                <li class="c-list__item">
                    <a href="#" class="c-excerpt c-excerpt--with-border">
                        <p class="c-excerp__subtitle">
                            Voting Intention: Con 35%, Lab 25%, Lib Dem 16%, Brex 11% (2-3 Sep)
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
                    <a href="#" class="c-excerpt c-excerpt--with-border">
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
                    <a href="#" class="c-excerpt c-excerpt--with-border">
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
            </ul>
        </div>
        <div class="c-newsfeed__btn-wrapper">
            <a href="https://www.edisoninvestmentresearch.com/widgets/901/50" class="c-underline-link" target="_blank">
                See more company research
                <span class="c-underline-link__icon o-icon-wrapper">
                    <svg class="o-icon o-icon--more">
                        <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="/static/svg/symbol/svg/sprite.symbol.svg#icon-more"></use>
                    </svg>
                </span>
            </a>
        </div>
    </div>
</div> #}
{# <div class="l-inner">
    <div class="l-callouts">
        <div class="l-callouts__content l-callouts__content--full-width">
            <ul class="c-list c-list--horizontal-wrap c-list--three-columns">
                <li class="c-list__item">
                    <div class="c-callouts">
                        <h4 class="c-callouts__heading">
                            Turnover
                        </h4>
                        <h2 class="c-callouts__price">
                            £116.6m
                        </h2>

                    </div>
                </li>
                <li class="c-list__item">
                    <div class="c-callouts">
                        <h4 class="c-callouts__heading">
                            Adjusted Operating Profit
                        </h4>
                        <h2 class="c-callouts__price">
                            £19.7m
                        </h2>

                    </div>
                </li>
                <li class="c-list__item">
                    <div class="c-callouts">
                        <h4 class="c-callouts__heading">
                            Headcount
                        </h4>
                        <h2 class="c-callouts__price">
                            816
                        </h2>
                    </div>
                </li>
                <li class="c-list__item">
                    <div class="c-callouts">
                        <h4 class="c-callouts__heading">
                            Revenue per head
                        </h4>
                        <h2 class="c-callouts__price">
                            £143,000
                        </h2>
                    </div>
                </li>
                <li class="c-list__item">
                    <div class="c-callouts">
                        <h4 class="c-callouts__heading">
                            Adjusted Earnings per Share
                        </h4>
                        <h2 class="c-callouts__price">
                            16.6p
                        </h2>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</div>
<div class="c-video-module js-video">
    <div class="c-video-module__media">
        <div class="c-video" style="background-image: url(./static/img/img-video-bg.jpg)">
        </div>
    </div>
    <div class="c-video-module__content-wrapper">
        <div class="l-inner">
            <div class="c-video-module__content">
                <div class="c-video-teaser">
                    <h4 class="c-video-teaser__heading t-headline-4 t-bold" style="color:#FFFFFF;">
                        Data privacy
                    </h4>
                    <h2 class="c-video-teaser__text t-headline-2" style="color:#FFFFFF;">
                        You trust us with your data. It’s our responsibility to be transparent about the data that we collect
                    </h2>
                </div>
                <a class="c-play c-underline-link" href="/compliance/privacy-security/" target="_self">
                    <div class="c-play__text t-button c-underline-link__icon o-icon-wrapper" style="color:#FFFFFF;">
                        <p>Read more
                            <svg class="o-icon o-icon--arrow-right">
                                <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="/static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right"></use>
                            </svg>
                        </p>
                    </div>
                </a>
            </div>
        </div>
    </div>
</div>
<div class="l-inner">
<div class="l-decor-wrapper l-decor-wrapper--top l-decor-wrapper--alt">
</div> #}
<div class="l-inner">
    <div class="c-widget">
        <div class="c-widget__col">
            <div class="c-widget-module" style="background-color: #00B7B5;">
                <div class="c-widget-module__main">
                    <h4 class="c-widget-module__title">
                        Company Factsheet
                    </h4>
                    <p class="c-widget-module__desc">
                        Coming soon
                    </p>
                    <div class="c-widget-module__action">
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
