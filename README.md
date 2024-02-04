# CUSTOM OLLAMA PYTHON BOT

This is a custom implementation of a TELEGRAM Bot made with Python with the aim of providing a custom chat by using [Ollama](https://github.com/ollama/ollama). 

This bot is under development, thanks for your patience!

This bot needs to connect with ollama, so you need to install it and run it. However, if you use the Docker implementation, ollama is already installed within in.

Now, you can chat with the model by typing /chat in the Bot. In the current version, to change the model, you need to modify the code. User control is allowed by modifying the allowed_users variable.

## Current Features
- Chat command
- User control
- List the available models with a command
- Change the model with a command
- Dockerfile and Docker Compose to deploy it as a container in an easy way
