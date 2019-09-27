/* globals google */
import $ from 'jquery'
import { isStyleguide, isMobile } from '../utils'
import _groupBy from 'lodash/groupBy'
import _forEach from 'lodash/forEach'
import _filter from 'lodash/filter'
import _reduce from 'lodash/reduce'
import _find from 'lodash/find'
import mapStyles from './mapStyles'
import locationsListTemplate from './templates/locations-list.handlebars'
import infowindowTemplate from './templates/infowindow.handlebars'

import MarkerClusterer from '../../vendor/markerclusterer'

const classes = {
  map: 'js-map',
  mapContainer: 'js-map-container',
  select: 'js-select',
  clearFilters: 'js-clear-filters',
  locationsContainer: 'js-locations-container',
  mapPopupContainer: 'js-map-popup-container',
  mapPopupClose: 'js-map-popup-close'
}

const selectors = {
  map: `.${classes.map}`,
  mapContainer: `.${classes.mapContainer}`,
  select: `.${classes.select}`,
  countrySelect: `.${classes.select}[name="country"]`,
  clearFilters: `.${classes.clearFilters}`,
  locationsContainer: `.${classes.locationsContainer}`,
  mapPopupContainer: `.${classes.mapPopupContainer}`,
  mapPopupClose: `.${classes.mapPopupClose}`
}

const MARKER_ICON_SRC = '/static/img/map-pin-small.png'
const MARKER_GROUPED_ICON_SRC = '/static/img/map-pin-small'
const MARKER_HEADQUARTER_ICON_SRC = '/static/img/map-pin.png'

const OfficesMap = {
  init: async function ($mapContainer) {
    if (!$mapContainer.length) return

    const [ officesLocations ] = await Promise.all([
      OfficesMap.fetchLocationsData($mapContainer),
      OfficesMap.loadGoogleAPIScript()
    ])

    const countryOptionsMap = _groupBy(officesLocations, 'country')
    const $mapBox = $mapContainer.find(selectors.map)
    const googleMapObject = OfficesMap.createGoogleMapObject($mapBox)

    OfficesMap.createMarkers(googleMapObject, officesLocations)
    google.maps.event.addDomListener(window, 'resize', function () {
      OfficesMap.zoomMapToVisibleMarkers(googleMapObject)
    })

    const $selectElements = $mapContainer.find(selectors.select)
    const $clearFiltersButton = $mapContainer.find(selectors.clearFilters)
    const $locationsContainer = $mapContainer.find(selectors.locationsContainer)
    const $mapPopupClose = $mapContainer.find(selectors.mapPopupClose)
    const $countrySelect = $selectElements.filter(selectors.countrySelect)

    _forEach(Object.keys(countryOptionsMap), country => {
      if (country !== 'null') {
        $countrySelect.append($('<option/>', {
          value: country,
          html: country
        }))
      }
    })

    $selectElements.on(
      'change',
      OfficesMap.onFilterSelectChange(
        $selectElements,
        googleMapObject,
        $locationsContainer,
        countryOptionsMap,
        officesLocations
      )
    )

    $clearFiltersButton.on(
      'click',
      OfficesMap.onClearFiltersClick(
        $selectElements,
        googleMapObject
      )
    )

    $mapPopupClose.on('click', OfficesMap.onInfoWindowCloseClick)
    OfficesMap.renderLocationsSection($locationsContainer, officesLocations)

    return googleMapObject
  },

  loadGoogleAPIScript () {
    return new Promise(resolve => {
      if (window.google === undefined) {
        $.getScript(
          `https://maps.googleapis.com/maps/api/js?key=${window.googleAPIKey}&libraries=visualization,drawing,places,weather,geometry`
        ).done(resolve)
      } else {
        resolve()
      }
    })
  },

  fetchLocationsData ($mapContainer) {
    return new Promise((resolve, reject) => {
      $.ajax({
        url: $mapContainer.data('json'),
        headers: {
          // Proxies request in development mode
          'Should-Proxy-Request': true
        }
      })
        .done(data => {
          resolve(data)
        })
        .fail(reject)
    })
  },

  createGoogleMapObject ($mapBox) {
    const { lat, lng } = $mapBox.data()
    const center = new google.maps.LatLng(lat, lng)
    const googleMapObject = new window.google.maps.Map(
      $mapBox.get(0),
      {
        zoom: Math.ceil(Math.log2($(window).width())) - 8.43,
        minZoom: Math.ceil(Math.log2($(window).width())) - 8.43,
        center,
        scrollwheel: false,
        disableDefaultUI: false
      }
    )
    const mapType = new google.maps.StyledMapType(mapStyles, {
      name: 'Outline'
    })

    googleMapObject.mapTypes.set('tehgrayz', mapType)
    googleMapObject.setMapTypeId('tehgrayz')
    googleMapObject.markers = []

    return googleMapObject
  },

  createMarkers (googleMapObject, officesLocations) {
    googleMapObject.infoWindowObject = new google.maps.InfoWindow({
      pixelOffset: new google.maps.Size(360, 320)
    })

    for (const markerData of officesLocations) {
      const { lat, lng, isHeadquarter } = markerData
      const marker = new google.maps.Marker({
        position: new google.maps.LatLng(lat, lng),
        map: googleMapObject,
        icon: isHeadquarter ? MARKER_HEADQUARTER_ICON_SRC : MARKER_ICON_SRC
      })

      marker.markerData = markerData
      googleMapObject.markers.push(marker)

      google.maps.event.addListener(marker, 'click', OfficesMap.onMarkerClick)
    }

    googleMapObject.markerClustererObject = new MarkerClusterer(
      googleMapObject,
      googleMapObject.markers,
      {
        imagePath: MARKER_GROUPED_ICON_SRC
      }
    )
  },

  onMarkerClick () {
    const { map, markerData } = this
    const { infoWindowObject } = map

    if (!isMobile()) {
      infoWindowObject.setContent(infowindowTemplate({
        ...markerData
      }))
      infoWindowObject.open(map, this)
    } else {
      $(selectors.mapPopupContainer)
        .addClass('is-opened')
        .find('.c-map__popup__content')
        .html(infowindowTemplate({ ...markerData }))
    }
  },

  onInfoWindowCloseClick () {
    $(selectors.mapPopupContainer)
      .removeClass('is-opened')
      .find('.c-map__popup__content')
      .html()
  },

  filterMarkers (googleMapObject, country) {
    const shouldShowPredicate = OfficesMap.createLocationsFilterDelegate(
      country
    )
    for (const marker of googleMapObject.markers) {
      marker.setVisible(shouldShowPredicate(marker.markerData))
    }
  },

  onFilterSelectChange: (
    $selectElements,
    googleMapObject,
    $locationsContainer,
    countryOptionsMap,
    officesLocations
  ) => function () {
    const $countrySelect = $selectElements.filter(selectors.countrySelect)
    const $clickedFilterSelect = $(this)
    const country = $countrySelect.val()

    if (country && $clickedFilterSelect.is($countrySelect)) {
      OfficesMap.filterMarkers(googleMapObject, country)
      OfficesMap.renderLocationsSection($locationsContainer, officesLocations, country)
      OfficesMap.zoomMapToVisibleMarkers(googleMapObject)
    }
  },

  onClearFiltersClick: ($selectElements, googleMapObject) => function () {
    $selectElements.val(null).trigger('change')
    OfficesMap.zoomMapToVisibleAllMarkers(googleMapObject)
  },

  zoomMapToVisibleAllMarkers (googleMapObject) {
    const bounds = new google.maps.LatLngBounds()

    _forEach(googleMapObject.markers, marker => {
      bounds.extend(marker.getPosition())
    })

    googleMapObject.fitBounds(bounds)
  },

  zoomMapToVisibleMarkers (googleMapObject) {
    const bounds = new google.maps.LatLngBounds()

    _forEach(googleMapObject.markers, marker => {
      if (marker.visible) {
        bounds.extend(marker.getPosition())
      }
    })

    googleMapObject.fitBounds(bounds)

    if (googleMapObject.getZoom() > 8) {
      googleMapObject.setZoom(8)
    }
  },

  createLocationsFilterDelegate: (country) => country
    ? markerData => (country === 'All') ? true : markerData.country === country
    : () => true,

  prepareCountriesTemplateData (region, country, officesLocations) {
    const locations = _filter(
      officesLocations,
      OfficesMap.createLocationsFilterDelegate(region, country)
    )
    const groupedLocations = _groupBy(
      locations,
      location => {
        location.country = location.country || ''
        return `${location.country}`
      }
    )
    const splittedLocations = _reduce(groupedLocations, (result, locations, groupKey) => {
      const headquarter = _find(locations, ({ isHeadquarter }) => isHeadquarter)
      const offices = _filter(locations, ({ isHeadquarter }) => !isHeadquarter)

      return {
        ...result,
        [groupKey]: {
          headquarter,
          offices
        }
      }
    }, {})

    return splittedLocations
  },

  renderLocationsSection ($locationsContainer, officesLocations, region, country) {
    const locations = OfficesMap.prepareCountriesTemplateData(region, country, officesLocations)

    $locationsContainer.html(
      locationsListTemplate({
        locations
      })
    )
  }
}

export default () => {
  if (!isStyleguide()) {
    return OfficesMap.init($(selectors.mapContainer))
  }

  return Promise.resolve()
}
