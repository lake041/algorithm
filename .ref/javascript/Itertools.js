const Combinations = (arr, selectNumber) => {
	const result = [];
	if (selectNumber === 1) return arr.map((item) => [item]);

	arr.forEach((fixed, index, origin) => {
		const rest = origin.slice(index + 1);
		const combinations = Combinations(rest, selectNumber - 1);
		const attached = combinations.map((item) => [fixed, ...item]);
		result.push(...attached);
	});

	return result;
};

const Permutations = (arr, selectNumber) => {
	const result = [];
	if (selectNumber === 1) return arr.map((item) => [item]);

	arr.forEach((fixed, index, origin) => {
		const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
		const permutations = Permutations(rest, selectNumber - 1);
		const attached = permutations.map((item) => [fixed, ...item]);
		result.push(...attached);
	});

	return result;
};

console.log(Combinations([0, 1, 2, 3, 4], 2));
console.log(Permutations([0, 1, 2, 3, 4], 2));
