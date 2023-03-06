// constants

const SET_ACCOUNTS = 'market/SET_ACCOUNTS';
const SET_ACCOUNT_TRANSACTIONS = 'market/SET_ACCOUNT_TRANSACTIONS';
const SET_ALL_TRANSACTIONS = 'market/SET_ALL_TRANSACTIONS';

const setAccounts = (accounts) => ({
  type: SET_ACCOUNTS,
  payload: accounts
});
const setAccountTransactions = (transactions, accountId) => ({
    type: SET_ACCOUNT_TRANSACTIONS,
    payload: transactions,
    account_id : accountId
});
const setAllTransactions = (transactions) => ({
    type: SET_ALL_TRANSACTIONS,
    payload: transactions,
});


const initialState = { };

export const getAllAccounts = () => async (dispatch) => {
  const response = await fetch('http://127.0.0.1:8000/api/accounts/',{
    method: "GET",
    headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
      }
  });
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return;
    }

    dispatch(setAccounts(data));
    // console.log(data)
  }
}

export const getAccountTransactions = (accountId) => async (dispatch) => {
    const response = await fetch(`http://127.0.0.1:8000/api/accounts/${accountId}/transactions/`,{
      method: "GET",
      headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('access_token')}`
        }
    });
    if (response.ok) {
      const data = await response.json();
      if (data.errors) {
        return;
      }

      dispatch(setAccountTransactions(data,accountId));
    }
  }

export const getAllTransactions = () => async (dispatch) => {
    const response = await fetch(`http://127.0.0.1:8000/api/accounts/transactions/all`,{
        method: "GET",
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('access_token')}`
        }
    });
    if (response.ok) {
        const data = await response.json();
        if (data.errors) {
        return;
        }

        dispatch(setAllTransactions(data));
        // console.log(data)
    }
}


export default function reducer(state = initialState, action) {
  switch (action.type) {
    case SET_ACCOUNTS:
      return { ...state, accounts: action.payload };
    case SET_ACCOUNT_TRANSACTIONS:
      let newState = state;
      // inside accounts, find the account with the id that matches the payload's account id
    //   console.log(action.account_id)
      newState.accounts.forEach((account) => {
        if (account.id === action.account_id) {
          if (action.payload.length > 0) account.transactions = action.payload;
          else account.transactions = ["No transactions"];
        }
      });
      return newState;
    case SET_ALL_TRANSACTIONS:
        return { ...state, transactions: action.payload };
    default:
      return state;
  }
}
