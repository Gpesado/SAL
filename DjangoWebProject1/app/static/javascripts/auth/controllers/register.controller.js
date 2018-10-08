(function () {
    'use strict';

    angular
        .module('django-angular.auth.controllers')
        .controller('RegisterController', RegisterController);

    RegisterController.$inject = ['$location', '$scope', 'Auth'];

    function RegisterController($location, $scope, Auth) {

      activate();

  		function activate() {
        // If the user is authenticated, they should not be here.
        if (Auth.isAuthenticated()) {
          $location.url('/');
        }
  		}

      var vm = this;
      vm.register = register;

      function register() {
        $scope.pass_field_color = "";
        $scope.email_field_color = "";

        if(vm.email != vm.email2){
          $scope.email_field_color = "red";
          $scope.error_message = "Emails must match.";
        }
        else if(vm.password != vm.password2){
          $scope.pass_field_color = "red";
          $scope.error_message = "Passwords must match.";
        }
        else
          Auth.register(vm.email, vm.password, vm.username, vm.name, vm.surname).then(registerSuccessFn, registerErrorFn);
      }

      function registerSuccessFn(data, status, headers, config) {
        console.error(data);
        Auth.login(vm.username, vm.password).then(loginSuccessFn, loginErrorFn);
      }

      function registerErrorFn(data, status, headers, config) {
        console.error(data);
      }

      function loginSuccessFn(data, status, headers, config) {
        Auth.setAuthenticatedAccount(data.data);
        window.location = '/';
      }

      function loginErrorFn(data, status, headers, config) {
        console.error('Epic failure!');
      }
    }
})();
