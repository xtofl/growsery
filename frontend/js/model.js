define([], 
		function(){

	var _joinedIngredients = function(ingredients){
		var ret = {};
		ingredients.forEach(function(ingredient){
			if (!ret[ingredient.name]) ret[ingredient.name] = 0;
			ret[ingredient.name] += ingredient.quantity;
		});
		return ret;

	};
	var ret = {
		joinedIngredients: function(ingredients) {
			return _joinedIngredients(ingredients);
		},
		create: function($scope){
			
			$scope.groceries = [
			                    ];
			
			$scope.allGroceries = function() {
				var groceries = $scope.groceries.slice(0);
				$scope.menu.forEach(function(dish){
					dish.recipe.ingredients.forEach(function(ingredient){
						groceries.push(ingredient);
					});
				});
				var sum = _joinedIngredients(groceries);
				
				var ret = [];
				for (var grocery in sum) {
					ret.push({name: grocery, quantity: sum[grocery]});
				};
				return ret;
			};
			var makeIngredient = function(){
				return {name: "", quantity: 1};
			};
			
			var makeDish = function(){
				var dishIngredients = [];
				var dish = {
					name: "",
					ingredients: dishIngredients,
					addIngredient: function(){
						dishIngredients.push(makeIngredient());
					},
					removeIngredient: function(ingredient){
						var index = dishIngredients.indexOf(ingredient);
						dishIngredients.splice(index, 1);
					},
					targetQuantity: 5
				};
				return dish;
			};
	
			$scope.addGrocery = function(grocery){
				grocery || (grocery = makeIngredient());
				$scope.groceries.push(grocery);
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
				$scope.dishes.push(makeDish());
			};
			$scope.removeDish = function(dish){
				var index = $scope.dishes.indexOf(dish);
				$scope.dishes.splice(index, 1);
			};
			$scope.menu = [];
			
			$scope.copyDishToMenu = function(dish) {
				$scope.menu.push({name: dish.name, quantity: dish.targetQuantity, recipe: dish});
			};
			
			Array.prototype.findFirstIndex = function(predicate){
				for(var i=0; i!=this.length; ++i){
					if(predicate(this[i])) return i;
				}
			};
			$scope.removeDishFromMenu = function(dishToRemove) {
				var index = $scope.menu.findFirstIndex(function(dish){return dishToRemove.name==dish.name;});
				$scope.menu.splice(index, 1);
			};
			
			$scope.showDishes = true;
			$scope.showDishesIngredients = true;
			$scope.showMenu = false;
			$scope.showAdditionalGroceries = false;
		}
	};	
	return ret;
});