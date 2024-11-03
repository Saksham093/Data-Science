import React, { useState } from 'react';
import './SearchDialog.css';

function SearchDialog({ items, onClose, onNavigate }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  // Handle search input change
  const handleSearchChange = (e) => {
    const term = e.target.value;
    setSearchTerm(term);

    if (term.trim() === '') {
      setSearchResults([]);
      return;
    }

    // Filter items by search term in DESCRIPTION
    const results = items.filter((item) => 
      item.DESCRIPTION && item.DESCRIPTION.toLowerCase().includes(term.toLowerCase())
    );

    setSearchResults(results);
  };

  // Render search results
  const renderResults = () => {
    return searchResults.map((item, index) => (
      <div key={index} className="search-result" onClick={() => onNavigate(item.ITEM)}>
        <table className="search-result-table">
          <thead>
            <tr>
              <th>Description</th>
              <th>Quantity</th>
              <th>Unit</th>
              <th>Unit Price (AED)</th>
              <th>Total Price (AED)</th>
              <th>Remarks</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{item.DESCRIPTION || '-'}</td>
              <td>{item.QUANTITY || '-'}</td>
              <td>{item.UNIT || '-'}</td>
              <td>{item["UNIT PRICE(AED)"] || '-'}</td>
              <td>{item["TOTAL PRICE (AED)"] || '-'}</td>
              <td>{item.REMARKS || '-'}</td>
            </tr>
          </tbody>
        </table>
      </div>
    ));
  };

  return (
    <div className="search-dialog-overlay">
      <div className="search-dialog">
        <button className="close-button" onClick={onClose}>✕</button>
        <h2>Search</h2>
        <input
          type="text"
          value={searchTerm}
          onChange={handleSearchChange}
          placeholder="Search by description..."
          className="search-input"
        />
        <div className="search-results">
          {renderResults()}
        </div>
      </div>
    </div>
  );
}

export default SearchDialog;
