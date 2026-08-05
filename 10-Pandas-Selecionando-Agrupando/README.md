# 🐼 Pandas: selecionando e agrupando dados

Exercícios do curso **Pandas: selecionando e agrupando dados** (Alura, Nível 1 #16).

Parte da minha jornada de transição para Análise de Dados — **Semana 4 (Fase 2)**.

## 📚 O que cobre

| Aula | Tópico | Atividades | Status |
|------|--------|------------|--------|
| 01 | Conhecendo os dados | 9 | ✅ Concluído |
| 02 | Agrupamento de dados | 9 | ✅ Concluído |
| 03 | Agrupamentos multi-index | 10 | 🔄 Em andamento |
| 04 | Unindo dados | 15 | ⏳ Pendente |

📋 Referência rápida dos métodos do curso: [`CHEATSHEET.md`](CHEATSHEET.md) (as seções das aulas 02–04 são antecipação — marcadas por aula)

## 🎯 Pontos de foco deste curso

- `loc` vs `iloc` vs `query` — seleção de dados
- `groupby` com múltiplas colunas e múltiplas agregações (`agg`)
- `transform` vs `agg` vs `apply` — quando usar cada um
- `MultiIndex` — criar, navegar, resetar, achatar
- `merge` / `join` / `concat` — tipos de junção e como cada um perde ou duplica linhas

## 🛠 Dependências adicionais

Além de pandas e jupyter (já instalados desde o módulo anterior): `openpyxl` para ler a planilha do SEEG (instalado no módulo `09-Pandas-IO`) e `matplotlib` para os gráficos dos agrupamentos (`.plot()` da aula 02).

## 📥 Dados (não versionados)

O dataset deste curso é a planilha do **SEEG** (Sistema de Estimativas de Emissões e Remoções de Gases de Efeito Estufa, do Observatório do Clima):

```
1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx   (~78 MB)
```

Por causa do tamanho, o arquivo **não está no repositório** (`.gitignore`). Para rodar os notebooks:

1. Baixe a planilha pelo link disponibilizado na aula do curso na Alura, ou direto pela [plataforma do SEEG](https://plataforma.seeg.eco.br/).
2. Salve em `01_conhecendo_os_dados/dados/` mantendo o nome original.

A aba usada é a **`GEE Estados`** (103.312 linhas × 63 colunas).

```python
emissoes_gases = pd.read_excel(
    'dados/1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx',
    sheet_name='GEE Estados'
)
```

> O `UserWarning: Unknown extension is not supported` do openpyxl ao abrir a planilha é inofensivo — é um recurso visual do Excel que a biblioteca ignora, sem afetar os dados.

## 📁 Estrutura

Uma pasta por aula, cada uma com notebook próprio e uma subpasta `dados/` com os arquivos de exemplo usados/gerados.
