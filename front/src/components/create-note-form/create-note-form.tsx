'use client';

import React, {FormEvent} from 'react';
import Button from "@/components/button/button";

import cl from './style.module.css';
import Input from "@/components/input/input";

const CreateNoteForm = () => {
    const onSubmit = async (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        const res = await fetch('http://127.0.0.1:8000/api/notes', {
            method: 'POST',
            body: JSON.stringify({
                title: (event.target as any).title.value,
                content: (event.target as any).content.value
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (res.ok) {
            console.log('Note created successfully');
        }
    }

    return (
        <form onSubmit={onSubmit}
              className={"max-w-[1200px] w-full flex flex-col items-center h-full gap-3"}>
            <Input name={"title"}
                   placeholder={"Title"}
                   fullWidth={true}
                   required={true}/>
            <textarea className={cl.noteContentInput}
                      name="content" id="content"
                      placeholder={"Type in your note"}
                      required>
            </textarea>
            <Button variant={'success'}>create</Button>
        </form>
    );
};

export default CreateNoteForm;