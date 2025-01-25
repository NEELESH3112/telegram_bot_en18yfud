import logging
import torch
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from transformers import AutoModelForCausalLM, AutoTokenizer

# Set your Telegram Bot Token directly (Replace with your actual token)
TELEGRAM_BOT_TOKEN = "7657512273:AAGIhNELTklxVMcOT8XeSEq4Upmpw87Xv8c"

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN is missing! Please set it correctly.")

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)

# Load the AI model (TinyLlama)
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
print("⏳ Loading TinyLlama model...")

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,  # Ensure correct precision
    device_map="auto" if torch.cuda.is_available() else None
).to(device)

print(f"✅ Model loaded successfully on {device}!")

# Function to handle the "/start" command
async def start(update: Update, context):
    await update.message.reply_text("Hello! I am your AI Assistant powered by TinyLlama. Ask me anything!")

# Function to generate AI responses
def generate_response(prompt):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)
    output = model.generate(input_ids, max_length=200, temperature=0.7, do_sample=True)  # Fixed sampling issue
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Function to handle user messages
async def handle_message(update: Update, context):
    user_text = update.message.text
    logging.info(f"Received message: {user_text}")  # Debugging
    ai_response = generate_response(user_text)
    logging.info(f"Generated response: {ai_response}")  # Debugging
    await update.message.reply_text(ai_response)

# Start the bot
if __name__ == "__main__":
    try:
        app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

        # Add command and message handlers
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        # Start polling
        print("🤖 Bot is running...")
        app.run_polling()
    except Exception as e:
        print(f"❌ Error starting the bot: {e}")
