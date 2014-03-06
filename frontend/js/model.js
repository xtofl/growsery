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
		create: function($scope, $http){
			
			$scope.groceries = [];
			
			$scope.allGroceries = [];
			var updateAllGroceries = function() {
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

				$scope.allGroceries = ret;
			};

			$scope.$watch("groceries", updateAllGroceries);
			$scope.$watch("dishes", updateAllGroceries);
			var makeIngredient = function(){
				return {name: "", quantity: 1};
			};
			
			var makeDish = function(prototype){
				var dishIngredients = prototype && prototype.ingredients && prototype.ingredients.slice() || [];
				var dish = {
					name: prototype && prototype.name || "",
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

			$scope.addDish = function(dish) {
				$scope.dishes.push(makeDish(dish));
			};
			$scope.removeDish = function(dish){
				var index = $scope.dishes.indexOf(dish);
				$scope.dishes.splice(index, 1);
			};
			$scope.menu = [];

			$scope.copyDishToMenu = function(dish) {
				$scope.menu.push({name: dish.name, quantity: dish.targetQuantity, recipe: dish});
			};
			
			var readCookbooks = function() {
				var cookbooks = angular.fromJson(localStorage.cookbooks); 
				if(!cookbooks) return {};
				else return cookbooks;
			};
			$scope.saveCookbook = function(name) {
				var cookbooks = readCookbooks();
				cookbooks[name] = $scope.dishes;
				localStorage.cookbooks = angular.toJson(cookbooks);
			};
			$scope.loadCookbook = function(name) {
				var cookbooks = readCookbooks();
				var dishes = cookbooks[name];
				$scope.dishes = angular.fromJson(dishes);
			};
			$scope.cookbookNames = function() {
				var ret = [];
				var book = readCookbooks();
				for(var key in book){
					ret.push(key);
				}
				return ret;
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
			
			$scope.removeAdditionalGrocery = function(toRemove) {
				var index = $scope.groceries.findFirstIndex(function(grocery){return toRemove.name==grocery.name;});
				$scope.groceries.splice(index, 1);
			};
			
			$scope.showDishes = true;
			$scope.showDishesIngredients = true;
			$scope.showMenu = true;
			$scope.showAdditionalGroceries = true;
			
			var makePersistent = function(name, property, url, factory) {
				$scope["save"+name] = function(){
					$http({method: 'post', url: url, data: angular.toJson({what: property, content: $scope[property]})})
						.success(function(data, status, header, config){
							$scope.status="saved "+name+" allright! "+data;
						})
						.error(function(data, status, headers, config){
							$scope.status="saving failed..."+status;
						});
				};
				$scope["load"+name] = function(){
					$http({method: 'get', url: url+"?what="+property})
					.success(function(data, status, header, config){
						$scope.status="loaded allright! ";
						var object = angular.fromJson(data);
						$scope[property] = factory ? factory(object) : object;
					})
					.error(function(data, status, headers, config){
						$scope.status="loaded failed..."+status;
					});
				};
			};
			makePersistent("Recipes", "dishes", "backend/recipes.php", function(dishes){
				return dishes.map(function(dish){ return makeDish(dish); });
			});
			makePersistent("Groceries", "groceries", "backend/recipes.php");
		}
	};	
	return ret;
});