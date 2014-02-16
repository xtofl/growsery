require([ "model" ], function(model) {

	test("Initial Values", function() {
		var scope = {};
		model.create(scope);
		deepEqual(scope.allGroceries(), [], "no groceries should be present initially");
	});

	test("Adding groceries", function() {
		var scope = {};
		model.create(scope);
		var groceries = [{name:"x", quantity: 10}, {name: "y", quantity: 5}];
		groceries.forEach(function(g){scope.addGrocery(g);});
		deepEqual(scope.allGroceries(), groceries, "adding groceries is reflected in allGroceries");

		var groceries = [{name:"x", quantity: 10}];
		groceries.forEach(function(g){scope.addGrocery(g);});
		deepEqual(scope.allGroceries(), 
				[{name:"x", quantity: 20}, {name: "y", quantity: 5}], 
				"adding equal groceries is reflected by increasing total in allGroceries");
	
	});
	
	test("Summing up groceries", function(){
		var scope = {};
		model.create(scope);
		var ingredients = [
		                   {name: "a", quantity: 5},
		                   {name: "a", quantity: 5}];
		var sum = model.joinedIngredients(ingredients);
		equal(10, sum["a"], "all equal ingredients are summed");
	});

    var setup = {
		additional:[
		                   {name: "a", quantity: 5},
		                   {name: "a", quantity: 5}],
		dish1 : {
				name: "dish1",
				ingredients: [{name: "dish1.a", quantity: 1}, {name: "common.a", quantity: 1}],
				targetQuantity: 5
		},
		dish2 : {
				name: "dish2",
				ingredients: [{name: "dish2.a", quantity: 1}, {name: "common.a", quantity: 1}],
				targetQuantity: 5
		}
	};
	
	function applyKnownSetup(scope){
		scope.copyDishToMenu(setup.dish1);
		scope.copyDishToMenu(setup.dish2);
		setup.additional.forEach(function(i){scope.addGrocery(i);});
	};
	
	function createEmptyScope(){
		var scope = {};
		model.create(scope);
		return scope;		
	};
	
	function createScope(setup){
		var scope = createEmptyScope();
		applyKnownSetup(scope);
		return scope;
	}

	test("Adding dishes to menu + additional groceries", function(){
		var scope = createScope();
		
		var expectedGroceries = {
			"a" : 10,
			"dish1.a" : 1,
			"dish2.a" : 1,
			"common.a" : 2
		};
		deepEqual(model.joinedIngredients(scope.allGroceries()), expectedGroceries, "ingredients from menu and additional groceries are summed up");
	});
	
	test("removing dish from menu", function(){
		var scope=createScope();
		
		scope.removeDishFromMenu(setup.dish1);

		var expectedGroceries = {
				"a" : 10,
				"dish2.a" : 1,
				"common.a" : 1
			};
		deepEqual(model.joinedIngredients(scope.allGroceries()), expectedGroceries, "ingredients from menu and additional groceries are summed up");
	
	});
	

	test("removing additionall grocery", function(){
		var scope=createScope();
		
		scope.removeAdditionalGrocery(setup.additional[0]);

		var expectedGroceries = {
				"a" : 5,
				"dish1.a" : 1,
				"dish2.a" : 1,
				"common.a" : 2
		};
		deepEqual(model.joinedIngredients(scope.allGroceries()), expectedGroceries, "ingredients from menu and additional groceries are summed up");
	
	});
});