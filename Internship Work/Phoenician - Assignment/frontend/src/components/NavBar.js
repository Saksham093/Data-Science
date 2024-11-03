// src/components/NavBar.js

import React from 'react';
import Breadcrumbs from './Breadcrumbs';
import SearchIcon from '@mui/icons-material/Search';
import './NavBar.css';
import SearchRoundedIcon from '@mui/icons-material/SearchRounded';


function NavBar({ onSearchClick }) {
  return (
    <nav className="navbar">
      <Breadcrumbs />
      <button className="search-icon" onClick={onSearchClick}>
        <SearchRoundedIcon />
      </button>
    </nav>
  );
}

export default NavBar;
