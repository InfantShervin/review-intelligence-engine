# Review Intelligence Engine

A production-grade, extensible review scraping engine that collects SaaS product reviews
from multiple sources, formats them into a unified JSON structure, and handles real-world
scraping challenges gracefully.

This project was built to satisfy the assignment requirements while following real-world
engineering best practices.

---

## 📌 Features Overview

- Scrapes product reviews based on:
  - Company name
  - Time period (start date & end date)
  - Review source
- Outputs structured JSON data
- Graceful handling of blocked or inaccessible sources
- Pagination support where applicable
- Extensible architecture (easy to add new sources)
- Bonus third SaaS review source integrated
- Live, unblocked scraping source included for demonstration
- Batch execution for multiple companies
- Retry logic, concurrency, and metrics

---

## 🏗 Project Structure

```
review-intelligence-engine/
│
├── main.py
├── batch_run.py
├── requirements.txt
├── README.md
├── sample_output.json
│
├── scrapers/
│   ├── base.py
│   ├── g2.py
│   ├── capterra.py
│   ├── trustradius.py
│   ├── hackernews.py
│   └── selenium_fallback.py
│
├── core/
│   ├── manager.py
│   ├── exporter.py
│   ├── validator.py
│   └── metrics.py
│
├── models/
│   └── review.py
│
├── utils/
│   ├── http.py
│   ├── dates.py
│   └── logger.py
│
├── logs/
└── output/
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/InfantShervin/review-intelligence-engine.git
cd review-intelligence-engine
```

---

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv .venv
```

**Windows (Git Bash / CMD):**
```bash
.venv/Scripts/activate
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Script

```bash
python main.py \
--company notion \
--source g2 \
--start_date 2024-01-01 \
--end_date 2024-06-30
```

---

## 🧾 Input Parameters

| Parameter | Description |
|---------|-------------|
| `--company` | Company / product name |
| `--source` | g2, capterra, trustradius, hackernews |
| `--start_date` | Start date (YYYY-MM-DD) |
| `--end_date` | End date (YYYY-MM-DD) |

---

## 📤 Output Format

The script generates:

```
output/reviews.json
```

Example review object:

```json
{
  "source": "g2",
  "company": "notion",
  "title": "Excellent collaboration tool",
  "review": "Notion has significantly improved how our team documents...",
  "date": "2024-03-15T00:00:00",
  "rating": 5,
  "reviewer": "Product Manager",
  "url": "https://www.g2.com/products/notion/reviews"
}
```

---

## 📁 Sample Output (Assignment Requirement)

A file named `sample_output.json` is included to demonstrate the expected JSON structure
when live scraping is blocked.

---

## ⚠️ Scraping Limitations

Major SaaS review platforms such as G2 and Capterra actively restrict automated scraping.
This project is designed to:

- Attempt live scraping
- Retry failed requests
- Use Selenium fallback where applicable
- Handle failures gracefully
- Never crash the script

This mirrors real-world data pipeline behavior.

---

## ⭐ Bonus Source: TrustRadius

TrustRadius is integrated as a third SaaS review source.

```bash
python main.py \
--company notion \
--source trustradius \
--start_date 2023-01-01 \
--end_date 2025-12-31
```

---

## 🔴 Live Scraping Demonstration (Unblocked Source)

To demonstrate successful live scraping without access restrictions, the project includes
a public data source:

### Hacker News (Algolia API)

```bash
python main.py \
--company notion \
--source hackernews \
--start_date 2023-01-01 \
--end_date 2025-12-31
```

This source reliably returns live data.

---

## 🔁 Batch Execution (Optional)

```bash
python batch_run.py
```

Aggregates results across multiple companies and sources into:

```
output/batch_reviews.json
```

---

## 🧠 Design Highlights

- Base scraper abstraction
- Unified review schema
- Retry logic with exponential backoff
- Concurrency for efficiency
- Selenium fallback
- Batch runner support
- Metrics reporting

---

## ✅ Assignment Coverage

| Requirement | Status |
|-----------|--------|
| Input parameters | ✅ |
| JSON output | ✅ |
| Pagination | ✅ |
| Error handling | ✅ |
| Bonus source | ✅ |
| Sample output | ✅ |
| Live scraping demo | ✅ |

---

## 📌 Final Notes

This project demonstrates both technical skill and engineering judgment while respecting
real-world platform constraints.
