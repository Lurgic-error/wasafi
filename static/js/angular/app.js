var myApp = angular.module('myApp', [
  'ngRoute',
  'ngSanitize',
  'ngResource',
  'djng.urls',
  'djng.forms',
  'mainControllers',

  // {% for module in ng_requires %}'{{ module }}'{% if not forloop.last %}, {% endif %}{% endfor %}

])


myApp.config(function($httpProvider) {
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

myApp.config(['$locationProvider', function($locationProvider) {
  $locationProvider.hashPrefix('');
}]);

myApp.config(['$routeProvider', function($routeProvider) {
  $routeProvider.
  when('/movies', {
    templateUrl : '../admin_partials/movies',
    controller  : 'movies'
  }).
  when('/series', {
    templateUrl : '../admin_partials/series',
    controller  : 'series'
  }).
  when('/payments', {
    templateUrl : '../admin_partials/payments',
    controller  : 'payments'
  }).
  when('/admins', {
    templateUrl : '../admin_partials/admins',
    controller  : 'admins'
  }).
  when('/customers', {
    templateUrl : '../admin_partials/customers',
    controller  : 'customers'
  }).
  when('/ads', {
    templateUrl : '../admin_partials/ads',
    controller  : 'ads'
  }).
  otherwise({
    redirectTo: 'movies'
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
          return original.apply($location, [path]);
        };
      }]);

myApp.run(['$rootScope','$http',function($rootScope,$http) {
  $rootScope.$on("$locationChangeStart", function(event, next, current) { 
    var clientsIP = {};
    $.get("http://ipinfo.io", function(response) {
      clientsIP = response
      str = window.location.href;
      if(str.indexOf('/auth') == -1 && str.indexOf('developer/docs') == -1){

        $http({
          method  : 'POST',
          url     : base_url+'ajax/assets/savepath',
          data    : $.param({'path':window.location.href,'clientsIP':clientsIP}),
          headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  
        })
        .then(function(data){
          str = window.location.href
          if(!data){
            //console.log(data)
            location.reload();
          }
        }, function(error) {
     //Error
   });
      }
    }, "jsonp");
  });
}]);

myApp.filter('nil', function ($filter) {
  return function (value) {
    return $filter('currency')(value, '')
  }
})

// String.prototype.splice = function(idx, rem, s) {
//     return (this.slice(0, idx) + s + this.slice(idx + Math.abs(rem)));
// };

// myApp.directive('currencyInput', function() {
//     return {
//         restrict: 'A',
//         scope: {
//             field: '='
//         },
//         replace: true,
//         template: function(scope,element,attrs){

//           attrStr = "";
//           angular.forEach(element.$attr, function(attr, key) {
//           if(attr != 'currency-input' && attr != 'ng-model'){
//             eval('x = element.'+key);
//             attrStr += ' '+attr+'="'+x+'"'; 
//           }
//           });
//           console.log(attrStr)

//           return '<span><input '+attrStr+' ng-model="field" /></span>'
//         },
//         link: function(scope, element, attrs) {

//             console.log(attrs.ngModel);


//             $(element).bind('keyup', function(e) {


//               //eval('x = element.'+key);

//                 var input = element.find('input');
//                 var inputVal = input.val();

//                 //clearing left side zeros
//                 while (scope.field.charAt(0) == '0') {
//                     scope.field = scope.field.substr(1);
//                 }

//                 scope.field = scope.field.replace(/[^\d.\',']/g, '');

//                 var point = scope.field.indexOf(".");
//                 if (point >= 0) {
//                     scope.field = scope.field.slice(0, point + 3);
//                 }

//                 var decimalSplit = scope.field.split(".");
//                 var intPart = decimalSplit[0];
//                 var decPart = decimalSplit[1];

//                 intPart = intPart.replace(/[^\d]/g, '');
//                 if (intPart.length > 3) {
//                     var intDiv = Math.floor(intPart.length / 3);
//                     while (intDiv > 0) {
//                         var lastComma = intPart.indexOf(",");
//                         if (lastComma < 0) {
//                             lastComma = intPart.length;
//                         }

//                         if (lastComma - 3 > 0) {
//                             intPart = intPart.splice(lastComma - 3, 0, ",");
//                         }
//                         intDiv--;
//                     }
//                 }

//                 if (decPart === undefined) {
//                     decPart = "";
//                 }
//                 else {
//                     decPart = "." + decPart;
//                 }
//                 var res = intPart + decPart;

//                 scope.$apply(function() {scope.field = res});

//             });

//         }
//     };
// });