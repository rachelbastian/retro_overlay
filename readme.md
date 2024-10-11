Retro Overlay

This app is designed to fetch data from the RetroAchievements API every 30 seconds, displaying recent achievement progress and recently played games for a specified user. It also includes an "Open Overlay" feature that opens a new tab, which can be integrated with OBS as an overlay for Twitch streams. The overlay updates in real-time every 30 seconds and uses a static, username-encoded URL for consistent display.

You can try out the live version at RetroCheevo.org or run the project locally by following the steps below.


To run this project locally, follow the steps below:

## Getting Started

To run this project, follow the steps below:

1. Obtain an API key by following the instructions at [RetroAchievements API Getting Started](https://api-docs.retroachievements.org/getting-started.html).
2. Create a virtual environment for Python by running the following commands:
    ```bash
    $ mkdir myproject
    $ cd myproject
    $ python3 -m venv .venv
    ```
3. Activate the virtual environment:
    ```bash
    $ . .venv/bin/activate
    ```
4. Install the required dependencies:
    ```bash
    $ pip install -r /path/to/requirements.txt
    ```
5. Edit the `.exampleenv` file by adding your API key and username, then rename the file to `.env`.
6. Edit the `gunicorn_config.py.example` file with your Hostname or IP:Port and rename it to `gunicorn_config.py`.
7. Finally, run the app with Gunicorn:
    ```bash
    $ gunicorn -c gunicorn_config.py app:app
    ```

The app will now be accessible at the designated IP:Port.

## Using the Overlay with OBS

To use the overlay in OBS for displaying recent achievement progress and recently played games, follow these steps:

1. Open OBS.
2. Add a new source by clicking **+** and selecting **Browser**.
3. Enter the URL of your overlay. For example:
    ```
    https://retrocheevo.org/recent-game-overlay/example
    ```
4. Set the dimensions of the browser source to **Width: 550px** and **Height: 250px**.
5. Click **OK** to save the source settings.

Your overlay will now appear in your OBS scene and will automatically update every 30 seconds.
