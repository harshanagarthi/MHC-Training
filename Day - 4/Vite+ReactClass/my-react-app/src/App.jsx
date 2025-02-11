import './App.css'
import ClickButton from './ClickButton';
import Counter from './Counter';
import Footer from './Footer';
import Greeting from './Greeting';
import Header from './Header';
import Hooks from './Hooks';
import InputHandling from './InputHandling';
import MainComp from './MainComp';
import WelcomeMessage from './WelcomeMessage';

function App() {
  const currentHour = new Date().getHours()
  let greetMessage;
  if (currentHour < 12) {
      greetMessage = "Good Morning"
  } else if (currentHour < 18) {
    greetMessage = "Good Afternoon"
  } else {
    greetMessage = "Good Evening"
  }
  return (
    <div>
      {/* <Greeting name="Harsha" greetMessage={greetMessage} hour={currentHour % 12} />
      <Hooks /> */}
      {/* <ClickButton />
      <InputHandling /> */}
      {/* <Counter /> */}
      {/* <Header />
      <WelcomeMessage />
      <InputHandling />
      <Counter />
      <Footer /> */}
      <WelcomeMessage />
    </div>
  )
}

export default App
