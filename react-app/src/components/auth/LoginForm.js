import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { login } from '../../store/session';

const LoginForm = ({ setToggleLogin }) => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(["Entered email or password is incorrect"]);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  useEffect(() => {
    if (user) {
      setToggleLogin(false);
    }
  }, [user, setToggleLogin])


  return (
    <form className="login-form" onSubmit={onLogin}>
      <div className='errors-login'>
        {errors.map((error, ind) => (
          <div key={ind}>{error}</div>
        ))}
      </div>
      <div className="new-card-input-wrapper">
        <input
          name='email'
          className="create-form-card-input"
          type='text'
          required
          maxLength={255}
          value={email}
          onChange={updateEmail}
        />
        <span htmlFor='email' className="create-form-card-label">Email</span>
      </div>
      <div className="new-card-input-wrapper">
        <input
          name='password'
          type='password'
          maxLength={40}
          required
          className="create-form-card-input"
          value={password}
          onChange={updatePassword}
        />
        <span htmlFor='password' className="create-form-card-label">Password</span>
      </div>
      <button className="navbar-create-button" id='login-submit-button' type='submit'>Login</button>
    </form>
  );
};

export default LoginForm;
