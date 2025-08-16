# chatr

A simple and extensible chat application built with a focus on modularity, real-time communication, and ease of use. This project serves as a foundation for building chat-based applications, whether for team collaboration, customer support, or general messaging purposes.

## Features

- Real-time chat between multiple users
- User authentication and session management
- Clean, responsive user interface
- Extensible architecture for adding new features (bots, emojis, file sharing, etc.)
- Database integration for persistent messaging

## Technology Stack

- **Backend:** Django 5.2.5, Channels 4.3.1, Daphne 4.2.1 (for ASGI support), Twisted 25.5.0, Autobahn 24.4.2
- **Frontend:** (See `src/` for details)
- **Real-time:** WebSockets via Django Channels and Daphne
- **Database:** (Configurable via Django ORM)
- **Other dependencies:** See below.

You can install these dependencies using:

```bash
pip install -r requirements.txt
```

> **Tip**: Make sure to use the exact versions listed above for compatibility.

## Getting Started

### Prerequisites

- Python 3.10+ recommended
- Node.js (v14 or higher) if using frontend build tooling
- npm or yarn (for frontend assets)
- [Optional] Docker for containerization

## Configuration

- All environment-specific settings are managed via the `.env` file.
- Refer to `.env.example` for required variables.

## Usage

1. Register a new user or log in with existing credentials.
2. Join or create a chat room.
3. Start messaging in real time with other users.

## Contributing

Contributions are welcome! Please open issues and pull requests as needed.

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Open a pull request describing your changes.

## License

This project is licensed under the MIT License.
