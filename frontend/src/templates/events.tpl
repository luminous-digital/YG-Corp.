{% extends "base/base.tpl" %}
{% block title %}
    Events
{% endblock %}
{% block bodyClass %}has-subnav{% endblock %}
{% set active_no = '' %}
{% set active_subnav_no = '' %}
{% block content %}

{% include "layout/event-calendar.tpl" %}

{% endblock %}
