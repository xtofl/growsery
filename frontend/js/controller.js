var growseryApp = angular.module('growceryApp', []);

growseryApp.controller('GrowceryController', function($scope){
	$scope.groceries = [
	                    ];
	$scope.addIngredient = function(){
		$scope.groceries.push({name: "?", quantity: 1});
	};
	$scope.dishes = [{name: "dish1", ingredients: [{name: "selder"}]}];
});
