import React, { useState } from 'react'

const ClickButton = () => {
    const [message, setMessage] = useState("");
    function handleClick() {
        setMessage("You clicked ME!!!");
        console.log(message);
    }
  return (
    <div>
          <button onClick={handleClick}>Click Me</button>
          <p>{message}</p>
    </div>
  )
}

export default ClickButton;

