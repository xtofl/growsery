define([], 
		function(){

	var joinedIngredients = function(ingredients){
		var ret = {};
		ingredients.forEach(function(ingredient){
			if (!ret[ingredient.name]) ret[ingredient.name] = 0;
			ret[ingredient.name] += ingredient.quantity;
		});
		return ret;

	};
	var ret = {
		joinIngredients: function(ingredients) {
			return joinedIngredients(ingredients);
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
				var sum = joinedIngredients(groceries);
				
				var ret = [];
				for (var grocery in sum) {
					ret.push({name: grocery, quantity: sum[grocery]});
				};
				return ret;
			};
			var makeIngredient = function(){
				return {name: "", quantity: 1};
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

		}
	};	
	return ret;
});