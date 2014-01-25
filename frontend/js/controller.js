var growseryApp = angular.module('growceryApp', []);


growseryApp.controller('GrowceryController', function($scope){
	$scope.groceries = [
	                    ];
	
	$scope.allGroceries = function() {
		var groceries = $scope.groceries.slice(0);
		$scope.menu.forEach(function(dish){
			dish.recipe.ingredients.forEach(function(ingredient){
				groceries.push(ingredient);
			});
		});
		return groceries;
	};
	var makeIngredient = function(){
		return {name: "", quantity: 1};
	};
	
	$scope.addGrocery = function(){
		$scope.groceries.push(makeIngredient());
	};
	
	$scope.load = function() {
		$scope.dishes = angular.fromJson(localStorage.dishes);
		$scope.menu = angular.fromJson(localStorage.menu);
		$scope.groceries = angular.fromJson(localStorage.groceries);
	};
	
	$scope.save = function() {
		localStorage.dishes = angular.toJson($scope.dishes);
		localStorage.menu = angular.toJson($scope.menu);
		localStorage.groceries = angular.toJson($scope.groceries);
	};


	$scope.dishes = [];

	$scope.addDish = function() {
		var dishIngredients = [];
		$scope.dishes.push(
				{
					name: "",
					ingredients: dishIngredients,
					addIngredient: function(){
						dishIngredients.push(makeIngredient());
					},
					targetQuantity: 5
				});
	};
	
	$scope.menu = [];
	
	$scope.copyDishToMenu = function(dish) {
		$scope.menu.push({name: dish.name, quantity: dish.targetQuantity, recipe: dish});
	};
});
