// src/components/Breadcrumbs.js

import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import './Breadcrumbs.css';

function Breadcrumbs() {
  const location = useLocation();
  const pathnames = location.pathname.split('/').filter((x) => x);

  return (
    <div className="breadcrumbs">
      <Link to="/">Home</Link>
      {pathnames.map((value, index) => {
        const to = `/${pathnames.slice(0, index + 1).join('/')}`;

        return (
          <span key={to}>
            {" / "}
            <Link to={to}>{value.replace(/-/g, ' ')}</Link>
          </span>
        );
      })}
    </div>
  );
}

export default Breadcrumbs;
