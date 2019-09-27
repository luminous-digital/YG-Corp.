const Cookies = {
  init: function () {
    if (!this.getCookie(this.settings.cookieName)) {
      this.cookieConsent()
    }
    if (this.getCookie(this.settings.cookieName) === 'accept') {
      /* eslint-disable */
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', window.GAID);
      /* eslint-enable */
    }
  },
  settings: {
    cookieName: 'yougovCookieConsent',
    cookieValue: {
      accept: 'accept',
      decline: 'decline'
    }
  },
  getCookie: function (name) {
    const value = '; ' + document.cookie
    const parts = value.split('; ' + name + '=')
    if (parts.length === 2) return parts.pop().split(';').shift()
  },
  cookieConsent: function () {
    const cookieBar = document.querySelector('.js-cookie')
    if (cookieBar) {
      cookieBar.classList.add('is-visible')
      const cookieAccept = cookieBar.querySelector('.js-cookie-accept')
      const cookieDecline = cookieBar.querySelector('.js-cookie-decline')
      if (cookieAccept && cookieDecline) {
        cookieAccept.addEventListener('click', (e) => {
          e.preventDefault()
          document.cookie = this.settings.cookieName + '=' + this.settings.cookieValue.accept + ';path=/'
          cookieBar.classList.remove('is-visible')
        })
        cookieDecline.addEventListener('click', (e) => {
          e.preventDefault()
          document.cookie = this.settings.cookieName + '=' + this.settings.cookieValue.decline + ';path=/'
          cookieBar.classList.remove('is-visible')
        })
      }
    }
  }
}

Cookies.init()
