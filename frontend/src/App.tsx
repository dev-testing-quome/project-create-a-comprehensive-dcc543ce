import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import PermitApplicationPage from './pages/PermitApplicationPage';
import PermitStatusPage from './pages/PermitStatusPage';

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/apply" element={<PermitApplicationPage />} />
        <Route path="/status" element={<PermitStatusPage />} />
        {/* Add more routes as needed */}
      </Routes>
    </BrowserRouter>
  );
};

export default App;