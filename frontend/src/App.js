// src/App.js
import './App.css';
import SkillAnalyzer from './components/SkillAnalyzer';
import JdComparator from './components/JdComparator';
import LengthAnalyzer from './components/LengthAnalyzer';
import { Divider } from '@mui/material';


function App() {
  return (
    <div className="App">
      <h1>AI Resume Analyzer</h1>
      <SkillAnalyzer />
      <Divider sx={{ my: 4 }} />
      <JdComparator />
      <Divider sx={{ my: 4 }} />
      <LengthAnalyzer />
    </div>
  );
}

export default App;