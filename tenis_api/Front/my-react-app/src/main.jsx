import { StrictMode } from 'react'
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route} from "react-router"; // Correto


import './index.css'
import App from './App.jsx'
import { Create } from '../pages/Create.jsx'
import { Delete } from '../pages/Delete.jsx'
import { Update } from '../pages/Update.jsx'
import { Home } from '../pages/Home.jsx';

const root = document.getElementById("root");

ReactDOM.createRoot(root).render(
  <StrictMode>
    <BrowserRouter>
        <Routes>

          <Route path="/" element={<App />} />
          <Route path="/home" element={<Home />} />
          <Route path="/create" element={<Create/>} />
          <Route path="/delete" element={<Delete />} />
          <Route path="/update" element={<Update />} />


        </Routes>
    </BrowserRouter>
  </StrictMode>
)
