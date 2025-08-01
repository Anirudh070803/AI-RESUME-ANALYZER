// src/components/LengthAnalyzer.js
import React, { useState } from 'react';
import axios from 'axios';
import { TextField, Button, Box, Typography, CircularProgress, Paper } from '@mui/material';
import LengthResult from './LengthResult'; // Import the new component

const LengthAnalyzer = () => {
    const [resumeText, setResumeText] = useState('');
    const [results, setResults] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async () => {
        setLoading(true);
        setResults(null);
        try {
            const response = await axios.post('http://localhost:8000/analyze-length/', {
                resume_text: resumeText
            });
            setResults(response.data.length_analysis);
        } catch (error) {
            console.error("There was an error analyzing the length:", error);
            alert("Failed to analyze length. Please check the console for details.");
        }
        setLoading(false);
    };

    return (
        <Box sx={{ my: 4 }}>
            <Typography variant="h5" gutterBottom>Resume Length Analysis</Typography>
            <Paper elevation={2} sx={{ p: 3 }}>
                <TextField
                    fullWidth
                    multiline
                    rows={8}
                    variant="outlined"
                    label="Paste Resume Text Here"
                    value={resumeText}
                    onChange={(e) => setResumeText(e.target.value)}
                    sx={{ mb: 2 }}
                />
                <Button variant="contained" onClick={handleSubmit} disabled={loading || !resumeText}>
                    {loading ? <CircularProgress size={24} /> : 'Analyze Length'}
                </Button>
            </Paper>

            {results && (
                <Box sx={{ mt: 4 }}>
                    <Typography variant="h6">Length Analysis Results:</Typography>
                    <Paper elevation={2} sx={{ p: 2, mt: 1, bgcolor: '#fff3e0' }}>
                       {/* Use the new component instead of the <pre> tag */}
                       <LengthResult data={results} />
                    </Paper>
                </Box>
            )}
        </Box>
    );
};

export default LengthAnalyzer;