(function () {
    'use strict';

    angular.module('app')
        .service('ClienteService', ['$http', function ($http) {
            this.findAll = () => $http.get('http://www.mocky.io/v2/5db5f2aa2f00005e007fe75e').then(resp => resp.data)
        }]);
})()