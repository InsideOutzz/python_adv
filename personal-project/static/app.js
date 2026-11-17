document.querySelectorAll("[data-edit]").forEach(button => {
  button.addEventListener("click", () => {
    const form = document.getElementById("edit-" + button.dataset.edit);
    form.classList.toggle("hidden");
  });
});
document.querySelectorAll("[data-cancel]").forEach(button => {
  button.addEventListener("click", () => document.getElementById("edit-" + button.dataset.cancel).classList.add("hidden"));
});
document.querySelectorAll("[data-edit-art]").forEach(button => {
  button.addEventListener("click", () => document.getElementById("edit-art-" + button.dataset.editArt).classList.toggle("hidden"));
});
document.querySelectorAll("[data-cancel-art]").forEach(button => {
  button.addEventListener("click", () => document.getElementById("edit-art-" + button.dataset.cancelArt).classList.add("hidden"));
});
document.querySelectorAll("[data-search]").forEach(input => {
  input.addEventListener("input", () => {
    const selector = "." + input.dataset.search;
    const query = input.value.toLowerCase().trim();
    document.querySelectorAll(selector).forEach(row => {
      row.style.display = row.dataset.searchText.includes(query) ? "" : "none";
    });
  });
});
setTimeout(() => document.querySelectorAll(".flash").forEach(item => item.classList.add("fade")), 4200);
