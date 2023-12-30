const find = (num) => {
	if (num % 2 === 0) return num + 1;

	const num_bin = Array.from("0" + num.toString(2), Number);
	let index = num_bin.length - 1;
	while (true) {
		index--;
		if (num_bin[index] === 0) {
			num_bin[index] = 1;
			num_bin[index + 1] = 0;
			break;
		}
	}

	return parseInt(num_bin.join(""), 2);
};

function solution(numbers) {
	return numbers.map(find);
}
