{% macro render() %}

{% import "../components/cookie.tpl" as c_cookie %}
{{ c_cookie.render() }}

<footer class="l-footer">
    <div class="l-footer__row">
        <div class="l-footer__about">
            <div class="c-about">
                <div class="c-about__heading">
                    <span class="o-icon-wrapper">
                        <svg class="o-icon o-icon--yougov">
                            <use xmlns:xlink="http://www.w3.org/1999/xlink"
                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-yougov">
                            </use>
                        </svg>
                    </span>
                </div>
                <div class="c-about__text c-wysiwyg">
                    <h5><strong>About YouGov</strong></h5>
                    <p>
                        At the heart of our company is a global online community, where millions of people and thousands of political, cultural and commercial organizations engage in a continuous conversation about their beliefs, behaviours and brands.
                    </p>
                </div>
                <div class="c-about__copyright">
                    <p>
                        Copyright &copy; 2018 YouGov PLC. All Rights Reserved.
                    </p>
                </div>
                <div class="c-about__policy">
                    <ul class="c-policy-list">
                        <li class="c-policy-list__item">
                            <a href="#" class="c-underline-link">
                                Privacy & Cookies Notice
                            </a>
                        </li>
                        <li class="c-policy-list__item">
                            <a href="#" class="c-underline-link">
                                Website Terms & Conditions
                            </a>
                        </li>
                    </ul>
                </div>
                <div class="c-about__social js-scroll-reveal">
                    <ul class="c-social-media c-social-media--alt">
                        <li class="c-social-media__list">
                            <a href="https://twitter.com/" class="c-icon-with-decor c-icon-with-decor--alt-dark" target="_blank" rel="noopener noreferrer">
                                <span class="o-icon-wrapper">
                                    <svg class="o-icon o-icon--twitter">
                                        <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-twitter"></use>
                                    </svg>
                                </span>
                            </a>
                        </li>
                        <li class="c-social-media__list">
                            <a href="#" class="c-icon-with-decor c-icon-with-decor--alt-dark" target="_blank" rel="noopener noreferrer">
                                <span class="o-icon-wrapper">
                                    <svg class="o-icon o-icon--linkedin">
                                        <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-linkedin"></use>
                                    </svg>
                                </span>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="l-footer__action">
            <a href="#" class="c-back-to-top js-scroll-up">
                <span class="c-back-to-top__icon o-icon-wrapper">
                    <svg class="o-icon o-icon--long-arrow-up">
                        <use xmlns:xlink="http:www.w3.org/1999/xlink"
                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-long-arrow-up">
                        </use>
                    </svg>
                </span>
                <div class="c-back-to-top__text">
                    <span>
                        Back to top
                    </span>
                </div>
            </a>
        </div>
    </div>
    <div class="l-footer__row l-footer__row--alt">
        <div class="l-footer__list">
            <div class="c-footer">
                <div class="c-footer__col c-footer__col--narrow">
                    <h4 class="c-footer__heading">Company</h4>
                    <ul class="c-footer-list">
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Modern slavery act
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Careers
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Join the panel
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Global offices
                            </a>
                        </li>
                    </ul>
                    <div class="c-footer__media-wrapper">
                        <span class="o-icon-wrapper">
                            <svg class="o-icon o-icon--assurance-mark">
                                <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                     xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-assurance-mark">
                               </use>
                            </svg>
                        </span>
                    </div>
                </div>
                <div class="c-footer__col c-footer__col--wide">
                    <h4 class="c-footer__heading">Global Sites</h4>
                    <ul class="c-footer-list c-footer-list--alt">
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Australia
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Canada
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Denmark
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Finland
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                France
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Germany
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Hong Kong
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                India
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Indonesia
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Italy
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Malaysia
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Mexico
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Middle East
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Norway
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Pakistan
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Philippines
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Poland
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Singapore
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Spain
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Sweden
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Taiwan
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Thailand
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                United Kingdom
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                United States
                            </a>
                        </li>
                        <li class="c-footer-list__item">
                            <a href="#" class="c-underline-link">
                                Vietnam
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</footer>
{% endmacro %}
