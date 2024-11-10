import { Button, Col, Divider, Input, Row } from 'antd';
import './Form2.css';
import 'animate.css';

function Form2({ prevPage, nextPage, direction, updateState, values }) {
  return (
    <>
      <div
        className={`form-input ${
          direction
            ? 'animate__animated animate__backInLeft'
            : 'animate__animated animate__backInRight'
        }`}
      >
        <Divider orientation='left'>Form Input</Divider>
        <div className='form-input__value'>
          <Row>
            <Col span={12}>
              <div className='form-input__value-item'>
                <div className='form-input__value-label'>Name</div>
                <Input
                  value={values.name}
                  className='form-input__value-input'
                  placeholder='Name input'
                  onChange={(e) => {
                    updateState('name', e.target.value);
                  }}
                />
              </div>
              <div className='form-input__value-item'>
                <div className='form-input__value-label'>Age</div>
                <Input
                  value={values.age}
                  type='number'
                  className='form-input__value-input'
                  placeholder='Basic usage'
                  onChange={(e) => {
                    updateState('age', e.target.value);
                  }}
                />
              </div>
              <div className='form-input__value-item'>
                <div className='form-input__value-label'>
                  Resting Blood Pressure <i>(trestbps)</i>
                </div>
                <Input
                  value={values.trestbps}
                  type='number'
                  className='form-input__value-input'
                  placeholder='Basic usage'
                  onChange={(e) => {
                    updateState('trestbps', e.target.value);
                  }}
                />
              </div>
            </Col>
            <Col span={12}>
              <div className='form-input__value-item'>
                <div className='form-input__value-label'>
                  Serum Cholesterol <i>(chol)</i>
                </div>
                <Input
                  value={values.chol}
                  type='number'
                  className='form-input__value-input'
                  placeholder='Basic usage'
                  onChange={(e) => {
                    updateState('chol', e.target.value);
                  }}
                />
              </div>
              <div className='form-input__value-item'>
                <div className='form-input__value-label'>
                  Heart Rate Achieved <i>(thalach)</i>
                </div>
                <Input
                  value={values.thalach}
                  type='number'
                  className='form-input__value-input'
                  placeholder='Basic usage'
                  onChange={(e) => {
                    updateState('thalach', e.target.value);
                  }}
                />
              </div>
              <div className='form-input__value-item'>
                <div className='form-input__value-label'>Oldpeak</div>
                <Input
                  value={values.oldpeak}
                  type='number'
                  className='form-input__value-input'
                  placeholder='Basic usage'
                  onChange={(e) => {
                    updateState('oldpeak', e.target.value);
                  }}
                />
              </div>
            </Col>
          </Row>
        </div>
        <Divider />
        <div className='button-control'>
          <Button
            className='button-control__item'
            type='primary'
            onClick={prevPage}
          >
            Previous
          </Button>
          <Button
            className='button-control__item'
            type='primary'
            onClick={nextPage}
          >
            Next
          </Button>
        </div>
      </div>
    </>
  );
}
export default Form2;
