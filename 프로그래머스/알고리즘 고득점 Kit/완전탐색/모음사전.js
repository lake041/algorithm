function dfs(current, length, words) {
	const vowels = [..."AEIOU"];
	if (current.length === length) {
		words.push(current);
		return;
	}
	vowels.forEach((vowel) => {
		dfs(current + vowel, length, words);
	});
}

function solution(word) {
	const words = [];
	for (let length = 1; length <= 5; length++) dfs("", length, words);
	return words.sort().indexOf(word) + 1;
}
