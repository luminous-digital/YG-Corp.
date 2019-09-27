import _forEach from 'lodash/forEach'

const classes = {
  menuOpenTrigger: 'js-menu-open-trigger',
  isMenuOpened: 'is-menu-opened',
  isOpened: 'is-opened',
  isSearchOpened: 'is-search-opened',
  isSubNavOpened: 'is-sub-nav-opened',
  subNavBox: 'c-sub-nav-box'
}

const selectors = {
  menuOpenTrigger: `.${classes.menuOpenTrigger}`,
  subNavBox: `.${classes.subNavBox}`
}

const ToggleMenu = {
  init (menuOpenTrigger) {
    if (!menuOpenTrigger) return

    const subNavItems = document.querySelectorAll(selectors.subNavBox)

    menuOpenTrigger.addEventListener('click', function (e) {
      e.preventDefault()
      document.body.classList.toggle(classes.isMenuOpened)
      if (document.body.classList.contains(classes.isSearchOpened)) {
        document.body.classList.remove(classes.isSearchOpened)
      }
      if (document.body.classList.contains(classes.isSubNavOpened)) {
        document.body.classList.remove(classes.isSubNavOpened)
        _forEach(subNavItems, item => {
          item.classList.remove(classes.isOpened)
        })
      }
    })
  }
}

ToggleMenu.init(document.querySelector(selectors.menuOpenTrigger))
