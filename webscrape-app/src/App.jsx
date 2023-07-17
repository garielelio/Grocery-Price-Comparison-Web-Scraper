import React, { createContext } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import WebHeader from './components/WebHeader'
import WebSearch from './components/WebSearch'
import WebResult from './components/WebResult'
import './App.css'
import {Route, Routes} from "react-router-dom"
import { useContext, useState } from 'react'

export const itemsContext = createContext()

function App() {
  const[items, setItems] = useState([])

  return (
    <itemsContext.Provider value={[items, setItems]}>
    <div>
      <WebHeader />
      <Routes>
        <Route path='/' element={<WebSearch/>}/>
        <Route path='/result' element={<WebResult/>}/>
      </Routes>
    </div>
    </itemsContext.Provider>
  )
}

export default App