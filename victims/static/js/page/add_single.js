var map;
var marker;

function initMap() {

    var mapOptions = {
        zoom: 1,
        center: new google.maps.LatLng(18.518, -30.787),
        styles: window.mapstyle
    };
    map = new google.maps.Map(document.getElementById('map-location'), mapOptions);

    google.maps.event.addListener(map, 'click', function(event) {
       placeMarker(event.latLng, map);
       $('#inputLocation').val(event.latLng.lat() + ', ' + event.latLng.lng());
    });

}
function placeMarker(location, map) {
    if (marker) {
        marker.setMap(null);
    }
    marker = new google.maps.Marker({
        position: location,
        map: map
    });
    map.panTo(location);
}
$('#inputLocation').on('change keyup', function() {
    var val = $(this).val().split(', ');
    if (val.length != 2) {
        return;
    }
    var lat = parseFloat(val[0]);
    var lng = parseFloat(val[1]);
    if (map) {
        placeMarker(new google.maps.LatLng(lat, lng), map);
    }
});
$('#inputDate').daterangepicker({
    singleDatePicker: true,
    showDropdowns: true,
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