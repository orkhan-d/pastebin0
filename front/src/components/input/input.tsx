import React from 'react';
import cl from './style.module.css';

const Input = ({name, placeholder, fullWidth = true, className = "", ...props}: {
    name: string,
    placeholder: string,
    fullWidth?: boolean,
    className?: string
}) => {
    let classes: string[] = [cl.input, className];
    if (fullWidth) {
        classes.push("w-full");
    }

    return (
        <input placeholder={placeholder}
               name={name}
               className={classes.join(' ')}
        />
    );
};

export default Input;