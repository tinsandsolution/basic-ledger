import './App.css';
import LoggedOutPage from './components/LoggedOutPage';
import { useSelector, useDispatch } from 'react-redux';
import { authenticate } from './store/session';
import React, { useState, useEffect } from 'react';


function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if(!loaded) {
    return null;
  }
  return (
    <div className="App">
      {/* if user is null, show loginform */}
      <div>hi</div>
      {user ? <div>hi</div> : <LoggedOutPage />}
    </div>
  );
}

export default App;
