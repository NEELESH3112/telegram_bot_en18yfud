# telegram_bot_en18yfud


# AI Telegram Assistant Bot

This project is a Telegram bot powered by TinyLlama, an AI model for generating natural language responses. The bot allows users to chat with the AI assistant through Telegram and receive intelligent responses to various queries.

## Features
- **Interactive AI Assistant:** Chat with a virtual assistant that uses the TinyLlama AI model.
- **Customizable Responses:** The bot can process any text input and provide a relevant AI-generated response.
- **Easy Setup:** Simple steps to set up the bot on your own system and integrate with Telegram.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NEELESH3112/telegram_bot_en18yfud.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Telegram bot:
   - Use [BotFather](https://core.telegram.org/bots#botfather) on Telegram to create a bot and get the token.
   - Replace the token in the `TELEGRAM_BOT_TOKEN` variable in the `bot.py` file.

4. Run the bot:

   ```bash
   python bot.py
   ```

## Usage

1. After setting up and running the bot, go to your Telegram app.
2. Search for your bot by its username.
3. Start a conversation by sending a message (e.g., "Hello").
4. The bot will reply with a generated response powered by TinyLlama.
5. You can ask it anything, and it will generate appropriate answers.

Example:

```plaintext
User: Tell me a fact about lions.
Bot: Lions are the only cats that live in groups, called prides.
```
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [TinyLlama](https://huggingface.co/models) for providing the pre-trained model.
- [Telegram API](https://core.telegram.org/bots) for making bot creation easy.
- [Hugging Face Transformers](https://huggingface.co/transformers/) for the AI model integration.

