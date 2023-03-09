# tme_chat_bot
Test chatGPT connection Bot


---
## Short Instruction
To create a Telegram bot based on aiogram that connects to the ChatGPT API and stores all requests, you can follow these steps:

- Install the necessary packages
- Create a new bot on Telegram and obtain the API token.
- Create a new file called env.json in the same directory as your Python code. This file will store your API token and other sensitive information that should not be hard-coded in your code
- Create a new Python file and import the necessary packages
- Load the environment variables from the env.json file
- Create a new instance of the Telegram Bot
- Define a function to handle incoming messages
- Register the handle_message function as a handler for text messages
- Start the bot


To create a Docker Compose solution for the previous Telegram bot, you will need to create the following files

- **Dockerfile:** This file describes how to build a Docker image for your Python application. It should be located in the same directory as your Python code. Here is an example of what the Dockerfile might look like
- **requirements.txt:** This file lists the Python packages that your application depends on. It should be located in the same directory as your Python code. Here is an example of what the requirements.txt file might look like
- **bot.py:** This is the Python file that contains your bot code. It should be located in the same directory as your Dockerfile and requirements.txt files
- **env.json:** This is the file that contains your sensitive information like API keys and other credentials. It should be located in the same directory as your Dockerfile and requirements.txt files
- **docker-compose.yml:** This file describes how to run your Docker container. It should be located in the same directory as your Dockerfile and requirements.txt files. Here is an example of what the docker-compose.yml file might look like


This **docker-compose.yml** file tells Docker to build an image from the Dockerfile in the current directory and then start a container based on that image. It also mounts the env.json and data_storage.txt files as volumes in the container, so that they are accessible by the bot code. Finally, the restart: always option tells Docker to automatically restart the container if it crashes or is stopped.
