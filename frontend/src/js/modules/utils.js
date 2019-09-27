const isMobileMatchMedia = window.matchMedia('(max-width: 767px)')

export const isStyleguide = () => !!window._styleguideConfig

export const isMobile = () => isMobileMatchMedia.matches
