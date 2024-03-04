import React from 'react';
import { Link } from 'react-router-dom';
import './LandingPage.css';
import welcomeImage from './healthinsurance.jpg'; 

const LandingPage = () => {
  return (
    <div className="landing-page">
      <div className="welcome-section">
        <div className="welcome-content">
          <h1>Welcome to Impact</h1>
          <p>At Impact, we understand the importance of having reliable health insurance coverage that meets your needs and protects your well-being. Our goal is to provide you with peace of mind by offering comprehensive health insurance plans tailored to your individual requirements.</p>
          <p>With our wide range of insurance options, you can find the perfect plan for you and your family, ensuring that you have access to quality healthcare when you need it most.</p>
          <p>Don't let uncertainty hold you back - let Impact be your partner in health and wellness.</p>
          <Link to="/register" className="get-started-button">Get Started</Link>

        </div>
        <div className="welcome-image">
          <img src={welcomeImage} alt="Welcome" />
        </div>
      </div>
      <div className="about-us-section">
        <h2>About Us</h2>
        <p>Impact is committed to providing exceptional health insurance solutions to individuals and families. With years of experience in the industry, we strive to offer comprehensive coverage, competitive premiums, and outstanding customer service.</p>
        <p>Our team of dedicated professionals is here to guide you through the process of selecting the right insurance plan for your needs. Whether you're looking for coverage for yourself, your family, or your employees, we have the expertise and resources to help you make informed decisions about your health insurance.</p>
        <p>At Impact, we believe that everyone deserves access to affordable and reliable health insurance. That's why we work tirelessly to find the best insurance solutions that fit your budget and provide you with the coverage you need to protect your health and well-being.</p>
      </div>
    </div>
  );
};

export default LandingPage;