import { Button, Divider } from 'antd';
import './Form1.css';
import 'animate.css';

function Form1({ nextPage, direction }) {
  return (
    <>
      <div className='form-welcome'>
        <Divider orientation='left'>Welcome</Divider>
        <div
          className={`form-welcome__image ${
            direction ? 'animate__animated animate__backInLeft' : ''
          } `}
        >
          <img id='image' src='./public/11080267.jpg' />
        </div>
        <div className='form-welcome__image'>
          <Button id='button-next' type='primary' onClick={nextPage}>
            Next
          </Button>
        </div>
      </div>
    </>
  );
}
export default Form1;
