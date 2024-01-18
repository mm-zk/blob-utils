# Example contract to use with 4844


Deployment:

```
export PRIVATE_KEY=XXX
export RPC_URL=YYY,
```


```
forge creaste src/Counter.sol:Counter --private-key $PRIVATE_KEY --rpc-url $RPC_URL
```

Regular send:

```
cast send -r $RPC_URL $DEPLOYED_ADDRESS "setNumber(uint256)" 18 --private_key $PRUVATE_KEY
```

Send with blobs:

```
./blob-utils tx --blob-file somedata.txt --rpc-url $RPC_URL --to $DEPLOYED_ADDRESS --private-key $PRIVATE_KEY --gas-limit 100000 --calldata 0x3fb5c1cb0000000000000000000000000000000000000000000000000000000000000012  --gas-price 2000000000
```

Checking that blob was actually received:

* on etherescan - transation type says '3'

```
curl -X POST \          
     -H "Content-Type: application/json" \
     --data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x9e981d", false],"id":1} $RPC_URL
```

Look for 'blobGasUsed' - this shows that some blobs were included in this block.


### pushing the yul code

Compilation:
```
~/.svm/0.8.19/solc-0.8.19 --assemble  yul/BlobVersionedHash.yul --bin  | tail -1
```

Then pushing with cast:

```
cast send -r $RPC_URL --private-key $PRIVATE_KEY --create 0x600e600d600039600e6000f3fe60003580498060005260206000f3
```

Got contract:
https://goerli.etherscan.io/address/0xc7dc9939df92e91b6f23b8367771d918b034d108#code



### Experiment 1

Deploy a 'counter' contract to Goerli with 'incrementByBlob' - that sets the number to the versioned hash of the blob that was included.

Contract was deployed on Goerli on: 0xC7319491f629b64B7566b09F3369C6A0A5713F61

And this was the transaction with blob: https://goerli.etherscan.io/tx/0x2bae93157ea260f5217bf8a30ba1479871c1be9f9dbaf773b915be0474075323


This was used to send the tx

```
./blob-utils tx --blob-file somedata.txt --rpc-url $RPC_URL --to 0xC7319491f629b64B7566b09F3369C6A0A5713F61 --private-key $PRIVATE_KEY --gas-limit 100000  --calldata 0xa30753db --chain-id 5 --gas-price 2000000000
```