function zip(arrays) {
	return arrays[0].map((_, i) => arrays.map((array) => array[i]));
}

let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];
let arr3 = [7, 8, 9];

console.log(zip([arr1, arr2, arr3])); // [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
