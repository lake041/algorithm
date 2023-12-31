function solution(cap, n, deliveries, pickups) {
	const D = deliveries.map((num, index) => Array(num).fill(index + 1)).flat();
	const P = pickups.map((num, index) => Array(num).fill(index + 1)).flat();

	let dist = 0;
	while (D.length || P.length) {
		const farthestD = D.length ? D[D.length - 1] : 0;
		const farthestP = P.length ? P[P.length - 1] : 0;
		const farthest = Math.max(farthestD, farthestP);

		dist += farthest * 2;

		for (let i = 0; i < cap; i++) {
			if (D.length) D.pop();
			if (P.length) P.pop();
		}
	}

	return dist;
}
