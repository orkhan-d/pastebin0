import React from 'react';
import cl from './style.module.css';

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
    fullwidth: boolean
}

const Input: React.FC<InputProps> = ({...props}) => {
    let classes: string[] = [cl.input];
    if (props.className)
        classes.push(props.className)
    if (props.fullwidth) {
        classes.push("w-full");
    }

    console.log(classes)

    return (
        <input {...props}
               className={classes.join(' ')}
        />
    );
};

export default Input;