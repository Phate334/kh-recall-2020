var searchApp = angular.module('searchStation', []);

searchApp.controller('StationList', function SearchListController($scope, $http) {
    $http.get("data.json").then(function (response) {
        $scope.stationData = response.data;
    });
});