import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom'; 
import axios from 'axios';
import './FindPolicyPage.css';
import SuggestedPolicyPage from './SuggestedPolicyPage';


const FindPolicyPage = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const queryParams = new URLSearchParams(location.search);

    const formData = {
        name: queryParams.get('name'),
        age: queryParams.get('age'),
        gender: queryParams.get('gender'),
        isSmoke: queryParams.get('isSmoke'),
        isDiabetic: queryParams.get('isDiabetic'),
        incomePerAnnum: queryParams.get('incomePerAnnum'),
        mail: queryParams.get('mail'),
        password: queryParams.get('password')
    };

    const handleFindPolicy = async () => {
        try {
            const response = await axios.post("http://localhost:3000/policy", formData);
            console.log("Response data:", response.data);
            if (response.status === 200) {
                navigate(`/suggested-policy`, { state: { suggestedPolicy: response.data.suggestedPolicy, mail:formData.mail } });
            } else {
                console.error('Failed to fetch suggested policy:', response.statusText);
            }
        } catch (error) {
            console.error('Error fetching suggested policy:', error.message);
        }
    };
    return (
        <div className="policy">
            <h2>Find Policy Page</h2>
            <div className="content">
                <p>Looking for the right insurance policy? </p> 
                <p>Our website makes it easy to find the perfect coverage for your needs. Simply provide us with some basic information such as your name, age, gender, and any relevant health habits. Our advanced algorithm will then analyze your data and suggest the best policy options tailored to your unique requirements. With just a few clicks, you'll be on your way to securing the peace of mind you deserve. Start your search today and discover the ideal insurance solution for you.</p>
            </div>
            <button class="find-policy-button" onClick={handleFindPolicy}>Find Policy</button>
        </div>
    );
};

export default FindPolicyPage;