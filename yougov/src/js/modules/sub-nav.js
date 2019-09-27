import $ from 'jquery'

const classes = {
  subNavOpenTrigger: 'js-sub-nav-open-trigger',
  subNavCloseTrigger: 'js-sub-nav-close-trigger',
  subNavBox: 'c-sub-nav-box',
  navItem: 'c-nav__item',
  isOpened: 'is-opened',
  isSubNavOpened: 'is-sub-nav-opened',
  isSearchOpened: 'is-search-opened'
}

const selectors = {
  subNavOpenTrigger: `.${classes.subNavOpenTrigger}`,
  subNavCloseTrigger: `.${classes.subNavCloseTrigger}`,
  subNavBox: `.${classes.subNavBox}`,
  navItem: `.${classes.navItem}`,
  body: 'body',
  subNavBoxOpened: `.${classes.subNavBox}.${classes.isOpened}`
}

const SubNav = {
  $body: $(document.body),

  init () {
    $(selectors.subNavOpenTrigger).on('click', SubNav.onNavItemClick)
    $(selectors.subNavCloseTrigger).on('click', SubNav.onMainMenuClick)
  },

  onNavItemClick (e) {
    e.preventDefault()

    const $clickedNavItem = $(this)
    const $clickedNavItemWrapper = $clickedNavItem.closest(selectors.navItem)
    const navItemHash = $clickedNavItem.attr('href')
    const currentlyOpenedNavHash = $(selectors.subNavBoxOpened).attr('id')
    const currentlyOpenedNavSelector = `#${currentlyOpenedNavHash}`

    if (currentlyOpenedNavHash === undefined) {
      const $navBoxToOpen = $(navItemHash)

      $navBoxToOpen.addClass(classes.isOpened)
      $clickedNavItemWrapper.addClass(classes.isOpened)
      SubNav.$body.addClass(classes.isSubNavOpened)

      return
    }

    if (navItemHash === currentlyOpenedNavSelector) {
      const $navBoxToClose = $(currentlyOpenedNavSelector)

      $navBoxToClose.removeClass(classes.isOpened)
      $clickedNavItemWrapper.removeClass(classes.isOpened)
      SubNav.$body.removeClass(classes.isSubNavOpened)

      return
    }

    const $navBoxToClose = $(currentlyOpenedNavSelector)
    const $navBoxToOpen = $(navItemHash)
    const $navItemToDeactivateWrapper = $(`[href="${currentlyOpenedNavSelector}"]`)
      .closest(selectors.navItem)

    $navBoxToClose.removeClass(classes.isOpened)
    $navItemToDeactivateWrapper.removeClass(classes.isOpened)

    $navBoxToOpen.addClass(classes.isOpened)
    $clickedNavItemWrapper.addClass(classes.isOpened)
  },

  onMainMenuClick (e) {
    e.preventDefault()

    $(this).closest(selectors.subNavBox).removeClass(classes.isOpened)
    $(selectors.navItem).removeClass(classes.isOpened)
    SubNav.$body.removeClass(`${classes.isSubNavOpened} ${classes.isSearchOpened}`)
  }
}

SubNav.init()
