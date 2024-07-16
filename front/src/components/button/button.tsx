'use client'

import React from 'react';
import cl from './button.module.css';

const styles = {
    success: cl.successBtn,
}

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
    variant: 'success',
    size?: 'default' | 'full' | 'icon'
}

const Button: React.FC<ButtonProps> = (props) => {

    return (
        <button onClick={props.onClick}
                className={[props.className, styles[props.variant]].join(' ')}>
            {props.children}
        </button>
    );
};



export default Button;