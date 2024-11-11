import { style } from '@vanilla-extract/css'
import { theme } from './theme.css'

export const navbar = style({
    position: 'sticky',
   
    // color: "#9fff87",
    color: theme.color.primary,
    backgroundColor: theme.color.background,
    
    padding: 20,
    margin: 0,
    
    width: '100vw',
    height: '8vh',
    
    fontFamily: theme.typography.fontFamily,
    fontSize: theme.typography.xl,

    letterSpacing: '0.05em',
    
    display: 'flex',
    alignItems: 'center',
})

export const item = style({
    
})
