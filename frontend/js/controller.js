

var growceryController = function($scope, $http){
	require(["model"], function(model){
		model.create($scope, $http);
	});
	
};

var growseryApp = angular.module('growceryApp', []);

growseryApp.controller('GrowceryController', growceryController);
