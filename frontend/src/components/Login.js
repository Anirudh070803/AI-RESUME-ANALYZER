import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import axios from 'axios';
import { Box, Paper, Typography, TextField, Button } from '@mui/material';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const { login } = useAuth();
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            // Note: FastAPI's OAuth2 form expects 'username' and 'password'
            const formData = new URLSearchParams();
            formData.append('username', email);
            formData.append('password', password);

            const response = await axios.post('http://localhost:8000/token', formData, {
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            });

            login(response.data.access_token);
            navigate('/'); // Redirect to homepage on successful login
        } catch (error) {
            console.error('Login failed:', error.response.data.detail);
            alert(`Login failed: ${error.response.data.detail}`);
        }
    };

    return (
        <Paper elevation={3} sx={{ p: 4, mt: 4, maxWidth: 400, mx: 'auto' }}>
            <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
                <Typography component="h1" variant="h5" align="center">
                    Log In
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
                    autoComplete="current-password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <Button 
                    type="submit" 
                    fullWidth 
                    variant="contained" 
                    sx={{ mt: 3, mb: 2 }}
                >
                    Sign In
                </Button>
            </Box>
        </Paper>
    );
};
export default Login;