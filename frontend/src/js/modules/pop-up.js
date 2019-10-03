import $ from 'jquery'

const classes = {
  popUpWrapper: 'l-popup-wrapper',
  isOpened: 'is-opened',
  popupCloseTrigger: 'js-popup-close-trigger',
  popupOpenTrigger: 'js-popup-open-trigger'
}

const selectors = {
  popUpWrapper: `.${classes.popUpWrapper}`,
  popupCloseTrigger: `.${classes.popupCloseTrigger}`,
  popupOpenTrigger: `.${classes.popupOpenTrigger}`
}

export const PopUp = {
  init: function () {
    $(selectors.popupCloseTrigger).on('click', PopUp.closePopUp)
    $(selectors.popupOpenTrigger).on('click', PopUp.openPopUp)
  },
  closePopUp () {
    $(selectors.popUpWrapper).removeClass(classes.isOpened)
  },
  openPopUp () {
    $(selectors.popUpWrapper).addClass(classes.isOpened)
  }
}

PopUp.init()
