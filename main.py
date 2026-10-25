import json
import urllib.request
import urllib.error
import tkinter as tk
from tkinter import ttk, messagebox

APP_NAME = "NKZ PROMPT AI"

AI_GUIDES = {
    "ChatGPT": "Organize o pedido com contexto, objetivo, requisitos, etapas e formato de saída.",
    "Claude": "Priorize contexto detalhado, instruções claras, critérios de qualidade e análise cuidadosa.",
    "Gemini": "Use instruções diretas, contexto relevante e peça uma resposta estruturada e prática.",
    "Grok": "Use um tom direto, criativo e objetivo, deixando explícitos o contexto e o resultado esperado.",
    "Lovable": "Descreva o produto web, páginas, componentes, identidade visual, responsividade e comportamento.",
    "Cursor": "Peça alterações por arquivos, explique a arquitetura e solicite código funcional e instruções de execução.",
    "GitHub Copilot": "Informe a linguagem, ambiente, objetivo, restrições e exemplos esperados.",
    "Midjourney": "Descreva assunto, composição, iluminação, paleta, estilo visual e proporção da imagem.",
    "Leonardo AI": "Detalhe o sujeito, cenário, estilo, iluminação, materiais e composição visual.",
    "Stable Diffusion": "Especifique assunto, estilo, enquadramento, iluminação, detalhes e elementos a evitar.",
    "Perplexity": "Peça uma resposta objetiva, com fontes confiáveis, comparação e indicação de incertezas.",
    "IA genérica": "Use contexto, objetivo, requisitos, limitações e formato de resposta."
}

CATEGORIES = {
    "Texto": "Produção ou revisão de textos",
    "Código": "Programação, depuração ou explicação de código",
    "Fotos / Imagens": "Criação de conceito visual ou imagem",
    "Website": "Planejamento e desenvolvimento de sites",
    "Aplicativo": "Criação de aplicativos desktop ou mobile",
    "Cybersegurança": "Estudo e defesa de sistemas em ambiente autorizado",
    "Marketing": "Conteúdo, divulgação e identidade de marca",
    "Estudos": "Aprendizagem, resumo e exercícios",
    "Negócios": "Planejamento de produto ou negócio",
    "Análise de dados": "Análise, organização e interpretação de dados",
    "Roblox / Games": "Jogos, mecânicas, scripts e design",
    "Outro": "Tarefa personalizada"
}

def make_prompt(ai, category, goal, level, style, extra):
    guide = AI_GUIDES.get(ai, AI_GUIDES["IA genérica"])
    category_desc = CATEGORIES.get(category, category)
    return f"""# PROMPT PROFISSIONAL

## Papel
Atue como um especialista experiente e didático, adequado à tarefa solicitada.

## Objetivo
{goal.strip()}

## Categoria
{category} — {category_desc}.

## Orientações para a IA escolhida
IA de destino: {ai}.
{guide}

## Nível de detalhe
{level}

## Estilo da resposta
{style}

## Requisitos
- Entregue uma resposta organizada, clara e prática.
- Não invente informações, resultados, links ou funcionalidades.
- Se faltar uma informação essencial, faça perguntas objetivas antes de assumir detalhes.
- Quando houver código, entregue uma solução funcional, explique onde salvar cada arquivo e como executar.
- Respeite segurança, privacidade e uso autorizado.
{("- Requisitos adicionais: " + extra.strip()) if extra.strip() else ""}

## Formato de saída
Use títulos e listas quando ajudarem. Termine com próximos passos ou instruções de uso, se fizer sentido.
"""

def ask_openai(api_key, model, prompt):
    payload = {
        "model": model.strip() or "gpt-4.1-mini",
        "messages": [
            {"role": "system", "content": "Você é um especialista em engenharia de prompts. Melhore e complete o prompt do usuário sem mudar sua intenção. Responda em português do Brasil."},
            {"role": "user", "content": "Aprimore este prompt para ficar específico, claro e completo. Retorne somente o prompt final, pronto para copiar:\n\n" + prompt}
        ],
        "temperature": 0.7
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=data,
        headers={"Content-Type": "application/json", "Authorization": "Bearer " + api_key.strip()},
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=60) as response:
        result = json.loads(response.read().decode("utf-8"))
    return result["choices"][0]["message"]["content"].strip()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("NKZ PROMPT AI")
        self.root.geometry("1120x760")
        self.root.minsize(900, 650)
        self.root.configure(bg="#080b14")
        self._style()
        self._build()

    def _style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox", fieldbackground="#111827", background="#111827",
                        foreground="#e5e7eb", arrowcolor="#a78bfa")
        style.map("TCombobox", fieldbackground=[("readonly", "#111827")],
                  foreground=[("readonly", "#e5e7eb")])
        style.configure("TNotebook", background="#080b14", borderwidth=0)
        style.configure("TNotebook.Tab", background="#111827", foreground="#cbd5e1",
                        padding=(14, 8))
        style.map("TNotebook.Tab", background=[("selected", "#312e81")],
                  foreground=[("selected", "#ffffff")])

    def label(self, parent, text, color="#cbd5e1", size=10, bold=False):
        return tk.Label(parent, text=text, bg=parent.cget("bg"), fg=color,
                        font=("Segoe UI", size, "bold" if bold else "normal"))

    def _build(self):
        header = tk.Frame(self.root, bg="#0b1020", padx=24, pady=18)
        header.pack(fill="x")
        tk.Label(header, text="NKZ", bg="#0b1020", fg="#a78bfa",
                 font=("Segoe UI", 23, "bold")).pack(side="left")
        tk.Label(header, text=" PROMPT AI", bg="#0b1020", fg="#f8fafc",
                 font=("Segoe UI", 23, "bold")).pack(side="left")
        tk.Label(header, text="PROMPT STUDIO  •  WINDOWS DESKTOP",
                 bg="#0b1020", fg="#60a5fa", font=("Segoe UI", 9, "bold")).pack(side="right", pady=10)

        main = tk.Frame(self.root, bg="#080b14", padx=20, pady=16)
        main.pack(fill="both", expand=True)

        left = tk.Frame(main, bg="#0f172a", padx=16, pady=16,
                        highlightbackground="#26324b", highlightthickness=1)
        left.pack(side="left", fill="y", padx=(0, 14))
        left.configure(width=340)
        left.pack_propagate(False)

        self.label(left, "CONFIGURAR PROMPT", "#a78bfa", 12, True).pack(anchor="w", pady=(0, 14))
        self.label(left, "IA DE DESTINO", size=9, bold=True).pack(anchor="w")
        self.ai_var = tk.StringVar(value="ChatGPT")
        ttk.Combobox(left, textvariable=self.ai_var, values=list(AI_GUIDES.keys()),
                     state="readonly").pack(fill="x", pady=(5, 13))

        self.label(left, "CATEGORIA", size=9, bold=True).pack(anchor="w")
        self.category_var = tk.StringVar(value="Código")
        ttk.Combobox(left, textvariable=self.category_var, values=list(CATEGORIES.keys()),
                     state="readonly").pack(fill="x", pady=(5, 13))

        self.label(left, "O QUE VOCÊ QUER CRIAR?", size=9, bold=True).pack(anchor="w")
        self.goal = tk.Text(left, height=7, wrap="word", bg="#080f1e", fg="#f1f5f9",
                            insertbackground="#a78bfa", relief="flat", padx=10, pady=10,
                            font=("Segoe UI", 10), highlightbackground="#334155",
                            highlightthickness=1)
        self.goal.pack(fill="x", pady=(5, 13))
        self.goal.insert("1.0", "Ex.: crie um site moderno para meu portfólio de programação")

        self.label(left, "NÍVEL DE DETALHE", size=9, bold=True).pack(anchor="w")
        self.level_var = tk.StringVar(value="Completo — passo a passo")
        ttk.Combobox(left, textvariable=self.level_var,
                     values=["Rápido e direto", "Intermediário", "Completo — passo a passo", "Avançado / profissional"],
                     state="readonly").pack(fill="x", pady=(5, 13))

        self.label(left, "ESTILO", size=9, bold=True).pack(anchor="w")
        self.style_var = tk.StringVar(value="Profissional e organizado")
        ttk.Combobox(left, textvariable=self.style_var,
                     values=["Profissional e organizado", "Criativo e original", "Didático para iniciantes",
                             "Técnico e detalhado", "Minimalista", "Cyberpunk / tecnologia"],
                     state="readonly").pack(fill="x", pady=(5, 13))

        self.label(left, "REQUISITOS EXTRAS (OPCIONAL)", size=9, bold=True).pack(anchor="w")
        self.extra = tk.Entry(left, bg="#080f1e", fg="#f1f5f9", insertbackground="#a78bfa",
                              relief="flat", font=("Segoe UI", 10))
        self.extra.pack(fill="x", ipady=8, pady=(5, 15))
        self.extra.insert(0, "Ex.: sem bibliotecas externas; interface escura")

        buttons = tk.Frame(left, bg="#0f172a")
        buttons.pack(fill="x", pady=(2, 0))
        tk.Button(buttons, text="✦ GERAR PROMPT", command=self.generate,
                  bg="#7c3aed", fg="white", activebackground="#6d28d9", activeforeground="white",
                  relief="flat", font=("Segoe UI", 10, "bold"), pady=10, cursor="hand2").pack(fill="x")
        tk.Button(buttons, text="LIMPAR CAMPOS", command=self.clear,
                  bg="#1e293b", fg="#cbd5e1", activebackground="#334155", activeforeground="white",
                  relief="flat", font=("Segoe UI", 9), pady=8, cursor="hand2").pack(fill="x", pady=(7, 0))

        right = tk.Frame(main, bg="#0f172a", padx=16, pady=16,
                         highlightbackground="#26324b", highlightthickness=1)
        right.pack(side="left", fill="both", expand=True)
        top = tk.Frame(right, bg="#0f172a")
        top.pack(fill="x")
        self.label(top, "EDITOR DE PROMPT", "#a78bfa", 12, True).pack(side="left")
        self.status = tk.Label(top, text="PRONTO", bg="#0f172a", fg="#34d399",
                               font=("Segoe UI", 9, "bold"))
        self.status.pack(side="right")

        self.output = tk.Text(right, wrap="word", bg="#080f1e", fg="#dbeafe",
                              insertbackground="#a78bfa", relief="flat", padx=14, pady=14,
                              font=("Consolas", 10), highlightbackground="#334155",
                              highlightthickness=1)
        self.output.pack(fill="both", expand=True, pady=(12, 12))
        self.output.insert("1.0", "Seu prompt profissional aparecerá aqui.\n\nEscolha a IA, a categoria e descreva o que deseja criar. Depois clique em GERAR PROMPT.")
        actionrow = tk.Frame(right, bg="#0f172a")
        actionrow.pack(fill="x")
        tk.Button(actionrow, text="COPIAR PROMPT", command=self.copy,
                  bg="#0e7490", fg="white", activebackground="#155e75", activeforeground="white",
                  relief="flat", font=("Segoe UI", 9, "bold"), pady=9, cursor="hand2").pack(side="left")
        tk.Button(actionrow, text="SALVAR .TXT", command=self.save,
                  bg="#1e293b", fg="#e2e8f0", activebackground="#334155", activeforeground="white",
                  relief="flat", font=("Segoe UI", 9, "bold"), pady=9, cursor="hand2").pack(side="left", padx=8)

        api = tk.Frame(self.root, bg="#0b1020", padx=20, pady=10)
        api.pack(fill="x")
        tk.Label(api, text="MODO IA REAL (opcional)", bg="#0b1020", fg="#a78bfa",
                 font=("Segoe UI", 9, "bold")).pack(side="left")
        tk.Label(api, text="Chave API OpenAI:", bg="#0b1020", fg="#94a3b8",
                 font=("Segoe UI", 9)).pack(side="left", padx=(12, 5))
        self.api_key = tk.Entry(api, show="•", bg="#111827", fg="#e2e8f0",
                                insertbackground="#a78bfa", relief="flat", width=24)
        self.api_key.pack(side="left", ipady=5)
        tk.Label(api, text="Modelo:", bg="#0b1020", fg="#94a3b8",
                 font=("Segoe UI", 9)).pack(side="left", padx=(10, 5))
        self.model = tk.Entry(api, bg="#111827", fg="#e2e8f0", insertbackground="#a78bfa",
                              relief="flat", width=15)
        self.model.insert(0, "gpt-4.1-mini")
        self.model.pack(side="left", ipady=5)
        tk.Button(api, text="APRIMORAR COM IA", command=self.enhance,
                  bg="#4338ca", fg="white", activebackground="#3730a3", activeforeground="white",
                  relief="flat", font=("Segoe UI", 9, "bold"), padx=10, pady=6,
                  cursor="hand2").pack(side="right")
        tk.Label(self.root, text="NKZ PROMPT AI • Gerador local funciona sem API. A chamada de IA real pode gerar custos na conta do provedor.",
                 bg="#080b14", fg="#64748b", font=("Segoe UI", 8)).pack(pady=(0, 7))

    def generate(self):
        goal = self.goal.get("1.0", "end").strip()
        if not goal or goal.startswith("Ex.:"):
            messagebox.showwarning("Falta uma descrição", "Descreva o que você quer criar.")
            return
        prompt = make_prompt(self.ai_var.get(), self.category_var.get(), goal,
                             self.level_var.get(), self.style_var.get(), self.extra.get())
        self.set_output(prompt)
        self.status.config(text="PROMPT GERADO", fg="#34d399")

    def set_output(self, value):
        self.output.delete("1.0", "end")
        self.output.insert("1.0", value)

    def copy(self):
        value = self.output.get("1.0", "end").strip()
        self.root.clipboard_clear()
        self.root.clipboard_append(value)
        self.status.config(text="COPIADO", fg="#22d3ee")

    def save(self):
        from tkinter import filedialog
        value = self.output.get("1.0", "end").strip()
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                filetypes=[("Arquivo de texto", "*.txt")], initialfile="nkz-prompt.txt")
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(value)
            self.status.config(text="ARQUIVO SALVO", fg="#34d399")

    def clear(self):
        self.goal.delete("1.0", "end")
        self.extra.delete(0, "end")
        self.set_output("")
        self.status.config(text="LIMPO", fg="#fbbf24")

    def enhance(self):
        key = self.api_key.get().strip()
        current = self.output.get("1.0", "end").strip()
        if not key:
            messagebox.showinfo("Chave de API necessária",
                "Para usar a IA real, informe sua chave de API OpenAI. Sem chave, o gerador local continua funcionando.")
            return
        if not current or current.startswith("Seu prompt profissional"):
            self.generate()
            current = self.output.get("1.0", "end").strip()
        self.status.config(text="CONECTANDO...", fg="#fbbf24")
        self.root.update_idletasks()
        try:
            improved = ask_openai(key, self.model.get(), current)
            self.set_output(improved)
            self.status.config(text="APRIMORADO COM IA", fg="#34d399")
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")[:500]
            self.status.config(text="ERRO NA API", fg="#fb7185")
            messagebox.showerror("Erro na API", f"Não foi possível chamar a API (HTTP {e.code}).\nConfira a chave, o modelo e os limites da conta.\n\n{detail}")
        except Exception as e:
            self.status.config(text="ERRO DE CONEXÃO", fg="#fb7185")
            messagebox.showerror("Falha na conexão", f"Não foi possível aprimorar o prompt.\nVerifique a internet e tente novamente.\n\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
