{% extends "base/base.tpl" %}
{% block title %}
Downloads Table
{% endblock %}
{% block content %}

<div class="l-inner">
    <div class="c-downloads-wrapper">
        <div class="c-tabs js-main-container">
            <div class="c-tabs__nav c-tabs__nav--no-margin">
                <button class="c-tabs__placeholder c-underline-link js-tabs-open">
                    <span class="js-main-tab-placeholder">
                        All
                    </span>
                    <span class="c-tabs__placeholder-icon o-icon-wrapper">
                        <svg class="o-icon o-icon--arrow-right-bold">
                            <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right-bold"></use>
                        </svg>
                    </span>
                </button>
                <ul class="c-tabs__nav-list js-main-tabs-nav">
                    <li class="c-tabs__nav-item js-tab-clear-filter is-active">
                        <button class="c-tabs__cta c-underline-link">
                            All
                        </button>
                    </li>
                    <li class="c-tabs__nav-item" data-tab="2019">
                        <button class="c-tabs__cta c-underline-link">
                            2019
                        </button>
                    </li>
                    <li class="c-tabs__nav-item" data-tab="2018">
                        <button class="c-tabs__cta c-underline-link">
                            2018
                        </button>
                    </li>
                </ul>
            </div>
            <div class="c-downloads-table c-downloads-table--teal js-table-content">
                <div class="c-downloads-table__heading c-downloads-table__heading--alt">
                    <div class="c-heading c-heading--alt">
                        <h6 class="c-heading__date">
                            Date
                        </h6>
                        <h6 class="c-heading__news">
                            Description
                        </h6>
                    </div>
                </div>
                <div class="c-downloads-table__content" data-tab="2019">
                    <div class="c-downloads">
                        <div class="c-downloads__post-wrapper">
                            <time datetime="0000-00-00" class="c-downloads__date">
                                2019/01/31
                            </time>
                            <h5 class="c-downloads__title">
                                Lorem ipum dolor et
                            </h5>
                        </div>
                        <div class="c-downloads__info-wrapper">
                            <a href="#" class="c-underline-link c-underline-link--inline c-underline-link--left" download>
                                <span class="c-underline-link__icon o-icon-wrapper">
                                    <svg class="o-icon o-icon--download">
                                        <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-download"></use>
                                    </svg>
                                </span>
                                <span class="c-underline-link__text-wrapper">
                                    <span class="c-underline-link__text">
                                        PDF 0.00Mb
                                    </span>
                                </span>
                            </a>
                        </div>
                    </div>
                </div>
                <div class="c-downloads-table__content" data-tab="2018">
                    <div class="c-downloads">
                        <div class="c-downloads__post-wrapper">
                            <time datetime="0000-00-00" class="c-downloads__date">
                                2018/01/31
                            </time>
                            <h5 class="c-downloads__title">
                                Lorem ipum dolor et
                            </h5>
                        </div>
                        <div class="c-downloads__info-wrapper">
                            <a href="#" class="c-underline-link c-underline-link--inline c-underline-link--left" download>
                                <span class="c-underline-link__icon o-icon-wrapper">
                                    <svg class="o-icon o-icon--download">
                                        <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-download"></use>
                                    </svg>
                                </span>
                                <span class="c-underline-link__text-wrapper">
                                    <span class="c-underline-link__text">
                                        PDF 0.00Mb
                                    </span>
                                </span>
                            </a>
                        </div>
                    </div>
                </div>
                <div class="c-downloads-table__content" data-tab="2018">
                    <div class="c-downloads">
                        <div class="c-downloads__post-wrapper">
                            <time datetime="0000-00-00" class="c-downloads__date">
                                2018/05/31
                            </time>
                            <h5 class="c-downloads__title">
                                Lorem ipum dolor et
                            </h5>
                        </div>
                        <div class="c-downloads__info-wrapper">
                            <a href="#" class="c-underline-link c-underline-link--inline c-underline-link--left" download>
                                <span class="c-underline-link__icon o-icon-wrapper">
                                    <svg class="o-icon o-icon--download">
                                        <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-download"></use>
                                    </svg>
                                </span>
                                <span class="c-underline-link__text-wrapper">
                                    <span class="c-underline-link__text">
                                        PDF 0.00Mb
                                    </span>
                                </span>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

{% endblock %}
