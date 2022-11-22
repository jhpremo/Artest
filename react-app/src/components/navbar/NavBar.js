
import React from 'react';
import { useState } from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import LoginForm from '../auth/LoginForm';
import "./navbar.css"

const NavBar = () => {
  const [toggleLogin, setToggleLogin] = useState(false)
  const [toggleSignup, setToggleSignup] = useState(false)
  const openLogin = () => {
    if (toggleSignup) {
      setToggleSignup(false)
    }
    setToggleLogin(true)
  }

  const openSignup = () => {
    if (toggleLogin) {
      setToggleLogin(false)
    }
    setToggleSignup(true)
  }

  const close = () => {
    setToggleLogin(false)
    setToggleSignup(false)
  }

  return (
    <>
      {toggleLogin && <div className='login-modal'>
        <div className='login-left'> <span>Artest</span></div>
        <div className='login-right'>
          <div onClick={close} className='close-modal-button'><i className="fa-solid fa-x" /></div>
        </div>
      </div>}
      <div className='navbar-wrapper'>
        <div className='navbar-left-wrapper'>
          <NavLink to='/' exact={true} activeClassName='n/a' className="navbar-home-button">
            Artest
          </NavLink>
          <NavLink to='/' exact={true} activeClassName='active' className="navbar-left-button">
            Home
          </NavLink>
          <NavLink to="/your-sets" className='navbar-left-button'>
            Your sets
          </NavLink>
          <NavLink to="/your-comparisons" className='navbar-left-button'>
            Your comparisons
          </NavLink>
          <button className='navbar-create-button'>
            Create <i className="fa-solid fa-chevron-down" />
          </button>
        </div>
        <div className='navbar-right-wrapper'>
          <button onClick={openLogin} className='navbar-login-button'>
            Login
          </button>
          <button onClick={openSignup} className='navbar-signup-button'>
            Sign Up
          </button>
        </div>
        {/* <LogoutButton /> */}
      </div>
    </>
  );
}

export default NavBar;
