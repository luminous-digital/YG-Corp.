"""Richtext hooks."""
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    InlineStyleElementHandler
)
from wagtail.core import hooks

@hooks.register("register_rich_text_features")
def register_lefttext_feature(features):
    """Creates centered text in our richtext editor and page."""

    # Step 1
    feature_name = "left"
    type_ = "LEFTTEXT"
    tag = "dl"

    # Step 2
    control = {
        "type": type_,
        "label": "Left",
        "description": "Left Text",
        "style": {
            "display": "block",
            "text-align": "left",
        },
    }

    # Step 3
    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )

    # Step 4
    db_conversion = {
        "from_database_format": {tag: InlineStyleElementHandler(type_)},
        "to_database_format": {
            "style_map": {
                type_: {
                    "element": tag,
                    "props": {
                        "style": "text-align: left;"
                    }
                }
            }
        }
    }

    # Step 5
    features.register_converter_rule("contentstate", feature_name, db_conversion)

    # Step 6
    features.default_features.append(feature_name)


@hooks.register("register_rich_text_features")
def register_centertext_feature(features):
    """Creates centered text in our richtext editor and page."""

    # Step 1
    feature_name = "center"
    type_ = "CENTERTEXT"
    tag = "dt"

    # Step 2
    control = {
        "type": type_,
        "label": "Center",
        "description": "Center Text",
        "style": {
            "display": "block",
            "text-align": "center",
        },
    }

    # Step 3
    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )

    # Step 4
    db_conversion = {
        "from_database_format": {tag: InlineStyleElementHandler(type_)},
        "to_database_format": {
            "style_map": {
                type_: {
                    "element": tag,
                    "props": {
                        "style": "text-align: center;"
                    }
                }
            }
        }
    }

    # Step 5
    features.register_converter_rule("contentstate", feature_name, db_conversion)

    # Step 6
    features.default_features.append(feature_name)


@hooks.register("register_rich_text_features")
def register_righttext_feature(features):
    """Creates centered text in our richtext editor and page."""

    # Step 1
    feature_name = "right"
    type_ = "RIGHTTEXT"
    tag = "dd"

    # Step 2
    control = {
        "type": type_,
        "label": "Right",
        "description": "Right Text",
        "style": {
            "display": "block",
            "text-align": "right",
        },
    }

    # Step 3
    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )

    # Step 4
    db_conversion = {
        "from_database_format": {tag: InlineStyleElementHandler(type_)},
        "to_database_format": {
            "style_map": {
                type_: {
                    "element": tag,
                    "props": {
                        "style": "text-align: right;"
                    }
                }
            }
        }
    }

    # Step 5
    features.register_converter_rule("contentstate", feature_name, db_conversion)

    # Step 6
    features.default_features.append(feature_name)
