// @ts-expect-error
import config from '@slidev/client/uno.config'
import { mergeConfigs, presetAttributify, presetIcons, presetWebFonts, presetWind3 } from 'unocss'

export default mergeConfigs([
  config,
  {
    rules: [
      ['font-math', { 'font-family': 'Latin Modern Roman, ui-serif, Georgia, Cambria, "Times New Roman", Times, serif' }],
    ],
    safelist: [
      ...Array.from({ length: 30 }, (_, i) => `delay-${(i + 1) * 100}`),
    ],
    presets: [
      presetWind3({
        dark: 'class',
      }),
      presetAttributify(),
      presetIcons({
        prefix: 'i-',
        extraProperties: {
          'display': 'inline-block',
          'vertical-align': 'middle',
        },
      }),
      presetWebFonts({
        fonts: {
          sans: 'DM Sans',
          cn: 'Noto Serif SC',
          hand: 'Playwrite IT Moderna',
          rounded: 'Comfortaa',
        },
        timeouts: {
          failure: 30000,
          warning: 30000,
        },
      }),
    ],
  },
])
