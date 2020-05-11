var searchApp = angular.module('searchStation', []);

searchApp.controller('StationList', function SearchListController($scope, $http) {
    $http.get("1589206881.json").then(function (response) {
        $scope.stationData = response.data;
    });
});