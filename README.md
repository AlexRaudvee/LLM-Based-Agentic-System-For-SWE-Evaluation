# LLM-Based-Agentic-System-For-SWE

An LLM-based agent that **fixes buggy Python code** and evaluates quality on the **Python subset of HumanEvalFix**.  
Designed to be lightweight, dockerized, and easy to iterate on from **VS Code (Reopen in Container)**.

---

## Task & Problem Description

**Goal.** Implement an **agentic system** (e.g., ReAct-style with a code interpreter tool) that proposes fixes for buggy Python functions and **evaluates** the fixes on **HumanEvalFix (Python)** using **pass@1** (or a subset).

**You may use:**
- Any agentic framework (suggested: **LangGraph**).
- Any LLM (suggested: a small open-source model like **Qwen3-0.6B**).  
- Any pass@1 implementation (original or fork).

**Constraints.**
- Sandboxed execution of LLM-generated code is **required**.
- If full HumanEvalFix is too heavy, use a **representative subsample**.

---

## Repository Structure

```
LLM-Based-Agentic-System-For-SWE/
├─ README.md
├─ LICENSE
├─ Dockerfile
├─ docker-compose.yml
├─ .devcontainer/
│  └─ devcontainer.json
├─ .gitignore
├─ requirements.txt
├─ Makefile
├─ configs/
│  └─ config.yaml
├─ scripts/
│  ├─ run_agent.py
│  └─ evaluate.py
├─ src/
│  └─ llm_agent/
│     ├─ __init__.py
│     ├─ agent.py
│     ├─ scaffold.py
│     ├─ registry.py
│     ├─ eval/
│     │  ├─ __init__.py
│     │  ├─ evaluator.py
│     │  └─ pass_at_k.py
│     └─ tools/
│        ├─ __init__.py
│        ├─ code_interpreter.py
│        └─ humanevalfix_loader.py
├─ data/
│  └─ README.md
└─ notebooks/
   └─ .gitkeep
```

---

## 🚀 How to Run

> **Prereqs:** Docker & VS Code with *Dev Containers* extension.

**Open in Dev Container**
1. Open the repo in VS Code.
2. Click **Reopen in Container** (uses `.devcontainer/devcontainer.json`).

**Install (inside container)**
```bash
pip install -r requirements.txt
```

**Run the Agent (dry-run / subset)**
```bash
python scripts/run_agent.py --subset 10 --model qwen3-0_6b --max-iters 6
```

**Evaluate on HumanEvalFix (pass@1)**
```bash
python scripts/evaluate.py --subset 50 --model qwen3-0_6b --passk 1
```

> You can point to a local or remote model via env/config. See `configs/config.yaml` for knobs.

---

## Results & Discussion (template)

- **Model:** Qwen3-0.6B (int4) via [your serving]
- **Subset:** 50 problems from HumanEvalFix (random seed 42)
- **Metric:** pass@1
- **Score:** (fill in)
- **Observations:**
  - Error types frequently fixed: (e.g., off-by-one, missing imports, type errors)
  - Failure modes: (e.g., hallucinated APIs, unsafe patches)
  - Next steps: (e.g., better tool-use prompting, few-shot traces)

> Please add your actual results after running `scripts/evaluate.py`.

---

## Configuration

- All runtime configuration lives in `configs/config.yaml` (model name, decoding params, subset size, timeouts, sandbox limits).
- Override any value via CLI flags or env vars.

---

## Acknowledgments

- [**HumanEvalFix**](https://arxiv.org/abs/2308.07124) authors & maintainers.
- [**LangGraph**](https://www.langchain.com/langgraph) for agentic workflows.
- [**Qwen**](https://huggingface.co/Qwen/Qwen3-0.6B) team for open models.
- [**ReAct**](https://arxiv.org/abs/2210.03629) for Synergizing Reasoning and Acting in Language Models paper.

---

## License

MIT — see [LICENSE](./LICENSE).
