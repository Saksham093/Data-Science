import React from 'react';
import './Sidebar.css';

function Sidebar({ items, onNavigate }) {
  // Recursive function to render the tree structure
  const renderTree = (parentCode) => {
    const level = parentCode ? parentCode.split('.').length + 1 : 1;

    return items
      .filter(item => {
        const itemLevel = item.ITEM.split('.').length;
        return item.ITEM.startsWith(parentCode ? `${parentCode}.` : '') && itemLevel === level;
      })
      .map((item) => (
        <div key={item.ITEM} className="sidebar-item" style={{ marginLeft: `${(level - 1) * 15}px` }}>
          <span className="sidebar-link" onClick={() => onNavigate(item.ITEM)}>
            {item.ITEM} - {item.DESCRIPTION}
          </span>
          {renderTree(item.ITEM)}
        </div>
      ));
  };

  return (
    <div className="sidebar">
      <h2>Contents</h2>
      {renderTree('')}
    </div>
  );
}

export default Sidebar;
