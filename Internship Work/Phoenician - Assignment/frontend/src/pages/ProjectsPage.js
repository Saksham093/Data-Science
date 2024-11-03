// src/pages/ProjectsPage.js

import React from 'react';
import { useNavigate } from 'react-router-dom';
import './ProjectsPage.css';

function ProjectsPage() {
  const navigate = useNavigate();
  const projects = [
    { id: 1, name: "Damac Lagoons - Central Hub", description: "Technical & Financial Proposal for Landscaping Works for Damac Lagoons Central Hub" },
    { id: 2, name: "Project Beta", description: "Another interesting project" },
  ];

  return (
    <div className="projects-page">
      <h1>Projects</h1>
      <div className="project-list">
        {projects.map(project => (
          <div key={project.id} onClick={() => navigate(`/projects/${project.id}`)} className="project-card">
            <h2>{project.name}</h2>
            <p>{project.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ProjectsPage;
