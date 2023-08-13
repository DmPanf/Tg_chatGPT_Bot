local requests = require("requests")
local cjson = require("cjson")

local env = dofile('env.lua')

local TELEGRAM_BOT_TOKEN = env.TELEGRAM_BOT_TOKEN
local CHATGPT_API_KEY = env.CHATGPT_API_KEY
local DATA_STORAGE_FILE = env.DATA_STORAGE_FILE

local function handle_message(message)
    local response = requests.post(
        'https://api.openai.com/v1/engines/davinci-codex/completions',
        {
            headers = { Authorization = "Bearer " .. CHATGPT_API_KEY },
            data = cjson.encode({
                prompt = message.text,
                max_tokens = 50,
                temperature = 0.7
            })
        }
    )
    
    local resp_data = cjson.decode(response.text)

    local file = io.open(DATA_STORAGE_FILE, "a")
    file:write("Request: " .. message.text .. "\nResponse: " .. resp_data.choices[1].text .. "\n\n")
    file:close()

    -- Здесь нужно будет добавить код для отправки ответа пользователю через Telegram API

end

-- Здесь нужно будет добавить код для обработки входящих сообщений от телеграм-бота
