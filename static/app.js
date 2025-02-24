import React from "react";
import "./AboutMe.css"; // Import the CSS for styling

const AboutMe = () => {
  return (
    <div className="about-container">
      <div className="about-card">
        <img src="/profile.jpg" alt="Profile" className="profile-img" />
        <h1>Hello, I'm Jhanvi</h1>
        <p>
          I am a healthcare management professional with a background in 
          dentistry and an MBA in healthcare. My expertise lies in 
          pharmaceutical forecasting, opportunity assessments, and investment strategies.
        </p>
        <p>
          Currently, I am exploring new opportunities in pharmaceutical analytics 
          and interested in AI and wellness-based startups. In my free time, 
          I enjoy learning to code and experimenting with digital health ideas.
        </p>
      </div>
    </div>
  );
};

export default AboutMe;