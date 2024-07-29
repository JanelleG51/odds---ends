/*jshint esversion: 6 */
$('.toast').toast('show');
$('#new-image').change(function() {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});