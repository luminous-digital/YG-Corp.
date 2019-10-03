import { isStyleguide } from './utils'
import _get from 'lodash/get'
import _forEach from 'lodash/forEach'

const classes = {
  searchToggler: 'js-search-toggler',
  searchForm: 'f-search-form',
  input: 'f-field__control',
  isSearchOpened: 'is-search-opened'
}

const selectors = {
  searchToggler: `.${classes.searchToggler}`,
  input: `.${classes.searchForm} .${classes.input}`
}

const ToggleSearch = {
  init (searchToggler) {
    const input = document.querySelector(selectors.input)

    if (!searchToggler) return

    searchToggler.addEventListener('click', function (e) {
      e.preventDefault()
      document.body.classList.toggle(classes.isSearchOpened)
    })

    input.addEventListener('focus', function () {
      document.body.classList.add(classes.isSearchOpened)
    })
  }
}

if (isStyleguide()) {
  window.addEventListener('styleguide:onRendered', event => {
    const elements = _get(event, 'detail.elements') || []

    _forEach(elements, element => {
      ToggleSearch.init(element.querySelector(selectors.searchToggler))
    })
  })
} else {
  ToggleSearch.init(document.querySelector(selectors.searchToggler))
}
