# INSTALLATION GUIDE

To install this product, please follow the steps below:

1. **Obtain a Mapbox API Key:**
   - Sign up or log in to your Mapbox account at [Mapbox](https://www.mapbox.com/).
   - Navigate to your Account page and create a new API key.

2. **Configure the API Key:**
   - Open the `Dockerfile` in the root directory of the project.
   - Find the line that sets the Mapbox API key environment variable (e.g., `ENV MAPBOX_API_KEY=your_mapbox_api_key_here`) and replace `your_mapbox_api_key_here` with your actual Mapbox API key.
   - Next, open the `mapCard.jsx` file located in the `frontend` directory.
   - Locate the line where the Mapbox API key is used (it might look something like `mapboxgl.accessToken = 'your_mapbox_api_key_here';`) and replace `your_mapbox_api_key_here` with your Mapbox API key.

3. **Build the Docker Containers:**
   - Open a terminal or command prompt.
   - Navigate to the root directory of the project where the `docker-compose.yml` file is located.
   - Run the following command to build the Docker containers:
     ```shell
     docker-compose build
     ```

4. **Run the Application:**
   - After the build process completes, start the application by running:
     ```shell
     docker-compose up
     ```
   - Wait for the containers to start. Once started, the application should be accessible.

By following these steps, you should have the application running with Mapbox integrated for map functionalities.
