import ollama
import AI_voice_output

conversation = [{"role" : "system", "content" : "You are a helpful assistant named U-Phoria that replies with a happy tone, addressing all queries with a sentence or two at most"}]

def action(user_input):
    try:
        conversation.append({"role" : "user", "content" : user_input})
        response=ollama.chat(
            model="llama3.2",
            messages = conversation
        )

        bot_reply=response["message"]["content"].strip()
        conversation.append({"role" : "assistant", "content" : bot_reply})

        if bot_reply:
            AI_voice_output.AI_voice_output(bot_reply)
            return bot_reply
        else:
            return "Sorry, I didn't get a response."

    except Exception as e:
        return f"Exception: {str(e)}"