
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Main from './components/Main';
import MainHeart from './components/MainHeart';



const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/heart-disease-prediction" element={<MainHeart />} />
      
      </Routes>
    </Router>
  );
}

export default App;
