# CNH CODE CHALLENGE V2 – LLM Edition 🚀

## Challenge Description

This challenge is an evolution of **Code Challenge V1**, which involved basic mathematical operations via API.

In this new version, the goal is to integrate an **LLM (Large Language Model)** that can interpret a *single string input* from the user, understand the intended operation, and return the correct result.

> **Example input:** `"What is the result of multiplying 3 and 7?"`

The LLM **must use tools** to perform calculations. It **must not** use its internal knowledge to answer the user directly.

---

## How to Run the Project

```bash
# 1. Clone the repository
git clone https://github.com/your-org/your-repo.git
cd your-repo

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the API locally
uvicorn main:app --reload
```

Access the application at: http://localhost:8000/docs

---

## Challenge: Implement the `/challenge` Route

You must implement the `/challenge` route, which should accept requests in the following format:

```json
{
  "prompt": "What is 10 divided by 2?"
}
```

The LLM should interpret the prompt, identify the intended mathematical operation, and **use the provided tools** to return the result, like this:

```json
{
  "result": 5.0
}
```

---

## Challenge Rules

- The existing mathematical operations module must be converted into a **tool module** that the LLM can access.
- The LLM **must not** respond directly using its own knowledge. It **must always call a tool** to generate the result.
- You are free to choose any **LLM framework** you prefer (e.g., [LangChain](https://docs.langchain.com/), [CrewAI](https://docs.crewai.com/), [Agno](https://docs.agno.io/), [Transformers + OpenAI](https://platform.openai.com/), etc.).
- All rules from the previous challenge still apply:
  - Follow the provided project architecture
  - Use the structured logging system and `.env` configuration
  - Create a new branch for your implementation
  - Submit a Pull Request with your solution
  - Add `@huelerssey-qd` as the reviewer
