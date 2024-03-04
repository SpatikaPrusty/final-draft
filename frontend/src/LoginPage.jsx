import React, { useState } from 'react';
import { Navigate } from 'react-router-dom';
import axios from 'axios';
import './LoginPage.css';

const LoginPage = () => {
    const [mail, setMail] = useState('');
    const [password, setPassword] = useState('');
    const [submitted, setSubmitted] = useState(false);
    const [user, setUser] = useState(null);
    const [error, setError] = useState('');

    const handleFindPolicy = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://localhost:3000/login", { mail, password });
            const { token, user } = response.data;
            localStorage.setItem("authToken", token);

            setSubmitted(true);
            setUser(user);
        } catch (error) {
            setError('Invalid email or password. Please try again.');
            console.error('Error logging in:', error.message);
        }
    };

    if (submitted && user) {
        return <Navigate to={`/findpolicy?name=${user.name}&age=${user.age}&gender=${user.gender}&isSmoke=${user.isSmoke}&isDiabetic=${user.isDiabetic}&incomePerAnnum=${user.incomePerAnnum}&mail=${user.mail}&password=${user.password}`} />;
    }

    return (
        <div className="login-container">
            <h2>Login</h2>
            {error && <div className="error-message">{error}</div>}
            <form onSubmit={handleFindPolicy} className="login-form">
                <div className="form-group">
                    <label htmlFor="email">Email:</label>
                    <input
                        type="email"
                        id="email"
                        value={mail}
                        onChange={(e) => setMail(e.target.value)}
                        required
                        className="form-control"
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                        className="form-control"
                    />
                </div>
                <button type="submit" className="btn-login">Login</button>
            </form>
        </div>
    );
};

export default LoginPage;
