import $ from 'jquery'
import { isStyleguide } from './utils'

const RemoveEmptyTag = {
  init () {
    const $realTextWrapper = $('.l-real-text')

    if (!$realTextWrapper.length) return

    $('p:empty, h1:empty, h2:empty, h3:empty, h4:empty, h5:empty, h6:empty').remove()
  }
}

if (!isStyleguide()) {
  RemoveEmptyTag.init()
}
