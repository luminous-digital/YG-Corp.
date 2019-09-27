import $ from 'jquery'
import { isStyleguide } from './utils'
import _get from 'lodash/get'
import _forEach from 'lodash/forEach'

const classes = {
  customDropdownWrapper: 'js-custom-dropdown-wrapper',
  customDropdownTrigger: 'js-custom-dropdown-trigger',
  isOpened: 'is-opened'
}

const selectors = {
  customDropdownWrapper: `.${classes.customDropdownWrapper}`,
  customDropdownTrigger: `.${classes.customDropdownTrigger}`
}

const CustomDropdown = {
  init ($customDropdownTrigger) {
    if (!$customDropdownTrigger.length) return

    $customDropdownTrigger.on('click', function (e) {
      e.preventDefault()
      const $currentClickedDropdown = $(this)
      const $parentWrapper = $currentClickedDropdown.closest(`${selectors.customDropdownWrapper}`)

      if ($parentWrapper.hasClass(classes.isOpened)) {
        $parentWrapper.removeClass(classes.isOpened)
      } else {
        $(selectors.customDropdownWrapper).removeClass(classes.isOpened)
        $parentWrapper.addClass(classes.isOpened)
      }
    })

    $(document).on('click', function (e) {
      const $container = $(`${selectors.customDropdownWrapper}`)

      if ($container.has(e.target).length === 0) {
        $container.removeClass(`${classes.isOpened}`)
      }
    })
  }
}

if (isStyleguide()) {
  $(window).bind('styleguide:onRendered', function (event) {
    const elements = _get(event, 'detail.elements') || []

    _forEach(elements, element => {
      CustomDropdown.init(element.querySelectorAll(selectors.customDropdownTrigger))
    })
  })
} else {
  CustomDropdown.init($(selectors.customDropdownTrigger))
}
