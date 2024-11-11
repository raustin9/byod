import { createTheme } from '@vanilla-extract/css'

export const [themeClass, theme] = createTheme({
  color: {
    primary: '#11E091',
    secondary: '#03dac6',
    background: '#181818',
    text: '#000000',
  },
  spacing: {
    small: '8px',
    medium: '16px',
    large: '24px',
  },
  typography: {
    fontFamily: 'Times New Roman',
    // fontFamily: 'Tahoma',
    xl: '1.3em',
  },
});
