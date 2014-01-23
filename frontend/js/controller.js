var growseryApp = angular.module('growceryApp', []);

growseryApp.controller('GrowceryController', function($scope){
	$scope.groceries = [
	                    ];
	$scope.addGrocery = function(){
		$scope.groceries.push({name: "", quantity: 1});
	};
	
	$scope.load = function() {
		var parsedGroceries = angular.fromJson(localStorage.growseryApp);
		$scope.groceries = parsedGroceries;
	};
	
	$scope.save = function() {
		var json = angular.toJson($scope.groceries);
		localStorage.growseryApp = json;
	};

});
