from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

# Remove the extra newline character from the API token
credentials = 'Авторизационные данные'
# Create GigaChat instance
chat = GigaChat(credentials=credentials, verify_ssl_certs=False)

messages = [
    SystemMessage(
        content="Ты эмпатичный бот-психолог, который помогает пользователю решить его проблемы."
    )
]

while True:
    # User input
    user_input = input("User: ")
    messages.append(HumanMessage(content=user_input))

    # Use invoke method instead of __call__
    res = chat.invoke(messages)

    messages.append(res)

    # Service response
    print("Bot:", res.content)
