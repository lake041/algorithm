class Queue {
  constructor() {
    this.storage = {};
    this.front = 0;
    this.rear = 0;
  }

  size() {
    return this.rear - this.front;
  }

  add(value) {
    this.storage[this.rear++] = value;
  }

  pop() {
    if (!this.size()) return null;
    const item = this.storage[--this.rear];
    delete this.storage[this.rear];
    return item;
  }

  popleft() {
    if (!this.size()) return null;
    const item = this.storage[this.front];
    delete this.storage[this.front++];
    return item;
  }
}
