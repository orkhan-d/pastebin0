'use client'

import React, {FC, useState} from 'react';
import cl from './style.module.css';
import Button from "@/components/button/button";

import { MdOutlineLink } from "react-icons/md";
import { MdContentCopy } from "react-icons/md";
import { MdDone } from "react-icons/md";

export interface NoteInfo {
    title: string;
    content: string;
}

const NoteInfoDisplay: FC<NoteInfo> = (data) => {
    const [copyLinkButtonIcon, setCopyLinkButtonIcon] = useState(<MdOutlineLink size={20}/>)

    const [copyContentButtonIcon, setCopyContentButtonIcon] = useState(<MdContentCopy size={20}/>)

    const copyAnimation = async (
        data: string,
        icon: React.JSX.Element,
        setIcon: React.Dispatch<React.SetStateAction<React.JSX.Element>>
    ) => {
        await navigator.clipboard.writeText(data);
        setIcon(<MdDone size={20}/>);
        setTimeout(() => {
            setIcon(icon);
        }, 1000);
    }

    return (
        <div className={"space-y-2 max-w-[1200px] mx-auto w-full"}>
            <div className={"flex flex-row items-center justify-between"}>
                <p>
                    <span className={cl.noteTitleLabel}>Note</span>&nbsp;
                    <span className={cl.noteTitle}>&#x00AB;{data.title}&#x00BB;</span>
                </p>
                <div className={"space-x-2"}>
                    <Button onClick={() => copyAnimation(
                        window.location.href,
                        copyLinkButtonIcon,
                        setCopyLinkButtonIcon
                    )} variant={'default'} size={'icon'}>{copyLinkButtonIcon}</Button>
                    <Button onClick={() => copyAnimation(
                        data.content,
                        copyContentButtonIcon,
                        setCopyContentButtonIcon
                    )} variant={'default'} size={'icon'}>{copyContentButtonIcon}</Button>
                </div>
            </div>
            <div className={cl.noteContent}>{data.content}</div>
        </div>
    );
};

export default NoteInfoDisplay;