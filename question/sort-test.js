const fs = require('fs');
const path = require('path');
function checkSorted(arr) {
    return arr.every((value, index, array) => {
        return index === 0 || array[index - 1] <= value;
    });
}

(async () => {
    const bytes = fs.readFileSync(path.join(__dirname, 'wasm', 'sort.wasm'));
    let wasm = await WebAssembly.instantiate(new Uint8Array(bytes));
    const { memory, sort } = wasm.instance.exports;
    function fillArrayWithRandomValues(array, minValue, maxValue) {
        for (let i = 0; i < array.length; i++) {
            array[i] = Math.floor(Math.random() * (maxValue - minValue + 1)) + minValue;
        }
    }
    const len = 1000;
    const arr = new Int32Array(memory.buffer, 0, len);
    fillArrayWithRandomValues(arr, 1, 10000);
    console.log("Array is sorted:", checkSorted(arr));
    console.log("Array:", arr);
    sort(arr.byteOffset, len);
    console.log("Sorted Array:", arr);
    console.log("Array is sorted:", checkSorted(arr));
})();
