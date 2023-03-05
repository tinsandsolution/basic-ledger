import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { redirect } from 'react-router-dom';
// import { login } from '../../store/session';
import { getAllAccounts } from '../../store/ledger';
import './AllAccounts.css';
// import { Button } from '@mui/material';

const AccountsPage = () => {
  const accounts = useSelector(state => state.ledger.accounts);
  const dispatch = useDispatch();
  const [isLoaded, setLoaded] = useState(false);

  useEffect(() => {
    (async() => {
      await dispatch(getAllAccounts());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!isLoaded) return <></>
  return (
    <div className='all-accounts'>
        {accounts.map(account => (
          <div className='account-block' key={account.id}>
            <div className='account-title'> Account Number </div>
            <div className='account-name'>{account.account_number}</div>
            <div className='account-balance'>{account.current_balance}</div>
          </div>
        ))}
    </div>
  );
};

export default AccountsPage;
