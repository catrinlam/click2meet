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
        const quantityDisplay = document.getElementById('quantityDisplay');
        const quantityInput = document.getElementById(quantityInputId);

        // Set initial value to 0
        quantityDisplay.textContent = '0';
        quantityInput.value = '0';

        document.getElementById('decreaseQuantity').addEventListener('click', function() {
            var currentValue = parseInt(quantityDisplay.textContent);
            if (currentValue > 0) {
                quantityDisplay.textContent = currentValue - 1;
                quantityInput.value = currentValue - 1;
                quantityDisplay.setAttribute('aria-valuenow', currentValue - 1);
            }
        });

        document.getElementById('increaseQuantity').addEventListener('click', function() {
            var currentValue = parseInt(quantityDisplay.textContent);
            quantityDisplay.textContent = currentValue + 1;
            quantityInput.value = currentValue + 1;
            quantityDisplay.setAttribute('aria-valuenow', currentValue + 1);
        });
    }

    document.getElementById('confirmCancel').addEventListener('click', function() {
        document.getElementById('cancelBookingForm').submit();
    });
});