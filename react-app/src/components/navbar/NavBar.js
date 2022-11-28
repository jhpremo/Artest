
import React, { useEffect } from 'react';
import { useState } from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import LoginForm from '../auth/LoginForm';
import "./navbar.css"
import SignUpForm from '../auth/SignUpForm';
import { useSelector } from 'react-redux';

const NavBar = () => {
  const [toggleLogin, setToggleLogin] = useState(false)
  const [toggleSignup, setToggleSignup] = useState(false)
  const [toggleLinkDisable, setToggleLinkDisable] = useState(false)
  const [toggleDropDown, setToggleDropDown] = useState(false)

  let sessionUser = useSelector((state) => state.session.user)

  const openDropDown = () => {
    if (toggleDropDown) return;
    setToggleDropDown(true);
  };

  useEffect(() => {
    if (!toggleDropDown) return;

    const closeDropDown = () => {
      setToggleDropDown(false);
    };

    document.addEventListener('click', closeDropDown);

    return () => document.removeEventListener("click", closeDropDown);
  }, [toggleDropDown]);

  let dropDownClass
  if (toggleDropDown) {
    dropDownClass = "navbar-create-dropdown-wrapper"
  } else dropDownClass = 'navbar-hidden'

  useEffect(() => {
    console.log(sessionUser)
    if (sessionUser) setToggleLinkDisable(false)
    else setToggleLinkDisable(true)
  }, [sessionUser])


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

  const manageUserLinks = (e) => {
    if (toggleLinkDisable) {
      e.preventDefault()
      setToggleLogin(true)
    }
  }
  return (
    <>
      {toggleLogin && <div className='login-modal'>
        <div className='login-left'> <span>Artest your knowledge</span></div>
        <div className='login-right'>
          <div className='close-modal-button'><i onClick={close} className="fa-solid fa-x" /></div>
          <div className='login-signup-buttons-wrapper'>
            <div className='login-signup-wrapper'>
              <button id='login-active' onClick={openLogin}>Log in</button>
              <i className="fa-solid fa-paintbrush" />
            </div>
            <div className='login-signup-wrapper'>
              <button onClick={openSignup}>Sign up</button>
            </div>
          </div>
          <LoginForm setToggleLogin={setToggleLogin} />
        </div>
      </div>}
      {toggleSignup && <div className='login-modal'>
        <div className='login-left'> <span>Artest your knowledge</span></div>
        <div className='login-right'>
          <div className='close-modal-button'><i onClick={close} className="fa-solid fa-x" /></div>
          <div className='login-signup-buttons-wrapper'>
            <div className='login-signup-wrapper'>
              <button onClick={openLogin}>Log in</button>
            </div>
            <div className='login-signup-wrapper'>
              <button id='signup-active' onClick={openSignup}>Sign up</button>
              <i className="fa-solid fa-paintbrush" />
            </div>
          </div>
          <SignUpForm setToggleSignup={setToggleSignup} />
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
          <NavLink onClick={manageUserLinks} to="/your-sets" className='navbar-left-button'>
            Your sets
          </NavLink>
          <NavLink onClick={manageUserLinks} to="/your-comparisons" className='navbar-left-button'>
            Your comparisons
          </NavLink>
          <div className='create-button-wrapper-nav'>
            <button className='navbar-create-button' onClick={openDropDown}>
              Create <i className="fa-solid fa-chevron-down" />
            </button>
            <div className={dropDownClass}>
              <NavLink onClick={manageUserLinks} to="/create-set">New Set</NavLink>
            </div>
          </div>
        </div>
        <div className='navbar-right-wrapper'>
          {!sessionUser && <><button onClick={openLogin} className='navbar-login-button'>
            Login
          </button>
            <button onClick={openSignup} className='navbar-signup-button'>
              Sign Up
            </button></>}
        </div>
        {sessionUser && <LogoutButton />}
      </div>
    </>
  );
}

export default NavBar;
