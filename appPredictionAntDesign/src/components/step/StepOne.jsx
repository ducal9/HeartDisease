import React, { Component } from 'react';
import { Card } from 'antd';
import { Steps } from 'antd';
import { Button, Form, Input } from 'antd';
import { Col, Divider, Row } from 'antd';

export class StepOne extends Component {
  continue = (e) => {
    e.preventDefault();
    this.props.nextStep();
  };

  render() {
    const { values, handleChange, step } = this.props;

    return (
      <div
        style={{
          display: 'flex',
          justifyContent: 'center',
          marginTop: '1vh',
        }}
      >
        <Card
          style={{
            width: '70vw',
            alignItems: 'center',
            height: '75vh',
            boxShadow: '0 4px 8px rgba(0, 0, 0, 0.2)',
          }}
        >
          <Steps
            current={this.props.step}
            items={[
              {
                title: 'First step',
                description: 'Continue Data',
              },
              {
                title: 'Second step',
                description: 'Categorial Data',
                // subTitle: 'Left 00:00:08',
              },
              {
                title: 'Finish step',
                description: 'Submit',
              },
            ]}
          />
          <div
            style={{
              marginTop: '8vh',
            }}
          >
            <Form
              name='basic'
              labelCol={{
                span: 8,
              }}
              wrapperCol={{
                span: 13,
              }}
              style={{
                maxWidth: '100vw',
              }}
              initialValues={{
                remember: true,
              }}
              autoComplete='off'
            >
              <Divider orientation='left'>Form 1</Divider>
              <Row gutter={16}>
                <Col className='gutter-row' span={12}>
                  <Form.Item
                    label='Age'
                    name='age'
                    rules={[
                      {
                        required: true,
                        message: 'Please input your username!',
                      },
                    ]}
                  >
                    <Input
                      name='age'
                      value={values.age}
                      onChange={handleChange('age')}
                    />
                  </Form.Item>
                </Col>
                <Col className='gutter-row' span={12}>
                  <Form.Item
                    label='Resting Blood Pressure'
                    name='restingBloodPressure'
                    rules={[
                      {
                        required: true,
                        message: 'Please input your username!',
                      },
                    ]}
                  >
                    <Input
                      name='restingBloodPressure'
                      value={values.restingBloodPressure}
                      onChange={handleChange('restingBloodPressure')}
                    />
                  </Form.Item>
                </Col>
                <Col className='gutter-row' span={12}>
                  <Form.Item
                    label='Serum Cholesterol'
                    name='serumCholesterol'
                    rules={[
                      {
                        required: true,
                        message: 'Please input your username!',
                      },
                    ]}
                  >
                    <Input
                      name='serumCholesterol'
                      value={values.serumCholesterol}
                      onChange={handleChange('serumCholesterol')}
                    />
                  </Form.Item>
                </Col>
                <Col className='gutter-row' span={12}>
                  <Form.Item
                    label='Heart Rate Achieved'
                    name='maximumHeartRateAchieved'
                    rules={[
                      {
                        required: true,
                        message: 'Please input your username!',
                      },
                    ]}
                  >
                    <Input
                      name='maximumHeartRateAchieved'
                      value={values.maximumHeartRateAchieved}
                      onChange={handleChange('maximumHeartRateAchieved')}
                    />
                  </Form.Item>
                </Col>
                <Col className='gutter-row' span={12}>
                  <Form.Item
                    label='Oldpeak'
                    name='oldPeak'
                    rules={[
                      {
                        required: true,
                        message: 'Please input your username!',
                      },
                    ]}
                  >
                    <Input
                      name='oldPeak'
                      value={values.oldPeak}
                      onChange={handleChange('oldPeak')}
                    />
                  </Form.Item>
                </Col>
              </Row>
              <Divider
                orientation='left'
                style={{ marginTop: '5vh' }}
              ></Divider>
              <Row gutter={24}>
                <Col className='gutter-row' span={24}>
                  <Form.Item
                    wrapperCol={{
                      offset: 12,
                      span: 12,
                    }}
                  >
                    <Button
                      type='primary'
                      htmlType='submit'
                      onClick={this.continue}
                    >
                      Continue
                    </Button>
                  </Form.Item>
                </Col>
              </Row>
            </Form>
          </div>
        </Card>
      </div>
    );
  }
}

export default StepOne;
