import React, { useState } from 'react';
import brandLogo from '../assets/navbar-brand.svg';
import footerIcon from '../assets/image-1.svg';

import './MainHeart.css';
import './hdp.css';
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




const Body = () => {
  
  const [formData, setFormData] = useState({
    age: '',
    sex: '',
    chestPainType: '',
    restingBloodPressure: '',
    serumCholesterol: '',
    fastingBloodSugar: '',
    electrocardiographicResults: '',
    maxHeartRate: '',
    exerciseInducedAngina: '',
    oldpeak: '',
    slopeOfPeakExerciseSTSegment: '',
    numMajorVessels: '',
    thal: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  return (
    <main className="body">
      <section className="playlist">
        <h1 className="playlist-title">Heart Disease Prediction</h1>
        <div className="hdp">
          <form>
            <label>
              Age (Tuổi):
              <input
                type="number"
                name="age"
                min="29"
                max="77"
                value={formData.age}
                onChange={handleChange}
              />
            </label>

            <label>
              Sex (Giới tính):
              <div>
                <label>
                  <input
                    type="radio"
                    name="sex"
                    value="0"
                    checked={formData.sex === '0'}
                    onChange={handleChange}
                  />
                  Female (Nữ)
                </label>
                <label>
                  <input
                    type="radio"
                    name="sex"
                    value="1"
                    checked={formData.sex === '1'}
                    onChange={handleChange}
                  />
                  Male (Nam)
                </label>
              </div>
            </label>

            <label>
              Chest Pain Type (Loại đau ngực):
              <select
                name="chestPainType"
                value={formData.chestPainType}
                onChange={handleChange}
              >
                <option value="0">Typical angina (Đau thắt ngực điển hình)</option>
                <option value="1">Atypical angina (Đau thắt ngực không điển hình)</option>
                <option value="2">Non-anginal pain (Đau không liên quan đến thắt ngực)</option>
                <option value="3">Asymptomatic (Không có triệu chứng)</option>
              </select>
            </label>

            <label>
              Resting Blood Pressure (Huyết áp lúc nghỉ):
              <input
                type="number"
                name="restingBloodPressure"
                min="80"
                max="250"
                value={formData.restingBloodPressure}
                onChange={handleChange}
              />
            </label>

            <label>
              Serum Cholesterol in mg/dl (Cholesterol huyết thanh):
              <input
                type="number"
                name="serumCholesterol"
                min="120"
                max="500"
                value={formData.serumCholesterol}
                onChange={handleChange}
              />
            </label>

            <label>
              Fasting Blood Sugar &gt; 120 mg/dl (Đường huyết lúc đói &gt; 120 mg/dl):
              <div> 
                <label>
                  <input
                    type="radio"
                    name="fastingBloodSugar"
                    value="0"
                    checked={formData.fastingBloodSugar === '0'}
                    onChange={handleChange}
                  />
                  False
                </label>
                <label>
                  <input
                    type="radio"
                    name="fastingBloodSugar"
                    value="1"
                    checked={formData.fastingBloodSugar === '1'}
                    onChange={handleChange}
                  />
                  True
                </label>
              </div>
            </label>

            <label>
              Resting Electrocardiographic Results (Kết quả điện tâm đồ lúc nghỉ):
              <select
                name="electrocardiographicResults"
                value={formData.electrocardiographicResults}
                onChange={handleChange}
              >
                <option value="0">Normal (Bình thường)</option>
                <option value="1">ST-T wave abnormality (Bất thường ST-T)</option>
                <option value="2">Left ventricular hypertrophy (Phì đại thất trái)</option>
              </select>
            </label>

            <label>
              Maximum Heart Rate Achieved (Nhịp tim tối đa khi tập thể dục):
              <input
                type="number"
                name="maxHeartRate"
                min="60"
                max="200"
                value={formData.maxHeartRate}
                onChange={handleChange}
              />
            </label>

            <label>
              Exercise Induced Angina (Đau thắt ngực do gắng sức):
              <div>
                <label>
                  <input
                    type="radio"
                    name="exerciseInducedAngina"
                    value="0"
                    checked={formData.exerciseInducedAngina === '0'}
                    onChange={handleChange}
                  />
                  No
                </label>
                <label>
                  <input
                    type="radio"
                    name="exerciseInducedAngina"
                    value="1"
                    checked={formData.exerciseInducedAngina === '1'}
                    onChange={handleChange}
                  />
                  Yes
                </label>
              </div>
            </label>

            <label>
              Oldpeak (ST Depression Induced by Exercise Relative to Rest):
              <input
                type="number"
                step="0.1"
                name="oldpeak"
                value={formData.oldpeak}
                onChange={handleChange}
              />
            </label>

            <label>
              The Slope of the Peak Exercise ST Segment (Độ dốc của đoạn ST khi tập luyện):
              <select
                name="slopeOfPeakExerciseSTSegment"
                value={formData.slopeOfPeakExerciseSTSegment}
                onChange={handleChange}
              >
                <option value="0">Độ dốc đi xuống(Downward slope)</option>
                <option value="1">Độ dốc bằng phẳng(Flat slope)</option>
                <option value="2">Độ dốc đi lên(Upward slope)</option>
              </select>
            </label>

            <label>
              Number of Major Vessels Colored by Fluoroscopy (Số lượng mạch máu chính được tô màu bằng fluoroscopy):
              <select
                name="numMajorVessels"
                value={formData.numMajorVessels}
                onChange={handleChange}
              >
                <option value="0">Không có mạch máu chính nào bị tắc nghẽn.(No major blood vessels are blocked.)</option>
                <option value="1">Một mạch máu chính bị tắc nghẽn.(A major blood vessel is blocked.)</option>
                <option value="2">Hai mạch máu chính bị tắc nghẽn.(Two major blood vessels are blocked.)</option>
                <option value="3">Ba mạch máu chính bị tắc nghẽn.(Three major blood vessels are blocked.)</option>
              </select>
            </label>

            <label>
              Thal (Thallium Stress Test Result):
              <select
                name="thal"
                value={formData.thal}
                onChange={handleChange}
              >
                <option value="1">Bình thường (normal)</option>
                <option value="2">Khiếm khuyết cố định (fixed defect)</option>
                <option value="3">Khiếm khuyết có thể hồi phục (reversible defect)</option>
              </select>
            </label>

            <button type="submit">Prediction</button>
          </form>
        </div>
      </section>
    </main>
  );
};



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
