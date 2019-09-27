import _forEach from 'lodash/forEach'
import _get from 'lodash/get'
import $ from 'jquery'
import { isStyleguide } from './utils'

const classes = {
  isHidden: 'is-hidden',
  isActive: 'is-active',
  isOpened: 'is-opened',
  tabsOpenTrigger: 'js-tabs-open-trigger',
  tabsNav: 'js-tabs-nav',
  tabsContent: 'js-tabs-content',
  tabsContainer: 'js-tabs-container',
  tabsPlaceholder: 'js-tabs-placeholder',
  tabsContentList: 'c-tabs__content-list',
  clearFilter: 'js-clear-filter'
}

const selectors = {
  tabsOpenTrigger: `.${classes.tabsOpenTrigger}`,
  tabsNav: `.${classes.tabsNav} > li:not(.${classes.clearFilter})`,
  tabsListItems: `.${classes.tabsContent} .${classes.tabsContentList} > li`,
  tabsContentList: `.${classes.tabsContent} .${classes.tabsContentList}`,
  tabsContent: `.${classes.tabsContent}`,
  tabsContainer: `.${classes.tabsContainer}`,
  dataTab: '*[data-tab]',
  tabsPlaceholder: `.${classes.tabsPlaceholder}`,
  isActive: `.${classes.isActive}`,
  clearFilter: `.${classes.clearFilter}`
}

const TabSelect = {
  init (mainContainer) {
    if (!mainContainer) return

    const $mainContainer = $(mainContainer)
    const $navToggleButton = $mainContainer.find(selectors.tabsOpenTrigger)
    const $filterButtons = $mainContainer.find(selectors.tabsNav)
    const $tabItemsContainer = $mainContainer.find(selectors.tabsContentList)
    const $clearFilterButton = $mainContainer.find(selectors.clearFilter)
    const $placeholderTextContainer = $mainContainer.find(selectors.tabsPlaceholder)

    // Create container for filtered out items
    const $hiddenItemsContainer = $('<ul/>', {
      style: 'display: none'
    })
    const $tabsListItems = $mainContainer
      .find(selectors.tabsListItems)

    $tabsListItems.each((index, item) => {
      $(item).attr('data-index', index)
    })
    $mainContainer.append($hiddenItemsContainer)

    $navToggleButton.on('click', TabSelect.onNavToggleClick($mainContainer))
    $filterButtons.on('click', TabSelect.onFilterButtonClick(
      $mainContainer,
      $tabItemsContainer,
      $hiddenItemsContainer,
      $placeholderTextContainer
    ))
    $clearFilterButton.on('click', TabSelect.onClearFilterButtonClick(
      $mainContainer,
      $tabItemsContainer,
      $hiddenItemsContainer,
      $placeholderTextContainer
    ))
  },

  onNavToggleClick: $mainContainer => function () {
    $mainContainer.toggleClass(classes.isOpened)
  },

  onClearFilterButtonClick: (
    $mainContainer,
    $tabItemsContainer,
    $hiddenItemsContainer,
    $placeholderTextContainer
  ) => function () {
    $mainContainer.removeClass(classes.isOpened)

    const $clearFiltersButton = $(this)
    const isActive = $clearFiltersButton.hasClass(classes.isActive)
    const placeholderText = $clearFiltersButton.text()

    if (isActive) return

    $placeholderTextContainer.text(placeholderText)

    $mainContainer
      .find(selectors.isActive)
      .removeClass(classes.isActive)

    $clearFiltersButton.addClass(classes.isActive)
    $tabItemsContainer.append($hiddenItemsContainer.children())

    // Reorder
    const $items = $tabItemsContainer.children()

    TabSelect.reorderItems($items)

    $tabItemsContainer.append($items)
  },

  onFilterButtonClick: (
    $mainContainer,
    $tabItemsContainer,
    $hiddenItemsContainer,
    $placeholderTextContainer
  ) => function () {
    $mainContainer.removeClass(classes.isOpened)

    const $clickedFilterItem = $(this)
    const filterValue = $clickedFilterItem.attr('data-tab')
    const isFilterActive = $clickedFilterItem.hasClass(classes.isActive)
    const placeholderText = $clickedFilterItem.text()

    if (isFilterActive) return

    $placeholderTextContainer.text(placeholderText)

    // Throw all the items from hidden container into the list
    $tabItemsContainer.append($hiddenItemsContainer.children())

    // Select the ones which should be hidden
    const $itemsToHide = $tabItemsContainer.find(`li.c-tabs__content-item[data-tab!="${filterValue}"]`)

    // Throw them into hidden container
    $hiddenItemsContainer.append($itemsToHide)

    $mainContainer
      .find(selectors.isActive)
      .removeClass(classes.isActive)

    $clickedFilterItem.addClass(classes.isActive)

    // Reorder
    const $items = $tabItemsContainer.children()

    TabSelect.reorderItems($items)

    $tabItemsContainer.append($items)
  },

  reorderItems ($items) {
    $items
      .detach()
      .sort((itemA, itemB) => {
        const itemAIndex = Number($(itemA).attr('data-index'))
        const itemBIndex = Number($(itemB).attr('data-index'))

        return itemAIndex - itemBIndex
      })
  }
}

if (isStyleguide()) {
  window.addEventListener('styleguide:onRendered', event => {
    const elements = _get(event, 'detail.elements') || []

    _forEach(elements, element => {
      TabSelect.init(element.querySelector(selectors.tabsContainer))
    })
  })
} else {
  TabSelect.init(document.querySelector(selectors.tabsContainer))
}
