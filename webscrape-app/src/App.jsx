import React from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import WebHeader from './components/WebHeader'
import WebSearch from './components/WebSearch'
import WebResult from './components/WebResult'
import './App.css'

function App() {

  const [toggleSwitch, setToggleSwitch] = React.useState(true)

  React.useEffect(() => {
    const storedToggleValue = sessionStorage.getItem('toggleSwitch')
    if (storedToggleValue) {
      setToggleSwitch(JSON.parse(storedToggleValue))
    }
  }, []);

  function toggle() {
    setToggleSwitch(currValue => {
      const newValue = !currValue
      sessionStorage.setItem('toggleSwitch', JSON.stringify(newValue))
      return newValue
    });
  }

  return (
    <div>
      <WebHeader />
      {toggleSwitch && <WebSearch clickButton={toggle}/>}
      {!toggleSwitch && <WebResult clickButton ={toggle}/>}
    </div>
  )
}

export default App



    // <>
    //   <div>
    //     <a href="https://vitejs.dev" target="_blank">
    //       <img src={viteLogo} className="logo" alt="Vite logo" />
    //     </a>
    //     <a href="https://react.dev" target="_blank">
    //       <img src={reactLogo} className="logo react" alt="React logo" />
    //     </a>
    //   </div>
    //   <h1>Vite + React</h1>
    //   <div className="card">
    //     <button onClick={() => setCount((count) => count + 1)}>
    //       count is {count}
    //     </button>
    //     <p>
    //       Edit <code>src/App.jsx</code> and save to test HMR
    //     </p>
    //   </div>
    //   <p className="read-the-docs">
    //     Click on the Vite and React logos to learn more
    //   </p>
    // </>