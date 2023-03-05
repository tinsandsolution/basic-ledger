import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { redirect } from 'react-router-dom';
// import { login } from '../../store/session';
import LoginForm from '../auth/login';
import SignupForm from '../auth/signup';
import './LoggedOutPage.css';
import { ToggleButtonGroup, ToggleButton } from '@mui/material';

const LoggedOutPage = () => {
  const [loggedIn, setLoggedIn] = useState("login");

  return (
    <div className='logged-out'>
      <div className='logged-out-toggle'>
        <ToggleButtonGroup
          value = {loggedIn}
          exclusive
          onChange = {(e, newLoggedIn) => { setLoggedIn(newLoggedIn) }}
          aria-label="login or signup"
        >
          <ToggleButton value="login" aria-label="login">
            Login
          </ToggleButton>
          <ToggleButton value="signup" aria-label="signup">
            Signup
          </ToggleButton>
        </ToggleButtonGroup>
        {loggedIn === "login" ? <LoginForm /> : <SignupForm />}
      </div>
    </div>
  );
};

export default LoggedOutPage;
