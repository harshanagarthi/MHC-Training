import React from 'react';

const Header = () => {
  const headerStyle = {
    backgroundColor: '#4a90e2',
    color: '#fff',
    textAlign: 'center',
    padding: '20px',
    borderRadius: '5px',
    boxShadow: '0 2px 5px rgba(0, 0, 0, 0.1)',
  };

  return (
    <div style={headerStyle}>
      <h1>A ReactJS Application</h1>
    </div>
  );
};

export default Header;
