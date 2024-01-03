class Heapq {
	constructor() {
		this.heap = [];
	}

	size() {
		return this.heap.length;
	}
	peek() {
		return this.heap[0];
	}
	parentIndex(i) {
		return Math.floor((i - 1) / 2);
	}
	leftIndex(i) {
		return i * 2 + 1;
	}
	rightIndex(i) {
		return i * 2 + 2;
	}
	parent(i) {
		return this.heap[this.parentIndex(i)];
	}
	left(i) {
		return this.heap[this.leftIndex(i)];
	}
	right(i) {
		return this.heap[this.rightIndex(i)];
	}
	item(i) {
		return this.heap[i];
	}
	swap(i, j) {
		this.heap[i], (this.heap[j] = this.heap[j]), this.heap[i];
	}

	push(value) {
		this.heap.push(value);
		let currentIndex = this.size() - 1;

		while (currentIndex > 0 && this.item(currentIndex) < this.parent(currentIndex)) {
			this.swap(currentIndex, this.parentIndex(currentIndex));
			currentIndex = this.parentIndex(currentIndex);
		}
	}

	pop() {
		if (this.size() === 0) return null;
		if (this.size() === 1) return this.heap.pop();

		const minValue = this.heap[0];
		this.heap[0] = this.heap.pop();
		let currentIndex = 0;

		while (this.leftIndex(currentIndex) < this.size()) {
			let minChildIndex = this.leftIndex(currentIndex);

			if (this.rightIndex(currentIndex) < this.size() && this.right(currentIndex) < this.heap[minChildIndex])
				minChildIndex = this.rightIndex(currentIndex);

			if (this.heap[currentIndex] <= this.heap[minChildIndex]) break;

			this.swap(currentIndex, minChildIndex);
			currentIndex = minChildIndex;
		}

		return minValue;
	}
}
