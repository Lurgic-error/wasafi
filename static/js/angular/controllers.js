
var mainControllers = angular.module('mainControllers', [
	'ngResource',
], function($httpProvider) {
  // Use x-www-form-urlencoded Content-Type
  $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
 
  /**
   * The workhorse; converts an object to x-www-form-urlencoded serialization.
   * @param {Object} obj
   * @return {String}
   */ 
  var param = function(obj) {
    var query = '', name, value, fullSubName, subName, subValue, innerObj, i;
      
    for(name in obj) {
      value = obj[name];
        
      if(value instanceof Array) {
        for(i=0; i<value.length; ++i) {
          subValue = value[i];
          fullSubName = name + '[' + i + ']';
          innerObj = {};
          innerObj[fullSubName] = subValue;
          query += param(innerObj) + '&';
        }
      }
      else if(value instanceof Object) {
        for(subName in value) {
          subValue = value[subName];
          fullSubName = name + '[' + subName + ']';
          innerObj = {};
          innerObj[fullSubName] = subValue;
          query += param(innerObj) + '&';
        }
      }
      else if(value !== undefined && value !== null)
        query += encodeURIComponent(name) + '=' + encodeURIComponent(value) + '&';
    }
      
    return query.length ? query.substr(0, query.length - 1) : query;
  };
 
  // Override $http service's default transformRequest
  $httpProvider.defaults.transformRequest = [function(data) {
    return angular.isObject(data) && String(data) !== '[object File]' ? param(data) : data;
  }];
})


mainControllers.factory('mainFactory', function ($rootScope,$route,$http,$resource,$q,$timeout) {

	var loading = {
    requests:0,
    total:0,
    total_finished:0,
    percentage:0,
  };

  var userPromice   = $q.defer();


  var promiseArray         = [];
 

  return{

    Page: false ,

    getLoading:function(){ return loading },

    Loading: function(start){

      if(loading.requests<0){
        loading.requests = 0;
        loading.total = 0;
        loading.total_finished = 0;
        loading.percentage = 0;
      } 

      start == 'start'?loading.requests += 1:'';
      start == 'end'?loading.requests -= 1:'';
      if(start == 'end' && loading.requests == 0){
        loading.total = 0;
        loading.total_finished = 0;
        loading.percentage = 0;
      }else{
        if(start == 'start'){
          loading.total += 1;
        }else if(start == 'end'){
          loading.total_finished += 1;
        }
      }
      loading.percentage = (loading.total_finished/loading.total)*100
    },

    getCookie:function(c_name)
    {
        if (document.cookie.length > 0)
        {
            c_start = document.cookie.indexOf(c_name + "=");
            if (c_start != -1)
            {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if (c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start,c_end));
            }
        }
        return "";
     },

    ajax:function($url,post_data){

      post_data = typeof post_data !== 'undefined' ? post_data          : null;
      post_data = post_data        !== null        ? $.param(post_data) : null;

      // The timeout property of the http request takes a deferred value
      // that will abort the underying AJAX request if / when the deferred
      // value is resolved.
      var deferredAbort  = $q.defer();


      var obj=this;
      obj.Loading('start');


      var request = $http({
        method  : post_data  ? 'POST' : 'GET' ,
        url     : base_url+$url,
        data    : post_data ,
        timeout : deferredAbort.promise,
        headers : { 'Content-Type': 'application/x-www-form-urlencoded', "X-CSRFToken": this.getCookie("csrftoken") } 
      })

      // Rather than returning the http-promise object, we want to pipe it
      // through another promise so that we can "unwrap" the response
      // without letting the http-transport mechansim leak out of the
      // service layer.
      var promise = request.then(
        function( response ) {
          obj.Loading('end');
          promiseArray.splice(promiseArray.indexOf(promise),1);
          return( response.data );
        },
        function(error) {
          obj.Loading('end');
          promiseArray.splice(promiseArray.indexOf(promise),1);
          error.url = base_url+$url;
          if(error.status == -1){
            // console.log(error)
            console.log('aborted');

          }else{
            console.log('error running page');
            //console.log(error)
          }
          return( $q.reject( 'Something went wrong' ) );
        }
      );

      // Now that we have the promise that we're going to return to the
      // calling context, let's augment it with the abort method. Since
      // the $http service uses a deferred value for the timeout, then
      // all we have to do here is resolve the value and AngularJS will
      // abort the underlying AJAX request.
      promise.abort = function() {
        deferredAbort.resolve();
        promiseArray.splice(promiseArray.indexOf(promise),1);
      };

      // Since we're creating functions and passing them out of scope,
      // we're creating object references that may be hard to garbage
      // collect. As such, we can perform some clean-up once we know
      // that the requests has finished.
      promise.finally(
        function() {
          promise.abort = angular.noop;
          deferredAbort = request = promise = null;
        }
      );

      promiseArray.push(promise);

      return( promise );
    },

    ajaxUndestructed:function($url,post_data){

      post_data = typeof post_data !== 'undefined' ? post_data          : null;
      post_data = post_data        !== null        ? $.param(post_data) : null;

      var q = $q.defer();
      var obj=this;
      obj.Loading('start');
      $http({
        method  : 'POST',
        url     : base_url+$url,
        data    : post_data ,
        headers : { 'Content-Type': 'application/x-www-form-urlencoded' }  
      })
      .then(function(data){
        obj.Loading('end');  
        q.resolve(data);
      }, function(error) {
     //Error
    });
      return q.promise;
    },

    destroyAllRequests : function(){

      angular.forEach(promiseArray, function(promise, key) {
        promise.abort();
      });
    },

    isOnline: true,

    setIsOnline: function(isonline){
      this.isOnline = isonline; 
    },

    getIsOnline: function(){
      return this.isOnline;
    },

    setPage: function(page){
      console.log(page)
      this.Page = page; 
    },

    getPage: function(){
      return this.Page;
    },


    //ASSETS
    getCountries: function() {
      return this.ajax('ajax/assets/getCountries',null)
    },
    getCurrencies: function() {
      return this.ajax('ajax/assets/getCurrencies',null)
    },
    getAppAPIs: function() {
      return this.ajax('ajax/assets/get_apis',null)
    },

    //USERS
    getUserAccounts: function() {
      return this.ajax('ajax/user/get_accounts',null)
    },

    getUserApps: function() {
      return this.ajax('ajax/user/get_apps',null)
    },

    //SHOP
    getUserShops: function() {
      return this.ajax('ajax/shop/get_shops');
    },
    
  };
 
});

