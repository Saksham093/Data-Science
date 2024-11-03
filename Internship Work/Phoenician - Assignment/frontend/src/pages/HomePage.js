// src/pages/HomePage.js

import React from 'react';
import { useNavigate } from 'react-router-dom';
import './HomePage.css';

function HomePage() {
  const navigate = useNavigate();

  return (
    <div className="homepage">
      <img src={`${process.env.PUBLIC_URL}/assets/images/phoenician.png`} alt="Logo" className="homepage-logo" />
      <h1>Welcome to Project Manager</h1>
      <p>Explore our projects and detailed item listings.</p>
      <button onClick={() => navigate('/projects')} className="explore-button">
        Explore Projects
      </button>
    </div>
  );
}

export default HomePage;
