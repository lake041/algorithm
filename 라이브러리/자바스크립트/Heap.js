class Heap {
  constructor() {
    this.heap = [];
  }

  size() {
    return this.heap.length;
  }

  peek() {
    return this.heap[0];
  }

  getPI(i) {
    return Math.floor((i - 1) / 2);
  }

  getLCI(i) {
    return i * 2 + 1;
  }

  getRCI(i) {
    return i * 2 + 2;
  }

  swap(i, j) {
    this.heap[i], (this.heap[j] = this.heap[j]), this.heap[i];
  }

  push(value) {
    this.heap.push(value);
    let currentIndex = this.size() - 1;

    while (
      currentIndex > 0 &&
      this.heap[currentIndex] < this.heap[this.getPI(currentIndex)]
    ) {
      this.swap(currentIndex, this.getPI(currentIndex));
      currentIndex = this.getPI(currentIndex);
    }
  }

  pop() {
    if (this.size() === 0) return null;
    if (this.size() === 1) return this.heap.pop();

    const minValue = this.heap[0];
    this.heap[0] = this.heap.pop();
    let currentIndex = 0;

    while (this.getLCI(currentIndex) < this.size()) {
      let minChildIndex = this.getLCI(currentIndex);

      if (
        this.getRCI(currentIndex) < this.size() &&
        this.heap[this.getRCI(currentIndex)] < this.heap[minChildIndex]
      ) {
        minChildIndex = this.getRCI(currentIndex);
      }

      if (this.heap[currentIndex] <= this.heap[minChildIndex]) {
        break;
      }

      this.swap(currentIndex, minChildIndex);
      currentIndex = minChildIndex;
    }

    return minValue;
  }
}
