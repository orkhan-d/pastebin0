'use client'

import React from 'react';
import cl from './button.module.css';

const styles = {
    success: cl.successBtn,
    'default': cl.defaultBtn
}

const sizes = {
    default: cl.defaultSize,
    full: cl.fullWidth,
    icon: cl.iconSize
}

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
    variant: 'success' | 'default',
    size?: 'default' | 'full' | 'icon',
}

const Button: React.FC<ButtonProps> = (props) => {
    let classes = [
        props.className,
        styles[props.variant],
        sizes[props.size ?? 'default']
    ];

    return (
        <button {...props}
                onClick={props.onClick}
                className={classes.join(' ')}>
            {props.children}
        </button>
    );
};



export default Button;