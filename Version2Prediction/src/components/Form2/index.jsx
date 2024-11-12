import { Button, Col, Divider, Form, Input, Row } from 'antd';
import './Form2.css';
import 'animate.css';

function Form2({ prevPage, nextPage, direction, updateState, values }) {
  const [form] = Form.useForm();
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
          <Form form={form} onFinish={nextPage}>
            <Row>
              <Col span={12}>
                <div className='form-input__value-item'>
                  <div className='form-input__value-label'>Name</div>
                  <Form.Item
                    name='name'
                    rules={[
                      { required: true, message: 'Nhập vào giá trị' },
                      {
                        validator: (_, value) => {
                          if (value && value.length < 3) {
                            return Promise.reject(
                              new Error('Tên phải có ít nhất 3 ký tự!')
                            );
                          }
                          return Promise.resolve();
                        },
                      },
                    ]}
                  >
                    <Input
                      value={values.name}
                      className='form-input__value-input'
                      placeholder='Name input'
                      onChange={(e) => {
                        updateState('name', e.target.value);
                      }}
                    />
                  </Form.Item>
                </div>
                <div className='form-input__value-item'>
                  <div className='form-input__value-label'>Age</div>
                  <Form.Item
                    name='age'
                    rules={[
                      { required: true, message: 'Nhập vào giá trị' },
                      {
                        validator: (_, value) => {
                          if (value < 29 || value > 77) {
                            return Promise.reject(
                              new Error('Giá trị phải nằm trong khoảng 29-77')
                            );
                          }
                          return Promise.resolve();
                        },
                      },
                    ]}
                  >
                    <Input
                      value={values.age}
                      type='number'
                      className='form-input__value-input'
                      placeholder='Age'
                      onChange={(e) => {
                        updateState('age', parseInt(e.target.value));
                      }}
                    />
                  </Form.Item>
                </div>
                <div className='form-input__value-item'>
                  <div className='form-input__value-label'>
                    Resting Blood Pressure <i>(trestbps)</i>
                  </div>
                  <Form.Item
                    name='trestbps'
                    rules={[
                      { required: true, message: 'Nhập vào giá trị' },
                      {
                        validator: (_, value) => {
                          if (value < 80 || value > 250) {
                            return Promise.reject(
                              new Error('Giá trị phải nằm trong khoảng 80-250')
                            );
                          }
                          return Promise.resolve();
                        },
                      },
                    ]}
                  >
                    <Input
                      value={values.trestbps}
                      type='number'
                      className='form-input__value-input'
                      placeholder='trestbps'
                      onChange={(e) => {
                        updateState('trestbps', parseInt(e.target.value));
                      }}
                    />
                  </Form.Item>
                </div>
              </Col>
              <Col span={12}>
                <div className='form-input__value-item'>
                  <div className='form-input__value-label'>
                    Serum Cholesterol <i>(chol)</i>
                  </div>
                  <Form.Item
                    name='chol'
                    rules={[
                      { required: true, message: 'Nhập vào giá trị' },
                      {
                        validator: (_, value) => {
                          if (value < 126 || value > 524) {
                            return Promise.reject(
                              new Error('Giá trị phải nằm trong khoảng 126-524')
                            );
                          }
                          return Promise.resolve();
                        },
                      },
                    ]}
                  >
                    <Input
                      value={values.chol}
                      type='number'
                      className='form-input__value-input'
                      placeholder='chol'
                      onChange={(e) => {
                        updateState('chol', parseInt(e.target.value));
                      }}
                    />
                  </Form.Item>
                </div>
                <div className='form-input__value-item'>
                  <div className='form-input__value-label'>
                    Heart Rate Achieved <i>(thalach)</i>
                  </div>
                  <Form.Item
                    name='thalach'
                    rules={[
                      { required: true, message: 'Nhập vào giá trị' },
                      {
                        validator: (_, value) => {
                          if (value < 71 || value > 202) {
                            return Promise.reject(
                              new Error('Giá trị phải nằm trong khoảng 71-202')
                            );
                          }
                          return Promise.resolve();
                        },
                      },
                    ]}
                  >
                    <Input
                      value={values.thalach}
                      type='number'
                      className='form-input__value-input'
                      placeholder='thalach'
                      onChange={(e) => {
                        updateState('thalach', parseInt(e.target.value));
                      }}
                    />
                  </Form.Item>
                </div>
                <div className='form-input__value-item'>
                  <div className='form-input__value-label'>Oldpeak</div>
                  <Form.Item
                    name='oldpeak'
                    rules={[
                      { required: true, message: 'Nhập vào giá trị' },
                      {
                        validator: (_, value) => {
                          if (value <= 0 || value > 6.2) {
                            return Promise.reject(
                              new Error('Giá trị phải nằm trong khoảng 0-6.2')
                            );
                          }
                          return Promise.resolve();
                        },
                      },
                    ]}
                  >
                    <Input
                      value={values.oldpeak}
                      type='number'
                      className='form-input__value-input'
                      placeholder='oldpeak'
                      onChange={(e) => {
                        updateState('oldpeak', parseInt(e.target.value));
                      }}
                    />
                  </Form.Item>
                </div>
              </Col>
            </Row>
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
                htmlType='submit'
              >
                Next
              </Button>
            </div>
          </Form>
        </div>
      </div>
    </>
  );
}
export default Form2;
