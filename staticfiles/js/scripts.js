
const categoryItems = document.querySelectorAll(".category");
console.log('category = ', categoryItems); // Log the NodeList to the console  

categoryItems.forEach((item) => {
  const text = item.textContent.trim(); // Get and clean the text inside the element

  switch (text) {
    case "Romance":
      item.style.color = "red";
      break;
    case "History":
      item.style.color = "blue";
      break;
    case "Science":
      item.style.color = "green";
      break;
    case "Fiction":
      item.style.color = "purple";
      break;
    case "Comedy":
      item.style.color = "yellow";
      break;
    case "Drama":
      item.style.color = "purple";
      break;
    default:
      item.style.color = "black";
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const bookTitle = document.querySelectorAll(".title");

  bookTitle.forEach((title) => {
    const text = title.textContent.trim();
    const capitalized = text
      .split(" ")
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
      .join(" ");
    title.textContent = capitalized;
  });
});
