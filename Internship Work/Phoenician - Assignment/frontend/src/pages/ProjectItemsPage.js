// import React, { useEffect, useState } from 'react';
// import { useParams } from 'react-router-dom';
// import axios from 'axios';

// function ProjectItemsPage() {
//   const { id } = useParams();
//   const [details, setDetails] = useState([]);

//   useEffect(() => {
//     axios.get(`/api/projects/${id}/details`).then((response) => {
//       setDetails(response.data);
//     });
//   }, [id]);

//   return (
//     <div>
//       <h1>Project Details</h1>
//       {details.map((detail, index) => (
//         <div key={index}>
//           <h3>{detail.title}</h3>
//           <ul>
//             {detail.items.map((item, i) => (
//               <li key={i}>
//                 {item.title}
//                 <ul>
//                   {item.subitems.map((subitem, j) => (
//                     <li key={j}>{subitem}</li>
//                   ))}
//                 </ul>
//               </li>
//             ))}
//           </ul>
//         </div>
//       ))}
//     </div>
//   );
// }

// export default ProjectItemsPage;




// src/pages/ProjectItemsPage.js

import React from 'react';
import NestedList from '../components/NestedList';
import './ProjectItemsPage.css';

function ProjectItemsPage() {
  return (
    <div className="project-items-page">
      <NestedList />
    </div>
  );
}

export default ProjectItemsPage;
