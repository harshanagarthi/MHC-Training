import React, { useState } from 'react'

const Hooks = () => {
    const [count, setCount] = useState(0);
    return (
    <div>
            <button onClick={() => setCount(count+1)}>Count is {count}</button>
    </div>
  )
}

export default Hooks
