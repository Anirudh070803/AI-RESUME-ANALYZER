import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { Box, Paper, Typography, TextField, Button } from '@mui/material';

const Register = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            await axios.post('http://localhost:8000/users/', {
                email: email,
                password: password
            });
            alert('Registration successful! Please log in.');
            navigate('/login');
        } catch (error) {
            console.error('Registration failed:', error.response.data.detail);
            alert(`Registration failed: ${error.response.data.detail}`);
        }
    };

    return (
        <Paper elevation={3} sx={{ p: 4, mt: 4, maxWidth: 400, mx: 'auto' }}>
            <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
                <Typography component="h1" variant="h5" align="center">
                    Register
                </Typography>
                <TextField 
                    margin="normal" 
                    required 
                    fullWidth 
                    id="email" 
                    label="Email Address" 
                    name="email" 
                    autoComplete="email" 
                    autoFocus
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <TextField 
                    margin="normal" 
                    required 
                    fullWidth 
                    name="password" 
                    label="Password" 
                    type="password" 
                    id="password" 
                    autoComplete="new-password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <Button 
                    type="submit" 
                    fullWidth 
                    variant="contained" 
                    sx={{ mt: 3, mb: 2 }}
                >
                    Sign Up
                </Button>
            </Box>
        </Paper>
    );
};
export default Register;