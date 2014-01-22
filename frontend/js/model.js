define(["knockout", "knockout-mapping", "proxy"], 
		function(ko, mapping, proxy){
	
	var makeIngredient = function() {
		var ret = {
				name: "ingr",
				quantity: ""
		};
		return ret;
	};
	
	var makeDish = function(){
		
		var ret = {
			name: "unnamed dish",
			ingredients: []
		};
		
		ret.addIngredient = function(){
			ret.ingredients.push(makeIngredient());
		};
		
		return ret;
	};
	
	return {
		create: function(){
			
			
			var ret = {
				dishes: [],
				plan: null,
				grocerylist: []
			};

			ret.addDish = function(){
				ret.dishes.push(makeDish());
			};

			ret.save = function(){
				localStorage.dishes = {};
				var dishes = mapping.toJS(ret);
				localStorage.model = ko.toJSON(ret);
			};
			
			ret.load = function(){
				var model = JSON.parse(localStorage.model);
				mapping.fromJS(model, ret);
			};
			
			return ret;
		}
		
	};
});