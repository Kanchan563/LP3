# Assignment 17 — Bank account smart contract

## Aim

Write and deploy a Solidity contract on an Ethereum test network that lets each user deposit ETH, withdraw only their own available balance, and view their balance.

## What you need

- Browser access to [Remix IDE](https://remix.ethereum.org/).
- MetaMask connected to **Sepolia** and a small amount of Sepolia test ETH for deployment and transactions.
- No real ETH. Testnet ETH has no real-world value.

## Solidity program

Create `BankAccount.sol` in Remix and paste this contract:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BankAccount {
    mapping(address => uint256) private balances;

    event Deposited(address indexed account, uint256 amount);
    event Withdrawn(address indexed account, uint256 amount);

    function deposit() external payable {
        require(msg.value > 0, "Deposit must be greater than zero");
        balances[msg.sender] += msg.value;
        emit Deposited(msg.sender, msg.value);
    }

    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal must be greater than zero");
        require(amount <= balances[msg.sender], "Insufficient account balance");

        // Update the user's balance before sending ETH (checks-effects-interactions).
        balances[msg.sender] -= amount;
        (bool sent, ) = payable(msg.sender).call{value: amount}("");
        require(sent, "ETH transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    function showBalance() external view returns (uint256) {
        return balances[msg.sender];
    }
}
```

The returned amounts are in **wei**. `1 ether = 1,000,000,000,000,000,000 wei`. Remix lets you choose the value unit when calling payable functions; alternatively enter the amount in wei.

## Procedure in Remix

1. Open Remix IDE and create `BankAccount.sol`.
2. Paste the contract and save it.
3. Open **Solidity Compiler**, select a compiler version `0.8.20` or compatible `0.8.x`, and compile `BankAccount.sol`.
4. Open **Deploy & Run Transactions**. In the environment selector, choose the injected MetaMask provider (the label can vary by Remix version).
5. In MetaMask, confirm the selected network is Sepolia and approve the connection request. Check the account shown in Remix.
6. Select `BankAccount` and click **Deploy**. Review the wallet confirmation and approve the testnet deployment.
7. After deployment confirms, expand the deployed contract in Remix. Record the contract address and deployment transaction hash.
8. To deposit, enter an amount in the Remix **Value** field and choose the `ether` unit. Click `deposit` and approve the transaction. Example: `0.01 ether` if the test wallet has enough Sepolia ETH for both deposit and gas.
9. Click `showBalance` and record the returned balance in wei. It should reflect the deposit made by the current account.
10. Enter a withdrawal amount in wei in the `withdraw` field, such as `1000000000000000` for `0.001 ether`, and submit. Confirm the transaction in MetaMask.
11. Call `showBalance` again. The recorded balance should decrease by the amount withdrawn (network gas is paid separately by the caller).
12. Optional check: try withdrawing more than the displayed balance. The transaction should revert with `Insufficient account balance`.
13. Record gas used and transaction fee for deployment, deposit, and withdrawal from transaction details.

## Expected observations

- Each wallet address has a separate balance.
- A user can withdraw only from their own recorded balance.
- An over-balance withdrawal reverts.
- Deployment and state-changing calls consume gas; `showBalance` is a read-only call and normally does not create an on-chain transaction when called locally in Remix.

## Practical journal checklist

- Aim, tools, and the contract source code.
- Compiler version and test network.
- Contract address and deployment transaction hash.
- Deposit, balance before/after withdrawal, and over-withdrawal observation.
- Gas used and fee for deployment, deposit, and withdrawal.
- Screenshot of the deployed contract and successful calls. Do not show recovery phrases/private keys.

## Suggested conclusion

“I compiled and deployed a bank-account contract on Sepolia. It tracked balances per wallet, allowed deposits and valid withdrawals, and rejected withdrawals exceeding the account balance. I recorded gas usage for deployment and state-changing calls.”
