# Simple ChatGPT proxy / relay
This is a simple ChatGPT client/sandbox that works like a proxy and can be installed on your own server. It requires OpenAI API key.

## How it works
The client-side portion of the app encrypts your query and sends it to your own backend. The backend decrypts the message and relays it to OpenAI API. The reply is then sent back to the browser in the encrypted form.

## Requirements
 - OpenAI API key can be created [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-api-key).
 - Hosting for a python application 

## Features
 - The app is protected by HTTP basic authentication
 - Communication between the client (browser) and the app is encrypted

## How to test locally
1. Prepare the environment 
```
git clone https://github.com/dzmitry-savitski/chatgpt-proxy
cd chatgpt-proxy
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```
2. Create secrets
```
# HTTP basic cretentials
 export AUTH_USER=user
 export AUTH_PASSWORD=password

# A secret for encrypting messages 
 export ENCR_PASSWORD=change_me

# ChatGPT API key 
 export OPENAI_API_KEY=your_api_key
```

3. Run the application
```
flask run
```
The app should be running on http://127.0.0.1:5000


## How to run it on [fly.io](https://fly.io/)
1. Prepare the deployment
```
fly launch
```
This will create the needed configuration files.
2. Create secrets
````
 fly secrets set AUTH_USER=user
 fly secrets set AUTH_PASSWORD=password
 fly secrets set ENCR_PASSWORD=change_me
 fly secrets set OPENAI_API_KEY=our_api_key
````
3. Deploy
````
fly deploy
````