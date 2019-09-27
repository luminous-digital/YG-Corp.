<html lang="en" class="no-js">
    <head>
        <meta charset="utf-8">
        <title>{% block title %} {{ title }} {% endblock %}</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
        {% include "base/head-links.tpl" %}
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=UA-144777637-1"></script>
        <script>
            window.GAID = 'UA-144777637-1';
            window.googleAPIKey = 'AIzaSyCxcJDx-yRo1eDiFXzzZS8tFR5hN_4SRz4';
        </script>
    </head>
    <body class="{% block bodyClass %}{% endblock %}">
        {% import "layout/header.tpl" as l_header %}
        {{ l_header.render(active_no, active_subnav_no) }}
        <main class="l-main js-scroll-to">
            {% block content %}
                <div class="l-inner">
                    <h1>This is default content</h1>
                </div>
            {% endblock %}
        </main>
        {% import "layout/footer.tpl" as l_footer %}
        {{ l_footer.render() }}
        {% import "components/search-modal.tpl" as l_modal %}
        {{ l_modal.render() }}
        <script src="./static/js/app.js"></script>
    </body>
</html>
