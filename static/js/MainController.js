app.controller('MainController', ['$scope', function($scope) { 
  $scope.likes = 0; 
  $scope.plusOne()=function(index){
  	$scope.likes += 1;
  };
}]);