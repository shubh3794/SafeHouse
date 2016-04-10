'use strict';
app.controller('dashboardController', ['$scope','$window','$location', 'AuthService','$routeParams','PollService',
               function ($scope, $window, $location, AuthService, $routeParams,PollService) {


    if(!$window.localStorage.token){
    	$location.path('/');
    }

   	$scope.getUser = function(){
   		var id = $routeParams.id.replace('user','');
   		AuthService.storeCurrUser(id).then(function(response){

   			$scope.Profile = response;
        $scope.votedQues = [];
   		}, function(response){
   			$scope.Profile = '';
   		});

   		

   	};
   	$scope.getUser();
   	$scope.AuthenticatedUser = JSON.parse($window.localStorage.getItem('user'));
   	
   	

}]);

app.controller('profileController', ['$scope','$window','$location', 'AuthService','$routeParams','PollService',
               function ($scope, $window, $location, AuthService, $routeParams,PollService) {


    if(!$window.localStorage.token){
      $location.path('/');
    }

    $scope.getUser = function(){
      AuthService.getAuthdUser().then(function(response){

        $scope.Profile = response;
      }, function(response){
        $scope.Profile = '';
      });

      

    };
    $scope.getUser();
    $scope.AuthenticatedUser = JSON.parse($window.localStorage.getItem('user'));

    var funn = function(){
      AuthService.updateUser({'lat':$scope.userLat, 'lon':$scope.userLong}).then(function(response){
        console.log(response);
      }, function(error){
        console.log(error);

      });
    };
    $scope.getLocation = function() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition($scope.showPosition);
    } else {
        console.log('geolocation is not supported by this browser');
    }
};
$scope.showPosition = function(position) {
    $scope.userLat = position.coords.latitude;
    $scope.userLong = position.coords.longitude;
    funn();
};

$scope.getLocation();
    




}]);