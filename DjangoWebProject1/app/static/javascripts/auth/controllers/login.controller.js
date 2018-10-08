(function () {
    'use strict';

    angular
        .module('django-angular.auth.controllers')
        .controller('LoginController', LoginController);

    LoginController.$inject = ['$location', '$scope', 'Auth'];

    // LoginController
    function LoginController($location, $scope, Auth) {
      var vm = this;
      vm.login = login;

      activate();

      function activate() {
        // If the user is authenticated, they should not be here.
        if (Auth.isAuthenticated()) {
          $location.url('/');
        }
      }

      //Log the user in
      function login() {
        Auth.login(vm.username, vm.password).then(loginSuccessFn, loginErrorFn);
      }

      function loginSuccessFn(data, status, headers, config) {
        Auth.setAuthenticatedAccount(data.data);
        window.location = '/';
      }

      function loginErrorFn(data, status, headers, config) {
        $scope.error_message = data.data.message;
      }
    }
})();
