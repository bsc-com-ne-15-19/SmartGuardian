/* eslint-disable react-refresh/only-export-components */
/* eslint-disable react/prop-types */
import { Room } from '@mui/icons-material';
import * as React from 'react';

function Pin({ crisisAlert }) {
  return (
    <Room
      sx={{
        fontSize: 40,
        color: crisisAlert ? 'red' : '#1677ff',
        // backgroundColor: 'white',
        borderRadius: '50%',
      }}
    />
  );
}

export default React.memo(Pin);
