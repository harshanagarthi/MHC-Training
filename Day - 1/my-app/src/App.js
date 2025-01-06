import logo from './logo.svg';
import './App.css';
import FirstComponent from './Components/FirstComponent';
import SecondComponent from './Components/SecondComponent';

function App() {
  return (
    <div className="App">
      <h1>Hello !!</h1>
      <img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" alt="Google Logo" />
      <FirstComponent />
      <SecondComponent />
    </div>
  );
}

export default App;
