import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.telegram.telegrambots.bots.TelegramLongPollingBot;
import org.telegram.telegrambots.meta.api.methods.send.SendMessage;
import org.telegram.telegrambots.meta.api.objects.Message;
import org.telegram.telegrambots.meta.api.objects.Update;
import org.telegram.telegrambots.meta.exceptions.TelegramApiException;

public class ChatGPTBot extends TelegramLongPollingBot {
    private final String TOKEN = "YOUR_TELEGRAM_BOT_TOKEN";
    private final String OPENAI_API_URL = "https://api.openai.com/v1/engines/davinci-codex/completions";
    private final String CHATGPT_API_KEY = "YOUR_CHATGPT_API_KEY";
    
    @Override
    public void onUpdateReceived(Update update) {
        if (update.hasMessage() && update.getMessage().hasText()) {
            Message message = update.getMessage();
            String userInput = message.getText();

            // Get response from OpenAI API
            String gptResponse = getOpenAIResponse(userInput);

            SendMessage responseMessage = new SendMessage();
            responseMessage.setChatId(message.getChatId().toString());
            responseMessage.setText(gptResponse);

            try {
                execute(responseMessage);
            } catch (TelegramApiException e) {
                e.printStackTrace();
            }
        }
    }

    private String getOpenAIResponse(String prompt) {
        String response = "";

        CloseableHttpClient client = HttpClients.createDefault();
        HttpPost httpPost = new HttpPost(OPENAI_API_URL);

        httpPost.setHeader("Authorization", "Bearer " + CHATGPT_API_KEY);

        String json = "{ \"prompt\": \"" + prompt + "\", \"max_tokens\": 50, \"temperature\": 0.7 }";
        StringEntity entity = new StringEntity(json, "UTF-8");
        httpPost.setEntity(entity);
        httpPost.setHeader("Accept", "application/json");
        httpPost.setHeader("Content-type", "application/json");

        try (CloseableHttpResponse httpResponse = client.execute(httpPost)) {
            response = EntityUtils.toString(httpResponse.getEntity(), "UTF-8");
        } catch (Exception e) {
            e.printStackTrace();
        }

        return response; // You might want to extract the actual text from the JSON response
    }

    @Override
    public String getBotUsername() {
        return "YOUR_BOT_USERNAME";
    }

    @Override
    public String getBotToken() {
        return TOKEN;
    }
}
