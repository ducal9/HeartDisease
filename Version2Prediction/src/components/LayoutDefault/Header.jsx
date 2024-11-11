import { HeartOutlined } from '@ant-design/icons';
import './css/Header.css';
function Header() {
  return (
    <>
      <div className='header'>
        <div className='header-logo'>
          <HeartOutlined />
          <div className='header-logo__name'>Prediction Heart Disease</div>
        </div>
      </div>
    </>
  );
}

export default Header;
