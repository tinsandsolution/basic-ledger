import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { redirect } from 'react-router-dom';
import { signUp } from '../../store/session';
import './Login.css'

const SignupForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [username, setUsername] = useState('');
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    let errors = []

    // const emailRegex = /^.{1,100}@.{1,100}?\..{1,100}$/
    // if (!email.match(emailRegex)) errors.push("Please enter a valid email")

    setErrors(errors)

    if (!errors.length) {
      const data = await dispatch(signUp(email, password, username));
      if (data) {
        console.log(data)
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

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  return (
    <form className="login-form" onSubmit={onLogin}>
      <div className='form-title'> Sign Up Here! </div>
      <div className='login-errors'>
        {errors.map((error, ind) => (
          <div className="modal-form-error" key={ind}>{error}</div>
        ))}
      </div>
      <div className='form-single-data'>
        <input
          name='email'
          type='text'
          placeholder='Email'
          value={email}
          onChange={updateEmail}
        />
      </div>
      <div className='form-single-data'>
        <input
          name='username'
          type='text'
          placeholder= 'Username'
          value={username}
          onChange={updateUsername}
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
      <button className="black-button button-margin" type='submit'>Sign Up</button>
    </form>
  );
};

export default SignupForm;
