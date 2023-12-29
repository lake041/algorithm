function solution(N, wires) {
	if (N === 2) return 0;

	ans = N;
	for (const wire of wires) {
		const sub = wires.filter((e) => e !== wire);
		const array = [sub[0]];
		for (const _ of sub) {
			sub.forEach(([u, v]) => {
				if (array.includes(u)) array.push(v);
				if (array.includes(v)) array.push(u);
			});
		}
		ans = min(ans, Math.abs(N - array.length * 2));
	}
	return ans;
}
