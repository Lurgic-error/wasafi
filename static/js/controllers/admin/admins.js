mainControllers.controller('admins', ['$location','$route','$routeParams','$scope','$q','$http','$interval','$timeout','mainFactory', function($location,$routeParams,$route,$scope, $q,$http, $interval,$timeout,mainFactory) {
	
	mainFactory.setPage('admins')
	$scope.static_url = static_url;
	$scope.base_url = base_url;

	$scope.new_admin_view = false;

	$scope.static_url = static_url;

	$scope.new_admin = {};

	$scope.countriesPromice = mainFactory.ajax('ajax/getcountries',null);
    $scope.countriesPromice.then(function(v){
      	$scope.countries = v;
      	$scope.new_admin.country = v[219][0];
    });

    $scope.adminsPromice = mainFactory.ajax('ajax/admin/getadmin',null);
    $scope.adminsPromice.then(function(v){
      	$scope.admins = v;
      	$scope.selectAdmin(v[0])
      	console.log(v);
    });

    $query = {'query':'admin-'}
    $scope.groupsPromice = mainFactory.ajax('ajax/getgroups',$query);
    $scope.groupsPromice.then(function(v){
      	$scope.groups = v;
    });


    $scope.editAdmin = {}

    $scope.selectAdmin = function(admin){
    	$scope.selectedAdmin = admin;
    	$scope.editAdmin = admin;
    }

	$scope.step = 1
	$scope.new_admin = function(admin){
		$scope.new_admin_view = true;
	}

	$scope.next_step = function(){

		console.log($scope.step)

		$scope.error = {};

		if ($scope.step == 1) {

			if($scope.error.first_name == ''){
				$scope.error.first_name = 'This field is required'
				console.log($scope.error)
				return false
			}

			if($scope.error.first_name == ''){
				$scope.error.last_name = 'This field is required'
				return false
			}

			if($scope.error.email == ''){
				$scope.error.email = 'This field is required'
				return false
			}

			var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
		    if(!re.test(String($scope.new_admin.email).toLowerCase())){
		    	$scope.error.email = 'This field requires an email'
				return false
		    }

			if($scope.new_admin.password != $scope.new_admin.confirm_password){
				$scope.error.email = 'Passwords do not match'
				return false
			}

			$http({
		        method  : 'POST',
		        url     : base_url+'ajax/admin/create',
		        data    : $.param($scope.new_admin),
		        headers : { 'Content-Type': 'application/x-www-form-urlencoded', "X-CSRFToken": mainFactory.getCookie("csrftoken")  }  
		    }).then(function(data) {
				 
				 $scope.admins.push(data)
				 $scope.step += 1
				 $scope.selectAdmin(data)

			}, function(error) {
				console.log(error)
				$scope.error = error.error
			});  
		   
		}else if($scope.step == 2){
			$scope.step += 1
		}else if($scope.step == 3){
			$scope.step = 1;
		}

	}

	$scope.prev_step = function(){
		if($scope.step > 1){
			$scope.step -= 1
		}
	}

	$scope.cancel_step = function(){
		$scope.new_admin_view = false;
		$scope.step == 1
	}


	$scope.changePage = function(page){
		$scope.page = page
	}
	$scope.changePage('info');

	$scope.change_image_modal = function(){
		$("#id_file").click()
	}


	$("#id_file").change(function () {
	  if (this.files && this.files[0]) {
	    var reader = new FileReader();
	    reader.onload = function (e) {
	      $("#image").attr("src", e.target.result);
	      $("#modalCrop").modal("show");
	    }
	    reader.readAsDataURL(this.files[0]);
	  }
	});






	 /* SCRIPTS TO HANDLE THE CROPPER BOX */
	var $image = $("#image");
	var cropBoxData;
	var canvasData;
	$("#modalCrop").on("shown.bs.modal", function () {


		// var id_x = '<input type="hidden" id="id_x" name="x">';
		// var id_y = '<input type="hidden" id="id_y" name="y">';
		// var id_height = '<input type="hidden" id="id_height" name="height">';
		// var id_width = '<input type="hidden" id="id_width" name="width">';
		// var id_user = '<input type="hidden" id="id_user" name="username" value="'+$scope.selectedAdmin.username+'">';

  //   	$('#formUpload').append(id_x);
  //   	$('#formUpload').append(id_y);
  //   	$('#formUpload').append(id_height);
  //   	$('#formUpload').append(id_width);
  //   	$('#formUpload').append(id_user);

	  $image.cropper({
	    viewMode: 1,
	    aspectRatio: 1/1,
	    minCropBoxWidth: 200,
	    minCropBoxHeight: 200,
	    ready: function () {
	      $image.cropper("setCanvasData", canvasData);
	      $image.cropper("setCropBoxData", cropBoxData);
	    }
	  });
	}).on("hidden.bs.modal", function () {
	  cropBoxData = $image.cropper("getCropBoxData");
	  canvasData = $image.cropper("getCanvasData");
	  $image.cropper("destroy");
	});


	function sendData(form) {

	    var XHR = new XMLHttpRequest();

	    // Bind the FormData object and the form element
	    var FD = new FormData(form);

	    // Define what happens on successful data submission
	    XHR.addEventListener("load", function(event) {
	      console.log(event.target.responseText);
	      $("#modalCrop").modal("hide");
	      $scope.selectedAdmin(eval(event.target.responseText))
	      $scope.admins
	    });

	    // Define what happens in case of error
	    XHR.addEventListener("error", function(event) {
	      alert('Oops! Something went wrong.');
	    });

	    

	    // Set up our request
	    XHR.open("POST", base_url+"ajax/admin/profilepicture");
	    XHR.setRequestHeader("X-CSRFToken" , mainFactory.getCookie("csrftoken"))
	    // XHR.setRequestHeader('Content-Type' , 'application/x-www-form-urlencoded')

	    // The data sent is what the user provided in the form
	    XHR.send(FD);
	}


	// Enable zoom in button
	$(".js-zoom-in").click(function () {
	  $image.cropper("zoom", 0.1);
	});
	// Enable zoom out button
	$(".js-zoom-out").click(function () {
	  $image.cropper("zoom", -0.1);
	});

	$(".js-crop-and-upload").click(function () {

        var cropData = $image.cropper("getData");

        $("#id_x").val(cropData["x"]);
        $("#id_y").val(cropData["y"]);
        $("#id_height").val(cropData["height"]);
        $("#id_width").val(cropData["width"]);

        var FD = document.getElementById("formUpload");

        console.log(FD);
        sendData(FD);
        // $("#formUpload").submit();
    });



}]);

