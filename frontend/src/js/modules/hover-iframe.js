import $ from 'jquery'

const classes = {
  playerIframe: 'c-video__player--iframe',
  video: 'c-video',
  videoClose: 'c-video__close',
  isSeen: 'is-seen'
}

const selectors = {
  playerIframe: `.${classes.playerIframe}`,
  video: `.${classes.video}`,
  videoClose: `.${classes.videoClose}`
}

export const iframeHover = {
  init: function () {
    if ($(selectors.playerIframe) !== null) {
      $(selectors.video).mouseenter(iframeHover.hoverOn)
      $(selectors.video).mouseleave(iframeHover.hoverOut)
    }
  },
  hoverOn () {
    $(selectors.videoClose).addClass(classes.isSeen)
  },
  hoverOut () {
    $(selectors.videoClose).removeClass(classes.isSeen)
  }
}

iframeHover.init()
