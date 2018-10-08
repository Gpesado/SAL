/**
* Auth
*/
(function () {
    'use strict';

    angular
        .module('django-angular.auth.services')
        .factory('Auth', Auth);

    Auth.$inject = ['$cookies', '$http'];

    function Auth($cookies, $http) {
      var Auth = {
        getAuthenticatedAccount: getAuthenticatedAccount,
        isAuthenticated: isAuthenticated,
        login: login,
        logout: logout,
        register: register,
        setAuthenticatedAccount: setAuthenticatedAccount,
        unauthenticate: unauthenticate
      };

      return Auth;


      //register user
      function register(email, password, username, first_name, last_name) {
        return $http.post('/api/v1/accounts/', {
          username: username,
          password: password,
          email: email,
          first_name: first_name,
          last_name: last_name
        });
      }

      // login user
      function login(username, password) {
        return $http.post('/api/v1/auth/login/', {
          username: username, password: password
        });
      }

      function getAuthenticatedAccount() {
        if (!$cookies.get('authenticatedAccount')) {
          return;
        }

        return JSON.parse($cookies.get('authenticatedAccount'));
      }

      function isAuthenticated() {
        return !!$cookies.get('authenticatedAccount');
      }

      function setAuthenticatedAccount(account) {
        $cookies.putObject('authenticatedAccount', account);
      }

      function unauthenticate() {
        $cookies.remove('authenticatedAccount');
      }

      // logout user
      function logout() {
        return $http.post('/api/v1/auth/logout/')
            .then(logoutSuccessFn, logoutErrorFn);

        function logoutSuccessFn(data, status, headers, config) {
            Auth.unauthenticate();
            window.location = '/';
        }

        function logoutErrorFn(data, status, headers, config) {
            console.error('Epic failure!');
        }
      }
    }
})();
