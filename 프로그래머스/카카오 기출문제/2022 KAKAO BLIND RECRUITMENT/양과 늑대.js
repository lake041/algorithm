const solution = (info, edges) => {
	const tree = {};
	for (const [parent, child] of edges) {
		if (!tree[parent]) tree[parent] = [];
		tree[parent].push(child);
	}

	const q = [[[1, 0], new Set(tree[0])]];
	let cursor = 0;
	let ans = 0;

	while (q[cursor]) {
		const [[sheep, wolf], children] = q[cursor];
		cursor++;

		if (sheep === wolf) continue;
		ans = Math.max(ans, sheep);

		for (const child of children) {
			const nextChildren = new Set([...children]);
			nextChildren.delete(child);
			for (const grand of tree[child] || []) nextChildren.add(grand);

			const nextStatus = info[child] ? [sheep, wolf + 1] : [sheep + 1, wolf];
			q.push([nextStatus, nextChildren]);
		}
	}

	return ans;
};
