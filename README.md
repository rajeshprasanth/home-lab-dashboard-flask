# Home Lab Dashboard (Flask)

[![GitHub stars](https://img.shields.io/github/stars/rajeshprasanth/home-lab-dashboard-flask)](https://github.com/rajeshprasanth/home-lab-dashboard-flask/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/rajeshprasanth/home-lab-dashboard-flask)](https://github.com/rajeshprasanth/home-lab-dashboard-flask/issues)
[![GitHub license](https://img.shields.io/github/license/rajeshprasanth/home-lab-dashboard-flask)](https://github.com/rajeshprasanth/home-lab-dashboard-flask/blob/main/LICENSE)

## Overview

The Home Lab Dashboard is an innovative Flask-based web application meticulously crafted to facilitate the efficient management and monitoring of your home lab environment. Tailored for simplicity and practicality, this dashboard offers a user-friendly interface, empowering users to seamlessly interact with various facets of their home lab setup. Whether overseeing configurations, tracking performance metrics, or managing resources, the Home Lab Dashboard streamlines these tasks, enhancing the overall user experience and optimizing the utilization of your home lab infrastructure.

## Features

- **User-Friendly Interface:** The dashboard provides an intuitive and easy-to-use interface.

- **Configuration Oversight:** Users can oversee and manage configurations of their home lab setup.

- **Performance Metrics:** Track performance metrics for better understanding and optimization.

- **Resource Management:** Efficiently manage resources within the home lab environment.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contacts](#contacts)

## Installation

Follow these steps to set up the Home Lab Dashboard on your machine:

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/rajeshprasanth/home-lab-dashboard-flask.git
    cd home-lab-dashboard-flask
    ```

2. **Create a Virtual Environment:**

   - On Windows:

     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Home Lab Dashboard:**

    ```bash
    python dashboard.py
    ```

5. **Access the Dashboard:**

    Open your web browser and go to [http://localhost:5000](http://localhost:5000) to access the Home Lab Dashboard.

Now, you have the "home-lab-dashboard-flask" project installed and running within a virtual environment. Remember to activate the virtual environment (`venv`) whenever you work on the project and deactivate it when you're done:

- To deactivate the virtual environment:

  ```bash
  deactivate
    ```

## Configuration Settings

Before running the application, ensure you have configured the following settings in `dashboard.py`:

- **Logging Configuration:** Adjust logging settings in the `RotatingFileHandler` initialization to suit your requirements.
  - Example:
    ```python
    log_file = "logs/flask.log"
    handler = RotatingFileHandler(log_file, maxBytes=100000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    ```

- **Server Configuration:** Customize server options such as `bind`, `workers`, `threads`, `loglevel`, `accesslog`, and `errorlog` as per your deployment needs. The default settings should work in most cases.
  - Example (for Gunicorn):
    ```python
    options = {
        'bind': f'{ip_address}:{port}',
        'workers': 4,
        'threads': 2,
        'loglevel': 'info',
        'accesslog': 'logs/gunicorn-access.log',
        'errorlog': 'logs/gunicorn-error.log'
    }
    ```
  - Example (for Waitress):
    ```python
    log_file = 'logs/waitress.log'
    serve(app, host=ip_address, port=port, threads=4, ident=None, _quiet=False)
    ```

Ensure that these configurations are appropriately set according to your application requirements and deployment environment. In most cases, the default settings should suffice.

### data.json File Format
The `data.json` file serves as a central repository for storing information about various components within your network infrastructure. It follows a structured format to ensure easy parsing and integration with the Flask application. Let's delve deeper into each component of the JSON structure:

 - **Category:** The `Category` field categorizes each component based on its type or function within the network. This allows for easy organization and filtering of components on the dashboard. Example categories include "Network", "RemoteAccess", "Infrastructure", "Storage", and "VirtualMachine".

 - **Label:** The `Label` field provides a human-readable label or name for each component. This label is typically displayed on the dashboard to identify the component to users. It should be descriptive and easily recognizable.

 - **Icon:** The `Icon` field contains the path to an icon image representing the component. Icons enhance the visual representation of components on the dashboard, making it easier for users to identify them at a glance. Ensure that the icon path is correct and accessible.

 - **Link1 and Link2** The `Link1` and `Link2` fields represent URLs associated with the component. These links provide direct access to the component's management interface, console, or other relevant resources. `Link1` typically serves as the primary link, while `Link2` can be used for additional resources or fallback links.

#### Example:

```json
{
    "Category": "Network",
    "Label": "Router 1",
    "Icon": "static/logos/Wireless_Router.svg",
    "Link1": "http://wlsrt.inet0.internal.das",
    "Link2": "http://192.168.1.1"
}

```
##### Explanation:

 - **Category:** "Network"
 - **Label:** "Router 1"
 - **Icon:** "static/logos/Wireless_Router.svg"
 - **Link1:** "http://wlsrt.inet0.internal.das"
 - **Link2:** "http://192.168.1.1"

This example represents a network router labeled "Router 1". It is categorized under "Network" and is associated with an icon representing a wireless router. The Link1 directs to an internal management interface, while Link2 provides access via the router's IP address.

##### Notes:
 - Ensure that the JSON file is properly formatted and valid to prevent errors during data loading.
 - You can customize the structure and fields as per your specific application requirements.
 - Icons should be visually representative of the component to aid user recognition and navigation.

By maintaining information in this structured format, you can easily manage and visualize your network components within the Flask application's dashboard, providing users with comprehensive insights into your infrastructure.

## Usage

### Running with Flask built-in server
Start the application using Flask's built-in server with the following command:

```bash
python dashboard.py
```
This will start the application using Flask's built-in development server. The application will be accessible at http://127.0.0.1:5000/ by default.

### Running with Gunicorn server

Deploy your application with Gunicorn for improved performance and scalability:
```bash
python dashboard.py gunicorn --ip <ip_address> --port <port_number>
```
Replace <ip_address> and <port_number> with your desired IP address and port. Gunicorn provides improved performance and scalability, suitable for production deployments.
### Running with Waitress server
For production-ready deployments, utilize Waitress server:
```bash
python dashboard.py waitress --ip <ip_address> --port <port_number>
```
Similar to Gunicorn, Waitress is another production-ready server that can be used to deploy the application. Replace <ip_address> and <port_number> accordingly.

### Accessing the Dashboard

Once the application is running, you can access the dashboard by opening a web browser and navigating to the URL provided by the server. Depending on the server used and the configured IP address and port, the URL may vary. By default, the dashboard can be accessed at http://127.0.0.1:5000/.

### Customization and Development

Feel free to customize the application according to your needs. You can modify the HTML templates (templates/) and static files (static/) to change the appearance and functionality of the dashboard. Additionally, you can extend the functionality of the application by adding new routes and features to dashboard.py.

### Stopping the Application

To stop the application, simply press Ctrl + C in the terminal where the application is running. This will gracefully shut down the server, and you'll be returned to the command prompt.

## Contributing

We welcome contributions! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Submit a pull request.

## License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.

## Contact

If you have any questions, feedback, or suggestions regarding the project, feel free to contact us:

- **Email:** [rajeshprasanth@rediffmail.com](mailto:rajeshprasanth@rediffmail.com)
- **GitHub Issues:** [Project Issues](https://github.com/rajeshprasanth/home-lab-dashboard-flask/issues)

We appreciate your interest in our project and welcome any contributions or ideas you may have!

