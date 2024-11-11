import { style } from "@vanilla-extract/css";
import { theme } from "./theme.css";

export const textarea = style({
    width: '80%',
    
    minWidth: '80%',
    maxWidth: '80%',
    padding: '10px',
    fontSize: '16px',
    border: '2px solid #ccc',
    borderRadius: '5px',
    outline: 'none',
    transition: 'border-color 0.3s ease',
    fontFamily: theme.typography.fontFamily,
});

export const input = style({
    border: '1px solid #ccc',
    borderRadius: '5px',
    outline: 'none',
    resize: 'none',
    padding: '5px 10px 5px 10px',
    fontFamily: theme.typography.fontFamily,
});

export const button = style({
    background: theme.color.green4,
    border: `1px solid ${theme.color.green2}`,
    outline: 'none',
    borderRadius: '5px',
    color: theme.color.white,
    fontFamily: theme.typography.fontFamily,
    fontSize: theme.typography.xl,
    padding: '0.5em 1em 0.5em 1em',
    transition: '100ms ease',

    ':hover': {
        cursor: 'grab',
        transition: '100ms ease',
        background: theme.color.green3,
        border: `1px solid ${theme.color.green1}`
    },
});
