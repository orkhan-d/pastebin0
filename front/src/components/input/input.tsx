import React from 'react';
import cl from './style.module.css';

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
    fullWidth?: boolean
}

const Input: React.FC<InputProps> = ({...props}) => {
    let classes: string[] = [cl.input, props.className ?? ''];
    if (props.fullWidth) {
        classes.push("w-full");
    }

    return (
        <input className={classes.join(' ')}
               {...props}
        />
    );
};

export default Input;