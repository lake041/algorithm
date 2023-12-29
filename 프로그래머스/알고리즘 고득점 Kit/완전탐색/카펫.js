function solution(brown, yellow) {
	let sum = (brown - 4) / 2;
	let mul = yellow;

	for (let c = 1; c <= Math.floor(sum / 2); c++) {
		if ((sum - c) * c === mul) {
			return [sum - c + 2, c + 2];
		}
	}
}
