// src/App.js
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Box, Divider } from '@mui/material';

import Navbar from './components/Navbar';
import Login from './components/Login';
import Register from './components/Register';
import SkillAnalyzer from './components/SkillAnalyzer';
import JdComparator from './components/JdComparator';
import LengthAnalyzer from './components/LengthAnalyzer';
import ProtectedRoute from './components/ProtectedRoute'; // Import ProtectedRoute
import MyAnalyses from './components/MyAnalyses';

function HomePage() {
  return (
    <>
      <SkillAnalyzer />
      <Divider sx={{ my: 4 }} />
      <JdComparator />
      <Divider sx={{ my: 4 }} />
      <LengthAnalyzer />
    </>
  )
}

function App() {
  return (
    <Router>
      <Navbar />
      <Box className="App">
        <Routes>
          <Route path="/" element={<ProtectedRoute><HomePage /></ProtectedRoute>} />
          <Route path="/my-analyses" element={<ProtectedRoute><MyAnalyses /></ProtectedRoute>} /> {/* Add this route */}
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </Box>
    </Router>
  );
}
export default App;