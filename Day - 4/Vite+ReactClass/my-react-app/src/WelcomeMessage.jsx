import React, { useState } from "react";
import InputHandling from "./InputHandling";
import Counter from "./Counter";
import Header from "./Header";
import Footer from "./Footer";
import "./WelcomMessage.css";

const WelcomeMessage = () => {
  const [LoggedIn, setLoggedIn] = useState(false);
  const [name, setName] = useState("");
  const toggleLogin = () => {
    setLoggedIn(!LoggedIn);
  };

  const handleNameChange = (e) => {
    setName(e.target.value);
  };
  if (LoggedIn) {
    return (
      <div className="loggedIn">
        {/* <WelcomeMessage /> */}
        <Header />
        <h1>Welcome back {name}</h1>
        <InputHandling />
        <Counter />
        <button onClick={toggleLogin}>Log Out</button>
        <Footer />
      </div>
    );
  } else {
    return (
      <div className="loggedOut">
        <Header />
        <h1>You are logged Out, please log in to continue</h1>
        <label for="name">Name</label>
        <input type="text" name="name" onChange={handleNameChange} />
        <button onClick={toggleLogin}>Log In</button>
        {/* <h1>Welcome User</h1>
        <button onClick={toggleLogin}>Log Out</button> */}
        <Footer />
      </div>
    );
  }
};

export default WelcomeMessage;

// header
// login comp
// input handling
// counter application
// simple footer
//
