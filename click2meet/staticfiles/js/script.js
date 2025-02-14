document.addEventListener("DOMContentLoaded", function() {
    console.log('DOM loaded');
    var cancelButtons = document.querySelectorAll('.cancel-booking');
    var cancelModal = document.getElementById('cancelModal');
    var cancelConfirm = document.getElementById('cancelConfirm');

    cancelButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var bookingId = this.getAttribute('data-booking-id');
            cancelConfirm.setAttribute('href', 'cancel/' + bookingId);
            var modal = new bootstrap.Modal(cancelModal);
            modal.show();
        });
    });
});