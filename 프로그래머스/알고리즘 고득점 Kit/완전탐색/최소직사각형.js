function solution(sizes) {
	let [R, C] = [0, 0];

	for (const [row, col] of sizes) {
		R = Math.max(Math.max(row, col), R);
		C = Math.max(Math.min(row, col), C);
	}

	return R * C;
}
