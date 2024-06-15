import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  token: null,
};

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    setLogin: (state, action) => {
      console.log(state);
      state.token = action.payload.access_token;
      console.log(state.token);
    },

    setLogout: (state, action) => {
      state.token = null;
    },
  },
});

export default authSlice.reducer;
export const { setLogin, setLogout } = authSlice.actions;
export const selectCurrentToken = (state) => state.auth.token;
