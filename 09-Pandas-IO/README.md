# 🐼 Pandas I/O — Trabalhando com diferentes formatos

Exercícios do curso **Pandas I/O: trabalhando com diferentes formatos de arquivos** (Alura, Nível 1 #15).

Parte da minha jornada de transição para Análise de Dados — **Semana 4 (Fase 2)**.

## 📚 O que cobre

| Aula | Tópico | Status |
|------|--------|--------|
| 01 | Leitura de arquivos CSV | ✅ Concluído |
| 02 | Utilizando planilhas (Excel) e Google Sheets | ✅ Concluído |
| 03 | Manipulando arquivos JSON e normalização de resposta de API | ✅ Concluído |
| 04 | Lendo dados em HTML (Wikipedia) e XML | ✅ Concluído |
| 05 | Trabalhando com banco de dados (SQLite via SQLAlchemy) | ✅ Concluído |

📋 Referência rápida de tudo que o módulo cobre: [`CHEATSHEET.md`](CHEATSHEET.md)

## 🛠 Dependências adicionais

Além de pandas e jupyter, este curso usa:

\`\`\`bash
py -m pip install --user openpyxl lxml html5lib sqlalchemy requests
\`\`\`

| Pacote | Para que serve |
|--------|---------------|
| openpyxl | Ler/escrever Excel (.xlsx) |
| lxml | Parser XML rápido |
| html5lib | Parser HTML (read_html) |
| sqlalchemy | Conexão com bancos SQL (aula 05) |
| requests | Chamadas a APIs e páginas web que bloqueiam o `urllib` padrão (aulas 03 e 04) |

## 📁 Estrutura

Uma pasta por aula, cada uma com notebook próprio e uma subpasta `dados/` com os arquivos de exemplo usados/gerados.