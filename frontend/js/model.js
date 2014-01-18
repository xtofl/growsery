define(["knockout", "proxy"], 
		function(ko, proxy){
	
	var makeIngredient = function() {
		var ret = {
				name: ko.observable(""),
				quantity: ko.observable("")
		};
		return ret;
	};
	
	var makeDish = function(){
		
		var ret = {
			name: ko.observable("unnamed dish"),
			ingredients: ko.observableArray()
		};
		
		ret.addIngredient = function(){
			ret.ingredients.push(makeIngredient());
		};
		
		return ret;
	};
	
	return {
		create: function(){
			
			
			var ret = {
				dishes: ko.observableArray(),
				plan: ko.observable(),
				grocerylist: ko.observableArray()
			};

			ret.addDish = function(){
				ret.dishes.push(makeDish());
			};
			return ret;
		}
		
	};
});