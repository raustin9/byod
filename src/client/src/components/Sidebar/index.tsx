import * as React from "react"
import { sidebar } from '../../styles/sidebar.css'
import { textarea } from '../../styles/ui.css'

export const Sidebar: React.FC = () => {
    return (
        <section className={sidebar}>
            <textarea placeholder="What is your prompt?" className={textarea}/>
        </section>
    );
}

