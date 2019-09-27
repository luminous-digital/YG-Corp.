import $ from 'jquery'

const classes = {
  isStickyHeader: 'is-sticky-header',
  isNotStickyHeader: 'is-not-sticky-header'
}

const HeaderScroll = {
  $body: $(document.body),

  init () {
    let lastScrollTop = 0
    $(window).on('scroll', function () {
      const headerHeight = $('.l-header').outerHeight()
      let currentScrollPosition = $(this).scrollTop()
      if (currentScrollPosition > lastScrollTop && (currentScrollPosition > headerHeight)) {
        HeaderScroll.$body.removeClass(classes.isStickyHeader)
        HeaderScroll.$body.addClass(classes.isNotStickyHeader)
      } else {
        HeaderScroll.$body.addClass(classes.isStickyHeader)
        HeaderScroll.$body.removeClass(classes.isNotStickyHeader)
      }
      lastScrollTop = currentScrollPosition
    })
  }
}

HeaderScroll.init()
