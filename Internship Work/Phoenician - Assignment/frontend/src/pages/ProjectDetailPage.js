// src/pages/ProjectDetailPage.js

import React, { useEffect, useState } from 'react';
import './ProjectDetailPage.css';
import Papa from 'papaparse';
import { useNavigate, useParams } from 'react-router-dom';

function ProjectDetailPage() {
  const [csvData, setCsvData] = useState([]);
  
  const project = {
    id: 1,
    ref: "PTS-QTN2023-Q065-L-0009A",
    date: "12th February 2024",
    attention: "Engr. Maher Ghossaini - Director Procurement",
    subject: "Technical & Financial Proposal for Landscaping Works for Damac Lagoons Central Hub\n (OPTION 1 - LANDSCAPE FURNITURE AS PER VALUE ENGINEERING, INCLUDING PURCHASING OF PALM AND TREES)",
    name: "Damac Lagoons - Central Hub",
    imageUrl: "/assets/images/project_image.png",
  };

  const { projectId } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    // Load and parse CSV file from the public folder
    Papa.parse(`${process.env.PUBLIC_URL}/data/page_Data_0.csv`, {
      download: true,
      header: false,
      complete: (result) => {
        setCsvData(result.data);
      },
    });
  }, []);
  

  return (
    <div className="project-detail-page">

      <h1>{project.name}</h1>
      
      <div className="project-detail-main">
        <div className="project-info">
          <table className="info-table">
            <tbody>
              <tr><td>Name:</td><td><b>{project.name}</b></td></tr>
              <tr><td>Ref:</td><td><b>{project.ref}</b></td></tr>
              <tr><td>Date:</td><td><b>{project.date}</b></td></tr>
              <tr><td>Attention:</td><td><b>{project.attention}</b></td></tr>
              <tr><td>Subject:</td><td><b>{project.subject}</b></td></tr>
            </tbody>
          </table>
        </div>
        <div className="project-image">
          <img src={project.imageUrl} alt={project.name} />
        </div>
      </div>
      
      <h2>Project Summary</h2>

      <table className="summary-table">
  <thead>
    <tr>
      {csvData.length > 0 &&
        Object.keys(csvData[0]).map((header, index) => (
          <th key={index}>{header}</th>
        ))
      }
    </tr>
  </thead>
  <tbody>
    {csvData.map((row, rowIndex) => (
      <tr key={rowIndex}>
        {Object.keys(csvData[0]).map((key, colIndex) => (
          <td key={colIndex}>{row[key] || ''}</td>
        ))}
      </tr>
    ))}
  </tbody>
</table>


      <button onClick={() => navigate(`/projects/${projectId}/items`)} className="view-items-button">
        View Project Items
      </button>
    </div>
  );
}

export default ProjectDetailPage;
