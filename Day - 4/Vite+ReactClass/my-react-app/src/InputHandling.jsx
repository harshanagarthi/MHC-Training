import React, { useState } from "react";

const InputHandling = () => {
  const [firstName, setFirstName] = useState("");
  const [secondName, setSecondName] = useState("");

  const handleFirstNameChange = (e) => {
    setFirstName(e.target.value);
  };

  const handleSecondNameChange = (e) => {
    setSecondName(e.target.value);
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif", lineHeight: "1.6" }}>
      <label
        htmlFor="first_name"
        style={{
          display: "block",
          marginBottom: "5px",
          color: "black",
          fontWeight: "bold",
        }}
      >
        First Name:
      </label>
      <input
        type="text"
        name="first_name"
        id="first_name"
        onChange={handleFirstNameChange}
        style={{
          width: "100%",
          padding: "8px",
          marginBottom: "15px",
          border: "1px solid #ccc",
          borderRadius: "4px",
          fontSize: "1em",
        }}
      />
      <label
        htmlFor="last_name"
        style={{
          display: "block",
          marginBottom: "5px",
          color: "black",
          fontWeight: "bold",
        }}
      >
        Last Name:
      </label>
      <input
        type="text"
        name="last_name"
        id="last_name"
        onChange={handleSecondNameChange}
        style={{
          width: "100%",
          padding: "8px",
          marginBottom: "15px",
          border: "1px solid #ccc",
          borderRadius: "4px",
          fontSize: "1em",
        }}
      />
      <p
        style={{
          fontSize: "1.2em",
          marginTop: "15px",
          color: "#333",
        }}
      >
        Your full name is {firstName} {secondName}
      </p>
    </div>
  );
};

export default InputHandling;
