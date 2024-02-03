import ollama
import telebot
import os

model = "llama2"


if __name__ == '__main__':

    print("Running LLMBot...")

    BOT_TOKEN = "<your_bot_token>"
    bot = telebot.TeleBot(BOT_TOKEN)

    #allowed_users = ["your_user"]

    @bot.message_handler(commands=['chat'])
    def chat_handler(message):
        #if message.chat.username in allowed_users:
        sent_msg = bot.send_message(message.chat.id,
                         "¿Qué quieres saber hoy? ",
                         parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg, message_handler)
        #else:
        #    bot.send_message(message.chat.id, "You are not allowed to use this bot", parse_mode="Markdown")


    @bot.message_handler(commands=['cambiarmodelo'])
    def chat_handler(message):
        #if message.chat.username in allowed_users:
        sent_msg = bot.send_message(message.chat.id,
                                    "¿Qué modelo quieres? ",
                                    parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg, model_change)
        #else:
        #    bot.send_message(message.chat.id, "You are not allowed to use this bot", parse_mode="Markdown")

    def message_handler(message):
        msg = message.text

        bot.send_message(message.chat.id, "Usando el modelo: " + model, parse_mode="Markdown")

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
        model = new_model

    bot.infinity_polling()


