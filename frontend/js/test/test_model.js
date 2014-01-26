require([ "model" ], function(model) {
	var scope = {};
	model.create(scope);

	test("Initial Values", function() {
		deepEqual(scope.allGroceries(), [], "no groceries should be present initially");
	});

	test("Adding groceries", function() {
		var groceries = [{name:"x", quantity: 10}, {name: "y", quantity: 5}];
		groceries.forEach(function(g){scope.addGrocery(g)});
		deepEqual(scope.allGroceries(), groceries, "adding groceries is reflected in allGroceries");
	});
	
	test("Summing up groceries", function(){
		var ingredients = [
		                   {name: "a", quantity: 5},
		                   {name: "a", quantity: 5}];
		var sum = model.joinIngredients(ingredients);
		equal(10, sum["a"], "all equal ingredients are summed");
	});

});