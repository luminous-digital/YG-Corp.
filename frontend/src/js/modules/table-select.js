import _forEach from 'lodash/forEach'
import _get from 'lodash/get'
import $ from 'jquery'
import { isStyleguide } from './utils'

const classes = {
  isHidden: 'is-hidden',
  isActive: 'is-active',
  isOpened: 'is-opened',
  mainContainer: 'js-main-container',
  tabsOpen: 'js-tabs-open',
  mainTabPlaceholder: 'js-main-tab-placeholder',
  mainTabsNav: 'js-main-tabs-nav',
  tabClearFilter: 'js-tab-clear-filter',
  tableContent: 'js-table-content'
}

const selectors = {
  dataTab: '*[data-tab]',
  isActive: `.${classes.isActive}`,
  mainContainer: `.${classes.mainContainer}`,
  tabsOpen: `.${classes.tabsOpen}`,
  mainTabPlaceholder: `.${classes.mainTabPlaceholder}`,
  mainTabsNav: `.${classes.mainTabsNav} > li:not(.${classes.tabClearFilter})`,
  tabClearFilter: `.${classes.tabClearFilter}`,
  tableContent: `.${classes.tableContent}`,
  tableItems: `.${classes.tableContent} > div`
}

const TableSelect = {
  init (mainContainer) {
    if (!mainContainer) return

    const $mainContainer = $(mainContainer)
    const $navToggleButton = $mainContainer.find(selectors.tabsOpen)
    const $filterButtons = $mainContainer.find(selectors.mainTabsNav)
    const $tabItemsContainer = $mainContainer.find(selectors.tableContent)
    const $tabClearFilterButton = $mainContainer.find(selectors.tabClearFilter)
    const $placeholderTextContainer = $mainContainer.find(selectors.mainTabPlaceholder)

    // Create container for filtered out items
    const $hiddenItemsContainer = $('<div/>', {
      style: 'display: none'
    })
    const $tableItems = $mainContainer
      .find(selectors.tableItems)

    $tableItems.each((index, item) => {
      $(item).attr('data-index', index)
    })
    $mainContainer.append($hiddenItemsContainer)

    $navToggleButton.on('click', TableSelect.onNavToggleClick($mainContainer))
    $filterButtons.on('click', TableSelect.onFilterButtonClick(
      $mainContainer,
      $tabItemsContainer,
      $hiddenItemsContainer,
      $placeholderTextContainer
    ))
    $tabClearFilterButton.on('click', TableSelect.ontabClearFilterButtonClick(
      $mainContainer,
      $tabItemsContainer,
      $hiddenItemsContainer,
      $placeholderTextContainer
    ))
  },

  onNavToggleClick: $mainContainer => function () {
    $mainContainer.toggleClass(classes.isOpened)
  },

  ontabClearFilterButtonClick: (
    $mainContainer,
    $tabItemsContainer,
    $hiddenItemsContainer,
    $placeholderTextContainer
  ) => function () {
    $mainContainer.removeClass(classes.isOpened)

    const $tabClearFiltersButton = $(this)
    const isActive = $tabClearFiltersButton.hasClass(classes.isActive)
    const placeholderText = $tabClearFiltersButton.text()

    if (isActive) return

    $placeholderTextContainer.text(placeholderText)

    $mainContainer
      .find(selectors.isActive)
      .removeClass(classes.isActive)

    $tabClearFiltersButton.addClass(classes.isActive)
    $tabItemsContainer.append($hiddenItemsContainer.children())

    // Reorder
    const $items = $tabItemsContainer.children()

    TableSelect.reorderItems($items)

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
    const $itemsToHide = $tabItemsContainer.find(`div.c-downloads-table__content[data-tab!="${filterValue}"]`)

    // Throw them into hidden container
    $hiddenItemsContainer.append($itemsToHide)

    $mainContainer
      .find(selectors.isActive)
      .removeClass(classes.isActive)

    $clickedFilterItem.addClass(classes.isActive)

    // Reorder
    const $items = $tabItemsContainer.children()

    TableSelect.reorderItems($items)

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
      TableSelect.init(element.querySelector(selectors.mainContainer))
    })
  })
} else {
  TableSelect.init(document.querySelector(selectors.mainContainer))
}
