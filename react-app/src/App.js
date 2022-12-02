import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import NavBar from './components/navbar/NavBar';
import { authenticate } from './store/session';
import HomePage from './components/HomePage/HomePage';
import YourSets from './components/YourSets/YourSets';
import SetPage from './components/SetPage/SetPage';
import NewSetPage from './components/NewSet/NewSetPage';
import EditSetPage from './components/NewSet/EditSetPage';
import YourComps from './components/YourComps/YourComps';
import CompPage from './components/CompPage/CompPage';
import NewComp from './components/NewComp/NewComp';
import EditComp from './components/NewComp/EditComp';

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
        <Route path='/your-comparisons' exact={true}>
          <YourComps />
        </Route>
        <Route path='/create-set' exact={true}>
          <NewSetPage />
        </Route>
        <Route path='/create-comparison' exact={true}>
          <NewComp />
        </Route>
        <Route exact={true} path='/comparisons/:compId'>
          <CompPage />
        </Route>
        <Route exact={true} path='/sets/:setId'>
          <SetPage />
        </Route>
        <Route exact={true} path='/sets/:setId/edit'>
          <EditSetPage />
        </Route>
        <Route exact={true} path='/comparisons/:compId/edit'>
          <EditComp />
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
      <h6 className="about-links-footer">
        <div className="about-links-github-icon"> <a target="_blank" href="https://github.com/jhpremo/Artest"><i className="fa-brands fa-github" /></a> <a target="_blank" href="https://www.linkedin.com/in/jhpremo/"><i className="fa-brands fa-linkedin" /></a></div>
        <div className="about-links-creators">Website clone created by Jason Premo</div>
      </h6>
    </BrowserRouter>
  );
}

export default App;
