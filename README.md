# Customer Churn Prediction Pipeline
Repositori untuk project Machine Learning Operations (MLOps) dengan TensorFlow Extended (TFX)

## Tentang Project
Project ini membangun pipeline machine learning untuk memprediksi customer churn menggunakan TensorFlow Extended (TFX). Pipeline ini mencakup:
- Pengolahan dan transformasi data
- Pelatihan model
- Validasi model
- Deployment model sebagai REST API
- Monitoring model dengan Prometheus

## Struktur Project
- `data/` - Berisi data Telco-Customer-Churn.csv
- `modules/` - Berisi komponen machine learning
  - `customer_churn_transform.py` - Modul untuk transformasi data
  - `customer_churn_trainer.py` - Modul untuk training model
  - `components.py` - Komponen pipeline TFX
- `output/` - Hasil pipeline dan model yang di-deploy
- `config/` - File konfigurasi untuk monitoring
- `monitoring/` - Konfigurasi Prometheus untuk model monitoring
- `Dockerfile` - File untuk membuat container model serving

## Menjalankan Pipeline Lokal
Untuk menjalankan pipeline secara lokal:

```bash
python local_pipeline.py
```

## Deployment ke Railway

Railway adalah platform deployment alternatif yang lebih mudah digunakan. Untuk deploy ke Railway:

1. Buat akun di [Railway](https://railway.app/) dan install Railway CLI:
```bash
npm i -g @railway/cli
```

2. Login ke Railway:
```bash
railway login
```

3. Inisialisasi project:
```bash
railway init
```

4. Link ke repository GitHub (opsional):
```bash
railway link
```

5. Deploy project:
```bash
railway up
```

Model akan di-deploy ke URL seperti: `https://ml-ops-telco-production.up.railway.app/`

## Membuat Prediksi

Untuk membuat prediksi menggunakan model yang telah di-deploy, gunakan script `create_string_request.py` untuk memformat data dengan benar:

```bash
python create_string_request.py
```

Atau gunakan curl untuk mengirim request secara langsung:

```bash
curl -X POST "https://ml-ops-telco-production.up.railway.app/v1/models/cc-model:predict" -H "Content-Type: application/json" -d "@input.json"
```

Format input JSON untuk prediksi:
```json
{
  "instances": [
    {
      "examples": {
        "b64": "BASE64_ENCODED_EXAMPLE"
      }
    }
  ]
}
```

## Deployment dengan Heroku (Alternatif)

- Install CLI heroku ([tautan](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli))
- Login ke heroku melalui CLI:
```
heroku login
```

- Login ke heroku container registry:
```
heroku container:login
```

- Push container ke heroku container registry:
```
heroku container:push web -a cc-prediction
```

- Release model serving:
```
heroku container:release web -a cc-prediction
```