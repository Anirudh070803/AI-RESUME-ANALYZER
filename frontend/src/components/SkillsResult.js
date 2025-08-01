// src/components/SkillsResult.js
import React from 'react';
import { Box, Typography, Chip } from '@mui/material';

const SkillsResult = ({ data }) => {
    // The data comes in as { "PROGRAMMING": [...], "TOOLS": [...], "ROLES": [...] }
    const categories = Object.keys(data);

    return (
        <Box>
            {categories.map(category => (
                <Box key={category} sx={{ mb: 2 }}>
                    <Typography variant="subtitle1" sx={{ fontWeight: 'bold', textTransform: 'capitalize' }}>
                        {category.toLowerCase()}
                    </Typography>
                    {data[category].length > 0 ? (
                        <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1, mt: 1 }}>
                            {data[category].map(skill => (
                                <Chip label={skill} key={skill} color="primary" variant="outlined" />
                            ))}
                        </Box>
                    ) : (
                        <Typography variant="body2" sx={{ fontStyle: 'italic', color: 'text.secondary' }}>
                            None detected.
                        </Typography>
                    )}
                </Box>
            ))}
        </Box>
    );
};

export default SkillsResult;