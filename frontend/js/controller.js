var growseryApp = angular.module('growceryApp', []);

growseryApp.controller('GrowceryController', function($scope){
	$scope.groceries = [
	                    ];
	$scope.addGrocery = function(){
		$scope.groceries.push({name: "", quantity: 1});
	};

});
