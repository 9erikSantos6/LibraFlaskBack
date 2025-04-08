# 📚 LibraFlaskBack

**LibraFlaskBack** é a API REST responsável por gerenciar os dados da aplicação **LibraFlask**, uma biblioteca digital minimalista.

> ⚠️ Este README está em desenvolvimento e será atualizado conforme novas funcionalidades forem implementadas.

---

## 🚀 Funcionalidades atuais

### ✅ Listar livros
- **Método:** `GET`
- **Rota:** `/livros`
- **Descrição:** Retorna uma lista de livros no formato JSON.
- **Resposta:**
  - `200 OK` com um array de livros

### ➕ Adicionar livro
- **Método:** `POST`
- **Rota:** `/livros/adicionar`
- **Descrição:** Adiciona um novo livro ao acervo.
- **Body (JSON):**
```json
{
  "titulo": "A mosca",
  "autor": "Aranha",
  "ano": "2000-05-22",
  "genero": "culinaria",
  "sinopse": "Huuuum, uma delicia"
}
```
- **Resposta:**
  - `201 Created` com os mesmos dados enviados

---

## 📦 Tecnologias utilizadas
- Python 3.x
- Flask
- SQLite3 (banco de dados local)
- JSON (para comunicação via API)
- `python-dotenv` (para variáveis de ambiente)

---

## ⚙️ Como executar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/LibraFlaskBack.git
cd LibraFlaskBack
```

### 2. (Recomendado) Crie e ative um ambiente virtual
```bash
python -m venv venv          # Ou: virtualenv venv
source venv/bin/activate     # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
- Copie o arquivo `.env.example` para `.env`:
```bash
cp .env.example .env
```
- No arquivo `.env`, você pode configurar a porta da aplicação:
```env
PORT=15000
```

### 5. Inicie a API
```bash
python run.py
```

A API estará disponível em: `http://localhost:<PORT>` (por padrão, `15000`)

---

## 📌 Próximas funcionalidades
- 📖 Detalhamento e busca de livros
- 🗃️ Atualização e remoção de livros

---

## 🤝 Contribuições
Pull requests são bem-vindos! Fique à vontade para abrir issues e propor melhorias.

---

## 📄 Licença
Este projeto está sob a licença MIT.
