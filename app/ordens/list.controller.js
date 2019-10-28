(function () {
    'use strict';

    angular.module('app')
        .controller('OrdemListController', ['OrdemService', 'DialogBuilder', function (OrdemService, DialogBuilder) {
            this.load = () => OrdemService.findAll().then(dados => (this.dados = dados))

            this.load()
        }]);
})()