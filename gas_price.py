import requests
import json

def get_block_by_number(url, block_number):
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": [block_number, False],
        "id": 1
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def fake_exponential(factor: int, numerator: int, denominator: int) -> int:
    i = 1
    output = 0
    numerator_accum = factor * denominator
    while numerator_accum > 0:
        output += numerator_accum
        numerator_accum = (numerator_accum * numerator) // (denominator * i)
        i += 1
    return output // denominator

MIN_BLOB_GASPRICE = 1
BLOB_GASPRICE_UPDATE_FRACTION = 3338477

def get_blob_gasprice(excess_blob_gas) -> int:
    return fake_exponential(
        MIN_BLOB_GASPRICE,
        excess_blob_gas,
        BLOB_GASPRICE_UPDATE_FRACTION
    )

def main():
    # Replace with your Ethereum node URL
    node_url = "https://rpc.ankr.com/eth_goerli"

    # Get latest block number
    latest_block = get_block_by_number(node_url, 'latest')

    excess_blob_gas = int(latest_block['result']['excessBlobGas'],16) 
    print(f"Excess blob gas: {excess_blob_gas}")

    blob_gas_price = get_blob_gasprice(excess_blob_gas)

    print(f"Blob byte gas price: {blob_gas_price}, in Gwei: {blob_gas_price//(10**9)}")
    print(f"Full blob would cost: {blob_gas_price * (2**17) / (10**18) } ETH")


if __name__ == "__main__":
    main()