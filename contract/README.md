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

