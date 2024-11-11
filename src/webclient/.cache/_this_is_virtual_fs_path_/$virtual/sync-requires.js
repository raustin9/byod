
// prefer default export if available
const preferDefault = m => (m && m.default) || m


exports.components = {
  "component---cache-dev-404-page-js": preferDefault(require("/home/raustin9/src/byod/src/webclient/.cache/dev-404-page.js")),
  "component---src-pages-404-tsx": preferDefault(require("/home/raustin9/src/byod/src/webclient/src/pages/404.tsx")),
  "component---src-pages-index-tsx": preferDefault(require("/home/raustin9/src/byod/src/webclient/src/pages/index.tsx"))
}

