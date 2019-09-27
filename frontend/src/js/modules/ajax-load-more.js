import $ from 'jquery'
import { isStyleguide } from './utils'

const classes = {
  loadMoreTrigger: 'js-ajax-load-more-trigger',
  loadMoreContainer: 'js-ajax-load-more-container',
  loadMoreList: 'js-ajax-load-more-list',
  isLoading: 'is-loading'
}

const selectors = {
  loadMoreTrigger: `.${classes.loadMoreTrigger}`,
  loadMoreContainer: `.${classes.loadMoreContainer}`,
  loadMoreList: `.${classes.loadMoreList}`
}

const AjaxLoadMore = {
  init () {
    const $loadMoreTrigger = $(selectors.loadMoreTrigger)
    const $loadMoreContainer = $(selectors.loadMoreContainer)

    $loadMoreTrigger.on('click', function (e) {
      e.preventDefault()
      const $loadMore = $(this)
      const url = $loadMore.attr('data-href')

      $loadMoreContainer.addClass(classes.isLoading)

      $.ajax({
        url,
        headers: {
          // Proxies request in development mode
          'Should-Proxy-Request': true
        }
      }).done(data => {
        const {
          // eslint-disable-next-line
          next_url,
          html
        } = data

        $(selectors.loadMoreList).append(html)

        // eslint-disable-next-line
        if (next_url) {
          // eslint-disable-next-line
          $loadMoreTrigger.attr('data-href', next_url)
        } else {
          $loadMoreTrigger.remove()
        }
      }).fail(() => {
        console.log('fail')
      }).always(() => {
        $loadMoreContainer.removeClass(classes.isLoading)
      })
    })
  }
}

if (!isStyleguide()) {
  AjaxLoadMore.init()
}
