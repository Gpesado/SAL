(function () {
  'use strict';

  angular
    .module('django-angular.home.services')
    .factory('Home', Home);

  Home.$inject = ['$http'];

  function Home($http) {
    var Home = {
      bleu_score: bleu_score
    };

    return Home;

    function bleu_score(input, output) {
      return $http.post('api/v1/bleu-score/', {input: input, output: output});
    }

  }
})();
