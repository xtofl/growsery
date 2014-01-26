

var growceryController = function($scope){
	require(["model"], function(model){
		model.create($scope);
	});
	
};

var growseryApp = angular.module('growceryApp', []);

growseryApp.controller('GrowceryController', growceryController);
