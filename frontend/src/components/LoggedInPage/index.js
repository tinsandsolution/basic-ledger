import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { redirect } from 'react-router-dom';
// import { login } from '../../store/session';
import './LoggedInPage.css';
import { Button } from '@mui/material';

const LoggedInPage = () => {
  const [view, setView] = useState("accounts");
  const user = useSelector(state => state.session.user);

  return (
    <div className='logged-in'>
      <div className='sidebar'>
        <div className='sidebar__header'> Hi, {user}! </div>
        <div className='sidebar__content'>
          <Button
            variant={view === "accounts" ? "contained" : "outlined"}
            sx={{ width: '80%',}}
            onClick={() => setView("accounts")}
          >Accounts</Button>
          <Button
            variant={view === "transactions" ? "contained" : "outlined"}
            sx={{ width: '80%',}}
            onClick={() => setView("transactions")}
          >Transactions</Button>
        </div>
      </div>
      <div className='main'></div>
    </div>
  );
};

export default LoggedInPage;
