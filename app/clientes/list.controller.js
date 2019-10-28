(function () {
    'use strict';

    angular.module('app')
        .controller('ClienteListController', ['ClienteService', 'DialogBuilder', function (ClienteService, DialogBuilder) {
            this.load = () => ClienteService.findAll().then(dados => (this.dados = dados))

            this.load()
        }]);
})()