mainControllers.controller('setting', ['$location','$route','$routeParams','$scope','$http','$interval','$timeout','mainFactory', function($location,$routeParams,$route,$scope, $http, $interval,$timeout,mainFactory) {

	$scope.userPromice = mainFactory.ajax('ajax/user/getUser',null);
	$scope.userPromice.then(function(v){
 		$scope.user = v
 		$scope.user.created = new Date($scope.user.created)
	});


	$scope.adressesPromice = mainFactory.ajax('ajax/user/get_adresses',null);
	$scope.adressesPromice.then(function(v){
 		$scope.adresses = v
	});
	$scope.new_adress = {}
	$scope.add_adress = function(){

		$('#edit_adress').modal('show')
	}
	$scope.edit_adress = function(adress){
		$scope.new_adress = adress;
		$('#edit_adress').modal('show')
	}
	$scope.save_adress = function(){
		console.log($scope.new_adress)
		$http({
        method  : 'POST',
        url     : base_url+'ajax/user/save_adress',
        data    : $.param($scope.new_adress),
        headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  
      	})
      	.then(function(data){
			$('#edit_adress').modal('hide')
			$scope.user.adresses.push(data);
		}, function(error) {
     //Error
    })
	}
	$scope.delete_adress = function(adress){

		$http({
        method  : 'POST',
        url     : base_url+'ajax/user/delete_adress',
        data    : $.param(adress),
        headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  
      	})
      	.then(function(data){
		
		}, function(error) {
		 //Error
		})
	}


	$scope.emailsPromice = mainFactory.ajax('ajax/user/get_emails',null);
	$scope.emailsPromice.then(function(v){
 		$scope.emails = v
	});
	$scope.new_email = {}
	$scope.add_email = function(){
		$('#edit_email').modal('show')
	}
	$scope.edit_email = function(email){
		$scope.new_email = email
		$('#edit_email').modal('show')
	}
	$scope.save_email = function(){
		$http({
        method  : 'POST',
        url     : base_url+'ajax/user/save_email',
        data    : $.param($scope.new_email),
        headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  
      	})
      	.then(function(data){
			//$('#edit_email').modal('hide')
			var_dump(data);
			//$scope.user.email.push(data);
		}, function(error) {
		 //Error
		})
	}
	$scope.delete_email = function(email){
		$http({
        method  : 'POST',
        url     : base_url+'ajax/user/delete_email',
        data    : $.param(email),
        headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  
      	})
      	.then(function(data){

		}, function(error) {
     //Error
    })
	}

	$scope.phonesPromice = mainFactory.ajax('ajax/user/get_phones',null);
	$scope.phonesPromice.then(function(v){
 		$scope.phones = v
	});
	$scope.new_phone = {}
	$scope.add_phone = function(){
		
		$('#edit_phone').modal('show')
	}
	$scope.edit_phone = function(phone){
		$scope.new_phone = phone;
		$('#edit_phone').modal('show')
	}
	$scope.save_phone = function(){
		$http({
        method  : 'POST',
        url     : base_url+'ajax/user/new_phone',
        data    : $.param($scope.new_phone),
        headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  
      	})
      	.then(function(data){
      		$scope.user.phone.push(data);
			$('#edit_phone').modal('hide')
		})
	}
	$scope.delete_phone = function(phone){
		$http({
        method  : 'POST',
        url     : base_url+'ajax/user/delete_phone',
        data    : $.param(phone),
        headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  
      	})
      	.then(function(data){

		}, function(error) {
     //Error
    })
	}



	$scope.new_password = {}
	$scope.edit_password = function(){	
		$('#edit_password').modal('show')
	}
	$scope.save_password = function(){
		$http({
        method  : 'POST',
        url     : base_url+'ajax/user/save_password',
        data    : $.param($scope.new_password),
        headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  
      	})
      	.then(function(data){
			$('#edit_password').modal('hide')
		}, function(error) {
     //Error
    })
	}
	



	$scope.new_security_question = {}
	$scope.edit_security_question = function(){
		
		$('#edit_security_question').modal('show')
	}

	$scope.save_security_question = function(){
		$http({
        method  : 'POST',
        url     : base_url+'ajax/user/save_security_question',
        data    : $.param($scope.new_security_question),
        headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  
      	})
      	.then(function(data){
			$('#edit_security_question').modal('hide')
		}, function(error) {
     //Error
    })
	}


	$scope.new_pin = {}
	$scope.edit_pin = function(){
		
		$('#edit_pin').modal('show')
	}

	$scope.save_pin = function(){
		$http({
        method  : 'POST',
        url     : base_url+'ajax/user/save_pin',
        data    : $.param($scope.new_pin),
        headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  
      	})
      	.then(function(data){
			$('#edit_pin').modal('hide')
		}, function(error) {
     //Error
    })
	}

	




}]);