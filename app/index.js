(function () {
    angular.module('app', ['ui.router']);

    angular.module('app').config(['$stateProvider', function ($stateProvider) {
        $stateProvider
            .state({
                name: 'inicio',
                url: '/'
            })

            .state({
                name: 'clientesList',
                url: '/clientes',
                templateUrl: '/views/clientes/list.html',
                controller: 'ClienteListController',
                controllerAs: 'vm'
            })
            .state({
                name: 'clientesNovo',
                url: '/clientes/novo',
                templateUrl: '/views/clientes/form.html',
                controller: 'ClienteFormController',
                controllerAs: 'vm'
            })


            .state({
                name: 'ordensList',
                url: '/ordens',
                templateUrl: '/views/ordens/list.html',
                controller: 'OrdemListController',
                controllerAs: 'vm'
            })
            .state({
                name: 'ordensNovo',
                url: '/ordens/novo',
                templateUrl: '/views/ordens/form.html',
                controller: 'OrdemFormController',
                controllerAs: 'vm'
            })
    }]);
})()