/**
 * PrivateRoute component to handle navigation based on access token.
 * @param {Object} props - The component props.
 * @param {ReactNode} props.children - The children nodes to render if access token exists.
 * @returns {ReactNode} - Either the children nodes or a Navigate component redirecting to the home page.
 */
import { useSelector } from 'react-redux';
import { Navigate } from 'react-router-dom';
import { selectCurrentAccessToken } from './features/auth/authSlice';

const PrivateRoute = ({ children }) => {
  const accessToken = useSelector(selectCurrentAccessToken);

  return accessToken ? children : <Navigate to="/" />;
};

export default PrivateRoute;
