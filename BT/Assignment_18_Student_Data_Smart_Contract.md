# Assignment 18 — Student data contract, fallback, gas, and fees

## Aim

Create and deploy a Solidity contract that stores student records in a struct array, includes a payable fallback, and lets you observe gas usage and transaction fees.

## What you need

- Browser access to [Remix IDE](https://remix.ethereum.org/).
- MetaMask connected to **Sepolia** with a small amount of Sepolia test ETH.
- Test ETH only; it has no real-world value.

## Solidity program

Create `StudentData.sol` in Remix and paste:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentData {
    struct Student {
        uint256 id;
        string name;
        uint256 age;
        string course;
    }

    Student[] private students;
    uint256 public etherReceived;

    event StudentAdded(uint256 indexed id, string name);
    event EtherReceived(address indexed sender, uint256 amount);

    function addStudent(
        uint256 id,
        string calldata name,
        uint256 age,
        string calldata course
    ) external {
        students.push(Student(id, name, age, course));
        emit StudentAdded(id, name);
    }

    function getStudent(uint256 index)
        external
        view
        returns (uint256 id, string memory name, uint256 age, string memory course)
    {
        require(index < students.length, "Student index does not exist");
        Student storage student = students[index];
        return (student.id, student.name, student.age, student.course);
    }

    function studentCount() external view returns (uint256) {
        return students.length;
    }

    // Called when ETH is sent with empty calldata and no function call.
    receive() external payable {
        etherReceived += msg.value;
        emit EtherReceived(msg.sender, msg.value);
    }

    // Called when calldata does not match a function; can also receive ETH.
    fallback() external payable {
        if (msg.value > 0) {
            etherReceived += msg.value;
            emit EtherReceived(msg.sender, msg.value);
        }
    }
}
```

## Procedure in Remix

1. Open Remix IDE, create `StudentData.sol`, paste the contract, and save it.
2. In **Solidity Compiler**, choose compiler version `0.8.20` or a compatible `0.8.x`, then compile.
3. Open **Deploy & Run Transactions** and select the injected MetaMask provider. Confirm MetaMask is connected to Sepolia.
4. Select `StudentData` and click **Deploy**. Approve the testnet deployment in MetaMask.
5. After confirmation, record the deployed contract address, transaction hash, gas used, gas limit (if shown), gas price/effective gas price, and transaction fee.
6. Expand the deployed contract and call `addStudent` with sample values:
   - `id`: `1`
   - `name`: `Asha Patil`
   - `age`: `20`
   - `course`: `Computer Engineering`
7. Approve the transaction. Record its gas used and fee. Add a second record with a different ID/name/course for comparison.
8. Call `studentCount`; it should return the number of records inserted. Call `getStudent(0)` to read the first record and record the result. These view calls are read-only when run locally in Remix.
9. To test `receive`, use MetaMask's send flow to send a small amount of Sepolia ETH to the deployed contract address with no data. Approve and record the transaction.
10. Confirm `etherReceived` increased. To test `fallback`, in Remix's low-level interaction area send a transaction with a small value and non-empty unmatched calldata, if the current Remix version exposes this safely. If that UI is unavailable, document and demonstrate the `receive` function; do not call arbitrary unknown websites or tools.
11. Open transaction details and record gas used and transaction fee for deployment, adding a student, and sending ETH. Fee is approximately `gas used × effective gas price`; convert Gwei to ETH by dividing by `1,000,000,000`.

## Expected observations

- Student records are appended to a dynamic array and can be read by index.
- `studentCount` increases after each successful `addStudent` transaction.
- `receive` accepts a plain ETH transfer; `fallback` handles unmatched function data and can accept ETH.
- Deployment generally uses more gas than a single student insertion, but actual gas and fee depend on compiler settings, transaction data, and network conditions.

## Practical journal checklist

- Aim, tools, Solidity source, and compiler version.
- Network and deployed contract address.
- Two inserted student records and readback output.
- Deployment and insertion gas/fee measurements.
- Receive/fallback test and observed `etherReceived` value.
- Transaction hashes and screenshots of Remix/MetaMask transaction details. Hide private credentials.

## Suggested conclusion

“I used a struct and dynamic array to store and retrieve student data, and implemented payable receive/fallback handlers. I deployed on Sepolia and compared gas usage and transaction fees for deployment, data insertion, and Ether transfer.”
