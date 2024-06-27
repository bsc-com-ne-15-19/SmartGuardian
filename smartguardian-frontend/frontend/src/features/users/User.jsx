import { Typography } from '@mui/material';
import { useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { selectUserById } from './usersApiSlice';

/**
 * Renders a user component.
 *
 * @component
 * @param {Object} props - The component props.
 * @param {string} props.userId - The ID of the user.
 * @returns {JSX.Element|null} The rendered User component.
 */
const User = ({ userId }) => {
  const user = useSelector((state) => selectUserById(state, userId));
  const navigate = useNavigate();
  if (user) {
    const handleEdit = () => navigate(`/dash/users/${userId}`);
    const userRolesString = user.roles.toString().replaceAll(',', ', ');

    <Typography>{user}</Typography>;
  } else return null;
};

export default User;
