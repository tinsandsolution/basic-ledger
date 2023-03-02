import './App.css';
import LoginForm from './auth/login';
import { useSelector, useDispatch } from 'react-redux';

function App() {
  const user = useSelector(state => state.session.user);

  return (
    <div className="App">
      {/* if user is null, show loginform */}
      <div>hi</div>
      {user ? <div>hi</div> : <LoginForm />}
    </div>
  );
}

export default App;
