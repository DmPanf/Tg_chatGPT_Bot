// teloxide is a popular crate for creating Telegram bots in Rust
// add teloxide, tokio, reqwest, and serde_json dependencies to your Cargo.toml file.

use std::fs::OpenOptions;
use std::io::prelude::*;
use serde_json::Value;
use reqwest;
use teloxide::prelude::*;

#[tokio::main]
async fn main() {
    let bot = Bot::from_env().auto_send();

    teloxide::repl(bot, |message| async move {
        handle_message(&message).await;
        respond!(message.text("Done"))
    })
    .await;
}

async fn handle_message(message: &teloxide::types::Message) {
    // Load the environment variables from the env.json file
    let file = std::fs::read_to_string("env.json").expect("Failed to read env.json");
    let env: Value = serde_json::from_str(&file).expect("Failed to parse env.json");
    
    let chatgpt_api_key = env["CHATGPT_API_KEY"].as_str().expect("CHATGPT_API_KEY not found");
    let data_storage_file = env["DATA_STORAGE_FILE"].as_str().expect("DATA_STORAGE_FILE not found");

    let client = reqwest::Client::new();

    let res = client.post("https://api.openai.com/v1/engines/davinci-codex/completions")
        .header("Authorization", format!("Bearer {}", chatgpt_api_key))
        .json(&json!({
            "prompt": message.text(),
            "max_tokens": 50,
            "temperature": 0.7
        }))
        .send()
        .await
        .expect("Failed to send request")
        .json::<Value>()
        .await
        .expect("Failed to parse response");

    // Save the request and response to the data storage file
    let mut file = OpenOptions::new()
        .write(true)
        .append(true)
        .open(data_storage_file)
        .expect("Failed to open file for appending");

    writeln!(
        file,
        "Request: {}\nResponse: {}\n\n",
        message.text(),
        res["choices"][0]["text"]
    )
    .expect("Failed to write to file");
}
