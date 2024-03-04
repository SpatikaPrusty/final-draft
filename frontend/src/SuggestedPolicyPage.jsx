import React from 'react';
import { useLocation } from 'react-router-dom';
import axios from 'axios';
import './SuggestedPolicy.css'

const SuggestedPolicyPage = () => {

  const location = useLocation();
  
  const suggestedPolicy = location.state && location.state.suggestedPolicy;
  const mail=location.state?.mail;
  const handleBuyNow = async () => {
    try {
      
      // Make a request to your backend to store the user_id and policy number
      const response = await axios.post('http://localhost:3000/policyHolder', {
        mail: mail,
        policyNum: suggestedPolicy.policyNum,
      });

      if (response.status === 200) {
        // Handle success
        console.log('Policy purchased successfully');
      } else {
        // Handle error
        console.error('Failed to purchase policy:', response.statusText);
      }
    } catch (error) {
      // Handle error
      console.error('Error purchasing policy:', error.message);
    }
  };

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
        <button onClick={handleBuyNow}>Buy Now</button>
    </div>
  );
};

export default SuggestedPolicyPage;