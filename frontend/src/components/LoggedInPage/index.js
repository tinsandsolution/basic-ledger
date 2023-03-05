import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { redirect } from 'react-router-dom';
// import { login } from '../../store/session';
import './LoggedInPage.css';

const LoggedInPage = () => {
  const [loggedIn, setLoggedIn] = useState("login");
  const user = useSelector(state => state.session.user);

  return (
    <div className='logged-in'>
      <div className='sidebar'>
        <div className='sidebar__header'> Hi, {user}! </div>
        <div className='sidebar__content'> </div>
      </div>
      <div className='main'></div>
    </div>
  );
};

export default LoggedInPage;
