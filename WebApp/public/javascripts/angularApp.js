var app = angular.module('PostureSensorWebApp', ['ngRoute']);

app.config(function($routeProvider) {
        $routeProvider

            // route for the home page
            .when('/', {
                templateUrl : 'pages/home.ejs',
                controller  : 'mainController'
            })

             // route for the tutorials page
            .when('/tutorials', {
                templateUrl : 'pages/tutorials.ejs',
                controller  : 'tutorialController'
            })

            .when('/tutorials/adafruit',{
                templateUrl : 'pages/adafruit.ejs',
                controller  : 'adafruitController'
            })

            .when('/tutorials/sms', {
                templateUrl : 'pages/sms.ejs',
                controller : 'smsController'
            })

    });


  
  


