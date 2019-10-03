{% extends "base/base.tpl" %}
{% block title %}
Homepage
{% endblock %}
{% set active_no = '' %}
{% set active_subnav_no = '' %}
{% block content %}

{% import "components/quote.tpl" as c_quote %}
{% import "components/quick-links.tpl" as c_quick_links %}
{% include "components/rich-editor.tpl" %}
<div class="l-inner">
    <div class="l-decor-wrapper l-decor-wrapper--mobile-bottom">
        <div class="l-two-cols l-two-cols--grid l-two-cols--flex">
            <div class="l-two-cols__box l-two-cols__box--socials">
                <ul class="c-social-media c-social-media--horizontal c-social-media--start">
                    <li class="c-social-media__list">
                        <a href="#" class="c-icon-with-decor c-icon-with-decor--light" target="_blank" rel="noopener noreferrer">
                            <span class="o-icon-wrapper">
                                <svg class="o-icon o-icon--twitter">
                                    <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-twitter"></use>
                                </svg>
                            </span>
                        </a>
                    </li>
                    <li class="c-social-media__list">
                        <a href="#" class="c-icon-with-decor c-icon-with-decor--light" target="_blank" rel="noopener noreferrer">
                            <span class="o-icon-wrapper">
                                <svg class="o-icon o-icon--linkedin">
                                    <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-linkedin"></use>
                                </svg>
                            </span>
                        </a>
                    </li>
                </ul>
            </div>
            <div class="l-two-cols__box l-two-cols__box--with-decor-left">
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
            <div class="l-two-cols__box l-two-cols__box--simple-widget">
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
                    <div class="c-widget__row">
                        <div class="c-widget__iframe">
                            <iframe src="http://www.bbc.co.uk/news/uk-politics-38265064/embed" class="c-iframe" frameborder="0" scrolling="no"></iframe>
                        </div>
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
                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right"></use>
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
</div>
{# <div class="l-inner">
    <div class="l-quote">
        {{ c_quote.render(
            quote='Access to permissioned data is a key differentiator, allowing for faster responses and increased automation and efficiency.',
            author='Name Surname',
            position='Edison Investment Research',
            url='#'
            )
        }}
    </div>
</div> #}
<div class="l-spacing l-spacing--m">
</div>
{% include "components/video-module.tpl" %}
<div class="l-inner">
    <div class="l-decor-wrapper l-decor-wrapper--top">
        <div class="l-two-cols l-two-cols--with-decor-top">
            <div class="l-two-cols__col">
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
            <div class="l-two-cols__col l-two-cols__col--center">
                <div class="c-widget">
                    <div class="c-widget__row">
                        {{ c_quick_links.render() }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<ul class="c-cards-list">
        <li class="c-cards-list__item">
            <div class="c-person-card js-accordion">
                <figure class="c-person-card__media">
                    <img src="/static/img/pic_person_1.jpg" alt="Office worker"/>
                </figure>
                <h5 class="c-person-card__title">
                    Name Surname
                </h5>
                <h6 class="c-person-card__subtitle">
                    Position
                </h6>
                <div class="c-person-card__details">
                    <p class="c-person-card__info">
                        Roger is Chair of Oxford Metrics and a Non-Executive Director of Uber UK. He was previously Chair of Future Publishing, Johnston Press and Shakespeare’s Globe Trust; a consultant with McKinsey & Co; CEO of More Group, and
                        CEO of Clear Channel International. Roger was educated at the universities of Oxford and Bristol. He is a Visiting Fellow of Oxford University. He was awarded the CBE in 2014. He is the author of five books including The
                        Ascent of Media.
                    </p>
                </div>
                <div class="c-person-card__action">
                    <button class="c-read-more-btn c-underline-link js-toggle-accordion">
                        <span class="c-read-more-btn__span">Read more</span>
                        <span class="c-read-more-btn__span">Read less</span>
                        <span class="c-underline-link__icon o-icon-wrapper">
                            <svg class="o-icon o-icon--cross">
                                <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-cross"></use>
                            </svg>
                        </span>
                    </button>
                </div>
            </div>
        </li>
        <li class="c-cards-list__item">
            <div class="c-person-card js-accordion">
                <figure class="c-person-card__media">
                    <img src="/static/img/pic_person_2.jpg" alt="Office worker"/>
                </figure>
                <h5 class="c-person-card__title">
                    Name Surname
                </h5>
                <h6 class="c-person-card__subtitle">
                    Position
                </h6>
                <div class="c-person-card__details">
                    <p class="c-person-card__info">
                        Roger is Chair of Oxford Metrics and a Non-Executive Director of Uber UK. He was previously Chair of Future Publishing, Johnston Press and Shakespeare’s Globe Trust; a consultant with McKinsey & Co; CEO of More Group, and
                        CEO of Clear Channel International. Roger was educated at the universities of Oxford and Bristol. He is a Visiting Fellow of Oxford University. He was awarded the CBE in 2014. He is the author of five books including The
                        Ascent of Media.
                    </p>
                </div>
                <div class="c-person-card__action">
                    <button class="c-read-more-btn c-underline-link js-toggle-accordion">
                        <span class="c-read-more-btn__span">Read more</span>
                        <span class="c-read-more-btn__span">Read less</span>
                        <span class="c-underline-link__icon o-icon-wrapper">
                            <svg class="o-icon o-icon--cross">
                                <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-cross"></use>
                            </svg>
                        </span>
                    </button>
                </div>
            </div>
        </li>
        <li class="c-cards-list__item">
            <div class="c-person-card js-accordion">
                <figure class="c-person-card__media">
                    <img src="/static/img/pic_person_1.jpg" alt="Office worker"/>
                </figure>
                <h5 class="c-person-card__title">
                    Name Surname
                </h5>
                <h6 class="c-person-card__subtitle">
                    Position
                </h6>
                <div class="c-person-card__details">
                    <p class="c-person-card__info">
                        Roger is Chair of Oxford Metrics and a Non-Executive Director of Uber UK. He was previously Chair of Future Publishing, Johnston Press and Shakespeare’s Globe Trust; a consultant with McKinsey & Co; CEO of More Group, and
                        CEO of Clear Channel International. Roger was educated at the universities of Oxford and Bristol. He is a Visiting Fellow of Oxford University. He was awarded the CBE in 2014. He is the author of five books including The
                        Ascent of Media.
                    </p>
                </div>
                <div class="c-person-card__action">
                    <button class="c-read-more-btn c-underline-link js-toggle-accordion">
                        <span class="c-read-more-btn__span">Read more</span>
                        <span class="c-read-more-btn__span">Read less</span>
                        <span class="c-underline-link__icon o-icon-wrapper">
                            <svg class="o-icon o-icon--cross">
                                <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-cross"></use>
                            </svg>
                        </span>
                    </button>
                </div>
            </div>
        </li>
    </ul>
</div>

{% endblock %}
