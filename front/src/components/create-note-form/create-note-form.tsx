'use client';

import React, {FormEvent} from 'react';
import Button from "@/components/button/button";

import cl from './style.module.css';
import Input from "@/components/input/input";

const CreateNoteForm = () => {
    const onSubmit = async (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();

    }

    return (
        <form onSubmit={onSubmit}
              className={"max-w-[1200px] w-full flex flex-col items-center h-full gap-3"}>
            <Input name={"title"} placeholder={"Title"} fullWidth={true}/>
            <textarea className={cl.noteContentInput}
                      name="content" id="content"
                      placeholder={"Type in your note"}>

            </textarea>
            <Button style={'success'}>create</Button>
        </form>
    );
};

export default CreateNoteForm;