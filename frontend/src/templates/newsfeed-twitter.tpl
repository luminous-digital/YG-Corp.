{% extends "base/base.tpl" %}
{% block title %}
Newsfeed-twitter
{% endblock %}
{% block bodyClass %}has-subnav{% endblock %}
{% set active_no = '' %}
{% set active_subnav_no = '' %}
{% block content %}

<div class="l-inner">
    <div class="l-decor-wrapper l-decor-wrapper--top">
        <div class="l-two-cols l-two-cols--with-decor-top">
            <div class="l-two-cols__col">
                <div class="l-two-cols__row">
                    <div class="c-widget">
                        <div class="c-widget__row">
                            <div class="c-newsfeed">
                                <h4 class="c-newsfeed__heading">
                                    Latest from Twitter
                                </h4>
                                <div class="c-newsfeed__content">
                                    <ul class="c-list">
                                        <li class="c-list__item">
                                            <a href="#" class="c-excerpt c-excerpt--twitter">
                                                <p class="c-excerpt__text">
                                                    <span class="c-excerpt__name">@Name</span>
                                                    Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio.
                                                </p>
                                                <div class="c-excerpt__signature">
                                                    <time class="c-excerpt__time" datetime="25-06-2019 16:32">25 Jun 16:32</time>
                                                    <p class="c-excerpt__name">@YouGov</p>
                                                </div>
                                            </a>
                                        </li>
                                        <li class="c-list__item">
                                            <a href="#" class="c-excerpt c-excerpt--twitter">
                                                <p class="c-excerpt__text">
                                                    <span class="c-excerpt__name">@Name</span>
                                                    Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio.
                                                </p>
                                                <div class="c-excerpt__signature">
                                                    <time class="c-excerpt__time" datetime="25-06-2019 16:32">25 Jun 16:32</time>
                                                    <p class="c-excerpt__name">@YouGov</p>
                                                </div>
                                            </a>
                                        </li>
                                        <li class="c-list__item">
                                            <a href="#" class="c-excerpt c-excerpt--twitter">
                                                <p class="c-excerpt__text">
                                                    <span class="c-excerpt__name">@Name</span>
                                                    Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio.
                                                </p>
                                                <div class="c-excerpt__signature">
                                                    <time class="c-excerpt__time" datetime="25-06-2019 16:32">25 Jun 16:32</time>
                                                    <p class="c-excerpt__name">@YouGov</p>
                                                </div>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                                <div class="c-newsfeed__btn-wrapper">
                                    <a href="#" class="c-underline-link" target="_blank">
                                        Read more
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
                                <a href="#" class="c-widget-module" style="background-color: #9078D7;">
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
            </div>
            <div class="l-two-cols__col l-two-cols__col--center">
                <div class="l-two-cols__row">
                    {% include "components/quick-links.tpl" %}
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
