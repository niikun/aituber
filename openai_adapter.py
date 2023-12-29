import openai
from dotenv import load_dotenv
import os

# APIkeyの設定
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")


class OpenAIAdapter:
    # system の初期設定
    def __init__(self):
        # 初期設定を syste_prompt.txt から読み込む
        with open("system_prompt.txt", "r", encoding="utf-8") as f:
            self.system_prompt = f.read()
        pass

    # message作成用の関数
    def _create_message(self, role, message):
        return {"role": role, "content": message}

    # chatの作成
    def create_chat(self, question):
        system_message = self._create_message("system", self.system_prompt)
        user_message = self._create_message("user", question)

        messages = [system_message, user_message]

        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )

        return res["choices"][0]["message"]["content"]


if __name__ == "__main__":
    adapter = OpenAIAdapter()

    response_text = adapter.create_chat("こんにちは")
    print(response_text)
