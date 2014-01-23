var growseryApp = angular.module('growceryApp', []);


growseryApp.controller('GrowceryController', function($scope){
	$scope.groceries = [
	                    ];
	
	var makeIngredient = function(){
		return {name: "", quantity: 1};
	};
	
	$scope.addGrocery = function(){
		$scope.groceries.push(makeIngredient());
	};
	
	$scope.load = function() {
		$scope.groceries = angular.fromJson(localStorage.groceries);
	};
	
	$scope.save = function() {
		var json = angular.toJson($scope.groceries);
		localStorage.groceries = json;
	};


	$scope.dishes = [];

	$scope.addDish = function() {
		var dishIngredients = [];
		$scope.dishes.push(
				{
					name: "",
					ingredients: dishIngredients,
					addIngredient: function(){
						dishIngredients.push(makeIngredient())
					},
					quantity: 5
				});
	};
});
