import $ from 'jquery'
import 'parsleyjs'
import { isStyleguide } from './utils'
import _get from 'lodash/get'
import _forEach from 'lodash/forEach'

import { PopUp } from './pop-up'

export const AJAX_FORM_ON_SUCCESS_EVENT = 'AJAX_FORM_ON_SUCCESS_EVENT'
export const AJAX_FORM_ON_FAIL_EVENT = 'AJAX_FORM_ON_FAIL_EVENT'

const classes = {
  form: 'js-form',
  ajaxForm: 'js-ajax-form',
  select: 'js-select',
  isVisible: 'is-visible',
  formSucces: 'c-form-info--success',
  formError: 'c-form-info--error'
}

const selectors = {
  form: `.${classes.form}`,
  ajaxForm: `.${classes.ajaxForm}`,
  select: `.${classes.select}`,
  isVisible: `.${classes.isVisible}`,
  formSucces: `.${classes.formSucces}`,
  formError: `.${classes.formError}`
}

const Validation = {
  init: function () {
    $(selectors.form).parsley()
    $('body').on('submit', selectors.ajaxForm, Validation.onSubmit)
    $(selectors.select).change(function () {
      $(selectors.select).trigger('input')
    })
  },
  onSubmit (event) {
    event.preventDefault()

    const $form = $(this)
    const url = $form.attr('action')
    const method = ($form.attr('method') || 'post').toUpperCase()
    const data = $form.serialize()

    $.ajax({
      method,
      data,
      url
    }).done((...args) => {
      $form.trigger(AJAX_FORM_ON_SUCCESS_EVENT, ...args)
      PopUp.openPopUp()
      $(selectors.formSucces).addClass(classes.isVisible)
    }).fail((...args) => {
      $form.trigger(AJAX_FORM_ON_FAIL_EVENT, ...args)
      PopUp.openPopUp()
      $(selectors.formError).addClass(classes.isVisible)
    })
  }
}

if (isStyleguide()) {
  $(window).bind('styleguide:onRendered', function (event) {
    const elements = _get(event, 'detail.elements') || []

    _forEach(elements, element => {
      Validation.init(element.querySelectorAll(selectors.form))
    })
  })
} else {
  Validation.init($(selectors.form))
}
