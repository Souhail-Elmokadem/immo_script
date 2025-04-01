import logo from './logo.svg';
import './App.css';
import Navbar from './componants/navbar/Navbar';
import Sidebar from './componants/sidebar/sidebar';
import Home from './pages/home/home';
import Layout from './pages/Layout';
import { BrowserRouter,Routes,Route } from 'react-router-dom';
import Scrape from './pages/scrape/Scrape';

function App() {
  return (
   

    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />} >
          <Route index element={<Home />} />
          <Route path="scrape" element={<Scrape />} />
        
        </Route>
       
      </Routes>
    </BrowserRouter>
     
    
   
  );
}

export default App;
