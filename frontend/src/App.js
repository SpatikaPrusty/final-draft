
import React from 'react';
import './App.css';
import LandingPage from './LandingPage';
import LoginPage from './LoginPage';
import SignupPage from './SignupPage';
// import ProfilePage from './ProfilePage';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import FindPolicyPage from './FindPolicyPage';
import SuggestedPolicyPage from './SuggestedPolicyPage.jsx'

function App() {
  return (
    <Router>
      <div className="app">
        <header className="navbar">
          <nav>
            <ul>
              <li><Link to="/">Home</Link></li>
              <li><a href="/login">Login</a></li>
              <li><a href="/register">Signup</a></li> 
            </ul>
          </nav>
        </header>
        <Routes>
          <Route path="/" exact element={<LandingPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<SignupPage />} /> 
          <Route path="/findpolicy" element={<FindPolicyPage />}/>
          <Route path="/suggested-policy" element={<SuggestedPolicyPage />} />
        </Routes>
      </div>
    </Router>
  );
}



export default App;
