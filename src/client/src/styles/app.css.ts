import { globalStyle } from '@vanilla-extract/css';
import { theme } from './theme.css'

globalStyle('body', {
    margin: 0,
    padding: 0,

    fontFamily: 'Times New Roman',
    color: theme.color.white,
});
