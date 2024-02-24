import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProfilePage = () => {
  const [profileData, setProfileData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProfileData = async () => {
        const token = localStorage.getItem('authToken');
        if (!token) {
            setError('User not authenticated');
            return;
        }
    
        try {
            const response = await axios.get('http://localhost:3000/api/profile', {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });
            setProfileData(response.data);
        } catch (error) {
            setError(error.response.data.message);
        }
    };    

    fetchProfileData();

    // Cleanup function to cancel any pending requests
    return () => {
      // Cleanup code if needed
    };
  }, []);

  return (
    <div>
      <h2>Profile</h2>
      {error && <p>{error}</p>}
      {profileData && (
        <div>
          <p>Name: {profileData.name}</p>
          <p>Age: {profileData.age}</p>
          <p>Gender: {profileData.gender}</p>
          <p>Is Smoke: {profileData.isSmoke ? 'Yes' : 'No'}</p>
          <p>Is Diabetic: {profileData.isDiabetic ? 'Yes' : 'No'}</p>
          <p>Income Per Annum: {profileData.incomePerAnnum}</p>
          <p>Email: {profileData.mail}</p>
        </div>
      )}
    </div>
  );
};

export default ProfilePage;
