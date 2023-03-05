// constants
const SET_USER = 'session/SET_USER';
const REMOVE_USER = 'session/REMOVE_USER';
// const EDIT_FUNDS = 'session/EDIT_FUNDS'

const setUser = (user) => ({
  type: SET_USER,
  payload: user
});

// const editFunds = (funds) => ({
//   type: EDIT_FUNDS,
//   payload: funds
// })

const removeUser = () => ({
  type: REMOVE_USER,
})

const initialState = { user: null };

export const authenticate = () => async (dispatch) => {
  const response = await fetch('http://127.0.0.1:8000/api/user/hello/', {
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
    console.log(data)
    dispatch(setUser(data.username));
  }
}

export const login = (username, password) => async (dispatch) => {
  const response = await fetch('http://127.0.0.1:8000/api/user/login/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      username,
      password
    })
  });


  if (response.ok) {
    const data = await response.json();
    dispatch(setUser(data.username))
    localStorage.setItem('access_token', data.access);
    localStorage.getItem('refresh_token', data.refresh);
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      console.log(data)
      return data.errors;
    }
  } else {
    return ['An error occurred. Please try again.']
  }

}

export const logout = () => async (dispatch) => {
  const response = await fetch('/api/auth/logout', {
    headers: {
      'Content-Type': 'application/json',
    }
  });

  if (response.ok) {
    dispatch(removeUser());
  }
};


export const signUp = (email, password, username) => async (dispatch) => {
  console.log(username, email, password)
  const response = await fetch('http://127.0.0.1:8000/api/user/create/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      username,
      email,
      password,
    }),
  });

  if (response.status === 201) {
    const data = await response.json();
    dispatch(login(username, password))
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    }
  } else {
    return ['An error occurred. Please try again.']
  }
}

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case SET_USER:
      return { user: action.payload }
    case REMOVE_USER:
      return { user: null }
    default:
      return state;
  }
}
