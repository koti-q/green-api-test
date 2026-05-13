# Green API Test Page

A simple web interface for testing Green API (green-api.com) WhatsApp & Telegram integration capabilities.

## Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python 3.14 (HTTP Server)
- **Containerization**: Docker
- **External API**: Green API (green-api.com)

## Description

This project provides a user-friendly web interface to interact with the Green API service. It allows you to:
- Retrieve instance settings
- Check instance state
- Send text messages via WhatsApp
- Send files via URL to WhatsApp contacts

## How to Use

### Using Docker

1. **Build the Docker image:**
   ```bash
   docker build -t green-api-test .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8080:8080 green-api-test
   ```

3. **Access the application:**
   Open your browser and navigate to `http://localhost:8080`

4. **Use the application:**
   - Enter your `idInstance` and `ApiTokenInstance` (from Green API dashboard)
   - Use the buttons and input fields to test different API endpoints
   - View responses in the right panel

### Without Docker (Local Setup)

- Just run index.html file

