class Deque {
	constructor() {
		this.storage = {};
		this.front = 0;
		this.rear = 0;
	}

	size() {
		return this.rear - this.front;
	}

	append(item) {
		this.storage[this.rear++] = item;
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

function solution(bridge_length, weight, truck) {
	const bridge = new Deque();
	for (let i = 0; i < bridge_length; i++) bridge.append(0);
	const trucks = new Deque();
	for (const truck_weight of truck) trucks.append(truck_weight);

	let total_weight = 0;
	let time = 0;

	while (trucks.size() || total_weight) {
		total_weight -= bridge.popleft();

		if (trucks.size() && total_weight + trucks.storage[trucks.front] <= weight) {
			let incoming_truck = trucks.popleft();
			total_weight += incoming_truck;
			bridge.append(incoming_truck);
		} else {
			bridge.append(0);
		}

		time += 1;
	}

	return time;
}
