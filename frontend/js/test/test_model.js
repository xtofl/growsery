require([ "model" ], function(model) {
	var scope = {};
	model.create(scope);

	test("Initial Values", function() {
		deepEqual(scope.allGroceries(), [], "no topics should be present.");
	});

});