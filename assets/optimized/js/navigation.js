(() => {
  const button = document.querySelector("[data-nav-toggle]");
  const navigation = document.querySelector("[data-navigation]");
  if (!button || !navigation) return;

  const close = () => {
    button.setAttribute("aria-expanded", "false");
    navigation.dataset.open = "false";
  };

  button.addEventListener("click", () => {
    const willOpen = button.getAttribute("aria-expanded") !== "true";
    button.setAttribute("aria-expanded", String(willOpen));
    navigation.dataset.open = String(willOpen);
  });
  navigation.addEventListener("click", (event) => {
    if (event.target.closest("a")) close();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      close();
      button.focus();
    }
  });
  window.matchMedia("(min-width: 56rem)").addEventListener("change", close);
})();
