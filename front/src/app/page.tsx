import {FormEvent} from "react";
import CreateNoteForm from "@/components/create-note-form/create-note-form";

export default function Home() {
    return (
        <div className="w-screen h-screen flex flex-col items-center justify-center gap-3 p-3">
            <div className={"flex flex-col items-center justify-center py-2"}>
                <p className={"description"}>Service to share text with other people. 🤩</p>
                <p className={"description"}>Just type in text below and send people the generated link! ✏️</p>
            </div>
            <CreateNoteForm/>
        </div>
    );
}
