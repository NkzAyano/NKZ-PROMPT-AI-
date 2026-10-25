# NKZ PROMPT AI

Painel desktop para Windows com tema escuro/cyberpunk, gerador de prompts e opção de aprimoramento usando a API da OpenAI.

## Recursos
- Seleção de IA de destino: ChatGPT, Claude, Gemini, Grok, Lovable, Cursor, Copilot e outras.
- Categorias: texto, código, imagens, website, aplicativos, cibersegurança, estudos, games e mais.
- Geração local de prompts, sem chave API.
- Modo opcional de aprimoramento com IA real pela API da OpenAI.
- Copiar prompt e salvar em `.txt`.
- Interface em português brasileiro.

## Requisitos
- Windows 10 ou Windows 11.
- Python 3.10+ para executar o código-fonte.
- Para o modo IA real: conexão com internet e uma chave de API válida da OpenAI. O uso da API pode ter custos separados da assinatura do ChatGPT.

## Executar pelo Python
1. Instale Python 3, se necessário.
2. Abra a pasta do projeto.
3. Execute `run.bat` ou rode `python main.py`.

## Criar o EXE
1. Instale Python.
2. Dê duplo clique em `build_exe.bat`.
3. O executável será criado em `dist\\NKZ_PROMPT_AI.exe`.

O script de compilação instala PyInstaller no ambiente Python, se necessário. A compilação precisa de internet na primeira vez caso o PyInstaller ainda não esteja instalado.

## Segurança da chave API
A chave é usada apenas durante a sessão e não é salva pelo aplicativo. Não compartilhe sua chave nem publique-a no GitHub. A chave é enviada à API da OpenAI quando você clica em “APRIMORAR COM IA”.

## Limitações
A seleção de Claude, Gemini, Grok, Lovable e outras serve para adaptar a estrutura do prompt. A chamada de IA real incluída nesta versão usa a API da OpenAI. Para conectar APIs de outros provedores, será necessário adicionar integrações específicas e suas respectivas chaves.



<img width="1121" height="764" alt="Captura de tela 2026-10-25 200436" src="https://github.com/user-attachments/assets/ca510e7d-22e0-4e3e-b771-6b717e0dbdab" />

