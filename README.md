## Simple run

In app directory

```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload 
```

## Installation via docker-compose

### 1.Run containers

In root directory

```sh
docker-compose up --build -d
```

### 2.Pull model (mistral default)

Enter the ollama container. If you have another container name replace roamingapi-ollama-1 with it. Then pull mistrall, or any model you want to use

```sh
docker exec -it roamingapi-ollama-1 /bin/sh
```

inside the llama container

```sh
ollama pull mistral
```

## API

http://0.0.0.0:8000/chat

```json
{
  "input": {
    "question": "Скіки коштує смс якщо я в Італії",
    "language": "Ukrainian",
    "session_id": "2"
  }
}
```
