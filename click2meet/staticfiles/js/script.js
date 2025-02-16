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
        const maxQuantity = parseInt(form.getAttribute('data-max-quantity'), 10);
        const quantityWarning = document.getElementById('quantityWarning');
        const purchaseButton = document.getElementById('purchaseButton');

        // Set initial value to 0
        quantityDisplay.textContent = '0';
        quantityInput.value = '0';
        purchaseButton.disabled = true;

        document.getElementById('decreaseQuantity').addEventListener('click', function() {
            var currentValue = parseInt(quantityDisplay.textContent);
            if (currentValue > 0) {
                quantityDisplay.textContent = currentValue - 1;
                quantityInput.value = currentValue - 1;
                quantityDisplay.setAttribute('aria-valuenow', currentValue - 1);
                quantityWarning.style.display = 'none';
                purchaseButton.disabled = currentValue - 1 === 0;
            }
        });

        document.getElementById('increaseQuantity').addEventListener('click', function() {
            var currentValue = parseInt(quantityDisplay.textContent);
            if (currentValue < maxQuantity) {
                quantityDisplay.textContent = currentValue + 1;
                quantityInput.value = currentValue + 1;
                quantityDisplay.setAttribute('aria-valuenow', currentValue + 1);
                quantityWarning.style.display = 'none';
                purchaseButton.disabled = false;
            } else {
                quantityWarning.style.display = 'block';
            }
        });

        form.addEventListener('submit', function(event) {
            if (parseInt(quantityInput.value) === 0) {
                event.preventDefault();
                quantityWarning.style.display = 'block';
                quantityWarning.textContent = 'You must select at least one ticket to purchase.';
            }
        });
    }

    document.getElementById('confirmCancel').addEventListener('click', function() {
        document.getElementById('cancelBookingForm').submit();
    });
});