{% macro render(_active_no, _active_subnav_no) %}
<header class="l-header js-header">
    <div class="l-header__wrapper">
        <div class="l-header__topbar">
            <div class="l-inner">
                <ul class="c-topbar">
                    <li class="c-topbar__item">
                        <p href="governance.html" class="t-body-2">
                            Our other sites:
                        </p>
                    </li>
                    <li class="c-topbar__item">
                        <a href="products-and-services.html" class="c-underline-link" target="_blank">
                            Products and services
                        </a>
                    </li>
                    <li class="c-topbar__item">
                        <a href="careers.html" class="c-underline-link" target="_blank">
                            Careers
                        </a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="l-header__main">
            <div class="l-inner">
                <div class="c-header">
                    <div class="c-header__action">
                        <a href="index.html" class="c-logo">
                            <span class="o-icon-wrapper">
                                <svg class="o-icon o-icon--yougov">
                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-yougov">
                                    </use>
                                </svg>
                            </span>
                        </a>
                        <button type="button" class="c-hamburger js-menu-open-trigger" title="Toggle menu">
                            <span class="c-hamburger__line c-hamburger__line--hidden">Toggle menu</span>
                            <span class="c-hamburger__line"></span>
                            <span class="c-hamburger__line"></span>
                            <span class="c-hamburger__line"></span>
                        </button>
                    </div>
                    <div class="c-header__main">
                        <div class="l-nav">
                            <div class="l-nav__main">
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
                                                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-down">
                                                        </use>
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
                                                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-down">
                                                        </use>
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
                                                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-down">
                                                        </use>
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
                                                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-down">
                                                        </use>
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
                                                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-down">
                                                        </use>
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
                                                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-down">
                                                        </use>
                                                    </svg>
                                                </span>
                                            </a>
                                        </li>
                                    </ul>
                                </nav>
                                {% include "components/search.tpl" %}
                            </div>
                            <div class="l-nav__sub js-sub-nav-container">
                                <div class="c-sub-nav">
                                    <div class="l-inner">
                                        <div id="about-sub-nav" class="c-sub-nav-box">
                                            <div class="c-sub-nav-box__download">
                                                <a href="#" class="c-download-box" download="#">
                                                    <figure class="c-download-box__media">
                                                        <img src="./static/img/pic-download-1.jpg" alt="alt" />
                                                    </figure>
                                                    <div class="c-download-box__action">
                                                        <span class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                                Download our factsheet&nbsp;
                                                                <span class="c-underline-link__icon o-icon-wrapper">
                                                                    <svg class="o-icon o-icon--arrow-right">
                                                                        <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                        </use>
                                                                    </svg>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </div>
                                                </a>
                                            </div>
                                            <div class="c-sub-nav-box__list">
                                                <a href="#"
                                                    class="c-sub-nav-box__back c-underline-link c-underline-link--revert js-sub-nav-close-trigger">
                                                    <span class="c-underline-link__icon o-icon-wrapper">
                                                        <svg class="o-icon o-icon--arrow-left">
                                                            <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                            </use>
                                                        </svg>
                                                    </span>
                                                    Main Menu
                                                </a>
                                                <ul class="c-list c-list--column-wrap">
                                                    <li
                                                        class="c-list__item{% if _active_no == '1.1' %} is-active{% endif %}">
                                                        <a href="about.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            About
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '1.2' %} is-active{% endif %}">
                                                        <a href="business-model.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Business model/strategy
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '1.3' %} is-active{% endif %}">
                                                        <a href="corporate-overview.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Corporate overview
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '1.4' %} is-active{% endif %}">
                                                        <a href="timeline.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Timeline/heritage
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '1.5' %} is-active{% endif %}">
                                                        <a href="faq.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            FAQs
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div id="investors-sub-nav" class="c-sub-nav-box">
                                            <div class="c-sub-nav-box__download">
                                                <a href="#" class="c-download-box" download="#">
                                                    <figure class="c-download-box__media">
                                                        <img src="./static/img/pic-download-1.jpg" alt="alt" />
                                                    </figure>
                                                    <div class="c-download-box__action">
                                                        <span class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                                Download our latest report&nbsp;
                                                                <span class="c-underline-link__icon o-icon-wrapper">
                                                                    <svg class="o-icon o-icon--arrow-right">
                                                                        <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                        </use>
                                                                    </svg>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </div>
                                                </a>
                                            </div>
                                            <div class="c-sub-nav-box__list">
                                                <a href="#"
                                                    class="c-sub-nav-box__back c-underline-link c-underline-link--revert js-sub-nav-close-trigger">
                                                    <span class="c-underline-link__icon o-icon-wrapper">
                                                        <svg class="o-icon o-icon--arrow-left">
                                                            <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                            </use>
                                                        </svg>
                                                    </span>
                                                    Main Menu
                                                </a>
                                                <ul class="c-list c-list--column-wrap">
                                                    <li
                                                        class="c-list__item{% if _active_no == '1.2' %} is-active{% endif %}">
                                                        <a href="investors.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Investors
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '2.2' %} is-active{% endif %}">
                                                        <a href="share-price.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Share price
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '2.3' %} is-active{% endif %}">
                                                        <a href="financial-reports.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Financial reports
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '2.4' %} is-active{% endif %}">
                                                        <a href="regulatory-announcements.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Regulatory announcements
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '2.5' %} is-active{% endif %}">
                                                        <a href="rns-alerts.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            RNS alerts
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '2.6' %} is-active{% endif %}">
                                                        <a href="financial-calendar.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Financial calendar
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '2.7' %} is-active{% endif %}">
                                                        <a href="presentations.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Presentations
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '2.8' %} is-active{% endif %}">
                                                        <a href="shareholders.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Shareholders
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '2.9' %} is-active{% endif %}">
                                                        <a href="research.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Research
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div id="governance-sub-nav" class="c-sub-nav-box">
                                            <div class="c-sub-nav-box__download">
                                                <a href="#" class="c-download-box" download="#">
                                                    <figure class="c-download-box__media">
                                                        <img src="./static/img/pic-download-1.jpg" alt="alt" />
                                                    </figure>
                                                    <div class="c-download-box__action">
                                                        <span class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                                Latest corporate document&nbsp;
                                                                <span class="c-underline-link__icon o-icon-wrapper">
                                                                    <svg class="o-icon o-icon--arrow-right">
                                                                        <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                        </use>
                                                                    </svg>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </div>
                                                </a>
                                            </div>
                                            <div class="c-sub-nav-box__list">
                                                <a href="#"
                                                    class="c-sub-nav-box__back c-underline-link c-underline-link--revert js-sub-nav-close-trigger">
                                                    <span class="c-underline-link__icon o-icon-wrapper">
                                                        <svg class="o-icon o-icon--arrow-left">
                                                            <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                            </use>
                                                        </svg>
                                                    </span>
                                                    Main Menu
                                                </a>
                                                <ul class="c-list c-list--column-wrap">
                                                    <li
                                                        class="c-list__item{% if _active_no == '1.3' %} is-active{% endif %}">
                                                        <a href="governance.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Governance
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '3.2' %} is-active{% endif %}">
                                                        <a href="board-of-directors.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Board of Directors
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '3.3' %} is-active{% endif %}">
                                                        <a href="aim-rule-26.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            AIM Rule 26
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '3.4' %} is-active{% endif %}">
                                                        <a href="corporate-documents.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Corporate documents
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '3.5' %} is-active{% endif %}">
                                                        <a href="advisors-and-registrars.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Advisors and Registrars
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '3.6' %} is-active{% endif %}">
                                                        <a href="corporate-responsibility.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Corporate responsibility
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '3.7' %} is-active{% endif %}">
                                                        <a href="registered-office.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Registered office
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div id="compliance-sub-nav" class="c-sub-nav-box">
                                            <div class="c-sub-nav-box__download">
                                                <a href="#" class="c-download-box" download="#">
                                                    <figure class="c-download-box__media">
                                                        <img src="./static/img/pic-download-1.jpg" alt="alt" />
                                                    </figure>
                                                    <div class="c-download-box__action">
                                                        <span class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                                Download our latest report&nbsp;
                                                                <span class="c-underline-link__icon o-icon-wrapper">
                                                                    <svg class="o-icon o-icon--arrow-right">
                                                                        <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                        </use>
                                                                    </svg>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </div>
                                                </a>
                                            </div>
                                            <div class="c-sub-nav-box__list">
                                                <a href="#"
                                                    class="c-sub-nav-box__back c-underline-link c-underline-link--revert js-sub-nav-close-trigger">
                                                    <span class="c-underline-link__icon o-icon-wrapper">
                                                        <svg class="o-icon o-icon--arrow-left">
                                                            <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                            </use>
                                                        </svg>
                                                    </span>
                                                    Main Menu
                                                </a>
                                                <ul class="c-list c-list--column-wrap">
                                                    <li
                                                        class="c-list__item{% if _active_no == '1.4' %} is-active{% endif %}">
                                                        <a href="compliance.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Compliance
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '4.2' %} is-active{% endif %}">
                                                        <a href="our-data-values.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Our data values
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '4.3' %} is-active{% endif %}">
                                                        <a href="data-protection.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Data protection
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '4.4' %} is-active{% endif %}">
                                                        <a href="data-security.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Data security
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '4.5' %} is-active{% endif %}">
                                                        <a href="clients.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Clients
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '4.6' %} is-active{% endif %}">
                                                        <a href="faq.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            FAQs
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '4.7' %} is-active{% endif %}">
                                                        <a href="sub-processors.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Sub-processors
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '4.8' %} is-active{% endif %}">
                                                        <a href="sub-processors.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Presentations
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div id="press-sub-nav" class="c-sub-nav-box">
                                            <div class="c-sub-nav-box__download">
                                                <a href="#" class="c-download-box" download="#">
                                                    <figure class="c-download-box__media">
                                                        <img src="./static/img/pic-download-1.jpg" alt="alt" />
                                                    </figure>
                                                    <div class="c-download-box__action">
                                                        <span class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                                Download our latest report&nbsp;
                                                                <span class="c-underline-link__icon o-icon-wrapper">
                                                                    <svg class="o-icon o-icon--arrow-right">
                                                                        <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                        </use>
                                                                    </svg>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </div>
                                                </a>
                                            </div>
                                            <div class="c-sub-nav-box__list">
                                                <a href="#"
                                                    class="c-sub-nav-box__back c-underline-link c-underline-link--revert js-sub-nav-close-trigger">
                                                    <span class="c-underline-link__icon o-icon-wrapper">
                                                        <svg class="o-icon o-icon--arrow-left">
                                                            <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                            </use>
                                                        </svg>
                                                    </span>
                                                    Main Menu
                                                </a>
                                                <ul class="c-list c-list--column-wrap">
                                                    <li
                                                        class="c-list__item{% if _active_no == '1.5' %} is-active{% endif %}">
                                                        <a href="press.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Press
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '5.2' %} is-active{% endif %}">
                                                        <a href="media-kit.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Media kit
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '5.3' %} is-active{% endif %}">
                                                        <a href="yougov-stories.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            YouGov stories
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div id="contact-sub-nav" class="c-sub-nav-box">
                                            <div class="c-sub-nav-box__download">
                                                <a href="#" class="c-download-box" download="#">
                                                    <figure class="c-download-box__media">
                                                        <img src="./static/img/pic-download-1.jpg" alt="alt" />
                                                    </figure>
                                                    <div class="c-download-box__action">
                                                        <span class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                                Download our latest report&nbsp;
                                                                <span class="c-underline-link__icon o-icon-wrapper">
                                                                    <svg class="o-icon o-icon--arrow-right">
                                                                        <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                        </use>
                                                                    </svg>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </div>
                                                </a>
                                            </div>
                                            <div class="c-sub-nav-box__list">
                                                <a href="#"
                                                    class="c-sub-nav-box__back c-underline-link c-underline-link--revert js-sub-nav-close-trigger">
                                                    <span class="c-underline-link__icon o-icon-wrapper">
                                                        <svg class="o-icon o-icon--arrow-left">
                                                            <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                            </use>
                                                        </svg>
                                                    </span>
                                                    Main Menu
                                                </a>
                                                <ul class="c-list c-list--column-wrap">
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '6.1' %} is-active{% endif %}">
                                                        <a href="contact.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Contact
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '6.2' %} is-active{% endif %}">
                                                        <a href="global-offices.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Global offices
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                    <li
                                                        class="c-list__item{% if _active_subnav_no == '6.3' %} is-active{% endif %}">
                                                        <a href="investor-contact.html" class="c-underline-link c-underline-link--inline">
                                                            <span class="c-underline-link__text">
                                                            Investor contact
                                                            <span class="c-underline-link__icon o-icon-wrapper">
                                                                <svg class="o-icon o-icon--arrow-right">
                                                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                                                                    </use>
                                                                </svg>
                                                            </span>
                                                            </span>
                                                        </a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="l-header__social-media">
            <div class="c-header__social-media">
                <ul class="c-social-media c-social-media--horizontal">
                    <li class="c-social-media__list">
                        <a href="#" class="c-icon-with-decor" target="_blank">
                            <span class="o-icon-wrapper">
                                <svg class="o-icon o-icon--twitter">
                                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-twitter"></use>
                                </svg>
                            </span>
                        </a>
                    </li>
                    <li class="c-social-media__list">
                        <a href="#" class="c-icon-with-decor" target="_blank">
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
        </div>
    </div>
</header>
{% endmacro %}
