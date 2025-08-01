// src/components/ProtectedRoute.js
import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const ProtectedRoute = ({ children }) => {
    const { token } = useAuth();

    if (!token) {
        // If no token exists, redirect to the login page
        return <Navigate to="/login" />;
    }

    return children; // If token exists, render the child components (the actual page)
};

export default ProtectedRoute;