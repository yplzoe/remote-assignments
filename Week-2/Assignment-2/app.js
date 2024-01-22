const clickHeadline = document.querySelector(".headline");
const clickButton = document.querySelector(".button");

clickHeadline.addEventListener("click", () => {
  clickHeadline.textContent = "Have a Good Time!";
});

clickButton.addEventListener("click", () => {
  const showContainer = document.querySelector(".hidden-first");
  showContainer.style.display = "flex";
});
