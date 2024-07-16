import React from 'react';
import styles from './navbar.module.css';
import Link from "next/link";

const Navbar = () => {
    return (
        <header className={styles.header}>
            <nav className={styles.navbar}>
                <Link href={"/"} className={"logo text-[20px]"}>PasteBin</Link>
            </nav>
        </header>
    );
};

export default Navbar;