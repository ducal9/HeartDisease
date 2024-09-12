import React from 'react';
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

const Body = () => (
  <main className="body">
    <section className="playlist">
      <h1 className="playlist-title">Playlist</h1>
      <div className="playlist-video">
        <div className="playlist-item">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/236DefZTLiM?si=G87ooxYiHoDWqGXz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
          <p className="playlist-description">Signs of heart disease</p>
        </div>
      </div>
    </section>
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
