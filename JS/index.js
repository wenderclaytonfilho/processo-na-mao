const showPopupButton = document.getElementById("showPopup");
const closePopupButton = document.getElementById("closePopup");
const popup = document.getElementById("popup");

showPopupButton.addEventListener("click", () => {
  popup.style.display = "flex";
});

closePopupButton.addEventListener("click", () => {
  popup.style.display = "none";
});
