import { createTheme, globalStyle } from '@vanilla-extract/css'

export const [themeClass, theme] = createTheme({
  color: {
    primary: '#11E091',
    secondary: '#03dac6',
    
    green1: '#11E091',
    green2: '#1ed18c',
    green3: '#25956a',
    green4: '#257556',
    
    white: '#fefefe',
    // background: '#181818',
    // background: '#26303e',
    background: '#13171c',
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
    md: '0.8em',
    sm: '0.5em',
  },
});

