'use client';

import React, {FormEvent, useState} from 'react';
import Button from "@/components/button/button";

import cl from './style.module.css';
import Input from "@/components/input/input";
import {useRouter} from "next/navigation";

const CreateNoteForm = () => {
    const router = useRouter();

    const [loading, setLoading] = useState(false)

    const onSubmit = async (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        setLoading(true);

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
            const data = await res.json();
            setLoading(false);
            router.push(`/n/${data.hash}`);
        }
    }

    return (
        <form onSubmit={onSubmit}
              className={"max-w-[1200px] w-full flex flex-col items-center h-full gap-3"}>
            <Input name={"title"}
                   placeholder={"Title"}
                   fullwidth={true}
                   required={true}
                   className={[loading ? 'opacity-80' : ''].join(' ').trim()}
                   disabled={loading}/>
            <textarea className={[
                cl.noteContentInput,
                loading ? 'opacity-80' : ''
            ].join(' ')}
                      name="content" id="content"
                      placeholder={"Type in your note"}
                      disabled={loading}
                      required>
            </textarea>
            <Button variant={'success'}>create</Button>
        </form>
    );
};

export default CreateNoteForm;