import * as React from "react"
import * as styles from '../../styles/navbar.css'



// For now we only have the one page so no need for links yet
const Navbar: React.FC = () => {
    return (
        <nav className={styles.navbar}>
            <div className={styles.item}>
                <h1>BYOD</h1>
            </div>
        </nav>
    )
}

export default Navbar;
