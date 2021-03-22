# Eventify

API do sistema de eventos.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.7+
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute o projeto.

```console
git clone https://github.com/mjr/eventify.git wevt
cd wevt
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py runserver
```

## Informações

### Estórias de usuário:

* Como USUÁRIO, preciso poder me inscrever no evento;
* Como USUÁRIO, preciso poder ver a programação do evento;
* Como ADMINISTRADOR, preciso poder cadastrar palestras;
* Como ADMINISTRADOR, preciso poder cadastrar cursos;

## Endpoint's:

### Subscriptions

Realiza a inscrição no evento
```
POST /subscriptions/
```

---

### Talks

Lista todas as palestras do evento
```
GET /talks/
```

Cadastra uma palestra no evento (cadastra as informações do palestrante junto)
```
POST /talks/
```

Altera alguma informação da palestra
```
PATCH /talks/
```

Ver as informações da palestra
```
GET /talks/[id]/
```

Apaga a palestra
```
DELETE /talks/[id]/
```

---

### Courses

Lista todas as palestras do evento
```
GET /courses/
```

Cadastra um curso no evento
```
POST /courses/
```

Altera alguma informação do curso
```
PATCH /courses/
```

Ver as informações do curso
```
GET /courses/[id]/
```

Apaga o curso
```
DELETE /courses/[id]/
```

---

### Schedule

Lista o cronograma do evento
```
GET /schedule/
```

## Exemplos de chamadas ao endpoints:

Realiza a inscrição no evento
```
POST /subscriptions/
```
```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name": "Test", "cpf": "00000000000", "email": "test@email.com", "phone": "(00) 00000-0000"}' \
  https://api-eventify.herokuapp.com/api/v1/subscriptions/
```

Lista todas as palestras do evento
```
GET /talks/
```
```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"title": "Rust", "description": "Uma linguagem capacitando todos a construir softwares confiáveis e eficientes.", "start": "08:00:00"}' \
  https://api-eventify.herokuapp.com/api/v1/talks/
```

Cadastra uma palestra no evento (cadastra as informações do palestrante junto)
```
POST /talks/
```
```bash
curl --request GET https://api-eventify.herokuapp.com/api/v1/talks/
```
