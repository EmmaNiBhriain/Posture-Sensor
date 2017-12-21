var app = angular.module('PostureSensorWebApp');


app.controller('mainController', ['$scope', function($scope) {
    // create a message to display in our view
    $scope.message = 'Welcome to the web application for the Posture Sensor IoT Project! Explore useful tutorials and more....';

}
  ]);
