import $ from 'jquery'
import _find from 'lodash/find'
import _throttle from 'lodash/throttle'

import { isStyleguide } from './utils'

const selectors = {
  iframe: 'iframe'
}

const IframeDimensions = {
  init: function ($iframes) {
    if (!$iframes.length) return

    $(window).on(
      'message onmessage',
      IframeDimensions.onMessageReceived(
        $iframes
      )
    )
  },

  onMessageReceived: $iframes => _throttle(
    ({ originalEvent: { source, data } }) => {
      const messageSenderFrame = _find(
        $iframes.toArray(),
        frame => frame.contentWindow === source
      )

      if (!messageSenderFrame) return

      $(messageSenderFrame).height(data)
    },
    500
  )
}

if (!isStyleguide()) {
  IframeDimensions.init($(selectors.iframe))
}
