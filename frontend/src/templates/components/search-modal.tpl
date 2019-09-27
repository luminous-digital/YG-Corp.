{% macro render() %}
<div id="search-modal" class="c-modal c-modal--search">
    <div class="c-modal__content">
        <div class="c-modal__head">
            <figure class="c-logo">
                <img class="c-logo__image" src="./static/img/logo-yougov.png" alt="YouGov" />
            </figure>
            <a href="#" class="c-modal__close js-close-modal-trigger">
                <span class="o-icon-wrapper">
                    <svg class="o-icon o-icon--cross">
                        <use xmlns:xlink="http://www.w3.org/1999/xlink"
                            xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-cross">
                        </use>
                    </svg>
                </span>
            </a>
        </div>
        <div class="c-modal__body">
            <form class="f-search-form">
                <div class="f-field f-field--search">
                    <input type="text" class="f-field__control" placeholder="Search" />
                    <a href="#" class="f-field__btn js-search-toggler">
                        <span class="o-icon-wrapper">
                            <svg class="o-icon o-icon--search">
                                <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-search">
                                </use>
                            </svg>
                        </span>
                    </a>
                    <button class="f-field__btn f-field__btn--hidden">
                        <span class="o-icon-wrapper">
                            <svg class="o-icon o-icon--search">
                                <use xmlns:xlink="http://www.w3.org/1999/xlink"
                                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-search">
                                </use>
                            </svg>
                        </span>
                    </button>
                </div>
            </form>
        </div>
    </div>
</div>
{% endmacro %}
