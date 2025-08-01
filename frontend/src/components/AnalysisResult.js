// src/components/AnalysisResult.js
import React from 'react';
import SkillsResult from './SkillsResult';
import ComparatorResult from './ComparatorResult';
import LengthResult from './LengthResult';

const AnalysisResult = ({ analysis }) => {
    // This component checks the 'analysis_type' and renders the correct component
    switch (analysis.analysis_type) {
        case 'skills':
            return <SkillsResult data={analysis.results.detected_skills} />;
        case 'comparison':
            return <ComparatorResult data={analysis.results.comparison_results} />;
        case 'length':
            return <LengthResult data={analysis.results.length_analysis} />;
        default:
            // A fallback in case the type is unknown
            return <pre>{JSON.stringify(analysis.results, null, 2)}</pre>;
    }
};

export default AnalysisResult;