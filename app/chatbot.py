from ollama import Client
import json

import os

OLLAMA_HOST = os.getenv('OLLAMA_API_HOST', 'http://ollama:11434')
client = Client(host=OLLAMA_HOST)

class ChatBot:
    def __init__(self):
        self.history = {}  # Словник для зберігання історії обговорення
        self.knowledge = self.load_knowledge()

    def load_knowledge(self):
        try:
            with open("knowledge.txt", "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return "База знань пуста."

    def get_response(self, session_id: str, question: str, language: str) -> str:

        # Історія обговорення зберігається не більше 8 останніх повідомлень
        if session_id not in self.history:
            self.history[session_id] = []
        if len(self.history[session_id]) > 8:
            self.history[session_id] = self.history[session_id][-8:]

        prompt = f"""
        You are chat-bot speaking {language}.
        Here is your knowledge base: {self.knowledge}
        Chat history: {json.dumps(self.history[session_id], ensure_ascii=False)}
        Now answer the question according to your knowledge base:
        {question}
        """       

        try:
            response = client.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
            answer = response["message"]["content"]
        except Exception as e:
            answer = f"Помилка: {str(e)}"

        # Зберігаємо історію обговорення
        self.history[session_id].append({"question": question, "answer": answer})

        return answer