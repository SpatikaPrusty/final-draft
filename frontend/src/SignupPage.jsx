import React from 'react';
import { useState } from 'react';
import { Navigate } from 'react-router-dom';
import axios from 'axios'; 
import './SignupPage.css'; 

const SignupPage = () => {

    const [formData, setFormData] = useState({
        name: '',
        age: 0,
        gender: '',
        isSmoke: false,
        isDiabetic: false,
        incomePerAnnum: 0,
        mail: '',
        password: ''
    });
    const [submitted, setSubmitted] = useState(false);

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: type === 'checkbox' ? checked : value
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        try {
            await axios.post('https://backend-claims.onrender.com/register', formData);
            setSubmitted(true);
        } catch (error) {
            console.error('Error submitting form:', error);
        }
    };
    if (submitted) {
        return <Navigate to={`/findpolicy?name=${formData.name}&age=${formData.age}&gender=${formData.gender}&isSmoke=${formData.isSmoke}&isDiabetic=${formData.isDiabetic}&incomePerAnnum=${formData.incomePerAnnum}&mail=${formData.mail}&password=${formData.password}`} />;
    }
    return (
        <div className="signup-container">
            <h2>Sign-up</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Name:
                    <input
                        type="text"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        placeholder="Please enter your name."
                    />
                </label>
                <br />
                <label>
                    Age:
                    <input
                        type="number"
                        name="age"
                        value={formData.age}
                        onChange={handleChange}
                        inputMode="numeric" 
                        style={{ MozAppearance: 'textfield' }}
                    />
                </label>
                <br />
                <label>
                    Gender:
                    <input
                        type="text"
                        name="gender"
                        value={formData.gender}
                        onChange={handleChange}
                    />
                </label>
                <br />
                <label>
                    Smoke:
                    <input
                    type="checkbox"
                    name="isSmoke"
                    checked={formData.isSmoke}
                    onChange={handleChange}
                    />
                </label>
                <br />
                <label>
                    Diabetic:
                    <input
                    type="checkbox"
                    name="isDiabetic"
                    checked={formData.isDiabetic}
                    onChange={handleChange}
                    />
                </label>
                <br />
                <label>
                    Income Per Annum:
                    <input
                        type="number"
                        name="incomePerAnnum"
                        value={formData.incomePerAnnum}
                        onChange={handleChange}
                        inputMode="numeric" 
                        style={{ MozAppearance: 'textfield' }} 
                    />
                </label>
                <br />
                <label>
                    Mail:
                    <input
                    type="email"
                    name="mail"
                    value={formData.mail}
                    onChange={handleChange}
                    />
                </label>
                <br />
                <label>
                    Password:
                    <input
                    type="password"
                    name="password"
                    value={formData.password}
                    onChange={handleChange}
                    placeholder='Password should consist atleast one number'
                    />
                </label>
                <br />
                <button type="submit" className="btn-submit">Submit</button>
            </form>
        </div>
    );
};

export default SignupPage;
