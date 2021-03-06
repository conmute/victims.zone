var map;
var marker;
var polyline;
var path = [];

function initMap() {

    var mapOptions = {
        zoom: 1,
        center: new google.maps.LatLng(18.518, -30.787),
        styles: window.mapstyle
    };
    map = new google.maps.Map(document.getElementById('map-polygon'), mapOptions);

    google.maps.event.addListener(map, "click", function (location) {
        path.push(location.latLng);

        if (polyline) {
            polyline.setMap(null);
        }


        if (marker) {
            marker.setMap(null);
        }

        marker = new google.maps.Marker({
            position: location.latLng,
            map: map
        });

        polyline = new google.maps.Polygon({
            path:path,
            strokeColor: "#FF0000",
            strokeOpacity: 1.0,
            strokeWeight: 2
        });

        polyline.setMap(map);

        var tmp = [];
        $.each(path, function(index, obj) {
            tmp.push({lat: obj.lat(), lng: obj.lng()});
        });

        $('#inputPolygon').val(JSON.stringify(tmp));

        map.setCenter(new google.maps.LatLng(map.getCenter().lat(),  map.getCenter().lng(), map.getZoom()));
    });

}

$('a#polygonClear').on('click', function(event) {
    if (polyline) {
        polyline.setMap(null);
    }
    if (marker) {
        marker.setMap(null);
    }
    path = [];
    $('#inputPolygon').val('');
});
$('#inputDateRange').daterangepicker({
    ranges: {
       'Today': [moment(), moment()],
       'Yesterday': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
       'Last 7 Days': [moment().subtract(6, 'days'), moment()],
       'Last 30 Days': [moment().subtract(29, 'days'), moment()],
       'This Month': [moment().startOf('month'), moment().endOf('month')],
       'Last Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
    },
    maxDate: new Date()
});
$('#inputCategory').select2({
    placeholder: "Select a category",
    tags: true
}).val('').trigger('change');
$('#inputTags').select2({
    placeholder: "Select tags",
    tags: true,
    maximumSelectionLength: 5
});