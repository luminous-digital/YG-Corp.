import $ from 'jquery'

const Modal = {
  init () {
    const $openModalTrigger = $('.js-open-modal-trigger')
    const $closeModalTrigger = $('.js-close-modal-trigger')
    const $modalContainer = $('.c-modal')
    const isModalOpenedClass = 'is-opened'
    const $body = $('body')

    $openModalTrigger.on('click', function (e) {
      e.preventDefault()
      const $currentOpenModal = $(this)
      const hash = $currentOpenModal.attr('href')
      $(`${hash}`).addClass(isModalOpenedClass)
      $body.addClass('is-modal-open')
    })

    $closeModalTrigger.on('click', function (e) {
      e.preventDefault()
      $body.removeClass('is-modal-open')
      $modalContainer.each(function () {
        const $currentModal = $(this)
        if ($currentModal.hasClass(isModalOpenedClass)) {
          $currentModal.removeClass(isModalOpenedClass)
        }
      })
    })
  }
}

Modal.init()
