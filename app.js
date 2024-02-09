// Decode base64 data into binary
import pako from 'pako';



function decompressTheData(basestring){
let base64Data = basestring

let binaryData = atob(base64Data);
// Convert binary data to ArrayBuffer
let arrayBuffer = new ArrayBuffer(binaryData.length);
let uint8Array = new Uint8Array(arrayBuffer);
for (let i = 0; i < binaryData.length; i++) {
    uint8Array[i] = binaryData.charCodeAt(i);
}

// Decompress the ArrayBuffer using the appropriate algorithm
let decompressedData;
try {
    // Try gzip decompression
    decompressedData = pako.inflate(uint8Array, { to: 'string' });
} catch (error) {
    try {
        // If gzip fails, try deflate decompression
        decompressedData = pako.inflateRaw(uint8Array, { to: 'string' });

    } catch (error) {
        try {
            // If deflate fails, try brotli decompression
            decompressedData = pako.inflate(uint8Array, { to: 'string' });
        } catch (error) {
            console.error("Error decompressing data:", error);
        }
    }
}
return decompressedData;
}

const data = "eJxFUNFyqjAQ/ZVMntoZLgREUDr3AbyKvahTa6m1nT6EECCGkBSwVTv998aHTp929+zu2XP2EyrcVzCAqpUWwT0tZXuCBsylwKy5zWFgG/AHv807GLz8sV8NWOsVTqnCJpFCzx90bV0i1slSnlldY2toInC1ZU0uPzqwegA2MtEN0IDn3oCj516DUKmabmmWsN4aDnxz4IGrZP6wXBigZpyCmBIur8GkaqWglu3YpqbQrBtc4Jb9rEzz8renRVz8nNBwtUj36Wbk30Xr8K+G2cWN47oGLBQMPiHTY31DVHXWzVYXxLo/jwezR3T3b5mgZoUep2F6VJEo36o5cxOfb/9H9+L5RNLkme/iSSXj2XoXRyUWtcyEKOVBpFt12jzFC4njiXiajXB2jEo5203V/GOd8reQh/pcr6X4yHdHvjNG/hB9GfCdth2TDQx8/caOXgRlFR77uehQVpdZWziEdLVEhUc82fSEHLwKtZnMkMIDrPLRnueidsaHjrCG792Cw69vn36Sjw=="

const a = decompressTheData(data)
console.log(a)
// Now you can use the decompressedData as needed
export default decompressTheData;



