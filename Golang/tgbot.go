package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"

	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api"
)

type Env struct {
	TELEGRAM_BOT_TOKEN string `json:"TELEGRAM_BOT_TOKEN"`
	CHATGPT_API_KEY    string `json:"CHATGPT_API_KEY"`
	DATA_STORAGE_FILE  string `json:"DATA_STORAGE_FILE"`
}

type OpenAIResponse struct {
	Choices []struct {
		Text string `json:"text"`
	} `json:"choices"`
}

func main() {
	file, _ := ioutil.ReadFile("env.json")
	var env Env
	_ = json.Unmarshal(file, &env)

	bot, _ := tgbotapi.NewBotAPI(env.TELEGRAM_BOT_TOKEN)

	u := tgbotapi.NewUpdate(0)
	u.Timeout = 60

	updates, _ := bot.GetUpdatesChan(u)

	for update := range updates {
		if update.Message == nil {
			continue
		}

		response := callOpenAI(env.CHATGPT_API_KEY, update.Message.Text)
		ioutil.WriteFile(env.DATA_STORAGE_FILE, []byte(fmt.Sprintf("Request: %s\nResponse: %s\n\n", update.Message.Text, response)), 0644)

		msg := tgbotapi.NewMessage(update.Message.Chat.ID, response)
		bot.Send(msg)
	}
}

func callOpenAI(apiKey string, prompt string) string {
	client := &http.Client{}
	reqBody := strings.NewReader(fmt.Sprintf(`{"prompt": "%s", "max_tokens": 50, "temperature": 0.7}`, prompt))
	req, _ := http.NewRequest("POST", "https://api.openai.com/v1/engines/davinci-codex/completions", reqBody)
	req.Header.Add("Authorization", "Bearer "+apiKey)
	resp, _ := client.Do(req)

	defer resp.Body.Close()
	body, _ := ioutil.ReadAll(resp.Body)

	var response OpenAIResponse
	_ = json.Unmarshal(body, &response)

	return response.Choices[0].Text
}
