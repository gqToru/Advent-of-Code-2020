const fs = require('fs');
const numbers = fs.readFileSync('./files/day1.txt', 'utf-8').split('\n').filter((x) => x).map((x) => parseInt(x));

for (let i = 0; i < numbers.length; i++) {
	for (let w = 1; w < numbers.length; w++) {
		let result = numbers[i] + numbers[i + w];
		if (result == 2020) {
			console.log(numbers[i] * numbers[i + w]);
		}
	}
}

// --- Part Two ---

for (let i = 0; i < numbers.length; i++) {
	for (let w = 1; w < numbers.length; w++) {
		for (let y = 0; y < numbers.length; y++) {
			let result = numbers[i] + numbers[i + w] + numbers[i + w + y];
			if (result == 2020) {
				console.log(numbers[i] * numbers[i + w] * numbers[i + w + y]);
			}
		}
	}
}
