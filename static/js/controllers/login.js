//admin
mainControllers.controller('login', ['$location','$route','$routeParams','$scope','$http','mainFactory','$interval','$timeout', function($location,$routeParams,$route,$scope, $http, mainFactory,$interval,$timeout) {
	console.log(base_url);

	
	$scope.countriesPromice = mainFactory.ajax('ajax/assets/getCountries',null);
   	$scope.countriesPromice.then(function(v){
   		$scope.countries = v;
   		$scope.selectCountry(v[0])
   		$.getJSON("http://freegeoip.net/json/", function(result){
        	angular.forEach($scope.countries, function(value, key) {

        	
  			if(value.iso == result.country_code)
  				$scope.selectCountry(value)
			});

        });
    });

    date           = new Date();
    $scope.max_Dob = date.getTime();
    $scope.min_Dob = parseInt($scope.max_Dob)-(1000*60*60*24*366*100);


	$scope.login_type = 'email' 


}]);