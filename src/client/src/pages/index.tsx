import * as React from "react"
import type { HeadFC, PageProps } from "gatsby"

import { themeClass } from '../styles/theme.css'
import Navbar from '../components/Navbar'
import { Sidebar } from "../components/Sidebar"


const IndexPage: React.FC<PageProps> = () => {
    return (
        <main className={themeClass}>
            <Navbar />
            <Sidebar />
        </main>
    )
}

export default IndexPage

export const Head: HeadFC = () => <title>Home Page</title>
