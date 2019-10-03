{% extends "base/base.tpl" %}
{% block title %}
    News
{% endblock %}
{% block bodyClass %}has-subnav{% endblock %}
{% set active_no = '' %}
{% set active_subnav_no = '' %}
{% block content %}
<div class="l-inner">
    <div class="l-news js-ajax-load-more-container">
        <ul class="c-list c-list--horizontal-wrap js-ajax-load-more-list">
            <li class="c-list__item">
                <a href="#" class="c-news-card">
                    <figure class="c-news-card__media">
                        <img class="c-news-card__img" src="/static/img/img-test.jpg" alt="News image"/>
                    </figure>
                    <time datetime="11-07-2019" class="c-news-card__date">
                        July 11, 2019
                    </time>
                    <h5 class="c-news-card__title">
                        Headline goes here
                    </h5>
                    <p class="c-news-card__info">
                        Lorem ipsum dolor sit amet, conse ctetur adipiscing elit. Maecenas va rius tortor nibh, sit amet tempor ni bh finibus et. Aenean eu enim jus to vestibulum aliquam
                    </p>
                </a>
            </li>
            <li class="c-list__item">
                <a href="#" class="c-news-card">
                    <figure class="c-news-card__media">
                        <img class="c-news-card__img" src="/static/img/img-test.jpg" alt="News image"/>
                    </figure>
                    <time datetime="11-07-2019" class="c-news-card__date">
                        July 11, 2019
                    </time>
                    <h5 class="c-news-card__title">
                        Headline goes here
                    </h5>
                    <p class="c-news-card__info">
                        Lorem ipsum dolor sit amet, conse ctetur adipiscing elit. Maecenas va rius tortor nibh, sit amet tempor ni bh finibus et. Aenean eu enim jus to vestibulum aliquam
                    </p>
                </a>
            </li>
            <li class="c-list__item">
                <a href="#" class="c-news-card">
                    <figure class="c-news-card__media">
                        <img class="c-news-card__img" src="/static/img/img-123.jpg" alt="News image"/>
                    </figure>
                    <time datetime="11-07-2019" class="c-news-card__date">
                        July 11, 2019
                    </time>
                    <h5 class="c-news-card__title">
                        Headline goes here
                    </h5>
                    <p class="c-news-card__info">
                        Lorem ipsum dolor sit amet, conse ctetur adipiscing elit. Maecenas va rius tortor nibh, sit amet tempor ni bh finibus et. Aenean eu enim jus to vestibulum aliquam
                    </p>
                </a>
            </li>
            <li class="c-list__item">
                <a href="#" class="c-news-card">
                    <figure class="c-news-card__media">
                        <img class="c-news-card__img" src="/static/img/img-news-3.jpg" alt="News image"/>
                    </figure>
                    <time datetime="11-07-2019" class="c-news-card__date">
                        July 11, 2019
                    </time>
                    <h5 class="c-news-card__title">
                        Headline goes here
                    </h5>
                    <p class="c-news-card__info">
                        Lorem ipsum dolor sit amet, conse ctetur adipiscing elit. Maecenas va rius tortor nibh, sit amet tempor ni bh finibus et. Aenean eu enim jus to vestibulum aliquam
                    </p>
                </a>
            </li>
            <li class="c-list__item">
                <a href="#" class="c-news-card">
                    <figure class="c-news-card__media">
                        <img class="c-news-card__img" src="/static/img/img-news-4.jpg" alt="News image"/>
                    </figure>
                    <time datetime="11-07-2019" class="c-news-card__date">
                        July 11, 2019
                    </time>
                    <h5 class="c-news-card__title">
                        Headline goes here
                    </h5>
                    <p class="c-news-card__info">
                        Lorem ipsum dolor sit amet, conse ctetur adipiscing elit. Maecenas va rius tortor nibh, sit amet tempor ni bh finibus et. Aenean eu enim jus to vestibulum aliquam
                    </p>
                </a>
            </li>
            <li class="c-list__item">
                <a href="#" class="c-news-card">
                    <figure class="c-news-card__media">
                        <img class="c-news-card__img" src="/static/img/img-test.jpg" alt="News image"/>
                    </figure>
                    <time datetime="11-07-2019" class="c-news-card__date">
                        July 11, 2019
                    </time>
                    <h5 class="c-news-card__title">
                        Headline goes here
                    </h5>
                    <p class="c-news-card__info">
                        Lorem ipsum dolor sit amet, conse ctetur adipiscing elit. Maecenas va rius tortor nibh, sit amet tempor ni bh finibus et. Aenean eu enim jus to vestibulum aliquam
                    </p>
                </a>
            </li>
            <li class="c-list__item">
                <a href="#" class="c-news-card">
                    <figure class="c-news-card__media">
                        <img class="c-news-card__img" src="/static/img/img-news-5.jpg" alt="News image"/>
                    </figure>
                    <time datetime="11-07-2019" class="c-news-card__date">
                        July 11, 2019
                    </time>
                    <h5 class="c-news-card__title">
                        Headline goes here
                    </h5>
                    <p class="c-news-card__info">
                        Lorem ipsum dolor sit amet, conse ctetur adipiscing elit. Maecenas va rius tortor nibh, sit amet tempor ni bh finibus et. Aenean eu enim jus to vestibulum aliquam
                    </p>
                </a>
            </li>
            <li class="c-list__item">
                <a href="#" class="c-news-card">
                    <figure class="c-news-card__media">
                        <img class="c-news-card__img" src="/static/img/img-news-8.jpg" alt="News image"/>
                    </figure>
                    <time datetime="11-07-2019" class="c-news-card__date">
                        July 11, 2019
                    </time>
                    <h5 class="c-news-card__title">
                        Headline goes here
                    </h5>
                    <p class="c-news-card__info">
                        Lorem ipsum dolor sit amet, conse ctetur adipiscing elit. Maecenas va rius tortor nibh, sit amet tempor ni bh finibus et. Aenean eu enim jus to vestibulum aliquam
                    </p>
                </a>
            </li>
            <li class="c-list__item">
                <a href="#" class="c-news-card">
                    <figure class="c-news-card__media">
                        <img class="c-news-card__img" src="/static/img/img-news-6.jpg" alt="News image"/>
                    </figure>
                    <time datetime="11-07-2019" class="c-news-card__date">
                        July 11, 2019
                    </time>
                    <h5 class="c-news-card__title">
                        Headline goes here
                    </h5>
                    <p class="c-news-card__info">
                        Lorem ipsum dolor sit amet, conse ctetur adipiscing elit. Maecenas va rius tortor nibh, sit amet tempor ni bh finibus et. Aenean eu enim jus to vestibulum aliquam
                    </p>
                </a>
            </li>
            <li class="c-list__item">
                <a href="#" class="c-news-card">
                    <figure class="c-news-card__media">
                        <img class="c-news-card__img" src="/static/img/img-news-2.jpg" alt="News image"/>
                    </figure>
                    <time datetime="11-07-2019" class="c-news-card__date">
                        July 11, 2019
                    </time>
                    <h5 class="c-news-card__title">
                        Headline goes here
                    </h5>
                    <p class="c-news-card__info">
                        Lorem ipsum dolor sit amet, conse ctetur adipiscing elit. Maecenas va rius tortor nibh, sit amet tempor ni bh finibus et. Aenean eu enim jus to vestibulum aliquam
                    </p>
                </a>
            </li>
            <li class="c-list__item">
                <a href="#" class="c-news-card">
                    <figure class="c-news-card__media">
                        <img class="c-news-card__img" src="/static/img/img-news-1.jpg" alt="News image" />
                    </figure>
                    <time datetime="11-07-2019" class="c-news-card__date">
                        July 11, 2019
                    </time>
                    <h5 class="c-news-card__title">
                        Headline goes here
                    </h5>
                    <p class="c-news-card__info">
                        Lorem ipsum dolor sit amet, conse ctetur adipiscing elit. Maecenas va rius tortor nibh, sit amet tempor ni bh finibus et. Aenean eu enim jus to vestibulum aliquam
                    </p>
                </a>
            </li>
            <li class="c-list__item">
                <a href="#" class="c-news-card">
                    <figure class="c-news-card__media">
                        <img class="c-news-card__img" src="/static/img/img-news-7.jpg" alt="News image"/>
                    </figure>
                    <time datetime="11-07-2019" class="c-news-card__date">
                        July 11, 2019
                    </time>
                    <h5 class="c-news-card__title">
                        Headline goes here
                    </h5>
                    <p class="c-news-card__info">
                        Lorem ipsum dolor sit amet, conse ctetur adipiscing elit. Maecenas va rius tortor nibh, sit amet tempor ni bh finibus et. Aenean eu enim jus to vestibulum aliquam
                    </p>
                </a>
            </li>
        </ul>
        <div class="l-news__action">
            <div class="c-loader">
                <div class="c-loader__item"></div>
                <div class="c-loader__item"></div>
                <div class="c-loader__item"></div>
                <div class="c-loader__item"></div>
            </div>
            <button data-href="/news/?ajax=1&page=1" class="c-read-more-btn c-underline-link js-ajax-load-more-trigger">
                <span class="c-read-more-btn__span">
                    Load more
                </span>
                <span class="c-underline-link__icon o-icon-wrapper">
                    <svg class="o-icon o-icon--cross">
                        <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-cross"></use>
                    </svg>
                </span>
            </button>
        </div>
    </div>
</div>
{% endblock %}
