mainControllers.controller('movies', ['$location','$route','$routeParams','$scope','$http','$q','$interval','$timeout','mainFactory', function($location,$routeParams,$route,$scope, $http, $q,$interval,$timeout,mainFactory) {
	
	mainFactory.setPage('movies')
	$scope.static_url = static_url;

}]);



