// src/components/LengthResult.js
import React from 'react';
import { Box, Typography, List, ListItem, ListItemIcon, ListItemText } from '@mui/material';
import { BarChart, AccessTime, Comment } from '@mui/icons-material';

const LengthResult = ({ data }) => {
    // The data comes in as { "word_count": 57, "estimated_reading_time_minutes": 0.3, "assessment": "..." }

    return (
        <Box>
            <List>
                <ListItem>
                    <ListItemIcon>
                        <BarChart />
                    </ListItemIcon>
                    <ListItemText primary="Word Count" secondary={data.word_count} />
                </ListItem>
                <ListItem>
                    <ListItemIcon>
                        <AccessTime />
                    </ListItemIcon>
                    <ListItemText primary="Estimated Reading Time" secondary={`${data.estimated_reading_time_minutes} minutes`} />
                </ListItem>
                <ListItem>
                    <ListItemIcon>
                        <Comment />
                    </ListItemIcon>
                    <ListItemText primary="Assessment" secondary={data.assessment} />
                </ListItem>
            </List>
        </Box>
    );
};

export default LengthResult;