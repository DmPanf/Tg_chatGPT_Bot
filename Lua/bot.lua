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

function send_telegram_message(chat_id, text, token)
    local url = "https://api.telegram.org/bot" .. token .. "/sendMessage"
    local response = requests.post(
        url,
        {data = {
            chat_id = chat_id,
            text = text
        }}
    )
    return response
end

function get_updates(offset, token)
    local url = "https://api.telegram.org/bot" .. token .. "/getUpdates"
    local params = {}
    if offset then
        params.offset = offset
    end
    local response = requests.get(url, {params = params})
    return cjson.decode(response.text)
end

local last_update_id = nil

while true do
    local updates = get_updates(last_update_id and (last_update_id + 1) or nil, TELEGRAM_BOT_TOKEN)
    for _, update in ipairs(updates.result) do
        if update.message and update.message.text then
            local chat_id = update.message.chat.id
            local message_text = update.message.text
            handle_message({text = message_text})
            send_telegram_message(chat_id, "Response text here (or get it from handle_message)", TELEGRAM_BOT_TOKEN)
            last_update_id = update.update_id
        end
    end
    os.execute("sleep " .. tonumber(5))
end

end
