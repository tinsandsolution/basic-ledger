import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { redirect } from 'react-router-dom';
// import { login } from '../../store/session';
import LoginForm from '../auth/login';
import './LoggedOutPage.css';
const LoggedOutPage = () => {


  return (
    <div className='logged-out'>
        <LoginForm />
    </div>
  );
};

export default LoggedOutPage;
