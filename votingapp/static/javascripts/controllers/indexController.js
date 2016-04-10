'use strict';
app.controller('indexController', ['$scope','$window','$location', 'PollService',
               function ($scope, $window, $location, PollService) {
  /*if (!$window.localStorage.token) {
    $location.path('/');
    return;
  }*/
  $scope.Disaster = undefined;
  var fun = function(){
    PollService.getIndexView().then(function(response){
      $scope.Disaster = response;
    },function(response){
      $scope.err = 'something went wrong try again';

    });
  };
  fun();
     
}]);


app.controller('resetController', ['$scope', '$window', '$location','httpService','$routeParams',
               function ($scope, $window, $location, httpService, $routeParams){ 
                 $scope.resetPasswordConfirm = function(pwd, confirm){
                  var uid = $routeParams.uid;
                  var activation_key = $routeParams.activation_key;
                  var url = 'authentication/password/reset/confirm/';
                  httpService.httpPost(url, {
                    'uid':uid,
                    'token':activation_key,
                    'new_password':pwd,
                    're_new_password':confirm
                  }).then( function(response){
                    $scope.Message = 'password set! login to continue';
                },function(error){
                  $scope.ResetError = 'Try again later with correct email which exist in our system';
                });
                };
               }]);


app.controller('MainCtrl', ['$scope', function ($scope) {
    // $scope.todoList = {};
    // $scope.todoItems = [];
    // $scope.channel = 'todos';

    // $dragon.onReady(function() {
    //     $dragon.subscribe('toask-item', $scope.channel, {auth:localStorage.getItem('token')}).then(function(response) {
    //         $scope.dataMapper = new DataMapper(response.data);
    //         console.log($scope.dataMapper);
    //     });

    //     $dragon.getSingle('toask-item', {auth:localStorage.getItem('token'), id:1}).then(function(response) {
    //         $scope.todoList = response.data;
    //         console.log($scope.todoList);
    //     });

    //     $dragon.getList('toask-item', {auth:localStorage.getItem('token'), list_id:1}).then(function(response) {
    //         $scope.todoItems = response.data;
    //         console.log($scope.dataMapper);
    //     });
    // });

    // $dragon.onChannelMessage(function(channels, message) {
    //     if (indexOf.call(channels, $scope.channel) > -1) {
    //         $scope.$apply(function() {
    //             $scope.dataMapper.mapData($scope.todoItems, message);
    //         });
    //     }
    // });

    // $scope.itemDone = function(item) {
    //     item.done = true != item.done;
    //     $dragon.update('todo-item', item);
    // }
}]);


app.directive('materialSelect', function() {
   return {
      restrict: 'A',
      link: function(scope, elem) {
         $(elem).material_select();
      }
   };
});
