import React from 'react'

import { Link } from 'react-router-dom'
function Sidebar() {
  return (
    <>
    <aside className="sidebar-wrapper" data-simplebar="true">
          <div className="sidebar-header">
            <div>
              <img src="assets/images/logo-icon.png" className="logo-icon" alt="logo icon" />
            </div>
            <div>
              <h4 className="logo-text">Onedash</h4>
            </div>
            <div className="toggle-icon ms-auto"> <i className="bi bi-list"></i>
            </div>
          </div>
          <ul className="metismenu" id="menu">
            <li>
                <Link to="/"  className="active">
              
                <div className="parent-icon"><i className="bi bi-house-fill"></i>
                </div>
                <div className="menu-title">Dashboard</div>
                </Link>
              
            </li>
            <li>
              <Link to="/scrape" className="">
                <div className="parent-icon"><i className="bi bi-cloud-arrow-down-fill"></i>
                </div>
                <div className="menu-title">Scrape</div>
                </Link>
            
            </li>

           

          </ul>
         
       </aside>
    
    </>
  )
}

export default Sidebar