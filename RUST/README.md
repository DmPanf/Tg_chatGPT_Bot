# telegram_bot.rs based on RUST


## Installation on Manjaro Linux
- **`curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`**
- **`source $HOME/.cargo/env`**
- **`cargo new telegram_bot_project`**
- **`cd telegram_bot_project`**
- **`nano Cargo.toml`**
- **`cargo build`**
- **`cargo run`**
- **`export TELOXIDE_TOKEN=your_telegram_bot_token`**
- **`cargo run`**


## Cargo.toml
<code>
[dependencies]
teloxide = "0.5"
tokio = { version = "1", features = ["full"] }
reqwest = "0.11"
serde_json = "1.0"
</code>

