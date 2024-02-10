// Decode base64 data into binary
import pako from 'pako';
import fs from 'fs';
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

const data = "eJy1Vm1T4zgM/itMPmfZJH3n0+3AsjBDD46yfKEdxk3c1JDYxXZaXqb//WTLSd3S5diZWwolkWxZlh490luwIHoeHAWVovKroloznqsgDPTLgoIYJKONsBApKUZaSJIb5ds4KAjPK3gbB0fjIB4H4ThQ9wuhmGaCW2HkhFPxfEulZmDBypMINYynRZXRIdXEW0+ftaQlPWWFptKTS7qk1oX00TtyRac/JFnMb8BpK76LQ/xE7uM/b2S7kq3PxJrO6IxUhf5baDYD3821zjn4tHTXiKOoj66lRDF+YSJEFTqhZUXDGSnU//yNnomFvqz0fSrJCl1BN3ITiJHxwg//XKxGxrFrwh9tqLzoZRBRtXWpxMoLovQtg1Ti2l7U6/TagyRpd3t1oqlMKUd9B22JkjB+nm3hQUuSPgKEhiJDp6YQqtQpM6LpqZAlQTMn4cHw4OHgxxFzt2EZwEbVaBqPwWz3MDqMv8bmGY1Qno00kfqC5XPN4aQTc6VvBeDN7rJRc+eV4POccH1jnKrB8iEQPg8WU0SclHhJLfhL/dfEc0g4VIuN6s+FufpObKMWxpGkqajAyRrQmJHS7aar3dI6E5K9Cq5dAmsosOxY8BnLrfDNBAxSdmXqFR6PrMCg9pTxDMrMyJJovW6C+nORihLC+au4GoBvIHQzr8rpiL1uAU9IfYIl5EnFksqCvFxJltJdNHIB4pJ+f04LexDWEq8KuJkhBsBXAYiAaqSIMi8KTbhQVtMCgN4xVKuL4S2FpCfEMY5XBdf0qaJKH5pUeTGrAxaF5l+DcSOygDRfVkXBayCzY0hsDhkBIjBr7u4m4ad/J9aQY8V9hpJ+K+50fs/cwkTaRMfZSVCc0UITjI4VR2ESt3vtfqvb7nkrrrDMvYVJFPYjXKFqWvHUX+LwS4zqtJJye28nisJ2BD+4APB1DbTKc6uFnfb66kKsIBFWhszniy9nMwdXXwdseDnD1rCt0kwXdEQJFH6TsyZlzDif0++cTAtAlNFb3kYdNiBfuTE7Q52E1pBu74OSygt6SySzDWNbOScAsyXUMObCv0GD/EqxJYZroy4rpc/Ikn4rCVT6vhCYFdCoPl5kKtLWiRG3McmAsk2CMAMrIulcAKEBgWS2m9fQCVthOwT8WWNuNtjQibkYmMdyWSP4PMqJOxHSCzR4yhtat1unUqyAQDe2LJXWCTueS4Gv1igwiN3d1GBiqxBPNMPLZze2D+Ou3enY51hUC7gstKR99KPuZUMm/V4XecZSx9D1FY9SpFJnRDlyS+Z0QJ8GxYOuyFM/ljp/YAv6wLqiW/B4ttMqbzQS+eYMSzqecdvnt7t27NYqUwND8nwpgdX/0dB9tnrgTh+qO1AyGHS6rdYgbjUjg2VPN8y8n6jquQql+yasnQaKTdIyeNMhC/I6SHp/5UZ4CN0Gz6455ZybdPmcDogclcwNN5s77RnTNsPg781h6KXpnTBTuAZt4SiaarKvppDMRFNgXVhZKgqvL9gNx6PbBntmS6PNqLK0sZ6YjruG8bpuLDBax2badrO1e7Vxg+d9UTObfz2oGgNmTN2/ysQJ/N/J3iT8rwnAuAKBBaMfzV+wykYVltWp80Tvy62mqvdzQKPZhXej8CdwuNEfG7/DgEGO+r0kDms6CY56638BniBbZg=="
const a = decompressTheData(data)
console.log(a)
// fs.writeFile('Product2.json',a,(err)=>{})
// Now you can use the decompressedData as needed
export default decompressTheData;



