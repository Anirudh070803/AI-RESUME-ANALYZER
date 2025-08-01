// src/components/ComparatorResult.js
import React from 'react';
import { Box, Typography, Chip, LinearProgress } from '@mui/material';

const ComparatorResult = ({ data }) => {
    const scorePercentage = data.similarity_score * 100;

    return (
        <Box>
            <Typography variant="subtitle1" sx={{ fontWeight: 'bold' }}>
                Similarity Score: {scorePercentage.toFixed(0)}%
            </Typography>
            <LinearProgress variant="determinate" value={scorePercentage} sx={{ my: 1, height: 10, borderRadius: 5 }} />

            <Typography variant="subtitle1" sx={{ fontWeight: 'bold', mt: 3 }}>
                Suggested Keywords to Add:
            </Typography>
            {data.suggested_keywords.length > 0 ? (
                <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1, mt: 1 }}>
                    {data.suggested_keywords.map(keyword => (
                        <Chip label={keyword} key={keyword} color="success" variant="outlined" />
                    ))}
                </Box>
            ) : (
                <Typography variant="body2" sx={{ fontStyle: 'italic', color: 'text.secondary', mt: 1 }}>
                    No major keywords missing!
                </Typography>
            )}
        </Box>
    );
};

export default ComparatorResult;