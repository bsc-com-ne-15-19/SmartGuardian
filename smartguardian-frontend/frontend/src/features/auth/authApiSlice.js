import { apiSlice } from '@/app/api/apiSlice';
import { setLogout } from '@/features/auth/authSlice';
import { setLogin } from './authSlice';
import { accessToken } from 'mapbox-gl';

/**
 * A function that creates an API slice for authentication endpoints.
 *
 * @param {object} apiSlice - The API slice object.
 * @returns {object} - The auth API slice.
 */
export const authApiSlice = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    /**
     * Endpoint for user login.
     *
     * @param {object} credentials - The user credentials.
     * @returns {object} - The login response.
     */
    login: builder.mutation({
      query: (credentials) => ({
        url: 'login_api/login/',
        method: 'POST',
        body: { ...credentials },
      }),
      async onQueryStarted(arg, { dispatch, queryFulfilled }) {
        try {
          const { data } = await queryFulfilled;
          console.log(Object.keys(data));  // print keys of the response data
          console.log(Object.values(data));  // print values of the response data
        } catch (err) {
          console.log(err);
        }
      },
    }),

    /**
     * Endpoint for user registration.
     *
     * @param {object} credentials - The user credentials.
     * @returns {object} - The registration response.
     */
    register: builder.mutation({
      query: (credentials) => ({
        url: 'login_api/login/',
        method: 'POST',
        body: { ...credentials },
      }),
    }),

    /**
     * Endpoint for user logout.
     *
     * @returns {void}
     */
    logout: builder.mutation({
      query: () => ({
        url: '/auth/logout',
        method: 'POST',
      }),
      async onQueryStarted(arg, { dispatch, queryFulfilled }) {
        try {
          await queryFulfilled;
          dispatch(apiSlice.util.resetApiState());
          dispatch(setLogout);
        } catch (err) {
          console.log(err);
        }
      },
    }),

    /**
     * Endpoint for refreshing user tokens.
     *
     * @returns {void}
     */
    refresh: builder.mutation({
      query: () => ({
        url: 'login_api/login/',
        method: 'GET',
      }),
      async onQueryStarted(arg, { dispatch, queryFulfilled }) {
        try {
          const { data } = await queryFulfilled;
          // console.log(Object.keys(data));  // print keys of the response data
          if ('access_token' in data && 'refresh_token' in data) {
            dispatch(setLogin({ access_token: data.access, refresh_token: data.refresh }));
          } else {
            // console.log('One or both keys do not exist');
          }
        } catch (err) {
          console.log(err);
        }
      },
    }),
  }),
});

export const {
  useLoginMutation,
  useRegisterMutation,
  useLogoutMutation,
  useRefreshMutation,
} = authApiSlice;