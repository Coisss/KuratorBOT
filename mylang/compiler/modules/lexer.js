let LEXER = function (content, dictionary) {
	let text = content.replace(/\s\s+/gm, " ");
	let strings = text.split(";");


	let lexems = [];

	for (let i = 0; i < strings.length; i++) {
		let currentString = strings[i].trim();

		if (currentString !== "") {
			let words = currentString.split(" ");
			let copyString = currentString;

			let stringObject = {};

			console.log(words);

		}

	}


	// PUT HERE A CODE

	return lexems;
};
module.exports.LEXER = LEXER;