import React from 'react';
import {
    Link
  } from "react-router-dom";

export function Header() {

return <header id="main-header">    
        <nav>
            <Link to="/">Home</Link>
            <ul>
                <li><Link to="/addeducation">Add education</Link></li>
            </ul>
        </nav>
    </header>
}