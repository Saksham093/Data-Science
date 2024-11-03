import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import HomePage from './pages/HomePage';
import ProjectsPage from './pages/ProjectsPage';
import ProjectDetailPage from './pages/ProjectDetailPage';
import ProjectItemsPage from './pages/ProjectItemsPage';
import NavBar from './components/NavBar';
import SearchDialog from './components/SearchDialog';
import axios from 'axios';
import './App.css';

function App() {
  const [items, setItems] = useState([]);
  const [expandedItems, setExpandedItems] = useState({});
  const [showSearchDialog, setShowSearchDialog] = useState(false);

  // Fetch items on mount
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/items/')
      .then(response => setItems(response.data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  // Expand path to item and scroll to it
  const expandAndScrollToItem = async (itemCode) => {
    const itemSegments = itemCode.split('.');
    let currentCode = '';

    for (let i = 0; i < itemSegments.length; i++) {
      currentCode = currentCode ? `${currentCode}.${itemSegments[i]}` : itemSegments[i];
      await expandItem(currentCode);
    }

    setTimeout(() => {
      const element = document.getElementById(itemCode);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }, 300);
  };

  // Expand specific item and fetch children if necessary
  const expandItem = async (itemCode) => {
    setExpandedItems((prev) => ({ ...prev, [itemCode]: true }));
    if (!items.some(item => item.ITEM.startsWith(`${itemCode}.`))) {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/items/?item_code=${itemCode}`);
        setItems((prevItems) => [...prevItems, ...response.data]);
      } catch (error) {
        console.error('Error fetching child items:', error);
      }
    }
  };

  return (
    <Router>
      <NavBar onSearchClick={() => setShowSearchDialog(true)} />

      {/* Search Dialog */}
      {showSearchDialog && (
        <SearchDialog
          items={items}
          onClose={() => setShowSearchDialog(false)}
          onNavigate={expandAndScrollToItem}
        />
      )}

      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/projects" element={<ProjectsPage />} />
        <Route path="/projects/:projectId" element={<ProjectDetailPage />} />
        <Route path="/projects/:projectId/items" element={<ProjectItemsPage 
          items={items}
          expandedItems={expandedItems}
          onExpand={expandItem}
        />} />
      </Routes>
    </Router>
  );
}

export default App;
