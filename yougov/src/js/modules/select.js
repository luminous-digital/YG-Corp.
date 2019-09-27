import $ from 'jquery'
import 'select2'
import { isStyleguide } from './utils'
import _get from 'lodash/get'
import _forEach from 'lodash/forEach'

const classes = {
  select: 'js-select',
  dropdownParent: 'f-field--select'
}

const selectors = {
  select: `.${classes.select}`,
  dropdownParent: `.${classes.dropdownParent}`
}

const Select = {
  init: function ($selectElements) {
    $selectElements.each(Select.initSelect)
  },

  initSelect () {
    const $select = $(this)
    const $dropdownParent = $select.closest(selectors.dropdownParent)

    $select.select2({
      allowClear: true,
      width: '100%',
      dropdownParent: $dropdownParent,
      minimumResultsForSearch: Infinity
    })
  }
}

if (isStyleguide()) {
  $(window).bind('styleguide:onRendered', function (event) {
    const elements = _get(event, 'detail.elements') || []

    _forEach(elements, element => {
      Select.init(element.querySelectorAll(selectors.select))
    })
  })
} else {
  Select.init($(selectors.select))
}
