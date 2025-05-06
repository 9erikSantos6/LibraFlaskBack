# 📚 LibraFlaskBack

**LibraFlaskBack** é a API REST responsável por gerenciar os dados da aplicação **LibraFlask**, uma biblioteca digital minimalista.

---

## 📦 Tecnologias utilizadas

* Python 3.x
* Flask
* SQLite3
* SQLAlchemy
* Marshmallow
* `python-dotenv` (para variáveis de ambiente)
* `flask-cors` (para configuração de CORS)

---

## ⚙️ Como configurar e executar

### 1. Clone o repositório

```bash
git clone https://github.com/9erikSantos6/LibraFlaskBack.git
cd LibraFlaskBack
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate     # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

* Copie o arquivo `.env.example` para `.env`:

```bash
cp .env.example .env
```

* Edite o arquivo `.env` conforme necessário:

  * Defina uma porta válida (entre 1024 e 65535).
  * Configure a URL do banco de dados, se desejar usar outro caminho.
  * Gere uma chave segura para `SERVER_SECRET_KEY`.
  * Ative a criação de administrador padrão com `SERVER_CREATE_DEFAULT_ADMIN=TRUE` se desejar.

### 5. Configure o CORS

* Copie o arquivo de exemplo de configuração de CORS:

```bash
cp .cors.config.example.json .cors.config.json
```

* Altere os domínios permitidos no ambiente de produção, se necessário.

### 6. Execute a aplicação

```bash
python run.py
```

A API estará disponível em:
`http://localhost:<SERVER_PORT>` (ex: `http://localhost:15000`)

---

## 📖 Documentação dos endpoints

Para detalhes sobre o uso da API e dos endpoints disponíveis, acesse:
👉 [Wiki da aplicação](https://github.com/9erikSantos6/LibraFlaskBack/wiki)

---

## 🤝 Contribuições

Pull requests são bem-vindos! Sinta-se à vontade para abrir issues e propor melhorias.

---

## 📄 Licença

Este projeto está sob a licença MIT.
