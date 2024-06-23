import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  accessToken: null,
  refreshToken: null,
};

console.log("Initial state: ", initialState);

/**
 * Represents the authentication slice of the application state.
 *
 * @typedef {Object} AuthSlice
 * @property {string|null} accessToken - The access token for the authenticated user.
 * @property {string|null} refreshToken - The refresh token for the authenticated user.
 */

/**
 * The authentication slice of the application state.
 *
 * @type {AuthSlice}
 */
const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    setLogin: (state, action) => {
      state.accessToken = action.payload.access_token;
      state.refreshToken = action.payload.refresh_token;
      console.log("Login state: ", state);
    },

    setLogout: (state, action) => {
      state.accessToken = null;
      state.refreshToken = null;
      console.log("Logout state: ", state);
    },
  },
});

console.log("Auth slice: ", authSlice);

export default authSlice.reducer;
export const { setLogin, setLogout } = authSlice.actions;
export const selectCurrentAccessToken = (state) => {
  // console.log("Current access token: ", state.auth.accessToken);
  return state.auth.accessToken;
};
export const selectCurrentRefreshToken = (state) => {
  // console.log("Current refresh token: ", state.auth.refreshToken);
  return state.auth.refreshToken;
};