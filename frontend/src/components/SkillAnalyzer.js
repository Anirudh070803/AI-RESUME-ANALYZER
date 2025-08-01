// src/components/SkillAnalyzer.js
import React, { useState } from 'react';
import axios from 'axios';
import { TextField, Button, Box, Typography, CircularProgress, Paper } from '@mui/material';
import SkillsResult from './SkillsResult'; // Import the new component

const SkillAnalyzer = () => {
    const [resumeText, setResumeText] = useState('');
    const [skills, setSkills] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async () => {
        setLoading(true);
        setSkills(null);
        try {
            const response = await axios.post('http://localhost:8000/analyze-skills/', {
                resume_text: resumeText
            });
            // The results are nested in the response
            setSkills(response.data.results.detected_skills);
        } catch (error) {
            console.error("There was an error analyzing the skills:", error);
            alert("Failed to analyze skills. Please check the console for details.");
        }
        setLoading(false);
    };

    return (
        <Box sx={{ my: 4 }}>
            <Typography variant="h5" gutterBottom>Analyze Skills</Typography>
            <Paper elevation={2} sx={{ p: 3 }}>
                <TextField
                    fullWidth
                    multiline
                    rows={10}
                    variant="outlined"
                    label="Paste Resume Text Here"
                    value={resumeText}
                    onChange={(e) => setResumeText(e.target.value)}
                    sx={{ mb: 2 }}
                />
                <Button variant="contained" onClick={handleSubmit} disabled={loading || !resumeText}>
                    {loading ? <CircularProgress size={24} /> : 'Analyze Skills'}
                </Button>
            </Paper>

            {skills && (
                <Box sx={{ mt: 4 }}>
                    <Typography variant="h6">Detected Skills:</Typography>
                    <Paper elevation={2} sx={{ p: 2, mt: 1, bgcolor: '#e3f2fd' }}>
                        {/* Use the new component instead of the <pre> tag */}
                        <SkillsResult data={skills} />
                    </Paper>
                </Box>
            )}
        </Box>
    );
};

export default SkillAnalyzer;