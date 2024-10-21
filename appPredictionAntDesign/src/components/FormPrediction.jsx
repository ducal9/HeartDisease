import React, { Component } from 'react';
import StepOne from './step/StepOne';
import StepTwo from './step/StepTwo';
import StepFinish from './step/StepFinish';

export class FormPrediction extends Component {
  state = {
    step: 0,
    // age: '', //input
    // sex: '', // autocomplete
    // chestPainType: '', // autocomplete
    // restingBloodPressure: '', //input
    // serumCholesterol: '', //input
    // fastingBloodSugar: '', // autocomplete
    // restingElectrocardiographicResults: '', // autocomplete
    // maximumHeartRateAchieved: '', //input
    // exerciseInducedAngina: '', // autocomplete
    // oldPeak: '', //input
    // slopeOfThePeakExcersiseSTSegment: '', // autocomplete
    // numberOfMajorVessels: '', // autocomplete
    // thaliumStressTestResult: '', // autocomplete
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
  };
  nextStep = () => {
    const { step } = this.state;
    this.setState({
      step: step + 1,
    });
  };
  prevStep = () => {
    const { step } = this.state;
    this.setState({
      step: step - 1,
    });
  };

  handleChange = (input) => (e) => {
    console.log({ [input]: e.target.value });

    this.setState({ [input]: parseInt(e.target.value) });
  };

  handleChangeSelect = (input) => (value) => {
    this.setState({ [input]: value });
  };

  handleSubmit = async (formData) => {
    try {
      const response = await fetch('http://127.0.0.1:8032/api-predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      console.log('API Response:', data);
    } catch (error) {
      console.error('Error sending data to API:', error);
    }
  };

  render() {
    const { step } = this.state;
    const {
      // age,
      // sex,
      // chestPainType,
      // restingBloodPressure,
      // serumCholesterol,
      // fastingBloodSugar,
      // restingElectrocardiographicResults,
      // maximumHeartRateAchieved,
      // exerciseInducedAngina,
      // oldPeak,
      // slopeOfThePeakExcersiseSTSegment,
      // numberOfMajorVessels,
      // thaliumStressTestResult,
      age,
      ca,
      chol,
      cp,
      exang,
      fbs,
      oldpeak,
      restecg,
      sex,
      slope,
      thal,
      thalach,
      trestbps,
    } = this.state;
    const values = {
      age,// age,
      ca,// numberOfMajorVessels,
      chol,// serumCholesterol,
      cp,// chestPainType,
      exang,// exerciseInducedAngina,
      fbs,// fastingBloodSugar,
      oldpeak,// oldPeak,
      restecg,// restingElectrocardiographicResults,
      sex,// sex,
      slope,// slopeOfThePeakExcersiseSTSegment,
      thal,// thaliumStressTestResult,
      thalach,// maximumHeartRateAchieved,
      trestbps, // restingBloodPressure,
    };
    switch (step) {
      case 0:
        return (
          <StepOne
            nextStep={this.nextStep}
            handleChange={this.handleChange}
            values={values}
            step={step}
          />
        );
      case 1:
        return (
          <StepTwo
            nextStep={this.nextStep}
            prevStep={this.prevStep}
            handleChangeSelect={this.handleChangeSelect}
            values={values}
            step={step}
          />
        );
      case 2:
        return (
          <StepFinish
            nextStep={this.nextStep}
            prevStep={this.prevStep}
            step={step}
            values={values}
            handleSubmit={this.handleSubmit}
          />
        );
    }
  }
}

export default FormPrediction;
