import * as React from "react"
import { sidebar, sidebarItem } from '../../styles/sidebar.css'
import { button, input, textarea } from '../../styles/ui.css'
import { theme } from "../../styles/theme.css";

export const Sidebar: React.FC = () => {
    return (
        <section className={sidebar}>
            <section className={sidebarItem}>
                <input type='text' className={input} placeholder="1234 Streetname, ST"/>
                <section style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '0.5em', fontFamily: theme.typography.fontFamily, fontSize: '18px', }}>
                    <label>Radius: </label>
                    <input type='number' className={input} style={{width: '70px',}}/>
                    <p>miles</p>
                </section>
            </section>
            <section className={sidebarItem}>
                <textarea placeholder="What is your prompt?" className={textarea}/>
                <button className={button}>Submit</button>
            </section>
        </section>
    );
}

