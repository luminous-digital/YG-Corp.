import $ from 'jquery'
import { isStyleguide } from './utils'
import _get from 'lodash/get'
import _forEach from 'lodash/forEach'

const classes = {
  accordion: 'js-accordion',
  toggleAccordion: 'js-toggle-accordion',
  isOpened: 'is-opened'
}

const selectors = {
  accordion: `.${classes.accordion}`,
  toggleAccordion: `.${classes.toggleAccordion}`
}

const ToggleAccordion = {
  init ($accordion) {
    if (!$accordion.length) return

    $(selectors.toggleAccordion).on('click', function (e) {
      e.preventDefault()

      const $clickedButton = $(this)
      const $clikedButtonWrapper = $clickedButton.closest(selectors.accordion)

      if ($clikedButtonWrapper.hasClass(classes.isOpened)) {
        $clikedButtonWrapper.removeClass(classes.isOpened)
      } else {
        $(selectors.accordion).removeClass(classes.isOpened)
        $clikedButtonWrapper.addClass(classes.isOpened)
      }
    })
  }
}

if (isStyleguide()) {
  $(window).bind('styleguide:onRendered', function (event) {
    const elements = _get(event, 'detail.elements') || []

    _forEach(elements, element => {
      ToggleAccordion.init(element.querySelectorAll(selectors.accordion))
    })
  })
} else {
  ToggleAccordion.init($(selectors.accordion))
}
