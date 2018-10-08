/**
* NavbarController for logging out users
*/
(function () {
    'use strict';

    angular
        .module('django-angular.layout.controllers')
        .controller('NavbarController', NavbarController);

    NavbarController.$inject = ['$scope', 'Auth'];

    function NavbarController($scope, Auth) {
        var vm = this;

        vm.logout = logout;

        //Log the user out
        function logout() {
            Auth.logout();
        }

        $(document).ready(function() {
            $(".button-collapse").sideNav();
        });
    }
})();
