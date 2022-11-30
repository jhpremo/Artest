import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { signUp } from '../../store/session';

const SignUpForm = ({ setToggleSignup }) => {
  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isSubmitted, setIsSubmited] = useState(false);
  const [repeatPassword, setRepeatPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  useEffect(() => {
    let errorArr = []
    if (!username || username.length > 40) errorArr.push('username must be between 1 and 40 characters')
    if (!email || !email.includes('@') || !email.includes('.')) errorArr.push('email address must be valid')
    if (password != repeatPassword) errorArr.push('passwords must match')

    setErrors(errorArr)

  }, [username, password, repeatPassword, email])


  const onSignUp = async (e) => {
    e.preventDefault();

    setIsSubmited(true)

    if (!errors.length) {
      const data = await dispatch(signUp(username, email, password));
      if (data) {
        setErrors(data)
      }
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  useEffect(() => {
    if (user) {
      setToggleSignup(false);
    }
  }, [user, setToggleSignup])

  return (
    <form className="login-form" onSubmit={onSignUp}>
      <div className='errors-login'>
        {isSubmitted && errors.map((error, ind) => (
          <div key={ind}>{error}</div>
        ))}
      </div>
      <div className="new-card-input-wrapper">
        <input
          type='text'
          name='username'
          onChange={updateUsername}
          required
          className="create-form-card-input"
          maxLength={40}
          value={username}
        ></input>
        <span htmlFor='email' className="create-form-card-label">Username</span>
      </div>
      <div className="new-card-input-wrapper">
        <input
          type='text'
          name='email'
          maxLength={255}
          required
          className="create-form-card-input"
          onChange={updateEmail}
          value={email}
        ></input>
        <span htmlFor='email' className="create-form-card-label">Email</span>
      </div>
      <div className="new-card-input-wrapper">
        <input
          type='password'
          name='password'
          maxLength={40}
          className="create-form-card-input"
          required
          onChange={updatePassword}
          value={password}
        ></input>
        <span htmlFor='email' className="create-form-card-label">Password</span>
      </div>
      <div className="new-card-input-wrapper">
        <input
          type='password'
          name='repeat_password'
          maxLength={40}
          className="create-form-card-input"
          required
          onChange={updateRepeatPassword}
          value={repeatPassword}
        ></input>
        <span htmlFor='email' className="create-form-card-label">Repeat Password</span>
      </div>
      <button className="navbar-create-button" id='signup-submit-button' type='submit'>Sign Up</button>
    </form>
  );
};

export default SignUpForm;
