import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { redirect } from 'react-router-dom';
import { login } from '../../store/session';
import './Login.css'

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    let errors = []

    // const emailRegex = /^.{1,100}@.{1,100}?\..{1,100}$/
    // if (!email.match(emailRegex)) errors.push("Please enter a valid email")

    setErrors(errors)

    if (!errors.length) {
      const data = await dispatch(login(email, password));
      if (data) {
        setErrors(data);
      }
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const loginDemo = () =>{
    setEmail('demo@aa.io');
    setPassword('password')
  }

  return (
    <form className="login-form" onSubmit={onLogin}>
      <div className='form-title'> Log In Here! </div>
      <div className='login-errors'>
        {errors.map((error, ind) => (
          <div className="modal-form-error" key={ind}>{error}</div>
        ))}
      </div>
      <div className='form-single-data'>
        <input
          name='email'
          type='text'
          placeholder='Email/Username'
          value={email}
          onChange={updateEmail}
        />
      </div>
      <div className='form-single-data'>
        <input
          name='password'
          type='password'
          placeholder='Password'
          value={password}
          onChange={updatePassword}
        />
      </div>
      <button className="black-button button-margin" type='submit'>Login</button>
      <button className="black-button button-margin-2" onClick={loginDemo}> Demo User </button>
    </form>
  );
};

export default LoginForm;
