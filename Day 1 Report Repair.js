// After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

// The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

// To save your vacation, you need to get all fifty stars by December 25th.

// Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

// Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

// Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

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
// The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

// Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

// In your expense report, what is the product of the three entries that sum to 2020?

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
