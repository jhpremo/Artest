import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import NavBar from './components/navbar/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import User from './components/User';
import { authenticate } from './store/session';
import HomePage from './components/HomePage/HomePage';
import YourSets from './components/YourSets/YourSets';
import SetCard from './components/sets/SetCard';
import SetPage from './components/SetPage/SetPage';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        <Route path='/your-sets' exact={true}>
          <YourSets />
        </Route>
        <Route path='/sets/:setId'>
          <SetPage />
        </Route>
        <Route path='/' exact={true} >
          <HomePage />
        </Route>
        <Route exact path='/403'>
          <h1>403 Error: Forbidden</h1>
        </Route>
        <Route path='/404'>
          <h1>404 Error: Not found</h1>
        </Route>
        <Route>
          <h1>404 Error: Not found</h1>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
