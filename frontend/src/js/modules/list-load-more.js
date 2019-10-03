import $ from 'jquery'

const classes = {
  searchList: 'js-search-list',
  searchListItem: 'c-list__item',
  listLoadMore: 'js-list-load-more',
  isVisible: 'is-visible'
}

const selectors = {
  searchList: `.${classes.searchList}`,
  searchListItem: `.${classes.searchList} .${classes.searchListItem}`,
  listLoadMore: `.${classes.listLoadMore}`
}

const ListLoadMore = {
  init: function () {
    const $lists = $(selectors.searchList)

    if (!$lists) return
    const $listItems = $(selectors.searchListItem)
    const $loadMoreBtn = $(selectors.listLoadMore)
    let elementsToShow = 10
    const listItemsSize = $listItems.length

    $loadMoreBtn.on('click', function () {
      elementsToShow = (elementsToShow + 10 <= listItemsSize) ? elementsToShow + 10 : listItemsSize
      $(`${selectors.searchListItem}:lt(${elementsToShow})`).addClass(classes.isVisible)
      if (elementsToShow === listItemsSize) {
        $loadMoreBtn.hide()
      }
    })
  }
}

ListLoadMore.init()
