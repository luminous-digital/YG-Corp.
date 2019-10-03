import $ from 'jquery'
import imagesLoaded from 'imagesloaded'
import { isStyleguide } from './utils'
import _get from 'lodash/get'
import _forEach from 'lodash/forEach'

const classes = {
  stickyContent: 'l-timeline__col--fixed',
  header: 'js-header',
  timeline: 'js-timeline',
  timelineCol: 'js-timeline--col',
  isSticky: 'is-sticky',
  isAbsolute: 'is-absolute'
}

const selectors = {
  stickyContent: `.${classes.stickyContent}`,
  header: `.${classes.header}`,
  timeline: `.${classes.timeline}`,
  timelineCol: `.${classes.timelineCol}`
}

const Sticky = {
  init () {
    if (!$(selectors.timeline).length) return
    let timelineNumbersHeight = $(selectors.stickyContent).outerHeight()
    let headerHeight = $(selectors.header).outerHeight()
    let timelinePosition = $(selectors.timeline).offset().top
    let timelineHeight = $(selectors.timeline).outerHeight()
    let deviceWidth = $(window).width()
    let lastScrollTop = 0

    $(window).on('scroll', function () {
      let scrollDistance = $(document).scrollTop()
      deviceWidth = $(window).width()
      let currentScrollPosition = $(this).scrollTop()

      if (deviceWidth < '767') {
        if (currentScrollPosition > lastScrollTop) {
          if (scrollDistance >= timelinePosition) {
            $(selectors.timelineCol).addClass(classes.isSticky)
            $(selectors.timelineCol).removeClass(classes.isAbsolute)
            $(selectors.stickyContent).css({
              top: '0',
              transition: 'all .3s ease'
            })
          } else {
            $(selectors.timelineCol).removeClass(classes.isSticky)
            $(selectors.timelineCol).removeClass(classes.isAbsolute)
            $(selectors.stickyContent).css({
              top: '0',
              transition: 'all .45s ease'
            })
          }
          if (scrollDistance > timelinePosition + timelineHeight - timelineNumbersHeight) {
            $(selectors.timelineCol).removeClass(classes.isSticky)
            $(selectors.timelineCol).addClass(classes.isAbsolute)
            $(selectors.stickyContent).css({
              top: 'auto'
            })
          }
        } else {
          if (scrollDistance >= timelinePosition - headerHeight) {
            $(selectors.timelineCol).addClass(classes.isSticky)
            $(selectors.timelineCol).removeClass(classes.isAbsolute)
            $(selectors.stickyContent).css({
              top: headerHeight,
              transition: 'all .6s ease'
            })
          } else {
            $(selectors.timelineCol).removeClass(classes.isSticky)
            $(selectors.timelineCol).removeClass(classes.isAbsolute)
            $(selectors.stickyContent).css({
              top: '0',
              transition: 'none'
            })
          }
          if (scrollDistance > timelinePosition + timelineHeight - timelineNumbersHeight - headerHeight) {
            $(selectors.timelineCol).removeClass(classes.isSticky)
            $(selectors.timelineCol).addClass(classes.isAbsolute)
            $(selectors.stickyContent).css({
              top: 'auto'
            })
          }
        }
        lastScrollTop = currentScrollPosition
      }
      if (deviceWidth >= '768') {
        if (scrollDistance >= timelinePosition - headerHeight) {
          $(selectors.timelineCol).addClass(classes.isSticky)
          $(selectors.timelineCol).removeClass(classes.isAbsolute)
          $(selectors.stickyContent).css({
            top: headerHeight,
            transition: 'none'
          })
        } else {
          $(selectors.timelineCol).removeClass(classes.isSticky)
          $(selectors.timelineCol).removeClass(classes.isAbsolute)
          $(selectors.stickyContent).css({
            top: '0',
            transition: 'none'
          })
        }
        if (scrollDistance > timelinePosition + timelineHeight - timelineNumbersHeight - headerHeight) {
          $(selectors.timelineCol).removeClass(classes.isSticky)
          $(selectors.timelineCol).addClass(classes.isAbsolute)
          $(selectors.stickyContent).css({
            top: 'auto',
            transition: 'none'
          })
        }
      }
    })
    $(window).on('resize', function () {
      timelineNumbersHeight = $(selectors.stickyContent).outerHeight()
      headerHeight = $(selectors.header).outerHeight()
      timelinePosition = $(selectors.timeline).offset().top
      timelineHeight = $(selectors.timeline).outerHeight()
      deviceWidth = $(window).width()
    })
  }
}

if (isStyleguide()) {
  $(window).bind('styleguide:onRendered', function (event) {
    const elements = _get(event, 'detail.elements') || []

    _forEach(elements, element => {
      Sticky.init(element.querySelectorAll(selectors.timeline))
    })
  })
} else {
  $(selectors.timeline).each(function () {
    imagesLoaded(this, {}, () => Sticky.init($(selectors.timeline)))
  })
}
