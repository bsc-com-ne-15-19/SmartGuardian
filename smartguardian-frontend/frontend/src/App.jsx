import { CssBaseline } from '@mui/material';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Dashboard } from './features/auth/Dashboard';
import Login from './features/auth/Login';

import AlertsList from './features/alerts/AlertsList';
import NewUserForm from './features/users/NewUserForm';
import UsersList from './features/users/UsersList';

function App() {
  return (
    <>
      <BrowserRouter>
        <CssBaseline />
        <Routes>
          {/* <Route index element={<Login />} /> */}

            <Route index element={<Dashboard />} />

          <Route path='home' >

            <Route path='users'>
              <Route index element={<UsersList />} />
              <Route path='create' element={<NewUserForm />} />
            </Route>
            <Route path='alerts'>
              <Route index element={<AlertsList />} />
            </Route>
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
