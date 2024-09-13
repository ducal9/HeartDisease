import React, { useEffect, useState } from 'react';
import brandLogo from '../assets/navbar-brand.svg';

import footerIcon from '../assets/image-1.svg';
import './Main.css';
import { Link } from 'react-router-dom';

const Header = () => (
  <header className="header">
    <div className="navbar-container">
      <div className="navbar-content">
        <img src={brandLogo} alt="Brand Logo" className="navbar-brand"/>
        <nav className="navbar-menu">
        <Link to="/" className="navbar-link">Home</Link>
      
        <Link to="/heart-disease-prediction" className="navbar-link">Heart disease prediction</Link><button className="navbar-button">USER</button>
        </nav>
      </div>
    </div>
  </header>
);




const Snowflake = () => {
  const [x, setX] = useState(Math.random() * window.innerWidth); // Vị trí ngang ngẫu nhiên
  const [y, setY] = useState(Math.random() * window.innerHeight); // Bắt đầu phía trên màn hình

  useEffect(() => {
    const interval = setInterval(() => {
      setY((prevY) => {
        // Nếu y vượt qua chiều cao màn hình, reset y về -20 và random lại x
        if (prevY > window.innerHeight) {
          setX(Math.random() * window.innerWidth); // Random lại tọa độ x
          return -20; // Reset y để trái tim rơi lại từ đầu
        }
        return prevY + 5; // Tăng tọa độ y để tạo hiệu ứng rơi xuống
      });
    }, 50); // Điều chỉnh tốc độ rơi

    return () => clearInterval(interval); // Cleanup interval khi unmount
  }, []);

  return (
    <div
      style={{
        position: "fixed",
        top: `${y}px`, // Di chuyển theo chiều dọc
        left: `${x}px`, // Di chuyển theo chiều ngang
        width: "20px", // Kích thước trái tim
        height: "20px",
        backgroundImage: `url(${footerIcon})`,
        backgroundRepeat: "no-repeat", 
        backgroundSize: "cover",
        // backgroundColor: "red", // Màu trái tim
        // clipPath: "polygon(50% 0%, 61% 15%, 75% 15%, 85% 25%, 85% 45%, 50% 100%, 15% 45%, 15% 25%, 25% 15%, 39% 15%)", // Hình trái tim
        opacity: 0.8,
      }}
    />
  );
};

const SnowfallEffect = () => {
  const snowflakes = Array.from({ length: 100 }); // Tạo 100 trái tim rơi

  return (
    <>
      {snowflakes.map((_, index) => (
        <Snowflake key={index} />
      ))}
    </>
  );
};





const Body = () => (
  <main className="body">
    <section className="playlist">
      <h1 className="playlist-title">Playlist</h1>
      <div className="playlist-video">
        <div className="playlist-item">
          <iframe
            width="560"
            height="315"
            src="https://www.youtube.com/embed/236DefZTLiM?si=G87ooxYiHoDWqGXz"
            title="YouTube video player"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerPolicy="strict-origin-when-cross-origin"
            allowFullScreen
          ></iframe>
          <p className="playlist-description">Signs of heart disease</p>
        </div>
      </div>
    </section>
    <SnowfallEffect /> {/* Add the snowflake effect here */}
  </main>
);



const Footer = () => (
  <footer className="footer">
    <div className="footer-container">
      <div className="footer-columns">
        <div className="footer-column">
          <h3 className="footer-title">Contact</h3>
          <p>Telegram: @baphongnhach</p>
          <p>Technical Support: @baphongnhach</p>
          <p className="footer-disclaimer">© 2024Heart disease prediction</p>
        </div>
        <div className="footer-column">
          <h3 className="footer-title">Address</h3>
          <p>Ha Noi City</p>
        </div>
        <div className="footer-column">
          <h3 className="footer-title">Social</h3>
          <p>Twitter</p>
          <p>Telegram</p>
          <p>Youtube</p>
          <p>Facebook</p>
        </div>
        <img src={footerIcon} alt="Footer Icon" className="footer-icon"/>
      </div>
    </div>
  </footer>
);

const Main = () => (
  <div>
    <Header />
    <Body />
    <Footer />
  </div>
);

export default Main;
