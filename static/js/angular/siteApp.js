var myApp = angular.module('myApp', [
  'ngRoute',
  'ngSanitize',
  'mainControllers',
  'ngResource',
  
]);

myApp..config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

myApp.config(['$routeProvider', function($routeProvider) {
  $routeProvider.
  when('/home/:page?', {
    templateUrl: base_url+'home/home',
    controller: 'home'
  }).
  otherwise({
    redirectTo: ''
  });
}]);

myApp.run(['$route', '$rootScope', '$location','$http','mainFactory', function ($route, $rootScope, $location,$http,mainFactory) {
    var original = $location.path;
    $location.path = function (path, reload) {
        if (reload === false) {
            var lastRoute = $route.current;
            var un = $rootScope.$on('$locationChangeSuccess', function () {
                $route.current = lastRoute;
                un();
            });
            //mainFactory.Loading('end')
        }
      if(path){
        $http({
          method  : 'POST',
          url     : base_url+'ajax/assets/savepath',
          data    : $.param({'path':path}),
          headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  
        })
        .then(function(data){
        }, function(error) {
     //Error
    });
      }
      return original.apply($location, [path]);
    };
}]);A