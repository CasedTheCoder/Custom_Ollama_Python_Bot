import ollama
import telebot
import os

model = "llama2"


if __name__ == '__main__':

    print("Running Ollama_Bot...")

    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    bot = telebot.TeleBot(BOT_TOKEN)

    allowed_users = os.environ.get("ALLOWED_USERS")
    allowed_users = allowed_users.split(",")

    allowed_models = ["llama2", "mistral", "dolphin-phi", "neural-chat", "starling-lm",
                      "codellama", "llama2-uncensored", "orca-mini", "vicuna", "llava"]

    model = "llama2"


    @bot.message_handler(commands=['listmodels'])
    def chat_handler(message):
        if message.chat.username in allowed_users:
            bot.send_message(message.chat.id,
                                        "Available models: \n- " + '\n- '.join(allowed_models),
                                        parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "You are not allowed to use this bot", parse_mode="Markdown")


    @bot.message_handler(commands=['chat'])
    def chat_handler(message):
        if message.chat.username in allowed_users:
            sent_msg = bot.send_message(message.chat.id,
                             "Ask me something! ",
                             parse_mode="Markdown")
            bot.register_next_step_handler(sent_msg, message_handler)
        else:
            bot.send_message(message.chat.id, "You are not allowed to use this bot", parse_mode="Markdown")


    @bot.message_handler(commands=['changemodel'])
    def chat_handler(message):
        if message.chat.username in allowed_users:
            sent_msg = bot.send_message(message.chat.id,
                                        "Which model do you want to use? ",
                                        parse_mode="Markdown")
            bot.register_next_step_handler(sent_msg, model_change)
        else:
            bot.send_message(message.chat.id, "You are not allowed to use this bot", parse_mode="Markdown")

    def message_handler(message):
        msg = message.text

        bot.send_message(message.chat.id, "Using model: " + model, parse_mode="Markdown")

        response = ollama.chat(model=model, messages=[
            {
                'role': 'user',
                'content': msg,
            },
        ])
        answer = response['message']['content']
        bot.send_message(message.chat.id, answer, parse_mode="Markdown")

    def model_change(message):
        new_model = message.text
        if message.text in allowed_models:
            data = ollama.list()

            # Check if your variable matches any 'name' field
            matched = False
            for mod in data['models']:
                if new_model in mod['name']:
                    matched = True

            if not matched:
                bot.send_message(message.chat.id, "Model not found, downloading it...", parse_mode="Markdown")
                ollama.pull(new_model)
                bot.send_message(message.chat.id, "Model successfully downloaded!!!", parse_mode="Markdown")

            global model
            model = new_model
            bot.send_message(message.chat.id, "Model changed to " + new_model, parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "The model " + new_model + " does not exist or it is not currently supported!", parse_mode="Markdown")

    bot.infinity_polling()


