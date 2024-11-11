import { Button, Col, Divider, Input, Row, Select } from 'antd';
import {
  dataChestPainType,
  dataElectrocardiographicResults,
  dataExerciseInducedAngina,
  dataFastingBloodSugar,
  dataNumberMajorVessels,
  dataSex,
  dataSlopeOfPeakExerciseSTSegment,
  dataThal,
} from '../../valueForData';
import 'animate.css';

function Form3({ prevPage, values, openModal, updateState }) {
  return (
    <>
      <div className='form-input animate__animated animate__backInRight'>
        <Divider orientation='left'>Form Select</Divider>
        <div className='form-input__value'>
          <Row>
            <Col span={12}>
              <div className='form-input__value-item'>
                <div className='form-input__value-label'>Sex</div>
                <Select
                  style={{
                    width: '100%',
                  }}
                  onChange={(value) => updateState('sex', value)}
                  value={values.sex}
                >
                  {dataSex.map((item) => (
                    <Select.Option key={item.value} value={item.value}>
                      {item.title}
                    </Select.Option>
                  ))}
                </Select>
              </div>
              <div className='form-input__value-item'>
                <div className='form-input__value-label'>
                  Chest Pain Type <i>(cp)</i>
                </div>
                <Select
                  style={{
                    width: '100%',
                  }}
                  onChange={(value) => updateState('cp', value)}
                  value={values.cp}
                >
                  {dataChestPainType.map((item) => (
                    <Select.Option key={item.value} value={item.value}>
                      {item.title}
                    </Select.Option>
                  ))}
                </Select>
              </div>
              <div className='form-input__value-item'>
                <div className='form-input__value-label'>
                  Fasting Blood Sugar <i>(fbs)</i>
                </div>
                <Select
                  style={{
                    width: '100%',
                  }}
                  onChange={(value) => updateState('fbs', value)}
                  value={values.fbs}
                >
                  {dataFastingBloodSugar.map((item) => (
                    <Select.Option key={item.value} value={item.value}>
                      {item.title}
                    </Select.Option>
                  ))}
                </Select>
              </div>
              <div className='form-input__value-item'>
                <div className='form-input__value-label'>
                  Electrocardiographic <i>(restecg)</i>
                </div>
                <Select
                  style={{
                    width: '100%',
                  }}
                  onChange={(value) => updateState('restecg', value)}
                  value={values.restecg}
                >
                  {dataElectrocardiographicResults.map((item) => (
                    <Select.Option key={item.value} value={item.value}>
                      {item.title}
                    </Select.Option>
                  ))}
                </Select>
              </div>
            </Col>
            <Col span={12}>
              <div className='form-input__value-item'>
                <div className='form-input__value-label'>
                  Exercise Induced Angina <i>(exang)</i>
                </div>
                <Select
                  style={{
                    width: '100%',
                  }}
                  onChange={(value) => updateState('exang', value)}
                  value={values.exang}
                >
                  {dataExerciseInducedAngina.map((item) => (
                    <Select.Option key={item.value} value={item.value}>
                      {item.title}
                    </Select.Option>
                  ))}
                </Select>
              </div>
              <div className='form-input__value-item'>
                <div className='form-input__value-label'>
                  ExcersiseSTSegment <i>(slope)</i>
                </div>
                <Select
                  style={{
                    width: '100%',
                  }}
                  onChange={(value) => updateState('slope', value)}
                  value={values.slope}
                >
                  {dataSlopeOfPeakExerciseSTSegment.map((item) => (
                    <Select.Option key={item.value} value={item.value}>
                      {item.title}
                    </Select.Option>
                  ))}
                </Select>
              </div>
              <div className='form-input__value-item'>
                <div className='form-input__value-label'>
                  Major Vessels <i>(ca)</i>
                </div>
                <Select
                  style={{
                    width: '100%',
                  }}
                  onChange={(value) => updateState('ca', value)}
                  value={values.ca}
                >
                  {dataNumberMajorVessels.map((item) => (
                    <Select.Option key={item.value} value={item.value}>
                      {item.title}
                    </Select.Option>
                  ))}
                </Select>
              </div>
              <div className='form-input__value-item'>
                <div className='form-input__value-label'>
                  Thalium Stress <i>(thal)</i>
                </div>
                <Select
                  style={{
                    width: '100%',
                  }}
                  onChange={(value) => updateState('thal', value)}
                  value={values.thal}
                >
                  {dataThal.map((item) => (
                    <Select.Option key={item.value} value={item.value}>
                      {item.title}
                    </Select.Option>
                  ))}
                </Select>
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
            onClick={openModal}
          >
            Submit
          </Button>
        </div>
      </div>
    </>
  );
}

export default Form3;
