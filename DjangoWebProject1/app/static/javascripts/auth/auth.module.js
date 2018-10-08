(function () {
    'use strict';

    angular
        .module('django-angular.auth', [
            'django-angular.auth.controllers',
            'django-angular.auth.services'
        ]);

    angular
        .module('django-angular.auth.controllers', []);

    angular
        .module('django-angular.auth.services', ['ngCookies']);
})();
