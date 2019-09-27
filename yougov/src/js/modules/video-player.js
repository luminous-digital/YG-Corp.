import { isStyleguide } from './utils'
import _get from 'lodash/get'
import _forEach from 'lodash/forEach'
import $ from 'jquery'

const classes = {
  player: 'js-video',
  playerAlt: 'c-video-module--alt',
  video: 'js-viewer',
  toggle: 'js-toggle-button',
  ranges: 'c-slider__bar',
  progressBar: 'c-progress__filled',
  progress: 'c-progress',
  playBtn: 'js-play',
  videoPlayer: 'js-video-module',
  stopBtn: 'js-video-close',
  currentTime: 'js-current-time',
  fullTime: 'js-full-time',
  controls: 'c-video__controls',
  visible: 'is-visible',
  playing: 'is-playing',
  time: 'js-time',
  iframe: 'c-video-module--iframe',
  iframePlayer: 'c-video__player--iframe',
  videoBox: 'c-video'
}

const VideoPlayer = {
  init (playBtns) {
    if (!playBtns) return

    this.selectors = {
      player: document.querySelector(`.${classes.player}`),
      playerAlt: document.querySelector(`.${classes.playerAlt}`),
      video: document.querySelector(`.${classes.video}`),
      toggle: document.querySelector(`.${classes.toggle}`),
      ranges: document.querySelectorAll(`.${classes.ranges}`),
      progressBar: document.querySelector(`.${classes.progressBar}`),
      progress: document.querySelector(`.${classes.progress}`),
      playBtn: document.querySelector(`.${classes.playBtn}`),
      videoPlayer: document.querySelector(`.${classes.videoPlayer}`),
      stopBtn: document.querySelector(`.${classes.stopBtn}`),
      currentTime: document.querySelector(`.${classes.currentTime}`),
      fullTime: document.querySelector(`.${classes.fullTime}`),
      controls: document.querySelector(`.${classes.controls}`),
      time: document.querySelector(`.${classes.time}`),
      iframe: document.querySelector(`.${classes.iframe}`),
      iframePlayer: document.querySelector(`.${classes.iframePlayer}`),
      videoBox: document.querySelector(`.${classes.videoBox}`)
    }

    _forEach(playBtns, playBtn => {
      if (this.selectors.iframePlayer !== null) {
        $(this.selectors.iframePlayer).remove()
      }
      this.selectors.video.addEventListener('loadedmetadata', () => {
        this.loadTime()
      })
      let mousedown = false
      playBtn.addEventListener('click', VideoPlayer.showPlayer.bind(this))
      this.selectors.stopBtn.addEventListener('click', VideoPlayer.stopVideo.bind(this))
      this.selectors.stopBtn.addEventListener('click', VideoPlayer.stopVideo.bind(this))
      this.selectors.toggle.addEventListener('click', VideoPlayer.togglePlay.bind(this))
      this.selectors.video.addEventListener('click', VideoPlayer.togglePlay.bind(this))
      this.selectors.video.addEventListener('play', VideoPlayer.playStopButton.bind(this))
      this.selectors.video.addEventListener('pause', VideoPlayer.playStopButton.bind(this))
      this.selectors.video.addEventListener('timeupdate', VideoPlayer.handleProgress.bind(this))
      this.selectors.ranges.forEach(range =>
        range.addEventListener('change', VideoPlayer.handleRangeUpdate(this))
      )
      this.selectors.ranges.forEach(range =>
        range.addEventListener('mousemove', VideoPlayer.handleRangeUpdate(this))
      )
      this.selectors.progress.addEventListener('click', VideoPlayer.scrub.bind(this))
      this.selectors.progress.addEventListener('mousemove', (e) => mousedown && VideoPlayer.scrub.bind(this)(e))
      this.selectors.progress.addEventListener('mousedown', () => { mousedown = true })
      this.selectors.progress.addEventListener('mouseup', () => { mousedown = false })
    })
  },
  showPlayer (e) {
    e.preventDefault()
    const iframeTemplate = this.selectors.video
    if (this.selectors.iframe === null) {
      this.selectors.player.classList.add(classes.playing)
      this.selectors.videoPlayer.classList.add(classes.visible)
      this.selectors.controls.classList.add(classes.visible)
      this.selectors.stopBtn.classList.add(classes.visible)
      this.selectors.video.play()
    } else {
      this.selectors.player.classList.add(classes.playing)
      this.selectors.videoPlayer.classList.add(classes.visible)
      this.selectors.stopBtn.classList.add(classes.visible)
      $(this.selectors.videoBox).prepend(iframeTemplate)
    }
  },
  stopVideo () {
    this.selectors.player.classList.remove(classes.playing)
    this.selectors.videoPlayer.classList.remove(classes.visible)
    this.selectors.controls.classList.remove(classes.visible)
    this.selectors.stopBtn.classList.remove(classes.visible)
    if (this.selectors.iframe === null) {
      this.selectors.video.pause()
    } else {
      $(this.selectors.iframePlayer).remove()
    }
  },
  togglePlay () {
    if (this.selectors.iframe === null) {
      const method = this.selectors.video.paused ? 'play' : 'pause'
      this.selectors.video[method]()
    }
  },
  playStopButton () {
    const icon = this.selectors.video.paused ? '►' : '❚❚'
    this.selectors.toggle.textContent = icon
  },
  handleProgress () {
    const percent = (this.selectors.video.currentTime / this.selectors.video.duration) * 100
    this.selectors.progressBar.style.flexBasis = `${percent}%`
    let time = this.selectors.video.currentTime.toFixed(0)
    const secToMin = (time - (time %= 60)) / 60 + (time > 9 ? ':' : ':0') + time
    this.selectors.currentTime.innerHTML = secToMin
  },
  handleRangeUpdate: instance => function () {
    instance.selectors.video[this.name] = this.value
  },
  scrub (e) {
    const scrubTime = (e.offsetX / this.selectors.progress.offsetWidth) * this.selectors.video.duration
    this.selectors.video.currentTime = scrubTime
  },
  loadTime () {
    let time = this.selectors.video.duration.toFixed(0)
    const secToMin = (time - (time %= 60)) / 60 + (time > 9 ? ':' : ':0') + time
    this.selectors.time.innerHTML = secToMin
    this.selectors.fullTime.innerHTML = secToMin
  }
}

if (isStyleguide()) {
  window.addEventListener('styleguide:onRendered', event => {
    const elements = _get(event, 'detail.elements') || []

    _forEach(elements, element => {
      VideoPlayer.init(element.querySelectorAll(`.${classes.playBtn}`))
    })
  })
} else {
  VideoPlayer.init(document.querySelectorAll(`.${classes.playBtn}`))
}
