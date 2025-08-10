# 📦 Kalash Inventory Management System

A modern, full-stack, three-tier web application for managing inventory, built with ReactJS, Python Flask, and MySQL. This project is containerized with Docker and includes an automated CI/CD pipeline using GitHub Actions for seamless deployment.

***

## 📝 Table of Contents

-   [Features](#-features)
-   [Tech Stack](#-tech-stack)
-   [Getting Started](#-getting-started)
-   [Project Structure](#-project-structure)
-   [Deployment](#-deployment)
-   [Contributing](#-contributing)
-   [License](#-license)

***

## ✨ Features

-   **Dashboard**: A clean, intuitive user interface to view and manage inventory.
-   **Add Products**: Easily add new products to the inventory with a simple form.
-   **RESTful API**: A robust backend API for managing product data.
-   **Three-Tier Architecture**: Separation of concerns between the frontend, backend, and database for better scalability and maintenance.
-   **Containerized**: The entire application stack is containerized with Docker, ensuring a consistent environment.
-   **Automated Deployment**: A CI/CD pipeline using GitHub Actions to automate the build, test, and deployment process.

***

## 🛠️ Tech Stack

This application is built on a modern three-tier architecture:

| Layer | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | `ReactJS` | A JavaScript library for building the user interface. |
| **Backend** | `Python (Flask)` | A micro-framework for building the RESTful API and handling business logic. |
| **Database** | `MySQL` | A robust relational database for data persistence. |
| **Containerization** | `Docker`, `Docker Compose` | For packaging and orchestrating the services into containers. |
| **CI/CD** | `GitHub Actions` | For automated build and deployment pipelines. |

***

## 🚀 Getting Started

Follow these steps to get the application up and running on your local machine.

### Prerequisites

You need to have the following software installed on your computer:
* **Git**: For cloning the repository.
* **Docker Desktop**: Includes Docker Engine and Docker Compose.

### Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/kalash-inventory.git](https://github.com/your-username/kalash-inventory.git)
    cd kalash-inventory
    ```

2.  **Run the application with Docker Compose:**
    From the root of the project directory, execute the following command. This will build the images, start the containers, and set up the database automatically.
    ```bash
    docker-compose up --build
    ```
    This command will build the Docker images and start the three services: `frontend`, `backend`, and `mysql`. The `--build` flag is needed the first time you run it.

### Accessing the Application

-   **Frontend**: Open your browser and navigate to `http://localhost`.
-   **Backend API**: The API is available at `http://localhost:5000/api`. You can use a tool like Postman or `curl` to test the endpoints.
-   **MySQL Database**: You can connect to the MySQL database from your local machine using a database client at `localhost:3306` with the user `user` and password `password`.

***

## 📂 Project Structure

This project follows a clear folder structure for easy navigation and maintenance.

-   **`/frontend`**: Contains all the ReactJS code for the user interface.
    -   `src/`: The source code for the React application.
-   **`/backend`**: Contains the Python Flask code for the REST API and business logic.
    -   `app.py`: The main entry point for the Flask application.
    -   `models.py`: Defines the database schemas using SQLAlchemy.
    -   `routes/`: Organizes API endpoints into modular blueprints.
-   **`docker-compose.yml`**: Defines and orchestrates all the Docker services.
-   **`Dockerfile.backend`**: Instructions for building the Python backend's Docker image.
-   **`Dockerfile.frontend`**: Instructions for building the React frontend's Docker image.
-   **`.github/workflows/main.yml`**: The GitHub Actions workflow for automated CI/CD.

***

## 🌐 Deployment

This project is set up for automated deployment using GitHub Actions. The workflow is configured to:
1.  Trigger on every push to the `main` branch.
2.  Build the Docker images for the frontend and backend.
3.  Push the images to a container registry (e.g., Docker Hub).
4.  Deploy the new containers to a cloud server via SSH.

To enable this, you need to configure your GitHub repository secrets for your Docker Hub and SSH credentials.

***

## 🤝 Contributing

We welcome contributions! Please feel free to fork the repository, open an issue, or submit a pull request.

***

## 📄 License

This project is licensed under the MIT License.

