{% extends "base/base.tpl" %}
{% block title %}
    Form
{% endblock %}
{% set active_no = '' %}
{% set active_subnav_no = '' %}
{% block content %}

<div class="l-inner l-inner--small">
    <form class="f-form f-form--validation js-form js-ajax-form">
        <div class="f-field">
            <input class="f-field__control" placeholder="First Name" type="text" required='' data-parsley-errors-container="#message-1"/>
            <span class="f-field__validation-icon o-icon-wrapper">
                <svg class="o-icon o-icon--error">
                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                    xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-fail">
                    </use>
                </svg>
                <svg class="o-icon o-icon--tick">
                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                    xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-tick">
                    </use>
                </svg>
            </span>
            <div class="f-field__message" id="message-1">
            </div>
        </div>
        <div class="f-field">
            <input class="f-field__control" placeholder="Last Name" type="text" required='' data-parsley-errors-container="#message-2"/>
            <span class="f-field__validation-icon o-icon-wrapper">
                <svg class="o-icon o-icon--error">
                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                    xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-fail">
                    </use>
                </svg>
                <svg class="o-icon o-icon--tick">
                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                    xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-tick">
                    </use>
                </svg>
            </span>
            <div class="f-field__message" id="message-2">
            </div>
        </div>
        <div class="f-field">
            <input class="f-field__control" placeholder="Job Title" type="text" required='' data-parsley-errors-container="#message-3"/>
            <span class="f-field__validation-icon o-icon-wrapper">
                <svg class="o-icon o-icon--error">
                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                    xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-fail">
                    </use>
                </svg>
                <svg class="o-icon o-icon--tick">
                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                    xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-tick">
                    </use>
                </svg>
            </span>
            <div class="f-field__message" id="message-3">
            </div>
        </div>
        <div class="f-field">
            <input class="f-field__control" placeholder="Company Name" type="text" required='' data-parsley-errors-container="#message-4"/>
            <span class="f-field__validation-icon o-icon-wrapper">
                <svg class="o-icon o-icon--error">
                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                    xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-fail">
                    </use>
                </svg>
                <svg class="o-icon o-icon--tick">
                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                    xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-tick">
                    </use>
                </svg>
            </span>
            <div class="f-field__message" id="message-4">
            </div>
        </div>
        <div class="f-field">
            <input class="f-field__control" placeholder="Company Email" type="email" required='' data-parsley-type="email" data-parsley-error-message="Must be valid email. example@yourdomain.com" data-parsley-errors-container="#message-5"/>
            <span class="f-field__validation-icon o-icon-wrapper">
                <svg class="o-icon o-icon--error">
                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                    xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-fail">
                    </use>
                </svg>
                <svg class="o-icon o-icon--tick">
                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                    xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-tick">
                    </use>
                </svg>
            </span>
            <div class="f-field__message" id="message-5">
            </div>
        </div>
        <div class="f-field">
            <input class="f-field__control" placeholder="Phone Number" type="tel" data-parsley-type="number" required='' data-parsley-errors-container="#message-6"/>
            <span class="f-field__validation-icon o-icon-wrapper">
                <svg class="o-icon o-icon--error">
                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                    xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-fail">
                    </use>
                </svg>
                <svg class="o-icon o-icon--tick">
                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                    xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-tick">
                    </use>
                </svg>
            </span>
            <div class="f-field__message" id="message-6">
            </div>
        </div>
        <div class="f-field f-field--select">
            <select class="f-field__control js-select" data-placeholder="Select" required=''>
                <option></option>
                <option value="Lorem ipsum">Lorem ipsum</option>
                <option value="Lorem ipsum">Lorem ipsum</option>
                <option value="Lorem ipsum">Lorem ipsum</option>
                <option value="Lorem ipsum">Lorem ipsum</option>
                <option value="Lorem ipsum">Lorem ipsum</option>
                <option value="Lorem ipsum">Lorem ipsum</option>
                <option value="Lorem ipsum">Lorem ipsum</option>
                <option value="Lorem ipsum">Lorem ipsum</option>
            </select>
            <span class="o-icon-wrapper">
                <svg class="o-icon o-icon--arrow-simple">
                    <use xmlns:xlink="http://www.w3.org/1999/xlink"
                    xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right-bold">
                    </use>
                </svg>
            </span>
        </div>
        <div class="f-field f-field--textarea">
            <textarea class="f-field__control" placeholder="How can we help?" required></textarea>
        </div>
        <div class="f-form__action">
            <button class="c-btn c-btn--fluid" type="submit">
                Submit
                <span class="c-btn__icon o-icon-wrapper">
                    <svg class="o-icon o-icon--error">
                        <use xmlns:xlink="http://www.w3.org/1999/xlink"
                        xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right">
                        </use>
                    </svg>
                </span>
            </button>
        </div>
    </form>
</div>

{% include "components/popup.tpl" %}

{% endblock %}
