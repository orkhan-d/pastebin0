'use client'

import React from 'react';
import cl from './button.module.css';

const styles = {
    success: cl.successBtn,
}

const Button = ({style, children, className, onClick, ...props}: {
    style: 'success',
    size?: 'default' | 'full' | 'icon',
    children?: React.ReactNode,
    className?: string,
    onClick?: () => void
}) => {

    return (
        <button onClick={onClick} className={[className, styles[style]].join(' ')}>
            {children}
        </button>
    );
};



export default Button;