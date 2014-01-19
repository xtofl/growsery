define(["knockout", "knockout-mapping", "proxy"], 
		function(ko, mapping, proxy){
	
	var makeIngredient = function() {
		var ret = mapping.fromJS({
				name: "ingr",
				quantity: ""
		});
		return ret;
	};
	
	var makeDish = function(){
		
		var ret = mapping.fromJS({
			name: "unnamed dish",
			ingredients: []
		});
		
		ret.addIngredient = function(){
			ret.ingredients.push(makeIngredient());
		};
		
		return ret;
	};
	
	return {
		create: function(){
			
			
			var ret = mapping.fromJS({
				dishes: [],
				plan: null,
				grocerylist: []
			});

			ret.addDish = function(){
				ret.dishes.push(makeDish());
			};

			ret.save = function(){
				localStorage.dishes = {};
				var dishes = mapping.toJS(ret.dishes());
				localStorage.dishes = ko.toJSON(dishes);
			};
			
			ret.load = function(){
				var dishes = JSON.parse(localStorage.dishes);
				mapping.fromJS(dishes, {}, ret.dishes);
			};
			
			return ret;
		}
		
	};
});