import React from 'react'
import Navbar from '../componants/navbar/Navbar'
import Sidebar from '../componants/sidebar/sidebar'
import { Outlet } from 'react-router-dom'
export default function Layout() {
  return (
    <>
    
    <Navbar />
      <Outlet />
      <Sidebar />
    </>
  )
}
