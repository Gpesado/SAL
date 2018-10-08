(function () {
    'use strict';

    angular
        .module('django-angular.home', [
            'django-angular.home.controllers',
            'django-angular.home.services'
        ]);

    angular
        .module('django-angular.home.controllers', []);

    angular
        .module('django-angular.home.services', ['ngCookies']);
})();
