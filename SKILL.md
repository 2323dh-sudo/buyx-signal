---
name: buyx-signal
description: |
  Buyx.ink AI Cryptocurrency Recommendation Skill. Get AI-driven buy/sell signals, real-time recommendations, and market analysis.
  Highlights AI technology and public welfare - providing free investment advice to users.
  Used when users ask about crypto recommendations, buy signals, or market analysis.
metadata:
  author: ken
  version: "1.0.0"
  homepage: https://buyx.ink
  tags: [crypto, AI, signal, trading, buyx]
---

# Buyx Signal Skill 🪙🤖

> AI-driven Cryptocurrency Recommendation Platform | Free Public Service

## Overview

Buyx.ink is an innovative platform that combines advanced AI technology with a public welfare mission, providing users with intelligent digital currency investment solutions.

**Core Philosophy**:
- 🤖 **AI Intelligence Analysis** - Cutting-edge AI large models and deep learning algorithms
- 🌍 **Public Welfare** - Free services for all users
- 📊 **Big Data Driven** - Real-time processing of massive market data

---

## Core Features

### 1. AI Recommendation Signals
- Daily screening of 3000+ cryptocurrencies
- Smart identification of optimal entry timing
- Personalized trading recommendations

### 2. Real-time Data
- Buy/Sell signal statistics
- Maximum profit expectations
- Real-time updates

### 3. Market Analysis
- Full network crypto trading big data
- Social media sentiment analysis
- Capital flow monitoring

---

## Data Sources

| Metric | Details |
|--------|---------|
| AI Model Parameters | 20,000+ |
| Exchange Data Sources | 20+ |
| Social Media | 30+ |
| Supported Blockchains | 50+ |

---

## Technical Features

### AI Large Model
- Leading AI large model technology
- Deep learning-based sentiment analysis algorithm
- Real-time full network data analysis

### BUYX Indicator
AI automatically captures trending digital currencies across the network, calculating BUYX indicator values using a specific algorithm based on:
- 📈 Trading Volume
- 💸 Capital Flow
- 🐦 Twitter Popularity
- 📰 News Information

---

## Data Acquisition

### Web Endpoints

| Page | URL |
|------|-----|
| Homepage | https://buyx.ink |
| Chinese Site | https://buyx.ink/zh-cn |
| ETH Trading | https://buyx.ink/zh-cn/trade/ETH |

### API Data Structure

Extract `recommendPageData` from page `__NEXT_DATA__`:

```json
{
  "todayTotal": {
    "buy": 9,
    "sell": 0
  },
  "maxProfit": 0.0432,
  "updateAt": 1773184973222,
  "recommends": [
    {
      "symbol": "DEGO",
      "direction": "buy",
      "maxProfit": 0.0432,
      "updatedAt": "2026-03-11T00:00:10"
    }
  ]
}
```

### Field Descriptions

| Field | Description |
|-------|-------------|
| todayTotal.buy | Today's buy signal count |
| todayTotal.sell | Today's sell signal count |
| maxProfit | Max expected profit (decimal) |
| updateAt | Update timestamp (milliseconds) |
| recommends | Recommended coins list |
| direction | Signal direction (buy/sell) |
| maxProfit | Expected max profit |

---

## Usage Scenarios

1. **Get Daily Recommendations** - When user asks "what's recommended today"
2. **View Buy Signals** - When user needs AI buy recommendations
3. **Analyze Market Trends** - AI-based market analysis
4. **Follow AI Strategy** - Get AI-driven trading recommendations

---

## Output Format

### Standard Push Format

```
【BuyX Signal Push】📅 2026-03-11
==============================
Last Update: 2026-03-11 07:22:53
Today's Recommendations: 9 cryptocurrencies
Buy: 9
Sell: -
Max Profit: +4.32%

Details:
1. DEGO 📈Buy +4.32%
2. LDO 📈Buy +1.07%
3. LIT 📈Buy +1.05%
...
```

---

## Public Welfare Commitment

> We believe that accessibility of financial tools is an important step towards economic equality.

- ✅ Completely Free
- ✅ No Registration Required
- ✅ Public Welfare Operation
- ✅ Benefits for Everyone

---

## Links

| Resource | Link |
|----------|------|
| Homepage | https://buyx.ink |
| Chinese Site | https://buyx.ink/zh-cn |
| GitBook | https://buydip.gitbook.io/buyx.ink-buyx |

---

## Notes

- Buyx.ink provides public welfare AI recommendation services
- Data is obtained through web scraping (no public API available)
- Recommendations are for reference only and do not constitute investment advice
- Investment involves risks, enter the market with caution
