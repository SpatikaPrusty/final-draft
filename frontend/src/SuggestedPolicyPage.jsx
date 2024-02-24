import React from 'react';
import { useLocation } from 'react-router-dom';
import './SuggestedPolicy.css'

const SuggestedPolicyPage = () => {

  const location = useLocation();
  
  const suggestedPolicy = location.state && location.state.suggestedPolicy;
  
  if (!suggestedPolicy) {
    return <div>No suggested policy found.</div>;
  }
  
  return (
    <div className="suggested-policy">
      <h1>Suggested Policy</h1>
        <div className="content">
            <p>Policy Number: {suggestedPolicy.policyNum}</p>
            <p>Premium: {suggestedPolicy.premium}</p>
            <p>Sum Assured: {suggestedPolicy.sumAssured}</p>
            <p>Policy Term: {suggestedPolicy.policyTerm}</p>
            <p>Policy Frequency: {suggestedPolicy.policyFrequency}</p>
        </div>
    </div>
  );
};

export default SuggestedPolicyPage;
