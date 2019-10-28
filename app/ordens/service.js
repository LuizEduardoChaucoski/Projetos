(function () {
    'use strict';

    angular.module('app')
        .service('OrdemService', ['$http', function ($http) {
            this.findAll = () => $http.get('http://www.mocky.io/v2/5db6065d2f000059007fe775').then(resp => resp.data)
        }]);
})()