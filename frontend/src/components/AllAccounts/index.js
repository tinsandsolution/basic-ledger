import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { redirect } from 'react-router-dom';
// import { login } from '../../store/session';
import { getAllAccounts, getAccountTransactions, getAllTransactions } from '../../store/ledger';
import './AllAccounts.css';
import { Button } from '@mui/material';
import { makeProperPrice } from '../../utils/priceFormatter';
import TransactionsPage from '../Transactions';

const AccountsPage = () => {
  const accounts = useSelector(state => state.ledger.accounts);
  const dispatch = useDispatch();
  const [isLoaded, setLoaded] = useState(false);
  const [clickedAccount, setClickedAccount] = useState(null);
  // we're going to sort accounts by account number
  if (accounts) accounts.sort((a, b) => a.account_number - b.account_number);

  useEffect(() => {
    (async() => {
      await dispatch(getAllAccounts());
    //   await dispatch(getAccountTransactions(15));
    //   await dispatch(getAllTransactions());
      setLoaded(true);
    })();
  }, [dispatch]);


  if (!isLoaded) return <></>
  return (
    <>
        <div className='all-accounts'>
            {accounts.map(account => (
            <div className='account-block' key={account.id}>
                <div className='account-title'> Account Number </div>
                <div className='account-name'>
                    {account.account_number.slice(0,4) + " "}
                    {account.account_number.slice(4,8) + " "}
                    {account.account_number.slice(8,12) + " "}
                    {account.account_number.slice(12,16) + " "}
                </div>
                <div className='account-balance'>
                    <span>Current Balance</span>
                    <span>{makeProperPrice(account.current_balance)}</span>
                </div>
                <div className='account-show-transactions'>
                    <Button
                        variant={clickedAccount === account.id ? "contained" : "outlined"}
                        onClick={() => {
                            setClickedAccount(account.id)
                        }}
                        size='small'
                    >Show Transactions</Button>
                </div>
            </div>
            ))}
        </div>
        { clickedAccount && <TransactionsPage account_id={clickedAccount} />}
    </>
  );
};

export default AccountsPage;
