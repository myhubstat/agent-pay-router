#!/usr/bin/env python3
"""Multi-chain EVM (0x) and Tron (TRC-20 Base58Check) payout validator and manifest generator."""
import argparse, hashlib, json, re, sys

ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def validate_evm(addr: str) -> bool:
    return bool(re.fullmatch(r"0x[0-9a-fA-F]{40}", addr))

def validate_tron_trc20(addr: str) -> bool:
    if not addr.startswith("T") or len(addr) != 34:
        return False
    num = 0
    for ch in addr:
        if ch not in ALPHABET:
            return False
        num = num * 58 + ALPHABET.index(ch)
    raw = num.to_bytes(25, "big")
    payload, checksum = raw[:-4], raw[-4:]
    h1 = hashlib.sha256(payload).digest()
    h2 = hashlib.sha256(h1).digest()
    return payload[0] == 0x41 and checksum == h2[:4]

def build_manifest(evm: str, tron: str) -> dict:
    return {
        "evm_valid": validate_evm(evm),
        "tron_valid": validate_tron_trc20(tron),
        "primary_rail": {"network": "eip155:8453 (Base / EVM)", "asset": "USDC", "address": evm},
        "backup_rail": {"network": "tron:mainnet (TRC-20)", "asset": "USDT", "address": tron},
    }

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--evm", default="0x669fBa588D75577610459a2577eabdbbBa080e4A")
    ap.add_argument("--tron", default="TMbSRkXiuURMnMAvHp6p7Fpr5BrzU3YMDB")
    args = ap.parse_args()
    print(json.dumps(build_manifest(args.evm, args.tron), indent=2))
