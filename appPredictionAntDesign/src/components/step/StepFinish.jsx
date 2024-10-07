import React, { Component } from 'react';
import { Button, Result } from 'antd';
import { Card } from 'antd';
import { Steps } from 'antd';
import { Spin } from 'antd';
import { LoadingOutlined } from '@ant-design/icons';

export class StepFinish extends Component {
  state = {
    isLoading: true,
  };
  continue = (e) => {
    e.preventDefault();
    this.props.nextStep();
  };

  back = (e) => {
    e.preventDefault();
    this.props.prevStep();
  };

  componentDidMount() {
    // Dùng setTimeout để thay đổi trạng thái sau 1 giây
    setTimeout(() => {
      this.setState({ isLoading: false });
    }, 1500); // 1000ms = 1 giây
  }

  render() {
    const { values, step, handleSubmit } = this.props;
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
              marginTop: '10vh',
            }}
          >
            {this.state.isLoading == true ? (
              <Spin
                indicator={
                  <LoadingOutlined
                    style={{
                      marginTop: '20vh',
                      fontSize: 48,
                    }}
                    spin
                  />
                }
              />
            ) : (
              <Result
                status='success'
                title='Successfully '
                subTitle='We will send the result after some minutes'
                extra={[
                  <Button type='primary' key='console' onClick={this.back}>
                    Back
                  </Button>,
                  <Button
                    type='primary'
                    htmlType='submit'
                    key='submit'
                    onClick={() => {
                      handleSubmit(values);
                    }}
                  >
                    Submit
                  </Button>,
                ]}
              />
            )}
          </div>
        </Card>
      </div>
    );
  }
}

export default StepFinish;
