import $ from 'jquery'
import { isStyleguide } from './utils'
import _get from 'lodash/get'
import _forEach from 'lodash/forEach'
import { CountUp } from 'countup.js'

const classes = {
  timelineItem: 'c-timeline-list__item',
  header: 'js-header',
  numberPanel: 'js-timeline-number-panel',
  numberEmployees: 'js-timeline-number-employees',
  numberOffices: 'js-timeline-number-offices'
}

const selectors = {
  timelineItem: `.${classes.timelineItem}`,
  header: `.${classes.header}`,
  numberPanel: `.${classes.numberPanel}`,
  numberEmployees: `.${classes.numberEmployees}`,
  numberOffices: `.${classes.numberOffices}`
}

const CounterScroll = {
  init () {
    if (!$(selectors.timelineItem).length) return
    let headerHeight = $(selectors.header).outerHeight()
    const dataPanelInitial = $(selectors.timelineItem).data('panel')
    const dataEmployeesInitial = $(selectors.timelineItem).data('employees')
    const dataOfficesInitial = $(selectors.timelineItem).data('offices')
    const panelArray = []
    const employeesArray = []
    const officesArray = []
    let currentIndex = 0
    let scrollPosition = 0

    const dataPanelInitialComas = ('' + dataPanelInitial).replace(/(\d)(?=(\d\d\d)+$)/g, '$1,')
    const dataEmployeesInitialComas = ('' + dataEmployeesInitial).replace(/(\d)(?=(\d\d\d)+$)/g, '$1,')
    const dataOfficesInitialComas = ('' + dataOfficesInitial).replace(/(\d)(?=(\d\d\d)+$)/g, '$1,')

    $(selectors.numberPanel).text(dataPanelInitialComas)
    $(selectors.numberEmployees).text(dataEmployeesInitialComas)
    $(selectors.numberOffices).text(dataOfficesInitialComas)

    $(selectors.timelineItem).each(function () {
      const dataPanel = $(this).data('panel')
      const dataEmployees = $(this).data('employees')
      const dataOffices = $(this).data('offices')
      panelArray.push(dataPanel)
      employeesArray.push(dataEmployees)
      officesArray.push(dataOffices)
    })

    $(document).on('scroll', function () {
      $(selectors.timelineItem).each(function (index) {
        let itemPosition = $(this).offset().top - $(window).scrollTop()
        let itemHeight = $(this).height()

        if ((itemPosition >= (-itemHeight + headerHeight)) && (itemPosition <= headerHeight * 2)) {
          const dataPanel = $(this).data('panel')
          const dataEmployees = $(this).data('employees')
          const dataOffices = $(this).data('offices')

          const dataPanelComas = ('' + dataPanel).replace(/(\d)(?=(\d\d\d)+$)/g, '$1,')
          const dataEmployeesComas = ('' + dataEmployees).replace(/(\d)(?=(\d\d\d)+$)/g, '$1,')
          const dataOfficesComas = ('' + dataOffices).replace(/(\d)(?=(\d\d\d)+$)/g, '$1,')

          $(selectors.numberPanel).text(dataPanelComas)
          $(selectors.numberEmployees).text(dataEmployeesComas)
          $(selectors.numberOffices).text(dataOfficesComas)
          const options = {
            useGrouping: true,
            useEasing: true,
            duration: 1,
            separator: ',',
            decimal: ','
          }

          if ((document.body.getBoundingClientRect()).top > scrollPosition) {
            if (currentIndex !== index) {
              const countUpPanel = new CountUp('countup-panel', dataPanel, { startVal: panelArray[index + 1], ...options })
              const countUpEmployees = new CountUp('countup-employees', dataEmployees, { startVal: employeesArray[index + 1], ...options })
              const countUpOffices = new CountUp('countup-offices', dataOffices, { startVal: officesArray[index + 1], ...options })
              countUpPanel.update(dataPanel)
              countUpEmployees.update(dataEmployees)
              countUpOffices.update(dataOffices)

              currentIndex = index
            }
          } else {
            if (currentIndex !== index) {
              const countUpPanel = new CountUp('countup-panel', dataPanel, { startVal: panelArray[index - 1], ...options })
              const countUpEmployees = new CountUp('countup-employees', dataEmployees, { startVal: employeesArray[index - 1], ...options })
              const countUpOffices = new CountUp('countup-offices', dataOffices, { startVal: officesArray[index - 1], ...options })
              countUpPanel.update(dataPanel)
              countUpEmployees.update(dataEmployees)
              countUpOffices.update(dataOffices)

              currentIndex = index
            }
          }
          scrollPosition = (document.body.getBoundingClientRect()).top
        }
      })
    })
  }
}

if (isStyleguide()) {
  $(window).bind('styleguide:onRendered', function (event) {
    const elements = _get(event, 'detail.elements') || []

    _forEach(elements, element => {
      CounterScroll.init(element.querySelectorAll(selectors.timelineItem))
    })
  })
} else {
  CounterScroll.init($(selectors.timelineItem))
}
