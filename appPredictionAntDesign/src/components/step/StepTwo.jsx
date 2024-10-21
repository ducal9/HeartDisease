import React, { Component } from 'react';
import { Card } from 'antd';
import { Steps } from 'antd';
import { Button, Form, Select } from 'antd';
import { Col, Divider, Row } from 'antd';
import {
  dataSex,
  dataChestPainType,
  dataElectrocardiographicResults,
  dataExerciseInducedAngina,
  dataFastingBloodSugar,
  dataSlopeOfPeakExerciseSTSegment,
  dataNumberMajorVessels,
  dataThal,
} from '../../assets/typeOfStatus';

export class StepTwo extends Component {
  continue = (e) => {
    e.preventDefault();
    this.props.nextStep();
  };

  back = (e) => {
    e.preventDefault();
    this.props.prevStep();
  };

  render() {
    const { values, handleChangeSelect, step } = this.props;
    const description = 'This is a description.';

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
                span: 16,
              }}
              style={{
                maxWidth: 1100,
              }}
              initialValues={{
                remember: true,
              }}
              autoComplete='off'
            >
              <Divider orientation='left'>Form 2</Divider>
              <Row
                gutter={{
                  xs: 8,
                  sm: 16,
                  md: 24,
                  lg: 32,
                }}
              >
                <Col className='gutter-row' span={12}>
                  <Form.Item label='Sex'>
                    <Select
                      onChange={handleChangeSelect('sex')}
                      value={values.sex}
                    >
                      {dataSex.map((item) => (
                        <Select.Option key={item.value} value={item.value}>
                          {item.title}
                        </Select.Option>
                      ))}
                    </Select>
                  </Form.Item>
                </Col>
                <Col className='gutter-row' span={12}>
                  <Form.Item label='Chest Pain Type'>
                    <Select
                      onChange={handleChangeSelect('cp')}
                      value={values.cp}
                    >
                      {dataChestPainType.map((item) => (
                        <Select.Option key={item.value} value={item.value}>
                          {item.title}
                        </Select.Option>
                      ))}
                    </Select>
                  </Form.Item>
                </Col>
                <Col className='gutter-row' span={12}>
                  <Form.Item label='Fasting Blood Sugar'>
                    <Select
                      onChange={handleChangeSelect('fbs')}
                      value={values.fbs}
                    >
                      {dataFastingBloodSugar.map((item) => (
                        <Select.Option key={item.value} value={item.value}>
                          {item.title}
                        </Select.Option>
                      ))}
                    </Select>
                  </Form.Item>
                </Col>
                <Col className='gutter-row' span={12}>
                  <Form.Item label='Electrocardiographic '>
                    <Select
                      onChange={handleChangeSelect(
                        'restecg'
                      )}
                      value={values.restecg}
                    >
                      {dataElectrocardiographicResults.map((item) => (
                        <Select.Option key={item.value} value={item.value}>
                          {item.title}
                        </Select.Option>
                      ))}
                    </Select>
                  </Form.Item>
                </Col>
                <Col className='gutter-row' span={12}>
                  <Form.Item label='Exercise Induced Angina'>
                    <Select
                      onChange={handleChangeSelect('exang')}
                      value={values.exang}
                    >
                      {dataExerciseInducedAngina.map((item) => (
                        <Select.Option key={item.value} value={item.value}>
                          {item.title}
                        </Select.Option>
                      ))}
                    </Select>
                  </Form.Item>
                </Col>
                <Col className='gutter-row' span={12}>
                  <Form.Item label='ExcersiseSTSegment'>
                    <Select
                      onChange={handleChangeSelect(
                        'slope'
                      )}
                      value={values.slope}
                    >
                      {dataSlopeOfPeakExerciseSTSegment.map((item) => (
                        <Select.Option key={item.value} value={item.value}>
                          {item.title}
                        </Select.Option>
                      ))}
                    </Select>
                  </Form.Item>
                </Col>
                <Col className='gutter-row' span={12}>
                  <Form.Item label='Major Vessels'>
                    <Select
                      onChange={handleChangeSelect('ca')}
                      value={values.ca}
                    >
                      {dataNumberMajorVessels.map((item) => (
                        <Select.Option key={item.value} value={item.value}>
                          {item.title}
                        </Select.Option>
                      ))}
                    </Select>
                  </Form.Item>
                </Col>
                <Col className='gutter-row' span={12}>
                  <Form.Item label='Thalium Stress'>
                    <Select
                      onChange={handleChangeSelect('thal')}
                      value={values.thal}
                    >
                      {dataThal.map((item) => (
                        <Select.Option key={item.value} value={item.value}>
                          {item.title}
                        </Select.Option>
                      ))}
                    </Select>
                  </Form.Item>
                </Col>
              </Row>
              <Divider
                orientation='left'
                style={{ marginTop: '2vh' }}
              ></Divider>
              <Row gutter={24}>
                <Col className='gutter-row' span={12}>
                  <Form.Item
                    wrapperCol={{
                      offset: 8,
                      span: 16,
                    }}
                  >
                    <Button type='primary' onClick={this.back}>
                      Back
                    </Button>
                  </Form.Item>
                </Col>
                <Col className='gutter-row' span={12}>
                  <Form.Item
                    wrapperCol={{
                      offset: 8,
                      span: 16,
                    }}
                  >
                    <Button type='primary' onClick={this.continue}>
                      Submit
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

export default StepTwo;
