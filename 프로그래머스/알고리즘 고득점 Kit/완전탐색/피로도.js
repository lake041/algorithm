function permute(arr) {
	if (arr.length === 0) return [[]];
	const permutations = [];
	for (let i = 0; i < arr.length; i++) {
		const rest = arr.slice(0, i).concat(arr.slice(i + 1));
		for (const perm of permute(rest)) {
			permutations.push([arr[i]].concat(perm));
		}
	}
	return permutations;
}

function solution(k, dungeons) {
	let answer = 0;

	for (let permutation of permute(dungeons)) {
		let fatigue = k;
		let cnt = 0;
		for (let [need, use] of permutation) {
			if (fatigue >= need) {
				fatigue -= use;
				cnt++;
			}
		}
		answer = Math.max(answer, cnt);
	}

	return answer;
}
