// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.20;



contract Counter {
    uint256 public number;
    address constant BLOB_VERSIONED_HASH_GETTER_ADDR = 0xC7Dc9939dF92E91B6F23B8367771d918B034d108;

    function setNumber(uint256 newNumber) public {
        number = newNumber;
    }

    function increment() public {
        number++;
    }

    function incrementByBlob() public {
        (bool success, bytes memory data) = BLOB_VERSIONED_HASH_GETTER_ADDR.staticcall(abi.encode(0));
        require(success, "vc");
        uint256 decodedData = abi.decode(data, (uint256));
        number = decodedData;
    }
}
