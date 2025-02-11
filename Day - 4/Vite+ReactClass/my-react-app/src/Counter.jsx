import React, { useState } from "react";

const Counter = () => {
  const [count, setCount] = useState(0);

  const handleIncrementCount = () => {
    setCount(count + 1);
  };

  const handleDecrementCount = () => {
    setCount(count - 1);
  };

  return (
    <div
      style={{
        display: "inline-block",
        textAlign: "center",
        padding: "20px",
        border: "1px solid #ccc",
        borderRadius: "8px",
        boxShadow: "0 2px 5px rgba(0, 0, 0, 0.1)",
        margin: "20px",
        backgroundColor: "#f9f9f9",
      }}
    >
      <button
        onClick={handleIncrementCount}
        style={{
          padding: "10px 20px",
          margin: "10px",
          fontSize: "1em",
          cursor: "pointer",
          backgroundColor: "#4CAF50",
          color: "white",
          border: "none",
          borderRadius: "5px",
        }}
      >
        Increase (+)
      </button>
      <h1
        style={{
          fontSize: "1.5em",
          color: "#333",
          margin: "15px 0",
        }}
      >
        Counter: {count}
      </h1>
      <button
        onClick={handleDecrementCount}
        style={{
          padding: "10px 20px",
          margin: "10px",
          fontSize: "1em",
          cursor: "pointer",
          backgroundColor: "#f44336",
          color: "white",
          border: "none",
          borderRadius: "5px",
        }}
      >
        Decrease (-)
      </button>
    </div>
  );
};

export default Counter;
