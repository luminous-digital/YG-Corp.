import $ from 'jquery'
import objectFitImages from 'object-fit-images'

const ObjectFit = {
  init: function () {
    const $images = $('.c-news-card__img')
    objectFitImages($images)
  }
}

ObjectFit.init()
