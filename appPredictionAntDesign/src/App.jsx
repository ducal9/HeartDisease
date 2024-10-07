import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavBar from './components/NavBar';
import FormPrediction from './components/FormPrediction';

function App() {
  return (
    <>
      <NavBar />
      <h1 className='bebas-neue-regular'>Form Status</h1>
      <FormPrediction />
    </>
  );
}

export default App;
