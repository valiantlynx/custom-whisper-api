# Custom Whispe API

## Overview

This project provides a custom API wrapper for the open-source Whisper model using FastAPI. It allows you to integrate Whisper into your applications for automatic speech recognition (ASR) tasks.

## Prerequisites

- [Docker](https://www.docker.com/) installed
- [docker-compose](https://docs.docker.com/compose/install/) installed

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd custom-whispe-api
```

### 2. Build and Start the Docker Containers

```bash
docker-compose up --build -d
```

This command builds and starts the Docker containers in the background.

### 3. Stop the Docker Containers

```bash
docker-compose down
```

Use this command to stop and remove the Docker containers.

## API Documentation

Once the containers are up and running, you can access the FastAPI documentation to understand and test the API endpoints.

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## API Endpoints

### ASR (Automatic Speech Recognition)

#### `POST /asr`

Submit an audio file for automatic speech recognition.

**Request:**
- Method: POST
- Endpoint: `/asr`
- Body: Audio file (multipart/form-data)

**Response:**
- Status Code: 200 OK
- Body: Transcription result

## Environment Variables

The API utilizes environment variables for configuration. You can customize these variables in the `.env` file.

- `WHISPER_MODEL_PATH`: Path to the Whisper model directory.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).