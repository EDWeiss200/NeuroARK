import './index.css'
import {BrowserRouter, Route, Routes} from 'react-router-dom'
import Auth from './pages/Auth'
import Home from './pages/Home'
import Registr from './pages/Registr'

function App() {


  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/auth' element={<Auth/>}/>
        <Route path='/register' element={<Registr/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
