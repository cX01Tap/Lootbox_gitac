# Lootbox Untitled

## Overview
Lootbox Untitled is a Flask web application designed to provide a seamless experience for users. This project is containerized using Docker and can be deployed using GitHub Actions.

## Project Structure
```
lootbox-untitled
├── src
│   ├── app.py          # Main application logic for the Flask app
│   └── __init__.py     # Initializes the Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker image configuration
└── .github
    └── workflows
        └── deploy.yml   # GitHub Actions workflow for deployment
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd lootbox-untitled
   ```

2. **Install dependencies:**
   Ensure you have Python 3.9 and pip installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   You can run the application locally using:
   ```bash
   python -m src.app
   ```

## Docker Instructions

To build and run the Docker container, use the following commands:

1. **Build the Docker image:**
   ```bash
   docker build -t lootbox-untitled .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 80:80 lootbox-untitled
   ```

## Deployment

This project uses GitHub Actions for deployment. The workflow is defined in `.github/workflows/deploy.yml`. Upon pushing changes to the main branch, the application will be automatically built and deployed.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.