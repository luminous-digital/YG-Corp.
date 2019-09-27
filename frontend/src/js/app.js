import 'idempotent-babel-polyfill'
import './polyfills'
import svg4everybody from 'svg4everybody'
import './modules/toggle-menu'
import './modules/toggle-search'
import './modules/modal'
import './modules/sub-nav'
import './modules/cookie'
import './modules/video-player'
import './modules/scroll'
import './modules/list-load-more'
import './modules/tab-select'
import './modules/toggle-accordion'
import './modules/select'
import './modules/validation'
import './modules/pop-up'
import './modules/sticky'
import './modules/counter-scroll'
import './modules/header-scroll'
// import './modules/animations'
// import './modules/offices-map'
import officesMapInit from './modules/offices-map'
import animationsInit from './modules/animations'
import './modules/iframe'
import './modules/custom-dropdown'
import './modules/ajax-load-more'
import './modules/table-select'
import './modules/object-fit-images'
import './modules/remove-empty-tag'
import './modules/hover-iframe'

officesMapInit().then(gogleMapObject => {
  if (gogleMapObject) {
    window.google.maps.event.addListenerOnce(gogleMapObject, 'idle', () => {
      animationsInit()
    })
  } else {
    animationsInit()
  }
})

svg4everybody()
