# Airflow Stock Data Extractor

Este projeto utiliza o **Apache Airflow** para automatizar a extração de dados históricos de ações de algumas das principais empresas do mercado.

---

## 📊 Ações monitoradas

O sistema faz a extração de dados históricos das seguintes ações:

- Apple (AAPL)  
- Microsoft (MSFT)  
- Google (GOOG)  
- Tesla (TSLA)  

Os dados são coletados **através da biblioteca `yfinance`** e salvos em arquivos CSV.

---

## ⚙️ Estrutura do Projeto

- `dags/` → Contém as DAGs do Airflow para execução das extrações.  
- `stocks/` → Pasta onde os arquivos CSV das ações são armazenados.  
- `venv/` → Ambiente virtual Python (não enviado ao GitHub).  
- `logs/` → Logs gerados pelo Airflow (não enviado ao GitHub).  

---

