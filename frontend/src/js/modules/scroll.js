import $ from 'jquery'

const ScrollDown = {
  init: function () {
    const $scrollTrigger = $('.js-scroll-up')
    const $scrollToEl = $('.js-scroll-to')
    const $scrollToElTop = $scrollToEl.offset().top
    const $headerHeight = $('.js-header').outerHeight()
    const $scrollToTop = $scrollToElTop - $headerHeight
    $scrollTrigger.on('click', function (e) {
      e.preventDefault()
      $('html, body').animate({
        scrollTop: $scrollToTop
      }, 500)
    })
  }
}

ScrollDown.init()
