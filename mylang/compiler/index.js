


let fs = require("fs");
let lexer = require("./modules/lexer.js").LEXER;



fs.readFile("../test.lang", "utf-8", function (error, content) {

	if(!!error) {
		let lexems = lexer(content);
		console.log(JSON.stringify(lexems, null, 4));
	}
	else {
		console.error("ERROR!");
		console.error(error);
	}






});
