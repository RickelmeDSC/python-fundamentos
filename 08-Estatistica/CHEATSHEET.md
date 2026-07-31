# 📋 Cheatsheet — Estatística

> ⚠️ Os arquivos `.py` deste módulo estão **vazios** (0 bytes desde o commit inicial).
> Este cheatsheet cobre os tópicos previstos no roadmap; quando os exercícios forem
> preenchidos, atualize os exemplos com o código real.

Python puro — módulo `statistics` da biblioteca padrão é permitido na Fase 1.

## 01 — Distribuição de frequência

```python
dados = [12, 15, 12, 18, 15, 12, 20]

# frequência absoluta
freq = {}
for x in dados:
    freq[x] = freq.get(x, 0) + 1

# frequência relativa
freq_rel = {x: n / len(dados) for x, n in freq.items()}
```

Classes (faixas): defina limites e conte com `sum(1 for x in dados if lim_inf <= x < lim_sup)`.

## 02 — Tendência central

```python
import statistics as st

st.mean(dados)      # média — sensível a outliers
st.median(dados)    # mediana — robusta a outliers
st.mode(dados)      # moda — valor mais frequente (multimode() se empatar)
```

Na mão:
```python
media   = sum(dados) / len(dados)
ordenado = sorted(dados)
n = len(ordenado)
mediana = ordenado[n // 2] if n % 2 else (ordenado[n//2 - 1] + ordenado[n//2]) / 2
```

**Média ≫ mediana** → cauda à direita (ex.: renda). Reporte a mediana.

## 03 — Separatrizes

```python
q = st.quantiles(dados, n=4)     # quartis → [Q1, Q2, Q3]
d = st.quantiles(dados, n=10)    # decis
p = st.quantiles(dados, n=100)   # percentis
```

- Q2 = mediana = P50.
- IQR = Q3 − Q1 → base da regra de outlier: fora de `[Q1 − 1.5·IQR, Q3 + 1.5·IQR]`.

## 04 — Dispersão

```python
st.pvariance(dados)   # variância POPULACIONAL (÷ n)
st.variance(dados)    # variância AMOSTRAL (÷ n−1)
st.pstdev(dados)      # desvio padrão populacional
st.stdev(dados)       # desvio padrão amostral

cv = st.stdev(dados) / st.mean(dados)    # coeficiente de variação — compara dispersões de escalas diferentes
```

⚠️ Amostral vs populacional: amostra usa `n−1` (correção de Bessel). Com dados completos da população, use as versões `p*`.

## Conexão com Pandas

| Aqui | Lá |
|---|---|
| `freq` na mão | `df['col'].value_counts()` |
| `st.mean/median` | `df['col'].mean()` / `.median()` |
| `st.quantiles` | `df['col'].quantile([.25, .5, .75])` |
| `st.stdev` | `df['col'].std()` (amostral por padrão!) |
| tudo de uma vez | `df['col'].describe()` |
