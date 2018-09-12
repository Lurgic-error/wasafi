mainControllers.controller('movies', ['$location','$route','$routeParams','$scope','$http','$q','$interval','$timeout','mainFactory', function($location,$routeParams,$route,$scope, $http, $q,$interval,$timeout,mainFactory) {
	
	mainFactory.setPage('movies')

	$scope.static_url = static_url

	$scope.changePage = function(page){
		$scope.page = page;
	}
	$scope.changePage('preview');

	$scope.step = 1;
	$scope.new_movie = function(movie){
		$scope.new_movie = movie;
		$scope.edit_movie_view(true);
	}

	$scope.next_step = function(){

		console.log($scope.step)

		if ($scope.step == 1) {

		}else if($scope.step == 2){

		}else if($scope.step == 3){
			$scope.step = 1;
		}

		if($scope.step < 3){
			$scope.step += 1
		}
	}

	$scope.prev_step = function(){
		if($scope.step > 1){
			$scope.step -= 1
		}
	}

	$scope.edit_movie_view = function(view){
		$scope.new_movie_view = view;
	}

	$scope.select_movie = function(movie){
		$selected_movie = movie
	}


}]);



