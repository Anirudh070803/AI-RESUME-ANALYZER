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
          {/* Wrap the HomePage Route with our new ProtectedRoute */}
          <Route 
            path="/" 
            element={
              <ProtectedRoute>
                <HomePage />
              </ProtectedRoute>
            } 
          />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </Box>
    </Router>
  );
}

export default App;