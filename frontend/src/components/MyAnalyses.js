import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Box, Paper, Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, CircularProgress } from '@mui/material';
import AnalysisResult from './AnalysisResult';
import { useAuth } from '../context/AuthContext';

const MyAnalyses = () => {
    const [analyses, setAnalyses] = useState([]);
    const [loading, setLoading] = useState(true);
    const { token } = useAuth();

    useEffect(() => {
        const fetchAnalyses = async () => {
            if (token) {
                try {
                    const response = await axios.get('http://localhost:8000/analyses/');
                    setAnalyses(response.data);
                } catch (error) {
                    console.error('Failed to fetch analyses:', error);
                }
                setLoading(false);
            }
        };

        fetchAnalyses();
    }, [token]);

    if (loading) {
        return <CircularProgress />;
    }

    return (
        <Box sx={{ my: 4 }}>
            <Typography variant="h4" gutterBottom>My Past Analyses</Typography>
            <TableContainer component={Paper}>
                <Table sx={{ minWidth: 650 }} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell sx={{ fontWeight: 'bold' }}>ID</TableCell>
                            <TableCell sx={{ fontWeight: 'bold' }}>Analysis Type</TableCell>
                            <TableCell sx={{ fontWeight: 'bold' }}>Results</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {analyses.map((row) => (
                            <TableRow key={row.id}>
                                <TableCell>{row.id}</TableCell>
                                <TableCell sx={{textTransform: 'capitalize'}}>{row.analysis_type}</TableCell>
                                <TableCell>
                                    {/* Use the new smart component here! */}
                                    <AnalysisResult analysis={row} />
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </Box>
    );
};

export default MyAnalyses;