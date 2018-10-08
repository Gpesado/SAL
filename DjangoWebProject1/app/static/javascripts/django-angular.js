(function () {
    'use strict';

    angular
        .module('django-angular', [
            'django-angular.config',
            'django-angular.routes',
            'django-angular.layout',
            'django-angular.home',
            'django-angular.auth',
        ])
        .run(run);

    run.$inject = ['$http'];

    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }

    angular
        .module('django-angular.config', []);

    angular
        .module('django-angular.routes', ['ngRoute']);
})();
