$('#exampleModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })
  $('#example1Modal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })

  $( "form" ).submit(function( event ) {
    event.preventDefault();
  });
