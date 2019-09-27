{% extends "base/base.tpl" %}
{% block title %}
    Full rich text
{% endblock %}
{% set active_no = '' %}
{% set active_subnav_no = '' %}
{% block content %}

<div class="l-real-text">
    <div class="l-inner l-inner--small">
        <div class="c-wysiwyg">
            <div class="rich-text">
                <h1>Headline H1</h1>
                <h2>Headline H2</h2>
                <h3>Headline H3</h3>
                <h4>Headline H4</h4>
                <h5>Headline H5</h5>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc hendrerit felis quis elit imperdiet tristique. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam nec lobortis tellus. Aliquam erat volutpat. Phasellus in maximus dui, sit amet fringilla dui. Pellentesque volutpat, arcu a viverra venenatis, nulla nisi facilisis ipsum, imperdiet viverra diam tellus at odio. Mauris lacinia, orci id finibus dictum, justo libero tristique elit, sit amet euismod urna ipsum sit amet diam. Nam facilisis quam quis pulvinar lacinia. Duis id dignissim diam.
                </p>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc hendrerit felis quis elit imperdiet tristique. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam nec lobortis tellus. Aliquam erat volutpat. Phasellus in maximus dui, sit amet fringilla dui. Pellentesque volutpat, arcu a viverra venenatis, nulla nisi facilisis ipsum, imperdiet viverra diam tellus at odio. Mauris lacinia, orci id finibus dictum, justo libero tristique elit, sit amet euismod urna ipsum sit amet diam. Nam facilisis quam quis pulvinar lacinia. Duis id dignissim diam.
                </p>
            </div>
        </div>
    </div>
</div>
<div class="l-quote">
    <div class="c-quote" style="color: #00B7B4;">
        <h4 class="c-quote__author t-headline-4 t-bold">
            Name Surname
        </h4>
        <h5 class="c-quote__position t-headline-5">
            Edison Investment Research
        </h5>
        <h2 class="c-quote__quotation t-headline-2">
            Access to permissioned data is a key differentiator, allowing for faster responses and increased automation and efficiency.
        </h2>
        <div class="c-quote__action">
            <a href="#" class="c-underline-link {$modifiers}" target="_blank">
                Find out more
                <span class="c-underline-link__icon o-icon-wrapper">
                    <svg class="o-icon o-icon--arrow-right">
                        <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right"></use>
                    </svg>
                </span>
            </a>
        </div>
    </div>
</div>
<div class="l-real-text">
    <div class="l-inner l-inner--small">
        <div class="c-wysiwyg">
            <figure>
                <img src="./static/img//pic_person_1.jpg" alt="pic"/>
                <figcaption>
                    Caption text goes here. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Lorem ipsum dolor sit amet, consecte
                </figcaption>
            </figure>
        </div>
    </div>
</div>
<div class="l-quote">
    <div class="c-quote" style="color: #00B7B4;">
        <h4 class="c-quote__author t-headline-4 t-bold">
            Name Surname
        </h4>
        <h5 class="c-quote__position t-headline-5">
            Edison Investment Research
        </h5>
        <h2 class="c-quote__quotation t-headline-2">
            Access to permissioned data is a key differentiator, allowing for faster responses and increased automation and efficiency.
        </h2>
        <div class="c-quote__action">
            <a href="#" class="c-underline-link {$modifiers}" target="_blank">
                Find out more
                <span class="c-underline-link__icon o-icon-wrapper">
                    <svg class="o-icon o-icon--arrow-right">
                        <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="./static/svg/symbol/svg/sprite.symbol.svg#icon-arrow-right"></use>
                    </svg>
                </span>
            </a>
        </div>
    </div>
</div>
<div class="l-real-text">
    <div class="l-inner l-inner--small">
        <div class="c-wysiwyg">
            <div class="rich-text">
                <h1>Headline H1</h1>
                <h2>Headline H2</h2>
                <h3>Headline H3</h3>
                <h4>Headline H4</h4>
                <h5>Headline H5</h5>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc hendrerit felis quis elit imperdiet tristique. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam nec lobortis tellus. Aliquam erat volutpat. Phasellus in maximus dui, sit amet fringilla dui. Pellentesque volutpat, arcu a viverra venenatis, nulla nisi facilisis ipsum, imperdiet viverra diam tellus at odio. Mauris lacinia, orci id finibus dictum, justo libero tristique elit, sit amet euismod urna ipsum sit amet diam. Nam facilisis quam quis pulvinar lacinia. Duis id dignissim diam.
                </p>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc hendrerit felis quis elit imperdiet tristique. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam nec lobortis tellus. Aliquam erat volutpat. Phasellus in maximus dui, sit amet fringilla dui. Pellentesque volutpat, arcu a viverra venenatis, nulla nisi facilisis ipsum, imperdiet viverra diam tellus at odio. Mauris lacinia, orci id finibus dictum, justo libero tristique elit, sit amet euismod urna ipsum sit amet diam. Nam facilisis quam quis pulvinar lacinia. Duis id dignissim diam.
                </p>
            </div>
        </div>
    </div>
</div>

{% endblock %}
