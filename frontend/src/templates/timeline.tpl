{% extends "base/base.tpl" %}
{% block title %}
    Timeline
{% endblock %}
{% set active_no = '' %}
{% set active_subnav_no = '' %}
{% block content %}
<section class="l-heading">
    <div class="c-heading">
        <h1 class="c-heading__title t-headline-2">
            Timeline
        </h1>
    </div>
</section>

<div class="l-inner">
    <div class="l-timeline js-timeline">
        <div class="l-timeline__col l-timeline__col--fixed js-timeline--col">
            <div class="c-counter-box">
                <p class="c-counter-box__number js-timeline-number-panel" id="countup-panel">
                    7,000,000
                </p>
                <p class="c-counter-box__desc">
                    panel members
                </p>
                <p class="c-counter-box__number js-timeline-number-employees" id="countup-employees">
                    7,000
                </p>
                <p class="c-counter-box__desc">
                    employees
                </p>
                <p class="c-counter-box__number js-timeline-number-offices" id="countup-offices">
                    900
                </p>
                <p class="c-counter-box__desc">
                    offices
                </p>
            </div>
        </div>
        <div class="l-timeline__col l-timeline__col--margin-top">
            <ul class="c-timeline-list">
                <li class="c-timeline-list__item" data-panel='102340' data-employees='202340' data-offices='3002'>
                    <div class="c-timeline-box">
                        <div class="c-timeline-box__heading t-headline-2">2000</div>
                        <div class="c-timeline-box__content c-wysiwyg c-wysiwyg--small">
                            <p>
                                YouGov is established as the pioneer of internet-based market research.
                            </p>
                            <p>
                                The company is co-founded by Stephan Shakespeare and Nadhim Zahawi, who first met while working in British politics.
                            </p>
                            <p>
                                The official company registration name is YouGov Dot Com Limited.
                            </p>
                            <p>
                                Shakespeare is named Chief Innovations Officer while Zahawi is Chief Executive Officer.
                            </p>
                        </div>
                    </div>
                </li>
                <li class="c-timeline-list__item" data-panel='22340' data-employees='3023430' data-offices='40230'>
                    <div class="c-timeline-box">
                        <div class="c-timeline-box__heading t-headline-2">2000</div>
                        <div class="c-timeline-box__content c-wysiwyg c-wysiwyg--small">
                            <p>
                                YouGov is established as the pioneer of internet-based market research.
                            </p>
                            <p>
                                The company is co-founded by Stephan Shakespeare and Nadhim Zahawi, who first met while working in British politics.
                            </p>
                            <p>
                                The official company registration name is YouGov Dot Com Limited.
                            </p>
                            <p>
                                Shakespeare is named Chief Innovations Officer while Zahawi is Chief Executive Officer.
                            </p>
                        </div>
                    </div>
                </li>
                <li class="c-timeline-list__item" data-panel='4023420' data-employees='503240' data-offices='63400'>
                    <div class="c-timeline-box">
                        <div class="c-timeline-box__heading t-headline-2">2000</div>
                        <div class="c-timeline-box__content c-wysiwyg c-wysiwyg--small">
                            <p>
                                YouGov is established as the pioneer of internet-based market research.
                            </p>
                            <p>
                                The company is co-founded by Stephan Shakespeare and Nadhim Zahawi, who first met while working in British politics.
                            </p>
                            <p>
                                The official company registration name is YouGov Dot Com Limited.
                            </p>
                            <p>
                                Shakespeare is named Chief Innovations Officer while Zahawi is Chief Executive Officer.
                            </p>
                            <img src="./static/img/pic-timeline-map.jpg" alt="Map">
                        </div>
                    </div>
                </li>
                <li class="c-timeline-list__item" data-panel='7020' data-employees='800' data-offices='90230'>
                    <div class="c-timeline-box">
                        <div class="c-timeline-box__heading t-headline-2">2000</div>
                        <div class="c-timeline-box__content c-wysiwyg c-wysiwyg--small">
                            <p>
                                YouGov is established as the pioneer of internet-based market research.
                            </p>
                            <p>
                                The company is co-founded by Stephan Shakespeare and Nadhim Zahawi, who first met while working in British politics.
                            </p>
                            <p>
                                The official company registration name is YouGov Dot Com Limited.
                            </p>
                            <p>
                                Shakespeare is named Chief Innovations Officer while Zahawi is Chief Executive Officer.
                            </p>
                            <img src="./static/img/img-news-4.jpg" alt="Pic">
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</div>

{% include "layout/contact-module.tpl" %}

{% endblock %}
