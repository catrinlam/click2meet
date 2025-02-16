document.addEventListener("DOMContentLoaded", function() {
    const cancelButtons = document.getElementsByClassName("cancel-booking");
    const cancelModal = document.getElementById("cancelModal");
    const cancelConfirm = document.getElementById("cancelConfirm");

    for (let button of cancelButtons) {
        button.addEventListener("click", (e) => {
            let bookingId = e.target.getAttribute("data-booking-id");
            cancelConfirm.href = `cancel/${bookingId}`;
            cancelModal.classList.add("show");
            cancelModal.style.display = "block";
            cancelModal.setAttribute("aria-modal", "true");
            cancelModal.removeAttribute("aria-hidden");
        });
    }

    document.querySelectorAll('[data-bs-dismiss="modal"]').forEach(function(button) {
        button.addEventListener("click", function() {
            cancelModal.classList.remove("show");
            cancelModal.style.display = "none";
            cancelModal.removeAttribute("aria-modal");
            cancelModal.setAttribute("aria-hidden", "true");
        });
    });

    const form = document.querySelector('form[data-quantity-id]');
    if (form) {
        const quantityInputId = form.getAttribute('data-quantity-id');

        document.getElementById('decreaseQuantity').addEventListener('click', function() {
            var quantityInput = document.getElementById(quantityInputId);
            var currentValue = parseInt(quantityInput.value);
            if (currentValue > 0) {
                quantityInput.value = currentValue - 1;
            }
        });

        document.getElementById('increaseQuantity').addEventListener('click', function() {
            var quantityInput = document.getElementById(quantityInputId);
            var currentValue = parseInt(quantityInput.value);
            quantityInput.value = currentValue + 1;
        });
    }

    document.getElementById('confirmCancel').addEventListener('click', function() {
        document.getElementById('cancelBookingForm').submit();
    });
});