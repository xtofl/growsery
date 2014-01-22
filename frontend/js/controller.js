var growseryApp = angular.module('growceryApp', []);

growseryApp.controller('GrowceryController', function($scope){
	$scope.groceries = [
	                    {
	                    	name: "selder",
	                    	quantity: 1
	                    }];
	$scope.dishes = [{name: "dish1", ingredients: [{name: "selder"}]}];
});
