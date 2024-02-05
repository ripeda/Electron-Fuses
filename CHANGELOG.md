# Electron Fuses

## 1.3.0
- Add support for Electron and Chromium version detection
- Add support for Electron release date detection
  - Requires network access to query Electron's repository
- Implement function caching to reduce redundant file reads

## 1.2.0
- Publish `framework()` as property

## 1.1.0
- Add new exception for missing `SENTINEL` in binary
  - `SentinelNotFound`

## 1.0.0
- Initial release