var map;

function initMap() {
    var mapOptions = {
        zoom: 1,
        center: new google.maps.LatLng(18.518, -30.787),
        styles: window.mapstyle
    };
    map = new google.maps.Map(document.getElementById('map'), mapOptions);

    // Define the LatLng coordinates for the polygon.
    var triangleCoords = [
        {lat: 25.774, lng: -80.190},
        {lat: 18.466, lng: -66.118},
        {lat: 32.321, lng: -64.757}
    ];

    var kmlLayer = new google.maps.KmlLayer({
        url: window.location.origin + '/data/get/all.kml?' + (new Date()).getTime(),
        suppressInfoWindows: true,
        map: map
    });

    map.setZoom(2);
    map.setCenter(new google.maps.LatLng(18.518, -30.787));

}