// Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

const fs = require('fs');
const map = fs.readFileSync('./files/day3.txt', 'utf-8').split('\r\n').map((x) => x.split(''));

let total_trees = 1;

let right_list = [ 1, 3, 5, 7, 1 ];
let down_list = [ 1, 1, 1, 1, 2 ];

function calcTrees(right, down) {
	let tree_count = 0;
	let y = 0;
	let x = 0;
	while (y < map.length) {
		if (x > map[0].length - 1) {
			x = x % map[0].length;
		}
		if (map[y][x] == '#') {
			tree_count += 1;
		}
		x += right;
		y += down;
	}
	return tree_count;
}

for (let i = 0; i < 5; i++) {
	total_trees *= calcTrees(right_list[i], down_list[i]);
}

console.log(total_trees);
