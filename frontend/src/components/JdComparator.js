// src/components/JdComparator.js
import React, { useState } from 'react';
import axios from 'axios';
import { TextField, Button, Box, Typography, CircularProgress, Paper, Grid } from '@mui/material';

const JdComparator = () => {
    const [resumeText, setResumeText] = useState('');
    const [jdText, setJdText] = useState('');
    const [results, setResults] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async () => {
        setLoading(true);
        setResults(null);
        try {
            // Send a POST request to our new backend endpoint
            const response = await axios.post('http://localhost:8000/compare-resume-jd/', {
                resume_text: resumeText,
                jd_text: jdText
            });
            setResults(response.data.comparison_results);
        } catch (error) {
            console.error("There was an error comparing the texts:", error);
            alert("Failed to compare. Please check the console for details.");
        }
        setLoading(false);
    };

    return (
        <Box sx={{ my: 4 }}>
            <Typography variant="h5" gutterBottom>Compare Resume to Job Description</Typography>
            <Paper elevation={2} sx={{ p: 3 }}>
                <Grid container spacing={2}>
                    <Grid item xs={6}>
                        <TextField
                            fullWidth
                            multiline
                            rows={10}
                            variant="outlined"
                            label="Paste Resume Text Here"
                            value={resumeText}
                            onChange={(e) => setResumeText(e.target.value)}
                        />
                    </Grid>
                    <Grid item xs={6}>
                        <TextField
                            fullWidth
                            multiline
                            rows={10}
                            variant="outlined"
                            label="Paste Job Description Text Here"
                            value={jdText}
                            onChange={(e) => setJdText(e.target.value)}
                        />
                    </Grid>
                </Grid>
                <Button sx={{ mt: 2 }} variant="contained" onClick={handleSubmit} disabled={loading || !resumeText || !jdText}>
                    {loading ? <CircularProgress size={24} /> : 'Compare'}
                </Button>
            </Paper>

            {results && (
                <Box sx={{ mt: 4 }}>
                    <Typography variant="h6">Comparison Results:</Typography>
                    <Paper elevation={2} sx={{ p: 2, mt: 1, bgcolor: '#e8f5e9' }}>
                        <pre>{JSON.stringify(results, null, 2)}</pre>
                    </Paper>
                </Box>
            )}
        </Box>
    );
};

export default JdComparator;