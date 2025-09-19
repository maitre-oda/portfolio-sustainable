# Portefeuille multi-objectif (finance durable) — Template débutant

Projet pas-à-pas pour construire un portefeuille équilibrant **rendement**, **risque (CVaR)** et **empreinte carbone (CO₂)**.

## Démarrage rapide (Codespaces)
1. Ouvre ce repo dans **GitHub Codespaces**.
2. Attends que l'installation automatique termine (postCreate).
3. Lance Jupyter : `jupyter notebook --ip 0.0.0.0 --port 8888 --no-browser`.

## Démarrage local (pip/venv)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

## Où commencer ?
- Édite `tickers.csv`
- Ouvre `notebooks/01_data_download.ipynb`, puis `02_preprocessing_and_baseline.ipynb`.