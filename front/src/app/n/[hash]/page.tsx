import React from 'react';
import NoteInfoDisplay, {NoteInfo} from "@/components/note-info-display/note-info-display";

const getNoteInfoByHash = async(hash: string) => {
    let noteId = atob(hash);

    const res = await fetch(`http://127.0.0.1:8000/api/notes/${noteId}`);

    return res.json();
}

const Page = async ({params}: {
    params: {
        hash: string;
    }
}) => {

    const data: NoteInfo = await getNoteInfoByHash(params.hash);

    return (
        <NoteInfoDisplay title={data.title} content={data.content}/>
    );
};

export default Page;