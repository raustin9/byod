import { style } from '@vanilla-extract/css'
import { theme } from './theme.css'

export const sidebar = style({
    color: theme.color.primary,
    background: theme.color.background,

    width: '15vw',
    height: '92vh',

    position: 'absolute',
    top: '8vh',
    left: 0,

    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    
    padding: '1% 0 0 0',
})
