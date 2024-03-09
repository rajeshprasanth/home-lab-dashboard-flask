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
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Installation

Follow these steps to set up the Home Lab Dashboard on your local machine:

### Prerequisites

Make sure you have the following installed:

- python (>=3.11.0)
- flask (>=2.3.2)
- art (>=6.0)
- coloredlogs (>=15.0.1)
- python-dotenv (>=1.0.1)
- waitress (>=2.1.2)


## Installation

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
    python app.py
    ```

5. **Access the Dashboard:**

    Open your web browser and go to [http://localhost:5000](http://localhost:5000) to access the Home Lab Dashboard.

Now, you have the "home-lab-dashboard-flask" project installed and running within a virtual environment. Remember to activate the virtual environment (`venv`) whenever you work on the project and deactivate it when you're done:

- To deactivate the virtual environment:

  ```bash
  deactivate
```
## Usage

To run the Home Lab Dashboard, use the following command:

```bash
python run_dashboard.py
```
Visit http://localhost:5000 in your web browser to access the dashboard.

## Configuration

Customize the port number by editing the configuration file located at apps/config/config.py

## Contributing

We welcome contributions! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Submit a pull request.

## License

This project is licensed under the MIT License.

