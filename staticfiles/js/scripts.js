addEventListener("DOMContentLoaded", function () {
  const sidebar = document.getElementById("sidebar");
  const arrow = document.querySelector(".arrow");
  const menu = document.querySelector(".menu");
  sidebar.addEventListener("mouseenter", function () {
    sidebar.classList.add("show");
    menu.classList.add("show");

    arrow.style.transform = "rotate(180deg)";
    arrow.style.transition = "transform 0.3s ease"; // smooth animation
  });
  sidebar.addEventListener("mouseleave", function () {
    sidebar.classList.remove("show");
    arrow.style.transform = "rotate(0deg)";
    arrow.style.transition = "transform 0.3s ease"; // smooth animation
    menu.classList.remove("show");
  });
});
