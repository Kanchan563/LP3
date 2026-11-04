# Assignment 15 — MetaMask and Ether spent per transaction

## Aim

Set up MetaMask, make a small **testnet** transaction, and observe how transaction fees are calculated. This practical is a wallet and blockchain activity; it does not require a Python program or a Solidity contract.

## What you need

- A laptop or phone with internet access.
- MetaMask, installed only from the official [MetaMask download page](https://metamask.io/download/).
- A testnet wallet and Sepolia test ETH. Test ETH has no real-world value.
- A second account address to receive the test transaction. You can create another account in your own MetaMask for this exercise.

## Procedure

1. Install the official MetaMask browser extension or mobile app and create a new practice wallet. Do not use a wallet that holds real funds for the lab.
2. Secure the wallet using the setup method you choose. If MetaMask gives you a Secret Recovery Phrase, write it down offline and keep it private. Never send it to a teacher, website, chat, or support agent.
3. In MetaMask, enable test networks from the network list/settings and select **Sepolia**. The menu wording can vary slightly by app version. See [MetaMask's testnet instructions](https://support.metamask.io/configure/networks/how-to-view-testnets-in-metamask/).
4. Copy your practice account's public address. Use MetaMask's official testnet faucet instructions to request a small amount of Sepolia ETH: [MetaMask testnet faucet guide](https://support.metamask.io/develop/blockchain-networks/testnets/using-the-testnet-faucet/). A faucet may require sign-in or have eligibility limits.
5. Wait for the test ETH to appear in the Sepolia account. Confirm that MetaMask still shows **Sepolia** before sending anything.
6. Copy the public address of a second account you control. In MetaMask, choose **Send**, paste that recipient address, enter a tiny test amount (for example, `0.001` Sepolia ETH if your faucet provides enough), review the screen, and confirm.
7. Open the completed transaction details in MetaMask or its block explorer link. Record the transaction hash, network, amount sent, gas used, effective gas price, and total fee. Do not include account secrets in your report.
8. Calculate/check the fee. In EVM networks, the basic relationship is:

   `Fee in ETH = gas used × effective gas price in Gwei ÷ 1,000,000,000`

9. Compare the fee for this transfer with another Sepolia transaction or with a contract deployment if your instructor provides one. Explain that gas measures computation and storage work; the fee depends on the network's gas pricing at that time.

## Record in your practical journal

| Field | Observation |
|---|---|
| Wallet software and version | |
| Network | Sepolia testnet |
| Transaction hash | |
| Amount sent | |
| Gas used | |
| Effective gas price | |
| Transaction fee | |
| Fee calculation | |
| Observation/conclusion | |

Attach screenshots of the network selection and transaction details if your instructor requires them. Hide account balances or addresses if requested by your college; never show your Secret Recovery Phrase or private key.

## Expected result

The test transaction appears as confirmed on Sepolia. You can identify its gas usage and testnet fee. The test ETH and transaction have no real-money value.

## Safety checklist

- Only use the official MetaMask site and testnet resources.
- Confirm the network says **Sepolia** before requesting or sending test funds.
- A public address can be shared to receive funds; a Secret Recovery Phrase/private key cannot.
- Never pay money to obtain testnet ETH and never switch to mainnet for this assignment.

## Suggested conclusion

“I installed and configured MetaMask for Sepolia, performed a test transfer, and observed the gas used, gas price, and transaction fee. The fee is related to computational work and network pricing, and testnet ETH is only for testing.”
