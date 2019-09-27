import $ from 'jquery'
import { isStyleguide } from './utils'
import ScrollReveal from '../vendor/scrollreveal.js'

const classes = {
  scrollReveal: 'js-scroll-reveal',
  main: 'l-main',
  footer: 'l-footer',
  info: 'c-info',
  infoTeaser: 'c-info-teaser',
  widget: 'c-widget',
  quickLink: 'c-quick-link',
  quote: 'c-quote',
  socialMedia: 'c-social-media',
  advisorListItem: 'c-advisor-list__item'
}

const selectors = {
  scrollReveal: `.${classes.scrollReveal}`,
  info: `.${classes.info}`,
  infoTeaser: `.${classes.infoTeaser}`,
  widget: `.${classes.widget}`,
  quickLink: `.${classes.quickLink}`,
  quote: `.${classes.quote}`,
  socialMedia: `.${classes.socialMedia}`,
  advisorListItem: `.${classes.advisorListItem}`,
  mainSocial: `.${classes.main} .${classes.socialMedia}`,
  footerSocial: `.${classes.footer} .${classes.socialMedia}`
}

const Animations = {
  init: function () {
    if (
      $(selectors.scrollReveal).length ||
      $(selectors.info).length ||
      $(selectors.infoTeaser).length ||
      $(selectors.widget).length ||
      $(selectors.quickLink).length ||
      $(selectors.quote).length ||
      $(selectors.footerSocial).length ||
      $(selectors.mainSocial).length ||
      $(selectors.advisorListItem).length
    ) {
      const animationConfig = {
        distance: '50px',
        origin: 'bottom',
        easing: 'cubic-bezier(0.25, 0.1, 0.25, 1)',
        interval: 50,
        duration: 700
      }

      const nodesList = [
        selectors.scrollReveal,
        selectors.info,
        selectors.infoTeaser,
        selectors.widget,
        selectors.quickLink,
        selectors.quote,
        selectors.mainSocial,
        selectors.advisorListItem,
        selectors.footerSocial
      ]

      nodesList.forEach(selector => {
        ScrollReveal().reveal(selector, animationConfig)
      })
    }
  }
}

export default async () => {
  if (!isStyleguide()) {
    Animations.init()
  }
}
