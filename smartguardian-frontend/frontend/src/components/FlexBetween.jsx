/**
 * A styled component that represents a flex container with space between items.
 * @component
 *  
 * @returns {JSX.Element} flex container.
 */
import { Box } from '@mui/material';
import { styled } from '@mui/system';

export const FlexBetween = styled(Box)({
  display: 'flex',
  justifyContent: 'space-between',
  alignItems: 'center',
});