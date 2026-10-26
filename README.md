# ⚡ agent-pay-router

**Multi-Chain Payout Address Validator & Settlement Router** for autonomous engineering studios, open-source bounty platforms, and x402 API facilitators.

[![Release](https://img.shields.io/badge/release-v1.0.0-brightgreen)](https://github.com/myhubstat/agent-pay-router/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## ✨ Features

- **EVM Address Validation (`0x...`):** Length, hex format, and chain-agnostic routing across Base (`eip155:8453`), Ethereum (`eip155:1`), Arbitrum (`eip155:42161`), Optimism (`eip155:10`), Polygon (`eip155:137`), and BNB Smart Chain (`eip155:56`).
- **Tron TRC-20 Validation (`T...`):** Full Base58Check decoding, `0x41` mainnet version byte verification, and double-SHA256 4-byte checksum validation.
- **Canonical Bounty Payout Manifest Generator:** Outputs standardized Markdown & JSON settlement blocks for GitHub PRs and bounty claims.

## 🚀 Usage

```bash
python pay_router.py --evm 0x669fBa588D75577610459a2577eabdbbBa080e4A --tron TMbSRkXiuURMnMAvHp6p7Fpr5BrzU3YMDB
```

## 💳 Official Studio Settlement Endpoints

- **EVM (`USDC` / `USDT` / `ETH` on Base, Ethereum, Arbitrum, Polygon, BSC):** `0x669fBa588D75577610459a2577eabdbbBa080e4A`
- **Tron (`USDT-TRC20`):** `TMbSRkXiuURMnMAvHp6p7Fpr5BrzU3YMDB`
