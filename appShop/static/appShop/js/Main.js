$(document).ready(function() {
  if (document.getElementById('messageModal')) {
      var myModal = new bootstrap.Modal(document.getElementById('messageModal'));
      myModal.show();
  }
});

$(document).ready(function() {
  $('.gallery-img').on('click', function() {
      var imgSrc = $(this).attr('src');
      var imgDescription = $(this).data('description');
      var imgLink = $(this).data('link');

      $('#modalImage').attr('src', imgSrc);
      $('#modalDescription').text(imgDescription);
      $('#modalLink').attr('href', imgLink);

      $('#fundacionesModal').modal('show');
  });
});
