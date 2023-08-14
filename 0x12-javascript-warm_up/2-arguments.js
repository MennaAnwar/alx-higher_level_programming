#!/usr/bin/node

switch (process.argv.length) {
	case 2:
		console.log('No argument');
		break;
	default:
		console.log('Arguments found');
}
