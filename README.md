# Twitch ChatGPT bot

#### This simple twitch bot allows you to communicate with ChatGPT from twitch chat!

## Table of Contents
    
   + [Installation](#Installation)
   * [OAuth obtaining](#OAuth_obtaining)
   - [Usage](#Contributing)
   + [OpenAI_API](#OpenAI_API)
   * [Contributing](#Contributing)

### Installation

> 1. First of all, let\`s install some modules:
```
pip install twitchio
pip install asyncio
pip install revChatGPT
```
> 2. Next up [download](https://github.com/atikiNBTW/twitch-chatgpt-bot/archive/refs/heads/main.zip) this bot and unpack it!

> 3. Then open a [config.json](/config.json) file and rewrite some options there:
+ "bot-token" - Enter the bot token here, which would have been obtained in [this](#OAuth_obtaining) article.
* "bot-prefix" - Here define prefix, which bot would use in commands/
- "openAI_key" - Here enter OpenAI API key, here\`s guide to obtain.
+ "channels": ['atikiNBTW', 'MORE CHANNELS']"

> 4. Create an account on Twitch for your bot.

### OAuth_obtaining

> #### 1. Log in to the Twitch account you created for your bot.

> #### 2. Go to [this link](https://dev.twitch.tv/console/apps/create) and create a new application.

> #### 3. Enter a name for your application and select the "Chat Bot" category.

> #### 4. In "OAuth Redirect URLs" section add "http://localhost" as the redirect URL.

> #### 5. Click the "Create" button.

> #### 6. Click the "New Secret" button to generate a new client secret.

> #### 7. Copy the "Client ID" and "Client Secret" values to a safe place.

> #### 8. Use the following URL in your browser and replace CLIENT_ID with the Client ID obtained in step 7 above:
```
https://id.twitch.tv/oauth2/authorize?response_type=code&client_id=CLIENT_ID&redirect_uri=http://localhost&scope=chat:read+chat:edit
```

> #### 9. You should be redirected to a Twitch authorization page. Log in with the Twitch account you created for your bot and click the "Authorize" button.

> #### 10. You should now be redirected to a blank page with a URL in the address bar. Copy the "code" value from the URL.

> #### 11. Open a command prompt (Windows) or terminal (Mac/Linux) and run the following command, replacing the placeholders with your client ID, client secret, and code obtained in the previous steps: 
```
curl -X POST "https://id.twitch.tv/oauth2/token?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&code=CODE&grant_type=authorization_code&redirect_uri=http://localhost"
```
> #### 12. This should return a JSON object containing the access token for your bot. Copy the "access_token" value to a config.json file.

### OpenAI_API

### Contributing

MIT License

Copyright (c) [2023] [atikiNBTW]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

You can modify this template to fit the specific needs of your project. Make sure to include all the necessary information to help others understand and contribute to your project.
