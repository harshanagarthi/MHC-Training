import React from 'react'

function Greeting(props){
  return (
    <div>
      <h2>Hello {props.name}!!! {props.greetMessage}, its {props.hour}'O Clock now</h2>
    </div>
  )
}

export default Greeting
