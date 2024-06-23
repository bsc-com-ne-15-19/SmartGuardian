


import { CssBaseline } from '@mui/material';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Dashboard } from './features/auth/Dashboard';
import Login from './features/auth/Login';

import AlertsList from './features/alerts/AlertsList';
import NewUserForm from './features/users/NewUserForm';
import UsersList from './features/users/UsersList';
import PrivateRoute from './PrivateRoute';


/**
 * Renders the main application component.
 *
 * @returns {JSX.Element} The rendered App component.
 */
function App() {
  return (
    <>
      <BrowserRouter>
        <CssBaseline />
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="home/*">
          {/* <Route path="home/*" element={<PrivateRoute><Dashboard /></PrivateRoute>}> */}
            <Route index element={<PrivateRoute><Dashboard /></PrivateRoute>} />
            <Route path="users">
              <Route index element={<PrivateRoute><UsersList /> </PrivateRoute>} />
              <Route path="create" element={<PrivateRoute><NewUserForm /></PrivateRoute>} />
            </Route>
            <Route path="alerts">
              <Route index element={<PrivateRoute><AlertsList /></PrivateRoute>} />
            </Route>
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;