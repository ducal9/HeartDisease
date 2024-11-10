import { Button, Modal, Spin, Steps } from 'antd';
import './FormPrediction.css';
import { useState } from 'react';
import Form1 from '../../components/Form1';
import 'animate.css';
import Form2 from '../../components/Form2';
import Form3 from '../../components/Form3';
import { LoadingOutlined } from '@ant-design/icons';
function FormPrediction() {
  const [state, setState] = useState({
    prediction: null,
    step: 0,
    name: null,
    age: null,
    ca: 0,
    chol: null,
    cp: 0,
    exang: 0,
    fbs: 0,
    oldpeak: null,
    restecg: 0,
    sex: 0,
    slope: 0,
    thal: 1,
    thalach: null,
    trestbps: null,
  });

  const [isModalOpen, setIsModalOpen] = useState(false);
  const predictResult = async (state) => {
    const response = await fetch('http://127.0.0.1:8031/predict', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        age: state.age,
        ca: state.ca,
        chol: state.chol,
        cp: state.cp,
        exang: state.exang,
        fbs: state.fbs,
        oldpeak: state.oldpeak,
        restecg: state.restecg,
        sex: state.sex,
        slope: state.slope,
        thal: state.thal,
        thalach: state.thalach,
        trestbps: state.trestbps,
      }),
    });
    const result = await response.json();
    return result;
  };
  const [isLoading, setLoading] = useState(true);
  const showModal = async () => {
    setIsModalOpen(true);
    const result = await predictResult(state);
    console.log(result.prediction);
    setState((prevState) => ({ ...prevState, prediction: result.prediction }));
    setTimeout(() => {
      setLoading(false);
    }, 1500);
  };
  const handleOk = () => {
    // setIsModalOpen(false);
    location.reload();
  };

  const [left, setLeft] = useState(false);
  const nextStep = () => {
    setState((prevState) => ({
      ...prevState,
      step: prevState.step + 1,
    }));
    setLeft(false);
  };

  const prevStep = () => {
    setState((prevState) => ({
      ...prevState,
      step: prevState.step - 1,
    }));
    setLeft(true);
  };

  const updateState = (field, value) => {
    setState((prevState) => ({
      ...prevState,
      [field]: value,
    }));
    console.log(state);
  };
  const renderContent = () => {
    switch (state.step) {
      case 0:
        return <Form1 nextPage={nextStep} direction={left} />;
      case 1:
        return (
          <Form2
            prevPage={prevStep}
            nextPage={nextStep}
            direction={left}
            values={state}
            updateState={updateState}
          />
        );
      case 2:
        return (
          <Form3
            prevPage={prevStep}
            values={state}
            openModal={showModal}
            direction={left}
            updateState={updateState}
          />
        );
      default:
        return <div>Unknown step</div>;
    }
  };

  return (
    <>
      <div className='form-main animate__animated animate__backInRight'>
        <p className='form-main__title '>Form user</p>
        <div className='form-main__card'>
          <Steps
            className='steps'
            current={state.step}
            items={[
              {
                title: 'Welcome',
              },
              {
                title: 'Form input',
                subTitle: 'Enter your value',
              },
              {
                title: 'Form select',
                subTitle: 'Choose your value',
              },
            ]}
          />
          {renderContent()}
        </div>
      </div>
      <Modal
        title='Result prediction'
        open={isModalOpen}
        closable={false}
        footer={
          <Button type='primary' onClick={handleOk}>
            OK
          </Button>
        }
      >
        <p>
          {isLoading ? (
            <div className='spin'>
              <Spin indicator={<LoadingOutlined spin />} size='large' />
            </div>
          ) : (
            <>
              {/* {state.prediction
                ? `Prediction: ${state.prediction}`
                : 'Loading...'} */}
              <div className='notify'>
                <p className='notify-item notify-hello'>
                  Xin chào, <b>{state.name}</b>
                </p>
                <p className='notify-item  notify-body'>
                  Theo như chỉ số bạn cung cấp chúng tôi dự đoán rằng:
                  <div>
                    <b>
                      Bạn
                      {state.prediction
                        ? ` đang có nguy cơ mắc bệnh tim`
                        : ' không có nguy cơ mắc bệnh tim'}
                    </b>
                  </div>
                </p>
              </div>
            </>
          )}
        </p>
      </Modal>
    </>
  );
}

export default FormPrediction;
